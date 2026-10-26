"""PAPER backtest of the leveraged 2% grid (1x reference, 2x, 5x) on REAL Binance USDⓈ-M XRPUSDT perp 5-min klines
from the public data.binance.vision archive, last 14/30/60 days. Funding: real Binance monthly funding files for complete
months, OKX XRP-USDT-SWAP funding history as a proxy for the current month (Binance's live API is geo-blocked in the US),
0.01%/8h if neither has a value. Output: backtest_leverage_output.txt."""
import json, os, time, datetime as dt
import levgrid, levdata
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, "config.json")))
today = dt.datetime.now(dt.timezone.utc).date()
days = [today - dt.timedelta(days=i) for i in range(61, 0, -1)]
candles = []
for d in days:
    try: candles += levdata.archive_klines(d.isoformat())
    except Exception as e: print("missing", d, e)
candles.sort()
fund = {}
fund_okx, _ = levdata.funding_since(candles[0][0] - 1)
for d in sorted({(x.year, x.month) for x in days}):
    try: fund.update(levdata.archive_funding(f"{d[0]}-{d[1]:02d}"))
    except Exception: pass
n_bin = len(fund)
for t, r in fund_okx.items(): fund.setdefault(t, r)
end = candles[-1][0] + 300
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
L = [f"PAPER backtest, leveraged 2% grid on Binance XRPUSDT perp 5-min candles. Data {iso(candles[0][0])} -> {iso(end)} UTC "
     f"({len(candles)} candles). Funding: {n_bin} real Binance settlements + OKX proxy for the rest. Run {iso(time.time())} UTC.",
     "Value = close-everything-now (taker 0.05% + 0.05% slippage). Baseline = keep $100 in XRP bought at the window start (0.05% cost).", "",
     "| Window | XRP price | Line | End value | P/L after fees | vs keep $100 in XRP | Liquidations (margin lost) | Max drawdown | Trading fees | Funding paid | Round trips |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
liq_log = []
for w in (14, 30, 60):
    sub = [c for c in candles if c[0] >= end - w * 86400]
    p0, pe = sub[0][1][0], sub[-1][1][-1]
    hold = 100 / (p0 * (1 + CFG["baseline_cost_pct"] / 100)) * pe
    lo = min(min(p) for _, p in sub)
    for lev in (1, 2, 5):
        cfg = dict(CFG["common"], leverage=lev)
        st = levgrid.new_state(p0, cfg)
        for t, path in sub:
            if t % 28800 == 0:
                r = fund.get(t, levdata.FUNDING_ASSUMED)
                levgrid.funding(st, cfg, t, r, path[0], iso(t), assumed=t not in fund)
            for e in levgrid.process(st, list(path), cfg, ts=iso(t)):
                if e["side"] == "LIQUIDATION": liq_log.append(f"{w}d {lev}x: {e}")
        v = levgrid.equity(st, pe, cfg)
        L.append(f"| {w}d | {p0:.4f} -> {pe:.4f} (low {lo:.4f}) | {'1x (reference)' if lev == 1 else f'{lev}x'} | ${v:.2f} | {v - 100:+.2f} | {v - hold:+.2f} | "
                 f"{st['liquidations']} (${st['liq_lost_usd']:.2f}) | {st['max_dd_pct']:.1f}% | ${st['fees_trade_usd']:.2f} | ${st['funding_usd']:.2f} | {st['sells']} |")
    L.append(f"| {w}d | | keep $100 in XRP | ${hold:.2f} | {hold - 100:+.2f} | — | 0 | {(1 - lo / max(max(p) for _, p in sub)) * 100:.1f}% (peak-to-low) | $0.05 | $0 | — |")
def run(sub, lev, fundmap):
    cfg = dict(CFG["common"], leverage=lev); st = levgrid.new_state(sub[0][1][0], cfg); liqs = []
    for t, path in sub:
        if t % 28800 == 0: levgrid.funding(st, cfg, t, fundmap.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        liqs += [e for e in levgrid.process(st, list(path), cfg, ts=iso(t)) if e["side"] == "LIQUIDATION"]
    return levgrid.equity(st, sub[-1][1][-1], cfg), st, liqs

def rolling(cs, fundmap, title, wdays=14):
    """One 14-day run starting at every UTC midnight: how often does each leverage get liquidated?"""
    starts = [i for i, (t, _) in enumerate(cs) if t % 86400 == 0 and t + wdays * 86400 <= cs[-1][0] + 300]
    R = ["", f"### Rolling {wdays}-day runs, one starting every day: {title} ({len(starts)} runs)", "",
         "| Line | Median P/L | Worst P/L | Best P/L | Median vs keep $100 in XRP | Worst vs keep $100 in XRP | Runs with a liquidation | Worst max drawdown |", "|---|---|---|---|---|---|---|---|"]
    for lev in (1, 2, 5):
        res = []
        for i in starts:
            sub = [c for c in cs[i:i + wdays * 288]]
            v, st, lq = run(sub, lev, fundmap)
            hold = 100 / (sub[0][1][0] * (1 + CFG["baseline_cost_pct"] / 100)) * sub[-1][1][-1]
            res.append((v - 100, v - hold, len(lq), st["max_dd_pct"]))
        pl = sorted(r[0] for r in res); vh = sorted(r[1] for r in res)
        R.append(f"| {'1x (reference)' if lev == 1 else f'{lev}x'} | {pl[len(pl) // 2]:+.2f} | {pl[0]:+.2f} | {pl[-1]:+.2f} | {vh[len(vh) // 2]:+.2f} | {vh[0]:+.2f} | "
                 f"{sum(r[2] > 0 for r in res)} of {len(res)} | {max(r[3] for r in res):.1f}% |")
    return R

L += rolling(candles, fund, "last 60 days, Binance perp")
import csv as _csv
old = []
for r in _csv.DictReader(open(os.path.join(HERE, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
    t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
    old.append((t, (o, h, l, c) if c < o else (o, l, h, c)))
L += rolling(old, {}, "STRESS TEST Oct 2024 - Mar 2025 (Bitstamp spot candles saved in data/, big rally then -40% swings; funding assumed 0.01%/8h, real funding was often higher then)")

L += ["", "Liquidations:" if liq_log else "Liquidations: none in any window."] + [f"- {x}" for x in liq_log]
out = "\n".join(L)
print(out)
open(os.path.join(HERE, "backtest_leverage_output.txt"), "w").write(out + "\n")
