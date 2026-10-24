#!/usr/bin/env python3
"""PAPER-TRADING ONLY runner for two XRP/RLUSD strategies on the XRP Ledger DEX.
Public data only. It holds no keys, signs nothing, and submits nothing to any network.

Each run (tick):
  1. reads the live XRP/RLUSD order book (`book_offers`), the RLUSD issuer's TransferRate
     (`account_info`) and reserves (`server_info`) from a public rippled node;
  2. reads CLOSED Bitstamp XRP/USD 5-minute candles since the last processed candle (intrabar highs/lows);
  3. feeds those prices to each strategy, then the live XRPL mid, and simulates fills;
  4. writes per-strategy state + logs, a tax-friendly CSV, logs/summary.csv and SUMMARY.md."""
import json, os, csv, time, urllib.request
from datetime import datetime, timezone
import scalper, dipladder

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, "config.json")))
MK = CFG["market"]
SDIR, LDIR = os.path.join(HERE, "state"), os.path.join(HERE, "logs")
MARKET_STATE = os.path.join(SDIR, "market.json")
TAX = os.path.join(LDIR, "tax_export.csv")
TAX_FIELDS = ["Date (UTC)", "Type", "Sent Asset", "Sent Amount", "Received Asset", "Received Amount",
              "Fee Asset", "Fee Amount", "Strategy", "Price (RLUSD per XRP)", "Description", "TxHash"]
FILL_FIELDS = ["ts", "side", "price", "xrp", "rlusd", "fee_xrp", "to_savings", "xrp_kept", "step_pct", "mkt"]

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")

def post(url, body, timeout=20):
    req = urllib.request.Request(url, json.dumps(body).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=timeout))

def get(url, timeout=20):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "xrpl-paper-runner"}), timeout=timeout))

def amt(a): return float(a) / 1e6 if isinstance(a, str) else float(a["value"])

def xrpl_snapshot():
    usd = {"currency": MK["rlusd_currency_hex"], "issuer": MK["rlusd_issuer"]}
    err = None
    for node in MK["rippled_nodes"]:
        try:
            asks = post(node, {"method": "book_offers", "params": [{"taker_gets": {"currency": "XRP"}, "taker_pays": usd, "limit": 20}]})["result"]["offers"]
            bids = post(node, {"method": "book_offers", "params": [{"taker_pays": {"currency": "XRP"}, "taker_gets": usd, "limit": 20}]})["result"]["offers"]
            def px(o, ask):
                g = amt(o.get("taker_gets_funded", o["TakerGets"])); p = amt(o.get("taker_pays_funded", o["TakerPays"]))
                xrp = g if ask else p
                if g <= 0 or p <= 0 or xrp < 1: return None   # dust/partially-funded offers give distorted prices
                return p / g if ask else g / p
            a = min(x for x in (px(o, 1) for o in asks) if x); b = max(x for x in (px(o, 0) for o in bids) if x)
            if not (0 < b < a) or (a - b) / ((a + b) / 2) > 0.02:   # crossed or absurd book = bad snapshot, try next node
                raise ValueError(f"bad book snapshot bid={b} ask={a}")
            iss = post(node, {"method": "account_info", "params": [{"account": MK["rlusd_issuer"], "ledger_index": "validated"}]})["result"]["account_data"]
            tr = iss.get("TransferRate", 0)
            vl = post(node, {"method": "server_info", "params": [{}]})["result"]["info"].get("validated_ledger", {})
            return {"node": node, "bid": b, "ask": a, "mid": (a + b) / 2, "ledger": vl.get("seq"),
                    "transfer_fee_pct": 0.0 if tr in (0, 1000000000) else (tr / 1e9 - 1) * 100,
                    "reserve_base": vl.get("reserve_base_xrp"), "reserve_inc": vl.get("reserve_inc_xrp")}
        except Exception as e:
            err = e
    raise RuntimeError(f"all rippled nodes failed: {err}")

def closed_candles(after_ts, now):
    """Closed 5-min candles with timestamp > after_ts. Returns [(ts, path, high, low)]."""
    try:
        rows = get(MK["candles_url"].format(start=int(after_ts) + 300))["data"]["ohlc"]
    except Exception as e:
        print("candles unavailable, using XRPL snapshot only:", e); return []
    out = []
    for r in rows:
        t = int(r["timestamp"])
        if t <= after_ts or t + 300 > now: continue
        o, h, l, c = (float(r[k]) for k in ("open", "high", "low", "close"))
        out.append((t, (o, h, l, c) if c < o else (o, l, h, c), h, l))
    return sorted(out)

def append(path, row, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def tax_row(name, e, desc=None):
    """Crypto-tax-friendly row. BUY: sent RLUSD, received XRP. SELL: sent XRP, received RLUSD."""
    buy = e["side"] == "BUY"
    return {"Date (UTC)": e["ts"], "Type": "Trade",
            "Sent Asset": "RLUSD" if buy else "XRP", "Sent Amount": e["rlusd"] if buy else e["xrp"],
            "Received Asset": "XRP" if buy else "RLUSD", "Received Amount": e["xrp"] if buy else e["rlusd"],
            "Fee Asset": "XRP", "Fee Amount": f"{e.get('fee_xrp', 0):.6f}", "Strategy": name, "Price (RLUSD per XRP)": e["price"],
            "Description": desc or f"PAPER {e['side'].lower()} XRP/RLUSD limit order (simulated)", "TxHash": "PAPER-NOT-ON-LEDGER"}

def load(path):
    return json.load(open(path)) if os.path.exists(path) else None

def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(obj, open(path, "w"), indent=1)

def init_strategy(name, sc, mid, now, ts_iso):
    """Create a fresh paper account. Reserve XRP is bought at the live mid + taker cost (logged as a trade)."""
    if sc["type"] == "scalp":
        st = scalper.new_state(mid, sc)
        rx = st["reserve_xrp"]; ru = st["budget_usd"] - st["trading_usd"]
    else:
        st = dipladder.new_state(mid, sc, now)
        rx = st["reserve_xrp"]; ru = st["reserve_cost_usd"]
    st.update(type=sc["type"], created=ts_iso)
    e = {"ts": ts_iso, "side": "BUY", "price": round(ru / rx, 6), "xrp": round(rx, 6), "rlusd": round(ru, 4), "fee_xrp": sc.get("tx_fee_xrp", 0.00001)}
    append(TAX, tax_row(name, e, "PAPER market buy of reserve XRP (base + trust line + per-offer reserve)"), TAX_FIELDS)
    append(os.path.join(LDIR, f"{name}_fills.csv"), dict(e, side="BUY_RESERVE"), FILL_FIELDS)
    return st

def run_strategy(name, sc, st, candles, snap, now, ts_iso):
    events = []
    if sc["type"] == "scalp":
        for t, path, h, l in candles:
            events += scalper.process(st, path, sc, ts=iso(t + 300))
            scalper.observe(st, sc, t, h, l, path[-1])
        if snap.get("mid") is not None: events += scalper.process(st, [snap["mid"]], sc, ts=ts_iso)
        x, usd = scalper.total_xrp(st), st["trading_usd"] + st["savings_usd"]
        fills, sells = st["buys"] + st["sells"], st["sells"]
        extra = {"open_buy_orders": sum(L["state"] == "buy" for L in st["levels"]),
                 "open_sell_orders": sum(L["state"] == "sell" for L in st["levels"]),
                 "xrp_kept_from_scalps": round(st["kept_xrp"], 6)}
    else:
        ref = snap.get("mid") if snap.get("mid") is not None else snap["ref"]
        dipladder.maybe_refresh(st, sc, candles[0][0] if candles else now, candles[0][1][0] if candles else ref)
        for t, path, h, l in candles:
            dipladder.maybe_refresh(st, sc, t, path[0])
            events += dipladder.process(st, path, sc, ts=iso(t + 300))
        dipladder.maybe_refresh(st, sc, now, ref)
        if snap.get("mid") is not None: events += dipladder.process(st, [snap["mid"]], sc, ts=ts_iso)
        x, usd = dipladder.total_xrp(st), dipladder.unspent_usd(st)
        fills, sells = st["buys"], st["sells"]
        extra = {"open_buy_orders": len(st["orders"]), "open_sell_orders": 0,
                 "ladder_ref": st["ref"], "next_refresh": iso(st["next_refresh_unix"]),
                 "order_prices": " ".join(f"{o['price']:.4f}" for o in st["orders"])}
    for e in events:
        append(os.path.join(LDIR, f"{name}_fills.csv"), e, FILL_FIELDS)
        append(TAX, tax_row(name, e), TAX_FIELDS)
    st["last_run"] = ts_iso
    return events, x, usd, fills + 1, sells, extra   # +1 = the reserve buy

# ---------------- amm_lp: paper liquidity position in the XRP/RLUSD AMM (separate 4th line) ----------------
AMM_STATE = os.path.join(SDIR, "amm_lp.json")

def amm_pool(ledger_index="validated"):
    err = None
    for node in MK["rippled_nodes"]:
        try:
            a = post(node, {"method": "amm_info", "params": [{"amm_account": CFG["amm_lp"]["amm_account"], "ledger_index": ledger_index}]}, timeout=30)["result"]["amm"]
            if isinstance(a["amount"], str): x, r = float(a["amount"]) / 1e6, float(a["amount2"]["value"])
            else: x, r = float(a["amount2"]) / 1e6, float(a["amount"]["value"])
            return {"x": x, "r": r, "lp": float(a["lp_token"]["value"]), "fee_pct": a["trading_fee"] / 1000, "node": node}
        except Exception as e: err = e
    raise RuntimeError(f"amm_info failed on all nodes: {err}")

def amm_lp_init(taker, mid, ts_iso):
    """Reconstruct the paper deposit at the backdated ledger if history is available, else start now."""
    c = CFG["amm_lp"]
    try: pool, start_ts, px, led, note = amm_pool(c["backdate_ledger"]), c["backdate_ts"], c["backdate_price"], c["backdate_ledger"], "backdated from historical pool state"
    except Exception as e:
        print("amm_lp: historical pool unavailable, starting now:", e)
        pool, start_ts, px, led, note = amm_pool(), ts_iso, mid, None, "started at first run (history unavailable)"
    ratio = pool["r"] / pool["x"]                      # RLUSD per XRP inside the pool at deposit time
    x = c["budget_usd"] / (px * taker + ratio)         # proportional deposit worth $100 at the start price
    r = x * ratio
    st = {"type": "amm_lp", "created": ts_iso, "start_ts": start_ts, "start_ledger": led, "start_price": px, "note": note,
          "deposit_xrp": x, "deposit_rlusd": r, "lp_tokens": pool["lp"] * x / pool["x"],
          "start_pool": {k: pool[k] for k in ("x", "r", "lp", "fee_pct")}}
    e = {"ts": start_ts, "side": "BUY", "price": px, "xrp": round(x, 6), "rlusd": round(x * px * taker, 4), "fee_xrp": 0.00001}
    append(TAX, tax_row("amm_lp", e, "PAPER buy of XRP half for AMM deposit (simulated)"), TAX_FIELDS)
    append(TAX, {"Date (UTC)": start_ts, "Type": "AMM Deposit", "Sent Asset": "XRP+RLUSD", "Sent Amount": f"{x:.6f} XRP + {r:.4f} RLUSD",
                 "Received Asset": "LP token", "Received Amount": f"{st['lp_tokens']:.6f}", "Fee Asset": "XRP", "Fee Amount": "0.000010",
                 "Strategy": "amm_lp", "Price (RLUSD per XRP)": px, "Description": "PAPER two-asset AMM deposit (simulated)", "TxHash": "PAPER-NOT-ON-LEDGER"}, TAX_FIELDS)
    return st

def amm_lp_tick(taker, snap, ts_iso, base_xrp):
    st = load(AMM_STATE) or amm_lp_init(taker, snap["mid"], ts_iso)
    pool = amm_pool(); share = st["lp_tokens"] / pool["lp"]
    x, r, mid = share * pool["x"], share * pool["r"], snap["mid"]
    hold_x, hold_r = st["deposit_xrp"], st["deposit_rlusd"]
    k = (pool["r"] / pool["x"]) / (st["start_pool"]["r"] / st["start_pool"]["x"])   # pool price change since deposit
    il_pct = (2 * k ** 0.5 / (1 + k) - 1) * 100                                     # theoretical IL vs holding the deposit
    lp_val, hold_val = x * mid + r, hold_x * mid + hold_r
    row = {"ts": ts_iso, "label": "PAPER-NOT-ON-LEDGER", "xrpl_mid": round(mid, 6), "lp_tokens": round(st["lp_tokens"], 6),
           "pool_share_pct": round(share * 100, 8), "xrp": round(x, 6), "rlusd": round(r, 4),
           "xrp_equiv": round(x + r / (mid * taker), 6), "value_usd": round(lp_val, 4),
           "hold5050_xrp_equiv": round(hold_x + hold_r / (mid * taker), 6), "hold5050_value_usd": round(hold_val, 4),
           "lump_xrp": round(base_xrp, 6), "lump_value_usd": round(base_xrp * mid, 4),
           "vs_hold5050_pct": round((lp_val / hold_val - 1) * 100, 4), "il_pct": round(il_pct, 4),
           "fees_est_pct": round(((lp_val / hold_val) / (1 + il_pct / 100) - 1) * 100, 4),
           "vs_lump_xrp_pct": round(((x + r / (mid * taker)) / base_xrp - 1) * 100, 3), "pool_fee_pct": pool["fee_pct"]}
    st["last_run"] = ts_iso; st["last"] = row
    save(AMM_STATE, st)
    append(os.path.join(LDIR, "amm_lp_ticks.csv"), row, list(row.keys()))
    return st, row

def append_summary(path, row):
    """Append to summary.csv; if new columns appeared (e.g. amm_lp_*), rewrite the header once, old rows keep blanks."""
    if os.path.exists(path):
        with open(path, newline="") as f:
            rd = csv.DictReader(f); old_fields = rd.fieldnames or []
            if any(k not in old_fields for k in row):
                rows = list(rd); fields = list(row.keys()) + [k for k in old_fields if k not in row]
                with open(path + ".tmp", "w", newline="") as g:
                    w = csv.DictWriter(g, fieldnames=fields); w.writeheader(); w.writerows(rows)
                os.replace(path + ".tmp", path)
    append(path, row, list(row.keys()) if not os.path.exists(path) else next(csv.reader(open(path))))

def candles_between(after_ts, until_ts, now):
    """Closed 5-min candles with after_ts < t <= until_ts, paging the 1000-candle API limit."""
    out, cur = [], after_ts
    while cur < until_ts:
        page = [c for c in closed_candles(cur, now) if c[0] <= until_ts]
        if not page: break
        out += page; cur = page[-1][0]
    return out

def backfill_new_strategy(name, sc, ms, now):
    """A strategy added after the experiment started is initialised at the experiment's start price/time and
    replayed over the same closed candles the others saw, so all lines share one start date."""
    start = datetime.fromisoformat(ms["started"]).timestamp()
    st = init_strategy(name, sc, ms["start_mid"], start, ms["started"])
    st["backfilled_from"] = ms["started"]
    hist = candles_between(int(start) // 300 * 300 - 300, ms["last_candle_ts"], now)
    snap0 = {"mid": None, "ref": hist[-1][1][-1] if hist else ms["start_mid"]}
    ev, *_ = run_strategy(name, sc, st, hist, snap0, start, ms["started"])
    print(f"backfilled {name}: {len(hist)} candles, {len(ev)} fills")
    return st

MID_AGREE_PCT = 1.0   # the XRPL book mid is used as a price point only if within 1% of the latest Bitstamp close

def book_mid_ok(mid, spread_pct, ref):
    return mid is not None and 0 < spread_pct < 2 and (ref is None or abs(mid / ref - 1) * 100 <= MID_AGREE_PCT)

def tick_row(name, sc, st, events, x, usd, fills, sells, extra, ts_iso, val_mid, taker):
    eq = x + usd / (val_mid * taker); val = x * val_mid + usd
    return {"ts": ts_iso, "strategy": name, "budget_usd": sc["budget_usd"], "xrpl_mid": round(val_mid, 6),
            "xrp_held": round(x, 6), "rlusd_unspent": round(usd, 4), "xrp_equiv": round(eq, 6),
            "value_usd": round(val, 4), "vs_start_usd": round(val - sc["budget_usd"], 4), "fills": fills, "xrp_sells_taxable": sells,
            "new_fills": len(events), **extra}

def build_srow(ts_iso, mid, spread_pct, n_candles, rows, ms):
    """USD/RLUSD scoreboard first. Every strategy is compared with keeping its own budget in XRP bought at the start
    (baseline_xrp is for $100, scaled by budget/100); the total is compared with the sum of those baselines."""
    base = ms["baseline_xrp"]; bu = ms.get("baseline_usd", CFG["baseline_usd"])
    tot_x = sum(r["xrp_held"] for r in rows); tot_u = sum(r["rlusd_unspent"] for r in rows); tot_eq = sum(r["xrp_equiv"] for r in rows)
    tot_val = sum(r["value_usd"] for r in rows); tot_bud = sum(r["budget_usd"] for r in rows)
    k_tot = tot_bud / bu
    srow = {"ts": ts_iso, "xrpl_mid": round(mid, 6), "total_value_usd": round(tot_val, 4), "total_vs_start_usd": round(tot_val - tot_bud, 4),
            "total_baseline_xrp_value_usd": round(base * k_tot * mid, 4), "total_vs_xrp_usd": round(tot_val - base * k_tot * mid, 4),
            "baseline_xrp_value_usd": round(base * mid, 4)}
    for r in rows:
        k = r["budget_usd"] / bu
        srow.update({f"{r['strategy']}_value_usd": r["value_usd"], f"{r['strategy']}_vs_start_usd": r["vs_start_usd"],
                     f"{r['strategy']}_vs_xrp_usd": round(r["value_usd"] - base * k * mid, 4)})
    srow.update({"spread_pct": round(spread_pct, 4), "candles": n_candles, "baseline_xrp": round(base, 6),
                 "total_baseline_xrp": round(base * k_tot, 6)})
    for r in rows:
        n = r["strategy"]; k = r["budget_usd"] / bu
        srow.update({f"{n}_xrp": r["xrp_held"], f"{n}_rlusd": r["rlusd_unspent"], f"{n}_xrp_equiv": r["xrp_equiv"],
                     f"{n}_vs_xrp_equiv_pct": round((r["xrp_equiv"] / (base * k) - 1) * 100, 3),
                     f"{n}_fills": r["fills"], f"{n}_xrp_sells": r["xrp_sells_taxable"]})
    srow.update({"total_xrp": round(tot_x, 6), "total_rlusd": round(tot_u, 4), "total_xrp_equiv": round(tot_eq, 6),
                 "vs_baseline_pct": round((tot_eq / (base * k_tot) - 1) * 100, 3)})
    return srow

def main():
    now = time.time(); ts_iso = iso(now)
    snap = xrpl_snapshot()
    taker = 1 + CFG.get("taker_cost_pct", 0.05) / 100
    if snap["transfer_fee_pct"] > 0:
        print(f"WARNING: RLUSD issuer now charges {snap['transfer_fee_pct']:.4f}%; adding it to per-fill cost")
    ms = load(MARKET_STATE)
    fresh = ms is None
    if fresh:
        ms = {"started": ts_iso, "start_mid": snap["mid"], "last_candle_ts": int(now) // 300 * 300 - 300,
              "baseline_usd": CFG["baseline_usd"], "baseline_xrp": CFG["baseline_usd"] / (snap["mid"] * taker)}
        candles = []
    else:
        candles = closed_candles(ms["last_candle_ts"], now)
    spread = (snap["ask"] - snap["bid"]) / snap["mid"] * 100
    ref = candles[-1][1][-1] if candles else ms.get("last_close")
    mid_ok = book_mid_ok(snap["mid"], spread, ref)
    if not mid_ok: print(f"XRPL mid {snap['mid']:.5f} disagrees with Bitstamp close {ref} by >{MID_AGREE_PCT}%: not used as a price point this tick")
    val_mid = snap["mid"] if mid_ok or ref is None else ref
    rows = []
    for name, sc in CFG["strategies"].items():
        sc = dict(sc, extra_cost_pct_per_fill=sc.get("extra_cost_pct_per_fill", 0) + snap["transfer_fee_pct"])
        spath = os.path.join(SDIR, f"{name}.json")
        st = load(spath)
        if st is None:
            st = backfill_new_strategy(name, sc, ms, now) if not fresh else init_strategy(name, sc, snap["mid"], now, ts_iso)
        events, x, usd, fills, sells, extra = run_strategy(name, sc, st, candles, {"mid": snap["mid"] if mid_ok else None, "ref": val_mid}, now, ts_iso)
        save(spath, st)
        row = tick_row(name, sc, st, events, x, usd, fills, sells, extra, ts_iso, val_mid, taker)
        append(os.path.join(LDIR, f"{name}_ticks.csv"), row, list(row.keys()))
        rows.append(row)
        for e in events: print(f"FILL [{name}]", e)
    if candles: ms["last_candle_ts"] = candles[-1][0]; ms["last_close"] = candles[-1][1][-1]
    ms.update(last_run=ts_iso, last_mid=snap["mid"], last_node=snap["node"], last_ledger=snap["ledger"],
              candles_this_run=len(candles))
    save(MARKET_STATE, ms)
    srow = build_srow(ts_iso, val_mid, spread, len(candles), rows, ms)
    base = ms["baseline_xrp"]
    lp = None
    if "amm_lp" in CFG:
        try:
            lp_st, lp = amm_lp_tick(taker, dict(snap, mid=val_mid), ts_iso, base)
            srow.update({"amm_lp_vs_start_usd": round(lp["value_usd"] - CFG["amm_lp"]["budget_usd"], 4), "amm_lp_xrp": lp["xrp"], "amm_lp_rlusd": lp["rlusd"], "amm_lp_xrp_equiv": lp["xrp_equiv"],
                         "amm_lp_value_usd": lp["value_usd"], "amm_lp_hold5050_value_usd": lp["hold5050_value_usd"],
                         "amm_lp_vs_hold5050_pct": lp["vs_hold5050_pct"], "amm_lp_vs_lump_xrp_pct": lp["vs_lump_xrp_pct"],
                         "amm_lp_vs_xrp_usd": round(lp["value_usd"] - lp["lump_value_usd"], 4)})
            lp = dict(lp, start_ts=lp_st["start_ts"], start_price=lp_st["start_price"], note=lp_st["note"],
                      dep_x=lp_st["deposit_xrp"], dep_r=lp_st["deposit_rlusd"])
        except Exception as e:
            print("amm_lp tick failed (other strategies unaffected):", e)
    append_summary(os.path.join(LDIR, "summary.csv"), srow)
    write_md(ms, dict(snap, mid=val_mid), rows, srow, lp)
    print(json.dumps(srow, indent=1))

def write_md(ms, snap, rows, s, lp=None):
    mid = snap["mid"]
    base = s["baseline_xrp"]; bvu = s["baseline_xrp_value_usd"]
    L = ["# XRP/RLUSD paper-trading experiment: SUMMARY", "",
         "> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.", "",
         "**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with "
         "**keep $100 in XRP** (bought at the start).", "",
         f"- Started: **{ms['started']}** at XRPL mid **${ms['start_mid']:.4f}**",
         f"- Last update: **{s['ts']}**, XRPL XRP/RLUSD mid **${mid:.4f}** (bid {snap['bid']:.4f} / ask {snap['ask']:.4f}, node {snap['node']}, ledger {snap['ledger']})",
         f"- RLUSD issuer transfer fee (live): {snap['transfer_fee_pct']:.4f}%  |  candles processed this run: {s['candles']}", "",
         "| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        n = r["strategy"]; lab = CFG["strategies"][n]["label"]; bx = bvu * r["budget_usd"] / ms["baseline_usd"]
        d = r["value_usd"] - bx
        L.append(f"| {lab} (`{n}`) | ${r['budget_usd']} | **${r['value_usd']:.2f}** | {r['vs_start_usd']:+.2f} | **{d:+.2f}** ({d / bx * 100:+.2f}%) | "
                 f"{r['xrp_held']:.4f} | ${r['rlusd_unspent']:.2f} | {r['xrp_equiv']:.4f} | {s[n + '_vs_xrp_equiv_pct']:+.2f}% | {r['fills']} | {r['xrp_sells_taxable']} |")
    tb = sum(r["budget_usd"] for r in rows); dt = s["total_vs_xrp_usd"]
    L.append(f"| **Experiment total** (all {len(rows)}) | ${tb} | **${s['total_value_usd']:.2f}** | {s['total_vs_start_usd']:+.2f} | **{dt:+.2f}** ({dt / s['total_baseline_xrp_value_usd'] * 100:+.2f}%) | "
             f"{s['total_xrp']:.4f} | ${s['total_rlusd']:.2f} | {s['total_xrp_equiv']:.4f} | {s['vs_baseline_pct']:+.2f}% | | |")
    L.append(f"| **Baseline: keep $100 in XRP** (bought at start) | ${ms['baseline_usd']} | ${bvu:.2f} | {bvu - ms['baseline_usd']:+.2f} | — | {base:.4f} | $0.00 | {base:.4f} | — | 1 | 0 |")
    L.append(f"| Baseline for the total: keep ${tb} in XRP | ${tb} | ${s['total_baseline_xrp_value_usd']:.2f} | {s['total_baseline_xrp_value_usd'] - tb:+.2f} | — | {s['total_baseline_xrp']:.4f} | $0.00 | {s['total_baseline_xrp']:.4f} | — | | |")
    L += ["", "_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy "
          "(earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._", "",
          f"**Experiment (${tb}) vs keep ${tb} in XRP: {dt:+.2f} USD ({dt / s['total_baseline_xrp_value_usd'] * 100:+.2f}%)** · XRP-equivalent: {s['vs_baseline_pct']:+.2f}%", "",
          "\\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. "
          "XRP held includes the XRP locked as ledger reserve (it is still yours).", "",
          "- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.",
          "- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.", ""]
    for r in rows:
        if r["strategy"] == "dip_ladder" or "order_prices" in r:
            L.append(f"- Dip ladder open buy orders: {r.get('order_prices') or 'none'} (reference {r.get('ladder_ref')}, next refresh {r.get('next_refresh')})")
        else:
            L.append(f"- `{r['strategy']}`: {r['open_buy_orders']} buy orders waiting, {r['open_sell_orders']} sell orders waiting, XRP kept from scalps {r['xrp_kept_from_scalps']}")
    if lp:
        L += ["", "## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)", "",
              f"$100 deposited 50/50 into the XRP/RLUSD AMM pool on {lp['start_ts']} at ${lp['start_price']:.4f} "
              f"({lp['dep_x']:.4f} XRP + {lp['dep_r']:.2f} RLUSD; {lp['note']}). Separate $100 line, not included in the $300 total.", "",
              "| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |", "|---|---|---|---|---|---|",
              f"| AMM LP position now (fees included) | **${lp['value_usd']:.2f}** | {lp['value_usd'] - 100:+.2f} | {lp['xrp']:.4f} | ${lp['rlusd']:.2f} | {lp['xrp_equiv']:.4f} |",
              f"| Hold the same 50/50 (no pool) | ${lp['hold5050_value_usd']:.2f} | {lp['hold5050_value_usd'] - 100:+.2f} | {lp['dep_x']:.4f} | ${lp['dep_r']:.2f} | {lp['hold5050_xrp_equiv']:.4f} |",
              f"| Baseline: keep $100 in XRP | ${lp['lump_value_usd']:.2f} | {lp['lump_value_usd'] - 100:+.2f} | {lp['lump_xrp']:.4f} | $0.00 | {lp['lump_xrp']:.4f} |", "",
              f"- LP vs hold-50/50: **{lp['vs_hold5050_pct']:+.3f}%** = impermanent loss {lp['il_pct']:+.3f}% + fees earned ≈ {lp['fees_est_pct']:+.3f}% (pool fee {lp['pool_fee_pct']:.3f}%, pool share {lp['pool_share_pct']:.6f}%)",
              f"- LP vs keep $100 in XRP: **{lp['value_usd'] - lp['lump_value_usd']:+.2f} USD** · XRP-equivalent: {lp['vs_lump_xrp_pct']:+.2f}%"]
    L += ["", "Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
