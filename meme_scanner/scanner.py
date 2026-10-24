#!/usr/bin/env python3
"""XRPL memecoin PAPER scanner. LOG-ONLY: reads public APIs, simulates $10 buys, never signs or submits anything.

Each run: discover new/trending XRPL tokens -> ledger safety checks -> paper-buy passing tokens (AMM math)
-> mark open paper positions to the live AMM pool and apply 3 exit strategies -> write logs + SUMMARY.md.
Stdlib only. Every row is labelled PAPER-NOT-ON-LEDGER.
"""
import csv, json, math, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, "config.json")))
STATE, LOGS = os.path.join(HERE, "state"), os.path.join(HERE, "logs")
NODES = ["https://xrplcluster.com", "https://s1.ripple.com:51234", "https://s2.ripple.com:51234"]
XRPLTO = "https://api.xrpl.to/v1/tokens"
XRPLTO_KEY = os.environ.get("XRPLTO_API_KEY", "").strip()  # optional free key; sent only as a header, never printed/logged
BLACKHOLES = {"rrrrrrrrrrrrrrrrrrrrrhoLvTp", "rrrrrrrrrrrrrrrrrrrrBZbvji", "rrrrrrrrrrrrrrrrrNAMEtxvNvQ", "rrrrrrrrrrrrrrrrrrrn5RM1rHd"}
LABEL = "PAPER-NOT-ON-LEDGER"
UA = {"User-Agent": "xrpl-meme-paper-scanner/1.0 (github.com/LeoNeo20022/xrpl-paper-trader)"}
NOW = time.time()
TS = datetime.fromtimestamp(NOW, timezone.utc).isoformat(timespec="seconds")
WARN = []  # source/API problems this run, shown in SUMMARY

# ---------------- io helpers ----------------
def http_json(url, body=None, timeout=25, headers=None):
    h = dict(UA, **(headers or {}))
    data = None
    if body is not None:
        data = json.dumps(body).encode(); h["Content-Type"] = "application/json"
    return json.load(urllib.request.urlopen(urllib.request.Request(url, data, h), timeout=timeout))

_node_ok = list(NODES)
def rpc(method, params):
    """Query public rippled with fallback. Returns result dict (may contain 'error')."""
    last = None
    for n in list(_node_ok):
        try:
            r = http_json(n, {"method": method, "params": [params]})["result"]
            if r.get("error") in ("slowDown", "tooBusy", "noNetwork", "notReady"):
                last = r["error"]; continue
            return r
        except Exception as e:  # network/timeout: try next node
            last = repr(e)
            if len(_node_ok) > 1: _node_ok.remove(n); _node_ok.append(n)
    raise RuntimeError(f"all XRPL nodes failed for {method}: {last}")

def load(name, default):
    p = os.path.join(STATE, name)
    return json.load(open(p)) if os.path.exists(p) else default

def save(name, obj):
    p = os.path.join(STATE, name)
    json.dump(obj, open(p + ".tmp", "w"), indent=1, sort_keys=True); os.replace(p + ".tmp", p)

def append(name, row, fields):
    p = os.path.join(LOGS, name); new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def cur_name(c):
    if len(c) == 40:
        try:
            s = bytes.fromhex(c).rstrip(b"\x00").decode("ascii")
            if s.isprintable(): return s
        except Exception: pass
        return c[:8] + "…"
    return c

def key(cur, iss): return f"{iss}-{cur}"

# ---------------- prices ----------------
def xrp_usd():
    for name, fn in [("bitstamp", lambda: float(http_json("https://www.bitstamp.net/api/v2/ticker/xrpusd/")["last"])),
                     ("kraken", lambda: float(list(http_json("https://api.kraken.com/0/public/Ticker?pair=XRPUSD")["result"].values())[0]["c"][0]))]:
        try: return fn(), name
        except Exception as e: WARN.append(f"XRP/USD from {name} failed: {e!r}")
    # last resort: on-ledger XRP/RLUSD AMM (RLUSD ~ $1)
    r = rpc("amm_info", {"asset": {"currency": "XRP"}, "asset2": {"currency": "524C555344000000000000000000000000000000", "issuer": "rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De"}})
    a = r["amm"]; return float(a["amount2"]["value"]) / (float(a["amount"]) / 1e6), "xrpl-rlusd-amm"

# ---------------- AMM simulation (XRPL constant product, fee charged on input) ----------------
def swap_out(pool_in, pool_out, amt_in, fee):
    eff = amt_in * (1 - fee)
    return pool_out * eff / (pool_in + eff)

def sim_buy(pool, xrp_in):
    """xrp_in XRP -> tokens. Returns (tokens_net, tokens_gross_at_spot)."""
    tf = pool["tf"] if CFG["apply_transfer_fee_both_legs"] else 0.0
    xrp_eff = xrp_in - CFG["network_fee_xrp"]
    out = swap_out(pool["x"], pool["t"], xrp_eff, pool["fee"]) / (1 + tf)
    return out, xrp_in / pool["spot"]

def sim_sell(pool, tokens):
    """tokens -> XRP. Returns (xrp_net, xrp_gross_at_spot)."""
    if not pool or pool["x"] <= 0: return 0.0, 0.0
    tf = pool["tf"]
    out = swap_out(pool["t"], pool["x"], tokens / (1 + tf), pool["fee"]) - CFG["network_fee_xrp"]
    return max(out, 0.0), tokens * pool["spot"]

def get_pool(cur, iss, tf):
    r = rpc("amm_info", {"asset": {"currency": "XRP"}, "asset2": {"currency": cur, "issuer": iss}, "ledger_index": "validated"})
    if r.get("error") == "actNotFound" or "amm" not in r: return None
    a = r["amm"]
    if isinstance(a["amount"], dict): x, t = float(a["amount2"]) / 1e6, float(a["amount"]["value"])
    else: x, t = float(a["amount"]) / 1e6, float(a["amount2"]["value"])
    if x <= 0 or t <= 0: return None
    return {"account": a["account"], "x": x, "t": t, "spot": x / t, "fee": a["trading_fee"] / 100000.0,
            "frozen": bool(a.get("asset2_frozen") or a.get("asset_frozen")), "tf": tf}

# ---------------- discovery ----------------
def discover(meta):
    d = CFG["discovery"]; found = {}
    def add(t, src, rank=None):
        cur, iss = t.get("currency"), t.get("issuer")
        if not cur or not iss or cur == "XRP": return
        k = key(cur, iss)
        e = found.setdefault(k, {"currency": cur, "issuer": iss, "name": t.get("name") or cur_name(cur), "sources": [], "x": t.get("_x")})
        e["sources"].append(src if rank is None else f"{src}#{rank}")
        if t.get("_x"): e["x"] = t["_x"]
    ok = 0
    for src, q, lim in [("new", "sortBy=dateon&sortType=desc", d["xrplto_newest_limit"]),
                        ("trending", "sortBy=trendingScore&sortType=desc", d["xrplto_trending_limit"])]:
        try:
            url = f"{XRPLTO}?start=0&limit={lim}&{q}&filter="
            use_key = bool(XRPLTO_KEY) and NOW - meta.get("key_rejected_t", 0) > 3600
            try: r = http_json(url, headers={"X-Api-Key": XRPLTO_KEY} if use_key else None)
            except urllib.error.HTTPError as he:
                if not (use_key and he.code in (401, 402, 403)): raise
                meta["key_rejected_t"] = NOW  # bad/expired key or out of credits: go anonymous (and throttled) for 1h
                WARN.append(f"xrpl.to rejected the API key (HTTP {he.code}); using anonymous access, 15-min throttle for 1h")
                r = http_json(url)
            toks = r.get("tokens") or []
            for i, t in enumerate(toks, 1):
                t["_x"] = t
                if src == "new":
                    age_h = (NOW * 1000 - (t.get("dateon") or 0)) / 3.6e6
                    if age_h > d["new_max_age_hours"]: continue
                    add(t, "new")
                else:
                    add(t, "trending", i)
            ok += 1
        except Exception as e:
            msg = repr(e).replace(XRPLTO_KEY, "***") if XRPLTO_KEY else repr(e)
            WARN.append(f"xrpl.to {src} list failed: {msg}")
    meta["xrplto_ok"] = ok
    if ok == 0:  # fallback: scan recent ledgers for AMMCreate XRP/<token> pools
        try:
            for c in ledger_new_pools(meta): add(c, "ledger-ammcreate")
        except Exception as e:
            WARN.append(f"ledger AMMCreate fallback failed: {e!r}")
    return found

def ledger_new_pools(meta):
    cur_l = int(rpc("ledger", {"ledger_index": "validated"})["ledger"]["ledger_index"])
    start = max(meta.get("last_scanned_ledger", 0) + 1, cur_l - CFG["discovery"]["ledger_fallback_max_ledgers"] + 1)
    out = []
    for li in range(start, cur_l + 1):
        lg = rpc("ledger", {"ledger_index": li, "transactions": True, "expand": True}).get("ledger", {})
        for tx in lg.get("transactions", []):
            tj = tx.get("tx_json", tx)
            meta_ = tx.get("meta") or tx.get("metaData") or {}
            if tj.get("TransactionType") != "AMMCreate" or meta_.get("TransactionResult") != "tesSUCCESS": continue
            a, b = tj.get("Amount"), tj.get("Amount2")
            iou = b if isinstance(a, str) and isinstance(b, dict) else a if isinstance(b, str) and isinstance(a, dict) else None
            if iou: out.append({"currency": iou["currency"], "issuer": iou["issuer"], "name": cur_name(iou["currency"])})
    meta["last_scanned_ledger"] = cur_l
    return out

# ---------------- safety ----------------
def issuer_info(iss):
    r = rpc("account_info", {"account": iss, "ledger_index": "validated", "signer_lists": True})
    if "account_data" not in r: raise RuntimeError(f"account_info {iss}: {r.get('error')}")
    a = r["account_data"]; f = a.get("Flags", 0)
    rk = a.get("RegularKey")
    signers = r.get("signer_lists") or a.get("signer_lists") or []
    tr = a.get("TransferRate", 0)
    return {"master_disabled": bool(f & 0x00100000), "no_freeze": bool(f & 0x00200000), "global_freeze": bool(f & 0x00400000),
            "clawback": bool(f & 0x80000000), "require_auth": bool(f & 0x00040000), "regular_key": rk, "has_signers": bool(signers),
            "blackholed": bool(f & 0x00100000) and (rk is None or rk in BLACKHOLES) and not signers,
            "transfer_fee_pct": 0.0 if tr in (0, 1000000000) else (tr / 1e9 - 1) * 100}

def top10_pct(cur, iss, amm_acct):
    """Top-10 holders' share of supply, excluding the AMM pool account (issuer holds no balance of its own token)."""
    bal, marker, pages = [], None, 0
    while True:
        p = {"account": iss, "ledger_index": "validated", "limit": 400}
        if marker: p["marker"] = marker
        r = rpc("account_lines", p); pages += 1
        for ln in r.get("lines", []):
            if ln.get("currency") != cur: continue
            v = -float(ln["balance"])
            if v > 0: bal.append((v, ln["account"]))
        marker = r.get("marker")
        if not marker: break
        if pages >= CFG["safety"]["holder_scan_max_pages"]: return None, len(bal)  # too many holders to scan cheaply
    supply = sum(v for v, _ in bal)
    if supply <= 0: return None, 0
    top = sorted((v for v, a in bal if a != amm_acct and a not in BLACKHOLES), reverse=True)[:10]
    return sum(top) / supply * 100, len(bal)

def check(tok, seen_entry, need_conc=True):
    """Run safety checks. Returns dict with pass/fail, reasons, warnings, pool."""
    s = CFG["safety"]; d = CFG["discovery"]; x = tok.get("x") or {}
    res = {"hard_fail": [], "warn": [], "pool": None, "issuer": None, "top10": None, "top10_src": ""}
    tags = x.get("tags") or []
    bad_tags = [t for t in tags if t in d["exclude_tags"]]
    if bad_tags: res["hard_fail"].append("excluded tag: " + "/".join(bad_tags))
    if (tok["name"] or "").upper() in d["exclude_names"] or x.get("kyc"): res["hard_fail"].append("not a meme (stablecoin/major/KYC issuer)")
    # cheap prefilter from xrpl.to TVL (TVL counts both sides) to save ledger calls
    tvl = x.get("tvl")
    if tvl is not None and tvl / 2 < s["min_pool_xrp"] * 0.8:
        res["hard_fail"].append(f"pool too small (xrpl.to TVL {tvl:,.0f} XRP)")
    if res["hard_fail"]: return res
    ii = issuer_info(tok["issuer"]); res["issuer"] = ii
    if ii["clawback"] and s["reject_clawback"]: res["hard_fail"].append("issuer has clawback enabled")
    if ii["require_auth"] and s["reject_require_auth"]: res["hard_fail"].append("issuer requires authorization")
    if ii["global_freeze"] and s["reject_global_freeze"]: res["hard_fail"].append("issuer global freeze ON")
    if ii["transfer_fee_pct"] > s["max_transfer_fee_pct"]: res["hard_fail"].append(f"transfer fee {ii['transfer_fee_pct']:.2f}%")
    if s["require_blackholed_issuer"] and not ii["blackholed"]:
        res["hard_fail"].append("issuer not blackholed (can still mint" + ("" if ii["no_freeze"] else "/freeze") + ")")
    if not ii["blackholed"] and not ii["no_freeze"]: res["warn"].append("issuer can freeze trust lines")
    pool = get_pool(tok["currency"], tok["issuer"], ii["transfer_fee_pct"] / 100)
    res["pool"] = pool
    if not pool: res["hard_fail"].append("no XRP AMM pool"); return res
    if pool["frozen"]: res["hard_fail"].append("AMM asset frozen")
    if pool["x"] < s["min_pool_xrp"]: res["hard_fail"].append(f"pool {pool['x']:,.0f} XRP < {s['min_pool_xrp']:,}")
    lpb = x.get("lpBurnedPercent")
    if lpb is not None and lpb < s["warn_lp_burned_below_pct"]: res["warn"].append(f"only {lpb:.0f}% of LP burned (liquidity can be pulled)")
    if res["hard_fail"]: return res
    # holder concentration (expensive): cache for 6h
    c = seen_entry.get("top10_cache")
    if c and NOW - c["t"] < 6 * 3600: res["top10"], res["top10_src"] = c["v"], c["src"]
    elif not need_conc:  # not entry-eligible anyway: use free xrpl.to figure, skip the paged ledger scan
        if x.get("top10") is not None: res["top10"], res["top10_src"] = float(x["top10"]), "xrpl.to"
    else:
        v, n = top10_pct(tok["currency"], tok["issuer"], pool["account"]); src = f"ledger ({n} holders)"
        if v is None and x.get("top10") is not None: v, src = float(x["top10"]), "xrpl.to (too many holders to scan)"
        res["top10"], res["top10_src"] = v, src
        seen_entry["top10_cache"] = {"t": NOW, "v": v, "src": src}
    if res["top10"] is None: res["warn"].append("top-10 concentration unknown")
    elif res["top10"] > s["max_top10_pct"]: res["hard_fail"].append(f"top-10 holders own {res['top10']:.0f}% (excl. AMM)")
    elif res["top10"] > s["warn_top10_pct"]: res["warn"].append(f"top-10 holders own {res['top10']:.0f}%")
    return res

# ---------------- strategy bankrolls / exits ----------------
STRATS = list(CFG["exits"].keys())
BOOK_FIELDS = ["ts", "label", "strategy", "token", "issuer", "currency", "sources", "usd", "xrp_usd", "xrp_in", "spot_xrp_per_token",
               "fill_xrp_per_token", "tokens", "buy_cost_pct_vs_spot", "amm_fee_pct", "transfer_fee_pct", "round_trip_cost_pct",
               "pool_xrp", "cash_after_usd", "warnings", "note"]

def new_book(px):
    b = CFG["bankroll"]
    return {"start_usd": b["start_usd"], "start_xrp_usd": px, "cash_usd": b["start_usd"], "day": "", "buys_today": 0,
            "positions": [], "closed": [], "last_exit": {}}

def migrate_v1(books, px):
    """One-time: seed every strategy with the 10 shared v1 paper buys (same fills/timestamps), $100 fully deployed."""
    old = load("positions.json", None)
    if old is None: return
    for s in STRATS:
        bk = books.setdefault(s, new_book(old[0]["xrp_usd_entry"] if old else px))
        for p in old:
            bk["positions"].append({k: p[k] for k in ("key", "name", "currency", "issuer", "t", "ts", "tf", "usd_cost", "xrp_usd_entry",
                "xrp_cost", "tokens_net", "tokens_gross", "entry_spot", "entry_eff_px", "pool_xrp_entry", "amm_fee", "warnings")}
                | {"remaining": 1.0, "tp_done": False, "legs": [], "seeded_from_v1": True})
            bk["cash_usd"] -= p["usd_cost"]
        bk["day"], bk["buys_today"] = old[0]["ts"][:10] if old else "", len(old)
        bk["cash_usd"] = round(bk["cash_usd"], 6)
    # old paper_buys.csv -> new columns, tagged as the shared seed
    pb = os.path.join(LOGS, "paper_buys.csv")
    if os.path.exists(pb):
        rows = list(csv.DictReader(open(pb)))
        with open(pb, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=BOOK_FIELDS, extrasaction="ignore"); w.writeheader()
            for r in rows: r["strategy"] = "hold+plus5+scalp (v1 seed)"; w.writerow(r)
    os.replace(os.path.join(STATE, "positions.json"), os.path.join(STATE, "positions_v1_migrated.json"))
    WARN.append("migrated v1 shared positions into 3 bankrolls")

def close_part(bk, pos, sname, frac, reason, pool, px):
    tokens = pos["tokens_net"] * frac
    xrp_net, _ = sim_sell(pool, tokens)
    xrp_gross = pos["tokens_gross"] * frac * pool["spot"] if pool else 0.0
    cost_xrp, cost_usd = pos["xrp_cost"] * frac, pos["usd_cost"] * frac
    usd_net, usd_gross = xrp_net * px, xrp_gross * px
    bk["cash_usd"] = round(bk["cash_usd"] + usd_net, 6)
    row = {"ts": TS, "label": LABEL, "strategy": sname, "token": pos["name"], "issuer": pos["issuer"], "reason": reason,
           "fraction_of_buy": round(frac, 4), "hours_held": round((NOW - pos["t"]) / 3600, 2),
           "entry_spot_xrp": pos["entry_spot"], "exit_spot_xrp": pool["spot"] if pool else 0,
           "cost_xrp": round(cost_xrp, 6), "proceeds_xrp_net": round(xrp_net, 6), "proceeds_xrp_gross": round(xrp_gross, 6),
           "pnl_xrp_net": round(xrp_net - cost_xrp, 6), "pnl_xrp_gross": round(xrp_gross - cost_xrp, 6),
           "cost_usd": round(cost_usd, 4), "xrp_usd": px, "proceeds_usd_net": round(usd_net, 4),
           "pnl_usd_net": round(usd_net - cost_usd, 4), "pnl_usd_gross": round(usd_gross - cost_usd, 4),
           "cash_after_usd": round(bk["cash_usd"], 4), "note": "exit at price observed at the ~5-min poll, not the exact trigger level"}
    append("exits.csv", row, list(row.keys()))
    pos["remaining"] = round(pos["remaining"] - frac, 10)
    pos["legs"].append({k: row[k] for k in ("ts", "reason", "fraction_of_buy", "pnl_xrp_net", "pnl_xrp_gross", "pnl_usd_net", "pnl_usd_gross")})

def manage(bk, sname, pool, px):
    rule = CFG["exits"][sname]; still = []
    for pos in bk["positions"]:
        age_h = (NOW - pos["t"]) / 3600
        if pool.get(pos["key"], "err") == "err": still.append(pos); continue  # couldn't price this run: hold
        pl = pool[pos["key"]]
        if pl is None: close_part(bk, pos, sname, pos["remaining"], "pool gone (rug?) -> 0", None, px)
        else:
            net, _ = sim_sell(pl, pos["tokens_net"]); ratio = net / pos["xrp_cost"]
            pos["last_ratio_net"] = round(ratio, 4)
            if not pos["tp_done"] and ratio >= rule["take_profit_mult"]:
                close_part(bk, pos, sname, min(rule["take_profit_fraction"], pos["remaining"]), f"take profit (x{ratio:.2f} net)", pl, px)
                pos["tp_done"] = True
            if pos["remaining"] > 1e-9:
                if ratio <= rule["stop_mult"]: close_part(bk, pos, sname, pos["remaining"], f"stop (x{ratio:.2f} net)", pl, px)
                elif age_h >= rule["max_hours"]: close_part(bk, pos, sname, pos["remaining"], f"time limit {rule['max_hours']}h (x{ratio:.2f} net)", pl, px)
        if pos["remaining"] > 1e-9: still.append(pos)
        else:
            pos["closed_ts"] = TS; pos["pnl_usd_net"] = round(sum(l["pnl_usd_net"] for l in pos["legs"]), 4)
            pos["pnl_xrp_net"] = round(sum(l["pnl_xrp_net"] for l in pos["legs"]), 6)
            bk["closed"].append(pos); bk["last_exit"][pos["key"]] = NOW
    bk["positions"] = still

def book_stats(bk, pools, px):
    open_val = open_cost = 0.0; unknown = 0
    for p in bk["positions"]:
        pl = pools.get(p["key"])
        if not isinstance(pl, dict): unknown += 1; open_cost += p["usd_cost"] * p["remaining"]; open_val += p["usd_cost"] * p["remaining"]; continue
        open_val += sim_sell(pl, p["tokens_net"] * p["remaining"])[0] * px
        open_cost += p["usd_cost"] * p["remaining"]
    legs = [l for p in bk["positions"] + bk["closed"] for l in p["legs"]]
    realized = sum(l["pnl_usd_net"] for l in legs); realized_g = sum(l["pnl_usd_gross"] for l in legs)
    realized_x = sum(l["pnl_xrp_net"] for l in legs)
    wins = sum(1 for p in bk["closed"] if p["pnl_usd_net"] > 0)
    eq = bk["cash_usd"] + open_val
    return {"cash": bk["cash_usd"], "open_n": len(bk["positions"]), "open_val": open_val, "unrealized": open_val - open_cost,
            "realized": realized, "realized_gross": realized_g, "realized_xrp": realized_x, "equity": eq, "equity_xrp": eq / px,
            "start_xrp": bk["start_usd"] / bk["start_xrp_usd"], "closed_n": len(bk["closed"]),
            "trades": len(bk["closed"]) + len(bk["positions"]), "win_rate": (wins / len(bk["closed"]) * 100) if bk["closed"] else None,
            "unpriced": unknown}

# ---------------- main ----------------
def main():
    t0 = time.time()
    os.makedirs(STATE, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
    meta = load("meta.json", {}); seen = load("seen.json", {}); books = load("strategies.json", {})
    px, px_src = xrp_usd()
    meta["xrp_usd"], meta["xrp_usd_src"] = px, px_src
    migrate_v1(books, px)
    for s in STRATS: books.setdefault(s, new_book(px))
    day = TS[:10]
    for bk in books.values():
        if bk["day"] != day: bk["day"], bk["buys_today"] = day, 0

    # 1) every run: price all open positions from the ledger (one amm_info per unique token) and apply exits
    pools = {}
    for bk in books.values():
        for p in bk["positions"]:
            if p["key"] in pools: continue
            try: pools[p["key"]] = get_pool(p["currency"], p["issuer"], p["tf"])
            except Exception as e: pools[p["key"]] = "err"; WARN.append(f"could not price {p['name']}: {e!r}")
    for s in STRATS: manage(books[s], s, pools, px)

    # 2) discovery + safety only if >= 15 min since the last one (keeps xrpl.to at <= 2 calls / 15 min)
    stats = {"discovery": False, "seen": 0, "checked": 0, "passed": 0, "bought": {s: 0 for s in STRATS}}
    since = NOW - meta.get("last_discovery_t", 0)
    keyed = bool(XRPLTO_KEY) and NOW - meta.get("key_rejected_t", 0) > 3600
    interval_min = 0 if keyed else CFG["discovery"]["min_interval_minutes"]  # keyed: discover every run; anonymous: throttle
    meta["xrplto_keyed"] = keyed
    if since >= interval_min * 60:
        stats["discovery"] = True; meta["last_discovery_t"] = NOW; meta["last_discovery"] = TS
        eligible = discover_and_check(meta, seen, books, px, stats)
        buy_round(books, eligible, px, stats, pools)
        save("seen.json", seen)
    else:
        stats["next_discovery_in_min"] = round((interval_min * 60 - since) / 60, 1)

    stats["runtime_s"] = round(time.time() - t0, 1)
    meta.update(last_run=TS, last_stats=stats, warnings=WARN[-20:])
    save("meta.json", meta); save("strategies.json", books)
    write_summary(meta, seen, books, pools, px, stats)
    out = {s: {k: (round(v, 2) if isinstance(v, float) else v) for k, v in book_stats(books[s], pools, px).items()} for s in STRATS}
    print(json.dumps({"ts": TS, "xrp_usd": px, **stats, "books": out, "warnings": WARN}, indent=1))

def discover_and_check(meta, seen, books, px, stats):
    found = discover(meta); stats["seen"] = len(found)
    held_by_all = set.intersection(*[{p["key"] for p in books[s]["positions"]} for s in STRATS])
    eligible = []
    cand_fields = ["ts", "label", "token", "issuer", "currency", "sources", "verdict", "reasons", "warnings", "pool_xrp", "amm_fee_pct",
                   "transfer_fee_pct", "blackholed", "no_freeze", "clawback", "global_freeze", "top10_pct", "top10_src",
                   "vol24h_xrp", "age_h", "round_trip_cost_pct", "url"]
    for k, tok in found.items():
        se = seen.setdefault(k, {"first_seen": TS, "name": tok["name"]})
        x = tok.get("x") or {}
        is_new = any(s.startswith("new") or s.startswith("ledger") for s in tok["sources"])
        top = any(s.startswith("trending#") and int(s.split("#")[1]) <= CFG["discovery"]["trending_top_n"] for s in tok["sources"])
        try: r = check(tok, se, need_conc=(is_new or top) and k not in held_by_all); stats["checked"] += 1
        except Exception as e:
            WARN.append(f"safety check error {tok['name']}: {e!r}"); continue
        pool, ii = r["pool"], r["issuer"] or {}
        rt = None
        if pool:
            xin = CFG["buy_usd"] / px; tn, _ = sim_buy(pool, xin)
            p2 = dict(pool, x=pool["x"] + xin * (1 - pool["fee"]), t=pool["t"] - tn)
            back, _ = sim_sell(p2, tn); rt = (1 - back / xin) * 100
        entry_fail = []
        if not r["hard_fail"]:
            if not (is_new or top): entry_fail.append("not new and not top trending")
            v = x.get("vol24hxrp")
            if v is not None and v < CFG["entry"]["min_vol24h_xrp"]: entry_fail.append(f"24h volume {v:,.0f} XRP too low")
            if rt is not None and rt > CFG["entry"]["max_round_trip_cost_pct"]: entry_fail.append(f"round-trip cost {rt:.1f}% too high")
        verdict = "FAIL_SAFETY" if r["hard_fail"] else ("SKIP_ENTRY" if entry_fail else "PASS")
        if verdict == "PASS": stats["passed"] += 1
        reasons = "; ".join(r["hard_fail"] + entry_fail)
        age_h = round((NOW * 1000 - x["dateon"]) / 3.6e6, 1) if x.get("dateon") else ""
        row = {"ts": TS, "label": LABEL, "token": tok["name"], "issuer": tok["issuer"], "currency": tok["currency"],
               "sources": "|".join(tok["sources"]), "verdict": verdict, "reasons": reasons, "warnings": "; ".join(r["warn"]),
               "pool_xrp": round(pool["x"]) if pool else (round(x["tvl"] / 2) if x.get("tvl") else ""),
               "amm_fee_pct": round(pool["fee"] * 100, 3) if pool else "",
               "transfer_fee_pct": round(ii.get("transfer_fee_pct", 0), 3) if ii else "", "blackholed": ii.get("blackholed", ""),
               "no_freeze": ii.get("no_freeze", ""), "clawback": ii.get("clawback", ""), "global_freeze": ii.get("global_freeze", ""),
               "top10_pct": round(r["top10"], 1) if r["top10"] is not None else "", "top10_src": r["top10_src"],
               "vol24h_xrp": round(x["vol24hxrp"]) if x.get("vol24hxrp") is not None else "", "age_h": age_h,
               "round_trip_cost_pct": round(rt, 2) if rt is not None else "",
               "url": f"https://xrpl.to/token/{tok['issuer']}-{tok['currency']}"}
        sig = verdict + "|" + reasons
        if se.get("sig") != sig: append("candidates.csv", row, cand_fields); se["sig"] = sig
        se.update(last_seen=TS, verdict=verdict, reasons=reasons, warnings=row["warnings"], name=tok["name"], pool_xrp=row["pool_xrp"], url=row["url"])
        if verdict == "PASS": eligible.append((0 if is_new else 1, -(x.get("trendingScore") or 0), k, tok, r, rt))
    eligible.sort(key=lambda e: (e[0], e[1]))
    return eligible

def buy_round(books, eligible, px, stats, pools):
    b = CFG["bankroll"]
    for s in STRATS:
        bk = books[s]; held = {p["key"] for p in bk["positions"]}
        for _, _, k, tok, r, rt in eligible:
            if bk["cash_usd"] + 1e-9 < CFG["buy_usd"] or bk["buys_today"] >= b["max_new_buys_per_day_utc"]: break
            if k in held: continue
            if NOW - bk["last_exit"].get(k, 0) < b["rebuy_cooldown_hours"] * 3600: continue
            pool = r["pool"]; xin = CFG["buy_usd"] / px
            tn, tg = sim_buy(pool, xin); eff = xin / tn
            pos = {"key": k, "name": tok["name"], "currency": tok["currency"], "issuer": tok["issuer"], "t": NOW, "ts": TS, "tf": pool["tf"],
                   "usd_cost": CFG["buy_usd"], "xrp_usd_entry": px, "xrp_cost": xin, "tokens_net": tn, "tokens_gross": tg,
                   "entry_spot": pool["spot"], "entry_eff_px": eff, "pool_xrp_entry": pool["x"], "amm_fee": pool["fee"],
                   "warnings": r["warn"], "remaining": 1.0, "tp_done": False, "legs": []}
            bk["positions"].append(pos); held.add(k); bk["buys_today"] += 1; stats["bought"][s] += 1
            bk["cash_usd"] = round(bk["cash_usd"] - CFG["buy_usd"], 6); pools.setdefault(k, pool)
            row = {"ts": TS, "label": LABEL, "strategy": s, "token": tok["name"], "issuer": tok["issuer"], "currency": tok["currency"],
                   "sources": "|".join(tok["sources"]), "usd": CFG["buy_usd"], "xrp_usd": px, "xrp_in": round(xin, 6),
                   "spot_xrp_per_token": pool["spot"], "fill_xrp_per_token": eff, "tokens": tn,
                   "buy_cost_pct_vs_spot": round((eff / pool["spot"] - 1) * 100, 3), "amm_fee_pct": round(pool["fee"] * 100, 3),
                   "transfer_fee_pct": round(pool["tf"] * 100, 3), "round_trip_cost_pct": round(rt, 3) if rt is not None else "",
                   "pool_xrp": round(pool["x"]), "cash_after_usd": round(bk["cash_usd"], 4), "warnings": "; ".join(r["warn"]),
                   "note": "simulated AMM fill incl. pool fee, slippage, transfer fee; CLOB ignored; trust line reserve 0.2 XRP not counted"}
            append("paper_buys.csv", row, BOOK_FIELDS)

def write_summary(meta, seen, books, pools, px, stats):
    L = [f"# XRPL meme scanner — PAPER ONLY ({LABEL})", "",
         "Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.",
         "Data by <a href=\"https://xrpl.to\">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.", "",
         f"Last run: **{meta['last_run']}** (UTC) · XRP/USD {px:.4f} ({meta['xrp_usd_src']}) · last discovery {meta.get('last_discovery', '–')} (UTC, {'every run, API key' if meta.get('xrplto_keyed') else 'every ≥15 min, anonymous'})", ""]
    if meta.get("warnings"): L += ["**Warnings this run:** " + " | ".join(meta["warnings"]), ""]
    desc = {"hold": "½ at +100%, stop −50%, 72h", "plus5": "all at +50%, stop −50%, 72h", "scalp": "+20% / −10% / 60 min"}
    L += ["## Bankrolls (each strategy started with its own $100)", "",
          "| Strategy | Rule | Cash | Open (n / value) | Equity USD | vs $100 | Equity XRP | vs start XRP | Realized net | Unrealized net | Win rate | Trades (closed) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in STRATS:
        st = book_stats(books[s], pools, px)
        wr = f"{st['win_rate']:.0f}%" if st["win_rate"] is not None else "–"
        L.append(f"| {s} | {desc.get(s, '')} | ${st['cash']:.2f} | {st['open_n']} / ${st['open_val']:.2f} | ${st['equity']:.2f} | {st['equity'] - books[s]['start_usd']:+.2f} | "
                 f"{st['equity_xrp']:.2f} | {st['equity_xrp'] - st['start_xrp']:+.2f} | ${st['realized']:+.2f} | ${st['unrealized']:+.2f} | {wr} | {st['trades']} ({st['closed_n']}) |")
    L += ["", "Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee "
          "(open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. "
          "Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. "
          "Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level.", ""]
    for s in STRATS:
        bk = books[s]
        L += [f"### {s} — open positions ({len(bk['positions'])})", ""]
        if bk["positions"]:
            L += ["| Token | Bought (UTC) | Cost | Now (net, x) | Warnings |", "|---|---|---|---|---|"]
            for p in sorted(bk["positions"], key=lambda p: p["t"], reverse=True):
                L.append(f"| [{p['name']}](https://xrpl.to/token/{p['issuer']}-{p['currency']}) | {p['ts'][:16]} | ${p['usd_cost'] * p['remaining']:.2f} | "
                         f"{p.get('last_ratio_net', 1):.2f} | {'; '.join(p['warnings'])} |")
        else: L.append("None.")
        L.append("")
    L += ["## Recently rejected (latest verdict per token)", "", "| Token | Verdict | Reasons | Pool XRP |", "|---|---|---|---|"]
    rej = sorted([v for v in seen.values() if v.get("verdict") and v["verdict"] != "PASS"], key=lambda v: v.get("last_seen", ""), reverse=True)[:40]
    for v in rej: L.append(f"| [{v['name']}]({v.get('url','')}) | {v['verdict']} | {v.get('reasons','')} | {v.get('pool_xrp','')} |")
    L += ["", "Logs: `logs/candidates.csv`, `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
