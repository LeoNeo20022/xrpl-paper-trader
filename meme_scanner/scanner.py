#!/usr/bin/env python3
"""XRPL memecoin PAPER scanner. LOG-ONLY: reads public APIs, simulates $10 buys, never signs or submits anything.

Each run: discover new/trending XRPL tokens -> ledger safety checks -> paper-buy passing tokens (AMM math)
-> mark open paper positions to the live AMM pool and apply the exit strategies -> write logs + SUMMARY.md.
Strategies: hold, plus5, scalp (original, unchanged) + slow_scalp, breakout, dip_bounce (added Oct 24, own entry rules in entry_v2).
Stdlib only. Every row is labelled PAPER-NOT-ON-LEDGER.
"""
import csv, hashlib, json, math, os, statistics, sys, time, urllib.request, urllib.error
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
    lists = [("new", "sortBy=dateon&sortType=desc", d["xrplto_newest_limit"]),
             ("trending", "sortBy=trendingScore&sortType=desc", d["xrplto_trending_limit"])]
    keyed = bool(XRPLTO_KEY) and NOW - meta.get("key_rejected_t", 0) > 3600
    if keyed or d.get("extra_lists_when_anonymous") or os.environ.get("MEME_FORCE_EXTRA") == "1":
        # v2 universe: top tokens by 24h XRP volume (dip_bounce) and by 1h price change (breakout). 1 credit each.
        lists += [("volume", "sortBy=vol24hxrp&sortType=desc", d.get("xrplto_volume_limit", 100)),
                  ("momentum", "sortBy=pro1h&sortType=desc", d.get("xrplto_momentum_limit", 50))]
    else:
        WARN.append("no xrpl.to API key: skipped volume/momentum lists (breakout/dip_bounce universe limited to new+trending)")
    meta["xrplto_calls_last_discovery"] = 0
    for src, q, lim in lists:
        try:
            url = f"{XRPLTO}?start=0&limit={lim}&{q}&filter="
            use_key = bool(XRPLTO_KEY) and NOW - meta.get("key_rejected_t", 0) > 3600
            meta["xrplto_calls_last_discovery"] += 1
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
                    add(t, src, i)
            if src in ("new", "trending"): ok += 1
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
LEGACY = ["hold", "plus5", "scalp"]                    # original strategies (unchanged rules)
V2 = [s for s in ("slow_scalp", "breakout", "dip_bounce") if s in STRATS]  # added Oct 24
BOOK_FIELDS = ["ts", "label", "strategy", "token", "issuer", "currency", "sources", "usd", "xrp_usd", "xrp_in", "spot_xrp_per_token",
               "fill_xrp_per_token", "tokens", "buy_cost_pct_vs_spot", "amm_fee_pct", "transfer_fee_pct", "round_trip_cost_pct",
               "pool_xrp", "cash_after_usd", "warnings", "note"]

TRUST_RESERVE_XRP = 0.2   # owner reserve per trust line: LOCKED while the line exists, returned when it is removed (not a cost)

def set_network_fee(meta):
    """Network fee per transaction, as if signed in Xaman: max(config floor, 0.00002 XRP, live open-ledger fee), capped at 0.01 XRP.
    Used for every simulated swap (buy/sell) and TrustSet (add line before a buy, remove it after a full exit). Since 2026-10-24."""
    live = None
    try: live = int(rpc("fee", {})["drops"]["open_ledger_fee"]) / 1e6
    except Exception as e: WARN.append(f"live fee unavailable: {e!r}")
    fee = max(CFG["network_fee_xrp"], 0.00002, min(live or 0, 0.01))
    CFG["network_fee_xrp"] = fee; meta["network_fee_xrp_used"] = fee; meta["open_ledger_fee_xrp"] = live
    return fee

def fee_book(bk):
    """Cumulative network-fee counter (XRP). Seeded once from the trade count at the 12-drop fee used before Oct 24."""
    if "net_fees_xrp" not in bk:
        n = len(bk["positions"]) + len(bk["closed"]) + sum(len(p["legs"]) for p in bk["positions"] + bk["closed"])
        bk["net_fees_xrp"] = n * 0.000012; bk["trustset_fees_xrp"] = 0.0
    return bk

def charge_trustset(bk, px):
    f = CFG["network_fee_xrp"]; fee_book(bk)
    bk["cash_usd"] = round(bk["cash_usd"] - f * px, 6); bk["net_fees_xrp"] += f; bk["trustset_fees_xrp"] += f

def new_book(px):
    b = CFG["bankroll"]
    return {"start_usd": b["start_usd"], "start_xrp_usd": px, "start_ts": TS, "cash_usd": b["start_usd"], "day": "", "buys_today": 0,
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
    if pool: fee_book(bk)["net_fees_xrp"] += CFG["network_fee_xrp"]   # the sell swap's network fee (already inside xrp_net)
    row = {"ts": TS, "label": LABEL, "strategy": sname, "token": pos["name"], "issuer": pos["issuer"], "reason": reason,
           "fraction_of_buy": round(frac, 4), "hours_held": round((NOW - pos["t"]) / 3600, 2),
           "entry_spot_xrp": pos["entry_spot"], "exit_spot_xrp": pool["spot"] if pool else 0,
           "cost_xrp": round(cost_xrp, 6), "proceeds_xrp_net": round(xrp_net, 6), "proceeds_xrp_gross": round(xrp_gross, 6),
           "pnl_xrp_net": round(xrp_net - cost_xrp, 6), "pnl_xrp_gross": round(xrp_gross - cost_xrp, 6),
           "cost_usd": round(cost_usd, 4), "xrp_usd": px, "proceeds_usd_net": round(usd_net, 4),
           "pnl_usd_net": round(usd_net - cost_usd, 4), "pnl_usd_gross": round(usd_gross - cost_usd, 4),
           "cash_after_usd": round(bk["cash_usd"], 4), "note": "exit at price observed at the ~5-min poll, not the exact trigger level",
           "peak_x": pos.get("peak_x", ""), "peak_hours": pos.get("peak_hours", ""), "trough_x": pos.get("trough_x", "")}  # tracking only (Oct 25)
    append("exits.csv", row, list(row.keys()))
    pos["remaining"] = round(pos["remaining"] - frac, 10)
    pos["legs"].append({k: row[k] for k in ("ts", "reason", "fraction_of_buy", "pnl_xrp_net", "pnl_xrp_gross", "pnl_usd_net", "pnl_usd_gross")})

EXCURSION_FIELDS = ["peak_x", "peak_hours", "trough_x"]

def track_excursion(pos, ratio):
    """TRACKING ONLY (added Oct 25): highest / lowest net multiple seen at the ~5-min polls (net = what selling the whole buy
    would return ÷ XRP cost, after pool fee, slippage, transfer and network fee) and hours after buy of the peak. Never read by exit rules."""
    h = round((NOW - pos["t"]) / 3600, 2)
    if ratio > pos.get("peak_x", -1.0): pos["peak_x"], pos["peak_hours"] = round(ratio, 4), h
    pos["trough_x"] = round(min(pos.get("trough_x", ratio), ratio), 4)
    pos.setdefault("excursion_src", "live from " + TS[:16])

def ensure_exit_columns():
    """Append peak_x/peak_hours/trough_x to logs/exits.csv once (older rows get blanks until backfilled)."""
    p = os.path.join(LOGS, "exits.csv")
    if not os.path.exists(p): return
    with open(p, newline="") as f: rows = list(csv.reader(f))
    if not rows or "peak_x" in rows[0]: return
    hdr = rows[0] + EXCURSION_FIELDS
    with open(p + ".tmp", "w", newline="") as f:
        w = csv.writer(f); w.writerow(hdr)
        for r in rows[1:]: w.writerow(r + [""] * (len(hdr) - len(r)))
    os.replace(p + ".tmp", p)

def ohlc_since(issuer, currency, t_from):
    """xrpl.to 5-min candles [t_ms, o, h, l, c, vol] in XRP per token since t_from (5 credits per call)."""
    md5 = hashlib.md5(f"{issuer}_{currency}".encode()).hexdigest()
    cb = min(1000, int((NOW - t_from) / 300) + 3)
    o = http_json(f"https://api.xrpl.to/v1/ohlc/{md5}?resolution=5&cb={cb}", headers={"X-Api-Key": XRPLTO_KEY} if XRPLTO_KEY else None).get("ohlc") or []
    return sorted(o, key=lambda c: c[0])

def candle_excursion(candles, t_buy, t_end, ref_ratio, ref_spot):
    """Peak/trough net multiple between t_buy and t_end from candle highs/lows, scaled from a known (net ratio, spot) pair.
    Approximation: assumes the sell cost (fee + slippage) at the peak equals the cost at the reference point."""
    if not ref_spot or ref_spot <= 0: return None
    win = [c for c in candles if c[0] / 1000 >= t_buy and c[0] / 1000 + 300 <= t_end + 1]
    pk = (ref_ratio, (t_end - t_buy) / 3600); tr = ref_ratio
    for c in win:
        hx, lx = ref_ratio * float(c[2]) / ref_spot, ref_ratio * float(c[3]) / ref_spot
        if hx > pk[0]: pk = (hx, (c[0] / 1000 + 150 - t_buy) / 3600)
        tr = min(tr, lx)
    return round(pk[0], 4), round(max(pk[1], 0), 2), round(tr, 4)

def backfill_excursions(meta, books, pools):
    """ONE-TIME (Oct 25): backfill peak/trough since entry for positions bought before tracking started, from 5-min candles.
    One /ohlc call per unique token (~32 tokens = ~160 credits once). Open positions: merged with live tracking.
    Closed trades: fills the blank peak/trough columns in logs/exits.csv and on closed positions in state."""
    if meta.get("excursion_backfill_done") or not (XRPLTO_KEY or os.environ.get("MEME_FORCE_BACKFILL") == "1"): return
    allpos = [(s, p) for s, bk in books.items() for p in bk["positions"] + bk["closed"]]
    p_ex = os.path.join(LOGS, "exits.csv")
    rows = list(csv.DictReader(open(p_ex, newline=""))) if os.path.exists(p_ex) else []
    need = {}
    for s, p in allpos: need[(p["issuer"], p["currency"])] = min(need.get((p["issuer"], p["currency"]), NOW), p["t"])
    cache, calls, fails = {}, 0, 0
    for (iss, cur), t0 in need.items():
        try: cache[(iss, cur)] = ohlc_since(iss, cur, t0); calls += 1
        except Exception as e:
            fails += 1; msg = repr(e).replace(XRPLTO_KEY, "***") if XRPLTO_KEY else repr(e); WARN.append(f"backfill ohlc failed: {msg}")
    cur_of = {p["issuer"] + "|" + p["name"]: p["currency"] for _, p in allpos}
    n_open = n_rows = 0
    for s, bk in books.items():
        for p in bk["positions"]:
            pl = pools.get(p["key"]); c = cache.get((p["issuer"], p["currency"]))
            if not isinstance(pl, dict) or c is None: continue
            r = candle_excursion(c, p["t"], NOW, sim_sell(pl, p["tokens_net"])[0] / p["xrp_cost"], pl["spot"])
            if not r: continue
            if r[0] > p.get("peak_x", -1): p["peak_x"], p["peak_hours"] = r[0], r[1]
            p["trough_x"] = min(p.get("trough_x", r[2]), r[2]); p["excursion_src"] = "5-min candles to " + TS[:16] + ", live after"; n_open += 1
    last_row = {}
    for r in rows:
        if r.get("peak_x") not in ("", None): continue
        cur = cur_of.get(r["issuer"] + "|" + r["token"]); c = cache.get((r["issuer"], cur))
        try:
            t_end = datetime.fromisoformat(r["ts"]).timestamp(); t_buy = t_end - float(r["hours_held"]) * 3600
            cost = float(r["cost_xrp"]); ref = float(r["proceeds_xrp_net"]) / cost if cost else 0.0; spot = float(r["exit_spot_xrp"])
        except Exception: continue
        if c is None or spot <= 0:
            if spot <= 0: r.update(peak_x="", peak_hours="", trough_x=0.0)
            continue
        ex = candle_excursion(c, t_buy, t_end, ref, spot)
        if ex: r["peak_x"], r["peak_hours"], r["trough_x"] = ex; n_rows += 1; last_row[(r["strategy"], r["issuer"], round(t_buy))] = ex
    if rows:
        with open(p_ex + ".tmp", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        os.replace(p_ex + ".tmp", p_ex)
    for s, bk in books.items():   # closed positions in state: take the excursion from their final exit row
        for p in bk["closed"]:
            if "peak_x" in p: continue
            m = [v for (st, iss, tb), v in last_row.items() if st == s and iss == p["issuer"] and abs(tb - p["t"]) < 120]
            if m: p["peak_x"], p["peak_hours"], p["trough_x"] = max(m); p["excursion_src"] = "5-min candles (backfill)"
    meta.update(excursion_backfill_done=TS, excursion_backfill_calls=calls, excursion_backfill_fails=fails,
                excursion_backfill_open=n_open, excursion_backfill_exit_rows=n_rows)

def manage(bk, sname, pool, px):
    rule = CFG["exits"][sname]; still = []
    for pos in bk["positions"]:
        age_h = (NOW - pos["t"]) / 3600
        if pool.get(pos["key"], "err") == "err": still.append(pos); continue  # couldn't price this run: hold
        pl = pool[pos["key"]]
        if pl is None: track_excursion(pos, 0.0); close_part(bk, pos, sname, pos["remaining"], "pool gone (rug?) -> 0", None, px)
        else:
            net, _ = sim_sell(pl, pos["tokens_net"]); ratio = net / pos["xrp_cost"]
            pos["last_ratio_net"] = round(ratio, 4)
            track_excursion(pos, ratio)   # tracking only: does not affect any exit below
            if "trail_pct" in rule:  # breakout: trailing stop on spot price vs highest spot seen since entry
                pos["peak_spot"] = max(pos.get("peak_spot", pos["entry_spot"]), pl["spot"])
                drop = (1 - pl["spot"] / pos["peak_spot"]) * 100
                if drop >= rule["trail_pct"]:
                    close_part(bk, pos, sname, pos["remaining"], f"trailing stop: {drop:.1f}% below high (x{ratio:.2f} net)", pl, px)
                elif age_h >= rule["max_hours"]:
                    close_part(bk, pos, sname, pos["remaining"], f"time limit {rule['max_hours']}h (x{ratio:.2f} net)", pl, px)
            elif not pos["tp_done"] and ratio >= rule["take_profit_mult"]:
                close_part(bk, pos, sname, min(rule["take_profit_fraction"], pos["remaining"]), f"take profit (x{ratio:.2f} net)", pl, px)
                pos["tp_done"] = True
            if pos["remaining"] > 1e-9:
                if "stop_mult" in rule and ratio <= rule["stop_mult"]: close_part(bk, pos, sname, pos["remaining"], f"stop (x{ratio:.2f} net)", pl, px)
                elif age_h >= rule["max_hours"]: close_part(bk, pos, sname, pos["remaining"], f"time limit {rule['max_hours']}h (x{ratio:.2f} net)", pl, px)
        if pos["remaining"] > 1e-9: still.append(pos)
        else:
            charge_trustset(bk, px)   # TrustSet to remove the line and unlock its 0.2 XRP reserve
            pos["closed_ts"] = TS; pos["pnl_usd_net"] = round(sum(l["pnl_usd_net"] for l in pos["legs"]), 4)
            pos["pnl_xrp_net"] = round(sum(l["pnl_xrp_net"] for l in pos["legs"]), 6)
            bk["closed"].append(pos); bk["last_exit"][pos["key"]] = NOW
    bk["positions"] = still

def book_stats(bk, pools, px):
    open_val = open_cost = open_val_x = open_cost_x = 0.0; unknown = 0
    for p in bk["positions"]:
        pl = pools.get(p["key"]); open_cost_x += p["xrp_cost"] * p["remaining"]
        if not isinstance(pl, dict):
            unknown += 1; open_cost += p["usd_cost"] * p["remaining"]; open_val += p["usd_cost"] * p["remaining"]
            open_val_x += p["xrp_cost"] * p["remaining"]; continue
        xn = sim_sell(pl, p["tokens_net"] * p["remaining"])[0]; open_val_x += xn
        open_val += xn * px
        open_cost += p["usd_cost"] * p["remaining"]
    legs = [l for p in bk["positions"] + bk["closed"] for l in p["legs"]]
    realized = sum(l["pnl_usd_net"] for l in legs); realized_g = sum(l["pnl_usd_gross"] for l in legs)
    realized_x = sum(l["pnl_xrp_net"] for l in legs)
    fee_book(bk)
    fees_usd = sum(l["pnl_usd_gross"] - l["pnl_usd_net"] for l in legs)            # closed legs: entry+exit AMM fee, price impact, transfer fee, network fee
    fees_usd += sum(p["xrp_cost"] * p["remaining"] * (1 - p["entry_spot"] / p["entry_eff_px"]) * p["xrp_usd_entry"] for p in bk["positions"])  # open: entry costs
    fees_usd += bk["trustset_fees_xrp"] * px
    wins = sum(1 for p in bk["closed"] if p["pnl_usd_net"] > 0); losses = len(bk["closed"]) - wins
    eq = bk["cash_usd"] + open_val
    return {"cash": bk["cash_usd"], "open_n": len(bk["positions"]), "open_val": open_val, "unrealized": open_val - open_cost,
            "realized": realized, "realized_gross": realized_g, "realized_xrp": realized_x, "equity": eq, "equity_xrp": eq / px,
            "start_xrp": bk["start_usd"] / bk["start_xrp_usd"], "closed_n": len(bk["closed"]),
            "trades": len(bk["closed"]) + len(bk["positions"]), "win_rate": (wins / len(bk["closed"]) * 100) if bk["closed"] else None,
            "unpriced": unknown, "wins": wins, "losses": losses, "unrealized_xrp": open_val_x - open_cost_x,
            "fees_usd": fees_usd, "net_fees_xrp": bk["net_fees_xrp"], "reserve_locked_xrp": TRUST_RESERVE_XRP * len(bk["positions"])}

# ---------------- main ----------------
def main():
    t0 = time.time()
    os.makedirs(STATE, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
    meta = load("meta.json", {}); seen = load("seen.json", {}); books = load("strategies.json", {})
    px, px_src = xrp_usd()
    meta["xrp_usd"], meta["xrp_usd_src"] = px, px_src
    set_network_fee(meta)
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
    ensure_exit_columns()
    try: backfill_excursions(meta, books, pools)   # one-time, tracking only
    except Exception as e: WARN.append(f"peak backfill failed: {e!r}")
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
    held_by_all = set.intersection(*[{p["key"] for p in books[s]["positions"]} for s in LEGACY])
    v2 = CFG.get("entry_v2", {}); bo, db = v2.get("breakout", {}), v2.get("dip_bounce", {})
    min_vol = CFG["entry"]["min_vol24h_xrp"]
    v2_elig = {s: [] for s in V2}; bo_queue = []
    eligible = []
    cand_fields = ["ts", "label", "token", "issuer", "currency", "sources", "verdict", "reasons", "warnings", "pool_xrp", "amm_fee_pct",
                   "transfer_fee_pct", "blackholed", "no_freeze", "clawback", "global_freeze", "top10_pct", "top10_src",
                   "vol24h_xrp", "age_h", "round_trip_cost_pct", "url"]
    for k, tok in found.items():
        x = tok.get("x") or {}
        is_new = any(s.startswith("new") or s.startswith("ledger") for s in tok["sources"])
        top = any(s.startswith("trending#") and int(s.split("#")[1]) <= CFG["discovery"]["trending_top_n"] for s in tok["sources"])
        legacy_src = any(s.startswith(("new", "ledger", "trending")) for s in tok["sources"])
        # cheap v2 prefilters from xrpl.to fields (no ledger calls unless one matches)
        vol = x.get("vol24hxrp")
        vol_ok = vol is not None and vol >= min_vol
        age_h_x = (NOW * 1000 - x["dateon"]) / 3.6e6 if x.get("dateon") else None
        hi24 = (x.get("maxMin24h") or [0])[0] or 0
        pre_bo = bool(bo) and vol_ok and (x.get("pro1h") or 0) >= bo["min_change_1h_pct"]
        pre_db = (bool(db) and vol_ok and age_h_x is not None and age_h_x > db["min_age_hours"] and hi24 > 0 and x.get("exch")
                  and x["exch"] <= hi24 * (1 - (db["min_dip_from_24h_high_pct"] - db.get("prefilter_slack_pct", 0)) / 100))
        if not legacy_src and not (pre_bo or pre_db): continue  # extra-list token with no v2 signal: don't spend ledger calls
        se = seen.setdefault(k, {"first_seen": TS, "name": tok["name"]})
        need = ((is_new or top) and k not in held_by_all) or pre_bo or pre_db
        try: r = check(tok, se, need_conc=need); stats["checked"] += 1
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
        # ---- v2 strategies ----
        if r["hard_fail"] or not pool: continue
        if verdict == "PASS":
            lim = v2["slow_scalp"]["max_round_trip_cost_pct"]
            ok = rt is not None and rt <= lim
            if ok: v2_elig["slow_scalp"].append((0 if is_new else 1, -(x.get("trendingScore") or 0), k, tok, r, rt, f"slow_scalp: new/top-15 trending, round trip {rt:.2f}% <= {lim}%"))
            log_signal(se, "slow_scalp", tok, "ELIGIBLE" if ok else "SKIP", "" if ok else f"round-trip cost {rt if rt is not None else float('nan'):.2f}% > {lim}%", {"round_trip_cost_pct": rt})
        if pre_bo:
            if rt is not None and rt <= bo["max_round_trip_cost_pct"]: bo_queue.append((-(x.get("pro1h") or 0), k, tok, r, rt, se, x))
            else: log_signal(se, "breakout", tok, "SKIP", "round-trip cost too high", {"pro1h_xrplto": x.get("pro1h"), "round_trip_cost_pct": rt})
        if pre_db:
            dip = (1 - pool["spot"] / hi24) * 100
            m = {"high24h_xrp": hi24, "spot_xrp": pool["spot"], "dip_pct": dip, "age_h": age_h_x, "round_trip_cost_pct": rt, "vol24h_xrp": vol}
            why = []
            if dip < db["min_dip_from_24h_high_pct"]: why.append(f"only {dip:.1f}% below 24h high (ledger spot)")
            if rt is None or rt > db["max_round_trip_cost_pct"]: why.append("round-trip cost too high")
            if not why: v2_elig["dip_bounce"].append((-dip, 0, k, tok, r, rt, f"dip_bounce: {dip:.1f}% below 24h high {hi24:.6g} XRP, age {age_h_x / 24:.1f}d"))
            log_signal(se, "dip_bounce", tok, "SKIP" if why else "ELIGIBLE", "; ".join(why), m)
    # breakout confirmation needs 5-min candles (xrpl.to /ohlc, 5 credits each): only for the best few prefiltered tokens
    bo_queue.sort(key=lambda e: e[0]); calls = 0
    for _, k, tok, r, rt, se, x in bo_queue:
        if calls >= bo["max_ohlc_calls_per_run"]: break
        calls += 1
        try: m = breakout_metrics(x, r["pool"])
        except Exception as e:
            msg = repr(e).replace(XRPLTO_KEY, "***") if XRPLTO_KEY else repr(e)
            WARN.append(f"ohlc {tok['name']} failed: {msg}"); continue
        m["round_trip_cost_pct"] = rt
        why = []
        if m["change_1h_pct"] < bo["min_change_1h_pct"]: why.append(f"1h change {m['change_1h_pct']:.1f}% < {bo['min_change_1h_pct']}% (ledger spot vs 1h-ago candle)")
        if bo.get("vol_last_hour_above_prev_hour") and not m["vol_last_h"] > m["vol_prev_h"]: why.append(f"last-hour volume {m['vol_last_h']:.0f} not above prior hour {m['vol_prev_h']:.0f} XRP")
        if bo.get("vol_last_hour_above_24h_hourly_avg") and not m["vol_last_h"] > m["vol_avg_h"]: why.append(f"last-hour volume {m['vol_last_h']:.0f} not above 24h hourly avg {m['vol_avg_h']:.0f} XRP")
        if not why: v2_elig["breakout"].append((-m["change_1h_pct"], 0, k, tok, r, rt, f"breakout: +{m['change_1h_pct']:.1f}% in 1h, vol last hour {m['vol_last_h']:.0f} vs prior {m['vol_prev_h']:.0f} / 24h avg {m['vol_avg_h']:.0f} XRP"))
        log_signal(se, "breakout", tok, "SKIP" if why else "ELIGIBLE", "; ".join(why), m)
    stats["ohlc_calls"] = calls
    eligible.sort(key=lambda e: (e[0], e[1]))
    out = {s: [(k, tok, r, rt, "") for _, _, k, tok, r, rt in eligible] for s in LEGACY}
    for s in V2:
        v2_elig[s].sort(key=lambda e: (e[0], e[1]))
        out[s] = [(k, tok, r, rt, note) for _, _, k, tok, r, rt, note in v2_elig[s]]
    stats["eligible"] = {s: len(v) for s, v in out.items()}
    return out

SIG_FIELDS = ["ts", "label", "strategy", "token", "issuer", "currency", "decision", "reasons", "change_1h_pct", "pro1h_xrplto", "vol_last_h",
              "vol_prev_h", "vol_avg_h", "high24h_xrp", "spot_xrp", "dip_pct", "age_h", "vol24h_xrp", "round_trip_cost_pct", "url"]
def log_signal(se, strat, tok, decision, reasons, m):
    """v2 entry decisions -> logs/signals.csv (a row only when the decision/reasons change for that token+strategy)."""
    sig = decision + "|" + "".join(ch for ch in reasons if not ch.isdigit())  # ignore changing numbers
    if se.get("sig_" + strat) == sig: return
    se["sig_" + strat] = sig
    row = {"ts": TS, "label": LABEL, "strategy": strat, "token": tok["name"], "issuer": tok["issuer"], "currency": tok["currency"],
           "decision": decision, "reasons": reasons, "url": f"https://xrpl.to/token/{tok['issuer']}-{tok['currency']}"}
    row.update({k: (float(f"{v:.6g}") if isinstance(v, float) else v) for k, v in m.items() if v is not None})
    append("signals.csv", row, SIG_FIELDS)

def breakout_metrics(x, pool):
    """1h price change and hourly volumes from xrpl.to 5-min candles ([t, o, h, l, c, vol_xrp]); current price from the ledger pool."""
    md5 = x.get("md5")
    if not md5: raise RuntimeError("no xrpl.to id")
    res = CFG["entry_v2"]["breakout"].get("ohlc_resolution_min", 5); per_h = 60 // res
    url = f"https://api.xrpl.to/v1/ohlc/{md5}?resolution={res}&cb={2 * per_h + 2}"
    keyed = bool(XRPLTO_KEY)
    o = http_json(url, headers={"X-Api-Key": XRPLTO_KEY} if keyed else None).get("ohlc") or []
    o = sorted(o, key=lambda c: c[0])
    if len(o) < 2 * per_h + 1: raise RuntimeError(f"only {len(o)} candles")
    last, prev = o[-per_h:], o[-2 * per_h:-per_h]
    ref = float(o[-per_h - 1][4])  # close of the candle that ended ~60 min ago
    return {"change_1h_pct": (pool["spot"] / ref - 1) * 100 if ref > 0 else 0.0, "pro1h_xrplto": x.get("pro1h"),
            "vol_last_h": sum(float(c[5] or 0) for c in last), "vol_prev_h": sum(float(c[5] or 0) for c in prev),
            "vol_avg_h": (x.get("vol24hxrp") or 0) / 24, "spot_xrp": pool["spot"]}

def buy_round(books, elig, px, stats, pools):
    b = CFG["bankroll"]
    for s in STRATS:
        bk = books[s]; held = {p["key"] for p in bk["positions"]}
        for k, tok, r, rt, trig in elig.get(s, []):
            if bk["cash_usd"] + 1e-9 < CFG["buy_usd"] or bk["buys_today"] >= b["max_new_buys_per_day_utc"]: break
            if k in held: continue
            if NOW - bk["last_exit"].get(k, 0) < b["rebuy_cooldown_hours"] * 3600: continue
            pool = r["pool"]; xin = CFG["buy_usd"] / px
            tn, tg = sim_buy(pool, xin); eff = xin / tn
            pos = {"key": k, "name": tok["name"], "currency": tok["currency"], "issuer": tok["issuer"], "t": NOW, "ts": TS, "tf": pool["tf"],
                   "usd_cost": CFG["buy_usd"], "xrp_usd_entry": px, "xrp_cost": xin, "tokens_net": tn, "tokens_gross": tg,
                   "entry_spot": pool["spot"], "entry_eff_px": eff, "pool_xrp_entry": pool["x"], "amm_fee": pool["fee"],
                   "warnings": r["warn"], "remaining": 1.0, "tp_done": False, "legs": []}
            if trig: pos["trigger"] = trig
            if "trail_pct" in CFG["exits"][s]: pos["peak_spot"] = pool["spot"]
            bk["positions"].append(pos); held.add(k); bk["buys_today"] += 1; stats["bought"][s] += 1
            bk["cash_usd"] = round(bk["cash_usd"] - CFG["buy_usd"], 6); pools.setdefault(k, pool)
            charge_trustset(bk, px); bk["net_fees_xrp"] += CFG["network_fee_xrp"]   # TrustSet before the buy + the buy swap's fee (inside tokens_net)
            row = {"ts": TS, "label": LABEL, "strategy": s, "token": tok["name"], "issuer": tok["issuer"], "currency": tok["currency"],
                   "sources": "|".join(tok["sources"]), "usd": CFG["buy_usd"], "xrp_usd": px, "xrp_in": round(xin, 6),
                   "spot_xrp_per_token": pool["spot"], "fill_xrp_per_token": eff, "tokens": tn,
                   "buy_cost_pct_vs_spot": round((eff / pool["spot"] - 1) * 100, 3), "amm_fee_pct": round(pool["fee"] * 100, 3),
                   "transfer_fee_pct": round(pool["tf"] * 100, 3), "round_trip_cost_pct": round(rt, 3) if rt is not None else "",
                   "pool_xrp": round(pool["x"]), "cash_after_usd": round(bk["cash_usd"], 4), "warnings": "; ".join(r["warn"]),
                   "note": (trig + " | " if trig else "") + "simulated AMM fill incl. pool fee, slippage, transfer fee; CLOB ignored; network fee per tx; TrustSet fee charged; trust line reserve 0.2 XRP locked, not spent"}
            append("paper_buys.csv", row, BOOK_FIELDS)

def fmt_x(v): return "–" if v in (None, "") else f"{float(v):.2f}"
def fmt_peak(p): return "–" if p.get("peak_x") is None else f"{p['peak_x']:.2f} @ {p.get('peak_hours', 0):.1f}h"

def how_high(books):
    """Tracking-only stats: how far positions ran up (net multiple), deduped by token + buy time across strategies."""
    best = {}
    for s, bk in books.items():
        for p in bk["positions"] + bk["closed"]:
            if p.get("peak_x") is None: continue
            k = (p["key"], p["ts"][:16])
            if k not in best or p["peak_x"] > best[k]["peak_x"]: best[k] = p
    v = list(best.values()); n = len(v)
    L = ["## How high do they run? (tracking only — no rule uses this)", ""]
    if not n: return L + ["No peak data yet.", ""]
    L += [f"{n} unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). "
          "Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), "
          "seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).", "",
          "| Reached at any point | Buys | Share |", "|---|---|---|"]
    for lvl in (10, 20, 30, 50, 100):
        c = sum(1 for p in v if p["peak_x"] >= 1 + lvl / 100)
        L.append(f"| ≥ +{lvl}% | {c} | {c / n * 100:.0f}% |")
    pk = [p["peak_x"] for p in v]; hrs = [p.get("peak_hours", 0) for p in v]; lo = [p["trough_x"] for p in v if p.get("trough_x") is not None]
    L += ["", f"Median peak **x{statistics.median(pk):.2f}** · median hours to peak **{statistics.median(hrs):.1f}h** · "
          f"best x{max(pk):.2f} · median low x{statistics.median(lo):.2f} · ≤ −10% at some point: {sum(1 for x in lo if x <= 0.9)} of {len(lo)}", ""]
    return L

def write_summary(meta, seen, books, pools, px, stats):
    L = [f"# XRPL meme scanner — PAPER ONLY ({LABEL})", "",
         "Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.",
         "Data by <a href=\"https://xrpl.to\">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.", "",
         f"Last run: **{meta['last_run']}** (UTC) · XRP/USD {px:.4f} ({meta['xrp_usd_src']}) · last discovery {meta.get('last_discovery', '–')} (UTC, {'every run, API key' if meta.get('xrplto_keyed') else 'every ≥15 min, anonymous'}) · "
         f"xrpl.to credits used by last discovery: {meta.get('xrplto_calls_last_discovery', 0) + 5 * (stats.get('ohlc_calls') or 0)}", ""]
    if meta.get("warnings"): L += ["**Warnings this run:** " + " | ".join(meta["warnings"]), ""]
    desc = {"hold": "½ at +100%, stop −50%, 72h", "plus5": "all at +50%, stop −50%, 72h", "scalp": "+20% / −10% / 60 min",
            "slow_scalp": "new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25)",
            "breakout": "up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h",
            "dip_bounce": ">3 days old, ≥15% below 24h high; +10% / −10% / 24h"}
    L += ["## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)", "",
          "| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in STRATS:
        st = book_stats(books[s], pools, px)
        wr = f"{st['wins']} / {st['losses']} ({st['win_rate']:.0f}%)" if st["win_rate"] is not None else "–"
        started = (books[s].get("start_ts") or "2026-10-24T11:16")[:16].replace("T", " ")
        L.append(f"| {s} | {desc.get(s, '')} | {started} | **${st['equity']:.2f}** | **{st['equity'] - books[s]['start_usd']:+.2f}** | ${st['cash']:.2f} | {st['open_n']} / ${st['open_val']:.2f} | "
                 f"${st['realized']:+.2f} | ${st['unrealized']:+.2f} | {wr} | {st['trades']} ({st['closed_n']}) | {st['realized_xrp']:+.2f} | {st['unrealized_xrp']:+.2f} | {st['equity_xrp']:.2f} | {st['equity_xrp'] - st['start_xrp']:+.2f} | ${st['fees_usd']:.2f} ({st['net_fees_xrp']:.5f}) | {st['reserve_locked_xrp']:.1f} |")
    if "hold" in books:  # baseline: the same $100 simply kept in XRP from the original start
        sp = books["hold"]["start_xrp_usd"]; bx = books["hold"]["start_usd"] / sp; bu = bx * px
        L.append(f"| *baseline: keep $100 in XRP* | buy XRP at ${sp:.4f}, hold | 2026-10-24 11:16 | **${bu:.2f}** | **{bu - 100:+.2f}** | – | – | – | – | – | – | – | – | {bx:.2f} | +0.00 | – | – |")
    L += ["", f"**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, "
          f"as if each tx were a plain transaction signed in Xaman (network fee now {meta.get('network_fee_xrp_used', CFG['network_fee_xrp']):.6f} XRP/tx = max(0.00002, live open-ledger fee {meta.get('open_ledger_fee_xrp')}), cap 0.01). "
          "Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; "
          "earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. "
          "Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).", "",
          "Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee "
          "(open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. "
          "Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. "
          "Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. "
          "The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.", ""]
    for s in STRATS:
        bk = books[s]
        L += [f"### {s} — open positions ({len(bk['positions'])})", ""]
        if bk["positions"]:
            L += ["| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |" + (" Why bought |" if s in V2 else ""), "|---|---|---|---|---|---|---|" + ("---|" if s in V2 else "")]
            for p in sorted(bk["positions"], key=lambda p: p["t"], reverse=True):
                L.append(f"| [{p['name']}](https://xrpl.to/token/{p['issuer']}-{p['currency']}) | {p['ts'][:16]} | ${p['usd_cost'] * p['remaining']:.2f} | "
                         f"{p.get('last_ratio_net', 1):.2f} | {fmt_peak(p)} | {fmt_x(p.get('trough_x'))} | {'; '.join(p['warnings'])} |" + (f" {p.get('trigger', '')} |" if s in V2 else ""))
        else: L.append("None.")
        L.append("")
    L += how_high(books)
    L += ["## Recently rejected (latest verdict per token)", "", "| Token | Verdict | Reasons | Pool XRP |", "|---|---|---|---|"]
    rej = sorted([v for v in seen.values() if v.get("verdict") and v["verdict"] != "PASS"], key=lambda v: v.get("last_seen", ""), reverse=True)[:40]
    for v in rej: L.append(f"| [{v['name']}]({v.get('url','')}) | {v['verdict']} | {v.get('reasons','')} | {v.get('pool_xrp','')} |")
    L += ["", "Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`."]
    open(os.path.join(HERE, "SUMMARY.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
