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
                return None if g <= 0 or p <= 0 else (p / g if ask else g / p)
            a = min(x for x in (px(o, 1) for o in asks) if x); b = max(x for x in (px(o, 0) for o in bids) if x)
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
        events += scalper.process(st, [snap["mid"]], sc, ts=ts_iso)
        x, usd = scalper.total_xrp(st), st["trading_usd"] + st["savings_usd"]
        fills, sells = st["buys"] + st["sells"], st["sells"]
        extra = {"open_buy_orders": sum(L["state"] == "buy" for L in st["levels"]),
                 "open_sell_orders": sum(L["state"] == "sell" for L in st["levels"]),
                 "xrp_kept_from_scalps": round(st["kept_xrp"], 6)}
    else:
        dipladder.maybe_refresh(st, sc, candles[0][0] if candles else now, candles[0][1][0] if candles else snap["mid"])
        for t, path, h, l in candles:
            dipladder.maybe_refresh(st, sc, t, path[0])
            events += dipladder.process(st, path, sc, ts=iso(t + 300))
        dipladder.maybe_refresh(st, sc, now, snap["mid"])
        events += dipladder.process(st, [snap["mid"]], sc, ts=ts_iso)
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
    rows = []
    for name, sc in CFG["strategies"].items():
        sc = dict(sc, extra_cost_pct_per_fill=sc.get("extra_cost_pct_per_fill", 0) + snap["transfer_fee_pct"])
        spath = os.path.join(SDIR, f"{name}.json")
        st = load(spath)
        if st is None:
            st = init_strategy(name, sc, snap["mid"], now, ts_iso)
        events, x, usd, fills, sells, extra = run_strategy(name, sc, st, candles, snap, now, ts_iso)
        save(spath, st)
        eq = x + usd / (snap["mid"] * taker)
        row = {"ts": ts_iso, "strategy": name, "budget_usd": sc["budget_usd"], "xrpl_mid": round(snap["mid"], 6),
               "xrp_held": round(x, 6), "rlusd_unspent": round(usd, 4), "xrp_equiv": round(eq, 6),
               "value_usd": round(x * snap["mid"] + usd, 4), "fills": fills, "xrp_sells_taxable": sells,
               "new_fills": len(events), **extra}
        append(os.path.join(LDIR, f"{name}_ticks.csv"), row, list(row.keys()))
        rows.append(row)
        for e in events: print(f"FILL [{name}]", e)
    if candles: ms["last_candle_ts"] = candles[-1][0]
    ms.update(last_run=ts_iso, last_mid=snap["mid"], last_node=snap["node"], last_ledger=snap["ledger"],
              candles_this_run=len(candles))
    save(MARKET_STATE, ms)
    # combined summary
    tot_x = sum(r["xrp_held"] for r in rows); tot_u = sum(r["rlusd_unspent"] for r in rows); tot_eq = sum(r["xrp_equiv"] for r in rows)
    base = ms["baseline_xrp"]
    srow = {"ts": ts_iso, "xrpl_mid": round(snap["mid"], 6), "spread_pct": round((snap["ask"] - snap["bid"]) / snap["mid"] * 100, 4),
            "candles": len(candles), "baseline_xrp": round(base, 6)}
    for r in rows:
        n = r["strategy"]
        srow.update({f"{n}_xrp": r["xrp_held"], f"{n}_rlusd": r["rlusd_unspent"], f"{n}_xrp_equiv": r["xrp_equiv"],
                     f"{n}_fills": r["fills"], f"{n}_xrp_sells": r["xrp_sells_taxable"]})
    srow.update({"total_xrp": round(tot_x, 6), "total_rlusd": round(tot_u, 4), "total_xrp_equiv": round(tot_eq, 6),
                 "vs_baseline_pct": round((tot_eq / base - 1) * 100, 3)})
    append(os.path.join(LDIR, "summary.csv"), srow, list(srow.keys()))
    write_md(ms, snap, rows, srow)
    print(json.dumps(srow, indent=1))

def write_md(ms, snap, rows, s):
    L = ["# XRP/RLUSD paper-trading experiment: SUMMARY", "",
         "> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.", "",
         f"- Started: **{ms['started']}** at XRPL mid **${ms['start_mid']:.4f}**",
         f"- Last update: **{s['ts']}**, XRPL XRP/RLUSD mid **${snap['mid']:.4f}** (bid {snap['bid']:.4f} / ask {snap['ask']:.4f}, node {snap['node']}, ledger {snap['ledger']})",
         f"- RLUSD issuer transfer fee (live): {snap['transfer_fee_pct']:.4f}%  |  candles processed this run: {s['candles']}", "",
         "| Strategy | Budget | XRP held | RLUSD unspent | XRP-equivalent* | Fills | XRP sells (taxable) |",
         "|---|---|---|---|---|---|---|"]
    for r in rows:
        lab = CFG["strategies"][r["strategy"]]["label"]
        L.append(f"| {lab} (`{r['strategy']}`) | ${r['budget_usd']} | {r['xrp_held']:.4f} | ${r['rlusd_unspent']:.2f} | {r['xrp_equiv']:.4f} | {r['fills']} | {r['xrp_sells_taxable']} |")
    L.append(f"| **Total** | ${sum(r['budget_usd'] for r in rows)} | **{s['total_xrp']:.4f}** | ${s['total_rlusd']:.2f} | **{s['total_xrp_equiv']:.4f}** | | |")
    L.append(f"| Baseline: ${ms['baseline_usd']} lump-sum XRP bought at start | ${ms['baseline_usd']} | {s['baseline_xrp']:.4f} | $0.00 | {s['baseline_xrp']:.4f} | 1 | 0 |")
    L += ["", f"**Experiment vs baseline (XRP-equivalent): {s['vs_baseline_pct']:+.2f}%**", "",
          "\\* XRP-equivalent = XRP held + unspent RLUSD converted at the current mid with a 0.05% taker cost. "
          "XRP held includes the XRP locked as ledger reserve (it is still yours).", ""]
    for r in rows:
        if r["strategy"] == "dip_ladder" or "order_prices" in r:
            L.append(f"- Dip ladder open buy orders: {r.get('order_prices') or 'none'} (reference {r.get('ladder_ref')}, next refresh {r.get('next_refresh')})")
        else:
            L.append(f"- `{r['strategy']}`: {r['open_buy_orders']} buy orders waiting, {r['open_sell_orders']} sell orders waiting, XRP kept from scalps {r['xrp_kept_from_scalps']}")
    L += ["", "Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/tax_export.csv`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
