"""Measure real fee yield of the XRP/RLUSD AMM pool from on-ledger history:
the invariant sqrt(XRP * RLUSD) per LP token only grows from trading fees (and auction-slot bids)."""
import json, urllib.request, math, sys
from datetime import datetime, timezone
N = "https://xrplcluster.com"
def q(m, p):
    r = urllib.request.Request(N, json.dumps({"method": m, "params": [p]}).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(r, timeout=40))["result"]
RL = {"currency": "524C555344000000000000000000000000000000", "issuer": "rMxCKbEDwqr76QuheSUMdEGf4B9xJ8m5De"}
RIPPLE_EPOCH = 946684800
def close_time(li):
    return q("ledger", {"ledger_index": li})["ledger"]["close_time"] + RIPPLE_EPOCH
def ledger_at(ts, hi):
    lo_i, hi_i = 32570, hi
    while hi_i - lo_i > 50:
        m = (lo_i + hi_i) // 2
        if close_time(m) < ts: lo_i = m
        else: hi_i = m
    return hi_i
def snap(li):
    a = q("amm_info", {"asset": {"currency": "XRP"}, "asset2": RL, "ledger_index": li})
    if "amm" not in a: return None
    a = a["amm"]; x = float(a["amount"]) / 1e6; y = float(a["amount2"]["value"]); lp = float(a["lp_token"]["value"])
    return dict(ledger=li, time=datetime.fromtimestamp(close_time(li), timezone.utc).isoformat(), xrp=x, rlusd=y,
                lp=lp, price=y / x, inv_per_lp=math.sqrt(x * y) / lp, fee=a["trading_fee"])
cur = q("ledger", {"ledger_index": "validated"})["ledger"]; cur_i = int(cur["ledger_index"])
now = cur["close_time"] + RIPPLE_EPOCH
out = {"now": snap(cur_i)}
for d in (7, 30, 90, 180, 365):
    li = ledger_at(now - d * 86400, cur_i); s = snap(li)
    if s:
        g = out["now"]["inv_per_lp"] / s["inv_per_lp"] - 1
        s["fee_yield_pct_period"] = g * 100; s["fee_apr_pct"] = g * 365 / d * 100
    out[f"{d}d_ago"] = s
    print(d, json.dumps(s))
json.dump(out, open("data/amm_rlusd_yield.json", "w"), indent=1)
