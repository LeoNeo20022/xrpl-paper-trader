"""PAPER backtest of leverage_ta (trend-pullback long/short, 2x and 5x) vs keep $100 in XRP and vs the long-only 2% grid (levgrid).
Data: real Binance XRPUSDT perp 5-min klines from data.binance.vision (75 days, the first ~15 only warm up the 1h EMA200),
real Binance monthly funding + OKX proxy for the current month; stress test on the saved Bitstamp Oct 2024 - Mar 2025 5-min
candles (funding assumed 0.01%/8h). Indicators are computed on the whole series; each run only trades inside its window.
Parameters come from ta_config.json and were fixed before running this (no tuning)."""
import json, os, csv, time, datetime as dt
import ta, levgrid, levdata
HERE = os.path.dirname(os.path.abspath(__file__))
TC = json.load(open(os.path.join(HERE, "ta_config.json"))); GC = json.load(open(os.path.join(HERE, "config.json")))
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")

def run_ta(sub, ind, lev, fundmap):
    cfg = dict(TC["common"], leverage=lev); st = ta.new_state(cfg); ev = []
    for t, path in sub:
        if t % 28800 == 0: ta.funding(st, t, fundmap.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        ev += ta.step(st, cfg, t, list(path), ind, iso(t))
    return ta.equity(st, sub[-1][1][-1], cfg), st, ev

def run_grid(sub, lev, fundmap):
    cfg = dict(GC["common"], leverage=lev); st = levgrid.new_state(sub[0][1][0], cfg)
    for t, path in sub:
        if t % 28800 == 0: levgrid.funding(st, cfg, t, fundmap.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        levgrid.process(st, list(path), cfg, ts=iso(t))
    return levgrid.equity(st, sub[-1][1][-1], cfg), st

def hold(sub): return 100 / (sub[0][1][0] * 1.0005) * sub[-1][1][-1]

today = dt.datetime.now(dt.timezone.utc).date()
rec = []
for i in range(75, 0, -1):
    try: rec += levdata.archive_klines((today - dt.timedelta(days=i)).isoformat())
    except Exception as e: print("missing day", e)
rec.sort()
fund, _ = levdata.funding_since(rec[0][0] - 1)
for m in sorted({(today - dt.timedelta(days=i)).strftime("%Y-%m") for i in range(75, 0, -1)}):
    try: fund.update(levdata.archive_funding(m))
    except Exception: pass
old = []
for r in csv.DictReader(open(os.path.join(HERE, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
    t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
    old.append((t, (o, h, l, c) if c < o else (o, l, h, c)))
ind_rec = ta.indicators(ta.bars_1h(rec), TC["common"]); ind_old = ta.indicators(ta.bars_1h(old), TC["common"])
end = rec[-1][0] + 300
L = [f"PAPER backtest leverage_ta. Recent data to {iso(end)} UTC (Binance perp 5-min). Stress: Bitstamp 5-min Oct 2024 - Mar 2025. Run {iso(time.time())} UTC.",
     "P/L after all fees, slippage and funding, valued as if closed at the end. Grid = the long-only 2% grid (lev_2x/lev_5x rules).", "",
     "| Window (XRP price) | Line | P/L after fees | Closed trades (entries long/short) | Win rate | Liquidations | Max drawdown | Fees / funding | vs keep $100 in XRP |",
     "|---|---|---|---|---|---|---|---|---|"]
log = []
def window(sub, ind, fm, label):
    h = hold(sub)
    for lev in (2, 5):
        v, st, ev = run_ta(sub, ind, lev, fm)
        log.extend(f"{label} {lev}x {e}" for e in ev if e["event"] != "FUNDING")
        wr = f"{st['wins'] / st['trades'] * 100:.0f}%" if st["trades"] else "—"
        L.append(f"| {label} ({sub[0][1][0]:.3f} -> {sub[-1][1][-1]:.3f}) | TA {lev}x | {v - 100:+.2f} | {st['trades']} ({st['longs']}/{st['shorts']}) | {wr} | "
                 f"{st['liquidations']} | {st['max_dd_pct']:.1f}% | ${st['fees_usd']:.2f} / ${st['funding_usd']:+.2f} | {v - h:+.2f} |")
    for lev in (2, 5):
        v, st = run_grid(sub, lev, fm)
        L.append(f"| | Grid {lev}x (long only) | {v - 100:+.2f} | {st['sells']} round trips | — | {st['liquidations']} | {st['max_dd_pct']:.1f}% | ${st['fees_trade_usd']:.2f} / ${st['funding_usd']:+.2f} | {v - h:+.2f} |")
    L.append(f"| | Keep $100 in XRP | {h - 100:+.2f} | — | — | 0 | — | $0.05 | — |")
for w in (14, 30, 60):
    window([c for c in rec if c[0] >= end - w * 86400], ind_rec, fund, f"{w}d")
first_ok = min(ind_old)   # stress runs start after the 1h EMA200 warm-up
window([c for c in old if c[0] >= first_ok], ind_old, {}, "Stress whole")

def rolling(cs, ind, fm, title):
    starts = [i for i, (t, _) in enumerate(cs) if t % 86400 == 0 and t >= min(ind) and t + 14 * 86400 <= cs[-1][0] + 300]
    R = ["", f"### 14-day runs, one starting every day: {title} ({len(starts)} runs)", "",
         "| Line | Median P/L | Worst run | Best run | Losing runs | Runs with a liquidation | Median trades | Median vs keep $100 in XRP | Worst max drawdown |",
         "|---|---|---|---|---|---|---|---|---|"]
    for kind in ("TA", "Grid"):
        for lev in (2, 5):
            res = []
            for i in starts:
                sub = cs[i:i + 14 * 288]
                if kind == "TA": v, st, _ = run_ta(sub, ind, lev, fm); n = st["trades"]
                else: v, st = run_grid(sub, lev, fm); n = st["sells"]
                res.append((v - 100, v - hold(sub), st["liquidations"], st["max_dd_pct"], n))
            pl = sorted(r[0] for r in res); vh = sorted(r[1] for r in res); nt = sorted(r[4] for r in res)
            R.append(f"| {kind} {lev}x | {pl[len(pl) // 2]:+.2f} | {pl[0]:+.2f} | {pl[-1]:+.2f} | {sum(r[0] < 0 for r in res)} of {len(res)} | {sum(r[2] > 0 for r in res)} | "
                     f"{nt[len(nt) // 2]} | {vh[len(vh) // 2]:+.2f} | {max(r[3] for r in res):.1f}% |")
    return R
L += rolling(rec, ind_rec, fund, "last 60 days")
L += rolling(old, ind_old, {}, "STRESS Oct 2024 - Mar 2025")
L += ["", "Trade log (recent windows overlap, so trades repeat):"] + [f"- {x}" for x in log if not x.startswith(("14d", "30d"))][:400]
out = "\n".join(L); print("\n".join(L[:60]))
open(os.path.join(HERE, "backtest_ta_output.txt"), "w").write(out + "\n")
