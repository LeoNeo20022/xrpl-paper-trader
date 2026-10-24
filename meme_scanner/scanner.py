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
XRPLTO = "https://api.xrpl.to/api/tokens"
BLACKHOLES = {"rrrrrrrrrrrrrrrrrrrrrhoLvTp", "rrrrrrrrrrrrrrrrrrrrBZbvji", "rrrrrrrrrrrrrrrrrNAMEtxvNvQ", "rrrrrrrrrrrrrrrrrrrn5RM1rHd"}
LABEL = "PAPER-NOT-ON-LEDGER"
UA = {"User-Agent": "xrpl-paper-meme-scanner (log-only; github.com/LeoNeo20022/xrpl-paper-trader)"}
NOW = time.time()
TS = datetime.fromtimestamp(NOW, timezone.utc).isoformat(timespec="seconds")
WARN = []  # source/API problems this run, shown in SUMMARY

# ---------------- io helpers ----------------
def http_json(url, body=None, timeout=25):
    h = dict(UA)
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
            r = http_json(f"{XRPLTO}?start=0&limit={lim}&{q}&filter=")
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
            WARN.append(f"xrpl.to {src} list failed: {e!r}")
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

# ---------------- positions / exits ----------------
STRATS = list(CFG["exits"].keys())

def close_part(pos, sname, frac_of_original, reason, pool, px_usd):
    st = pos["strategies"][sname]
    tokens = pos["tokens_net"] * frac_of_original
    tokens_g = pos["tokens_gross"] * frac_of_original
    xrp_net, _ = sim_sell(pool, tokens)
    xrp_gross = tokens_g * pool["spot"] if pool else 0.0
    cost_xrp = pos["xrp_cost"] * frac_of_original; cost_usd = pos["usd_cost"] * frac_of_original
    row = {"ts": TS, "label": LABEL, "token": pos["name"], "issuer": pos["issuer"], "strategy": sname, "reason": reason,
           "fraction_of_buy": round(frac_of_original, 4), "hours_held": round((NOW - pos["t"]) / 3600, 2),
           "entry_spot_xrp": pos["entry_spot"], "exit_spot_xrp": pool["spot"] if pool else 0,
           "cost_xrp": round(cost_xrp, 6), "proceeds_xrp_net": round(xrp_net, 6), "proceeds_xrp_gross": round(xrp_gross, 6),
           "pnl_xrp_net": round(xrp_net - cost_xrp, 6), "pnl_xrp_gross": round(xrp_gross - cost_xrp, 6),
           "cost_usd": round(cost_usd, 4), "xrp_usd": px_usd,
           "pnl_usd_net": round(xrp_net * px_usd - cost_usd, 4), "pnl_usd_gross": round(xrp_gross * px_usd - cost_usd, 4),
           "note": "exit at price observed at 15-min poll, not the exact trigger level"}
    append("exits.csv", row, list(row.keys()))
    st["remaining"] = round(st["remaining"] - frac_of_original, 10)
    st.setdefault("closed", []).append({k: row[k] for k in ("reason", "fraction_of_buy", "pnl_xrp_net", "pnl_xrp_gross", "pnl_usd_net", "pnl_usd_gross", "cost_xrp", "cost_usd")})
    if st["remaining"] <= 1e-9: st["open"] = False; st["closed_ts"] = TS

def manage(pos, pool, px_usd):
    age_h = (NOW - pos["t"]) / 3600
    # mark-to-market ratio of what we'd actually get (net) vs what we paid
    full_net, _ = sim_sell(pool, pos["tokens_net"])
    ratio = full_net / pos["xrp_cost"] if pos["xrp_cost"] else 0
    pos["last_ratio_net"] = round(ratio, 4); pos["last_spot"] = pool["spot"] if pool else 0; pos["last_mark_ts"] = TS
    for sname, rule in CFG["exits"].items():
        st = pos["strategies"][sname]
        if not st["open"]: continue
        if pool is None: close_part(pos, sname, st["remaining"], "pool gone (rug?) -> 0", None, px_usd); continue
        if not st.get("tp_done") and ratio >= rule["take_profit_mult"]:
            f = min(rule["take_profit_fraction"], st["remaining"])
            close_part(pos, sname, f, f"take profit (x{ratio:.2f} net)", pool, px_usd); st["tp_done"] = True
            if not st["open"]: continue
        if ratio <= rule["stop_mult"]: close_part(pos, sname, st["remaining"], f"stop (x{ratio:.2f} net)", pool, px_usd)
        elif age_h >= rule["max_hours"]: close_part(pos, sname, st["remaining"], f"time limit {rule['max_hours']}h (x{ratio:.2f} net)", pool, px_usd)
    pos["open"] = any(s["open"] for s in pos["strategies"].values())

# ---------------- main ----------------
def main():
    os.makedirs(STATE, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
    meta = load("meta.json", {}); seen = load("seen.json", {}); positions = load("positions.json", [])
    px, px_src = xrp_usd()
    meta["xrp_usd"], meta["xrp_usd_src"] = px, px_src

    # 1) mark open positions (ledger only, independent of discovery API)
    for pos in positions:
        if not pos["open"]: continue
        try:
            pool = get_pool(pos["currency"], pos["issuer"], pos["tf"])
            manage(pos, pool, px)
        except Exception as e: WARN.append(f"could not mark {pos['name']}: {e!r}")

    # 2) discover + safety
    found = discover(meta)
    owned = {key(p["currency"], p["issuer"]) for p in positions}
    day = TS[:10]
    if meta.get("day") != day: meta["day"], meta["buys_today"] = day, 0
    open_n = sum(1 for p in positions if p["open"])
    stats = {"seen": len(found), "checked": 0, "passed": 0, "bought": 0, "rejected": 0}
    eligible = []
    cand_fields = ["ts", "label", "token", "issuer", "currency", "sources", "verdict", "reasons", "warnings", "pool_xrp", "amm_fee_pct",
                   "transfer_fee_pct", "blackholed", "no_freeze", "clawback", "global_freeze", "top10_pct", "top10_src",
                   "vol24h_xrp", "age_h", "round_trip_cost_pct", "url"]
    for k, tok in found.items():
        se = seen.setdefault(k, {"first_seen": TS, "name": tok["name"]})
        x = tok.get("x") or {}
        is_new = any(s.startswith("new") or s.startswith("ledger") for s in tok["sources"])
        top = any(s.startswith("trending#") and int(s.split("#")[1]) <= CFG["discovery"]["trending_top_n"] for s in tok["sources"])
        try: r = check(tok, se, need_conc=(is_new or top) and k not in owned); stats["checked"] += 1
        except Exception as e:
            WARN.append(f"safety check error {tok['name']}: {e!r}"); continue
        pool, ii = r["pool"], r["issuer"] or {}
        rt = None
        if pool:
            xin = CFG["buy_usd"] / px; tn, _ = sim_buy(pool, xin)
            p2 = dict(pool, x=pool["x"] + xin * (1 - pool["fee"]), t=pool["t"] - tn)  # pool after our buy
            back, _ = sim_sell(p2, tn); rt = (1 - back / xin) * 100
        entry_fail = []
        if not r["hard_fail"]:
            if not (is_new or top): entry_fail.append("not new and not top trending")
            v = x.get("vol24hxrp")
            if v is not None and v < CFG["entry"]["min_vol24h_xrp"]: entry_fail.append(f"24h volume {v:,.0f} XRP too low")
            if rt is not None and rt > CFG["entry"]["max_round_trip_cost_pct"]: entry_fail.append(f"round-trip cost {rt:.1f}% too high")
        verdict = "FAIL_SAFETY" if r["hard_fail"] else ("SKIP_ENTRY" if entry_fail else "PASS")
        if verdict == "PASS": stats["passed"] += 1
        else: stats["rejected"] += 1
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
        # log a candidate row on first sight or when its verdict/reasons change (keeps the CSV small)
        sig = verdict + "|" + reasons
        if se.get("sig") != sig: append("candidates.csv", row, cand_fields); se["sig"] = sig
        se.update(last_seen=TS, verdict=verdict, reasons=reasons, warnings=row["warnings"], name=tok["name"], pool_xrp=row["pool_xrp"],
                  url=row["url"])
        if verdict == "PASS" and k not in owned: eligible.append((0 if is_new else 1, -(x.get("trendingScore") or 0), k, tok, r, rt))

    # 3) paper buys (once per token, capped)
    eligible.sort(key=lambda e: (e[0], e[1]))
    for _, _, k, tok, r, rt in eligible:
        if open_n >= CFG["max_open_positions"]: WARN.append("max open positions reached; skipped further buys"); break
        if meta["buys_today"] >= CFG["max_new_buys_per_day_utc"]: WARN.append("daily buy cap reached; skipped further buys"); break
        pool = r["pool"]; xin = CFG["buy_usd"] / px
        tn, tg = sim_buy(pool, xin)
        eff_px = xin / tn
        pos = {"key": k, "name": tok["name"], "currency": tok["currency"], "issuer": tok["issuer"], "t": NOW, "ts": TS, "tf": pool["tf"],
               "usd_cost": CFG["buy_usd"], "xrp_usd_entry": px, "xrp_cost": xin, "tokens_net": tn, "tokens_gross": tg,
               "entry_spot": pool["spot"], "entry_eff_px": eff_px, "pool_xrp_entry": pool["x"], "amm_fee": pool["fee"],
               "sources": tok["sources"], "warnings": r["warn"], "open": True,
               "strategies": {s: {"open": True, "remaining": 1.0} for s in STRATS}}
        positions.append(pos); owned.add(k); open_n += 1; meta["buys_today"] += 1; stats["bought"] += 1
        slip = (eff_px / pool["spot"] - 1) * 100
        row = {"ts": TS, "label": LABEL, "token": tok["name"], "issuer": tok["issuer"], "currency": tok["currency"],
               "sources": "|".join(tok["sources"]), "usd": CFG["buy_usd"], "xrp_usd": px, "xrp_in": round(xin, 6),
               "spot_xrp_per_token": pool["spot"], "fill_xrp_per_token": eff_px, "tokens": tn,
               "buy_cost_pct_vs_spot": round(slip, 3), "amm_fee_pct": round(pool["fee"] * 100, 3),
               "transfer_fee_pct": round(pool["tf"] * 100, 3), "round_trip_cost_pct": round(rt, 3) if rt is not None else "",
               "pool_xrp": round(pool["x"]), "warnings": "; ".join(r["warn"]),
               "note": "simulated AMM fill incl. pool fee, slippage, transfer fee; CLOB ignored; trust line reserve 0.2 XRP not counted"}
        append("paper_buys.csv", row, list(row.keys()))
        pos["buy_cost_pct"] = round(slip, 3); pos["round_trip_cost_pct"] = row["round_trip_cost_pct"]

    meta.update(last_run=TS, last_stats=stats, warnings=WARN[-20:])
    save("meta.json", meta); save("seen.json", seen); save("positions.json", positions)
    write_summary(meta, seen, positions, stats)
    print(json.dumps({"ts": TS, "xrp_usd": px, **stats, "open_positions": sum(p["open"] for p in positions), "warnings": WARN}, indent=1))

def write_summary(meta, seen, positions, stats):
    L = [f"# XRPL meme scanner — PAPER ONLY ({LABEL})", "",
         "Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.",
         "Token data by <a href=\"https://xrpl.to\">xrpl.to</a>; safety checks and prices from the public XRP Ledger.", "",
         f"Last run: **{meta['last_run']}** (UTC) · XRP/USD {meta['xrp_usd']:.4f} ({meta['xrp_usd_src']}) · "
         f"this run: {stats['seen']} tokens seen, {stats['passed']} passed, {stats['bought']} paper-bought · buys today {meta.get('buys_today',0)}/{CFG['max_new_buys_per_day_utc']}", ""]
    if meta.get("warnings"): L += ["**Source warnings this run:** " + " | ".join(meta["warnings"]), ""]
    L += ["## Results per exit strategy (closed trades, each buy scored separately under all 3)", "",
          "| Strategy | Rule | Closed | Win rate | P&L XRP gross | P&L XRP net | P&L USD gross | P&L USD net | Open |", "|---|---|---|---|---|---|---|---|---|"]
    desc = {"hold": "½ at +100%, stop −50%, 72h", "plus5": "all at +50%, stop −50%, 72h", "scalp": "+20% / −10% / 60 min"}
    for s in STRATS:
        closed = [p for p in positions if not p["strategies"][s]["open"]]
        legs = [c for p in positions for c in p["strategies"][s].get("closed", [])]
        tot = lambda f: sum(c[f] for c in legs)
        wins = sum(1 for p in closed if sum(c["pnl_xrp_net"] for c in p["strategies"][s]["closed"]) > 0)
        wr = f"{wins / len(closed) * 100:.0f}%" if closed else "–"
        L.append(f"| {s} | {desc.get(s, '')} | {len(closed)} | {wr} | {tot('pnl_xrp_gross'):+.3f} | {tot('pnl_xrp_net'):+.3f} | "
                 f"{tot('pnl_usd_gross'):+.2f} | {tot('pnl_usd_net'):+.2f} | {sum(1 for p in positions if p['strategies'][s]['open'])} |")
    L += ["", "Gross = at pool spot price with no fees/slippage. Net = simulated AMM swaps incl. pool trading fee, price impact, issuer transfer fee and network fee. "
          "USD P&L also moves with XRP/USD. Exits fire at the price seen at each ~15-min poll, so real fills could be better or worse than the trigger level.", ""]
    op = [p for p in positions if p["open"]]
    L += [f"## Open paper positions ({len(op)}/{CFG['max_open_positions']})", ""]
    if op:
        L += ["| Token | Bought (UTC) | Cost | Buy cost vs spot | Now (net, x) | Strategies still open | Warnings |", "|---|---|---|---|---|---|---|"]
        for p in sorted(op, key=lambda p: p["t"], reverse=True):
            L.append(f"| [{p['name']}](https://xrpl.to/token/{p['issuer']}-{p['currency']}) | {p['ts'][:16]} | ${p['usd_cost']:.0f} = {p['xrp_cost']:.2f} XRP | "
                     f"{p.get('buy_cost_pct', 0):.2f}% | {p.get('last_ratio_net', 1):.2f} | {', '.join(s for s in STRATS if p['strategies'][s]['open'])} | {'; '.join(p['warnings'])} |")
    else: L.append("None.")
    L += ["", "## Recently rejected (latest verdict per token)", "", "| Token | Verdict | Reasons | Pool XRP |", "|---|---|---|---|"]
    rej = sorted([v for v in seen.values() if v.get("verdict") and v["verdict"] != "PASS"], key=lambda v: v.get("last_seen", ""), reverse=True)[:40]
    for v in rej: L.append(f"| [{v['name']}]({v.get('url','')}) | {v['verdict']} | {v.get('reasons','')} | {v.get('pool_xrp','')} |")
    L += ["", "Logs: `logs/candidates.csv`, `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
