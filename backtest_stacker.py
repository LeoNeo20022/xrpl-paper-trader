"""PAPER backtest: xrp_stacker 4% vs 6% steps on Bitstamp XRP/USD 15-min candles (last 14/30/45/60 days).
Same rules as the live paper lines: 4 slices x 15% of sellable stack, 0.25%/fill, 14-day forced rebuy, trail-down."""
import json, time, urllib.request, stacker
now = time.time(); start = int(now) - 61 * 86400; out = []; cur = start
while True:
    u = f"https://www.bitstamp.net/api/v2/ohlc/xrpusd/?step=900&limit=1000&start={cur + 900}"
    rows = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "xrpl-paper-trader backtest"})))["data"]["ohlc"]
    rows = [r for r in rows if int(r["timestamp"]) > cur and int(r["timestamp"]) + 900 <= now]
    if not rows: break
    for r in rows:
        o, h, l, c = (float(r[k]) for k in ("open", "high", "low", "close"))
        out.append((int(r["timestamp"]), (o, h, l, c) if c < o else (o, l, h, c)))
    cur = out[-1][0]
end = out[-1][0]
print("| Window | XRP price | Step | XRP-eq vs holding | Round trips | Forced rebuys | RLUSD parked at end |")
print("|---|---|---|---|---|---|---|")
for days in (14, 30, 45, 60):
    sub = [c for c in out if c[0] >= end - days * 86400]; p0 = sub[0][1][0]; pe = sub[-1][1][-1]
    for sp in (4, 6):
        cfg = dict(budget_usd=100, spacing_pct=sp, slice_pct=15, levels=4, fee_pct_per_fill=0.25, max_park_days=14, tx_fee_xrp=0.00002)
        st = stacker.new_state(p0, cfg)
        for t, path in sub: stacker.process(st, list(path), cfg, ts_unix=t + 900)
        eq = st["xrp"] + st["parked_usd"] / pe; d = eq - st["start_xrp"]
        print(f"| {days}d | {p0:.3f} -> {pe:.3f} | {sp}% | {d:+.2f} XRP ({d / st['start_xrp'] * 100:+.2f}%) | {st['round_trips']} | {st['forced_rebuys']} ({st['xrp_lost_forced']:+.2f} XRP) | ${max(0.0, st['parked_usd']):.2f} |")
