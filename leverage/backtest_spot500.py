"""PAPER backtest (no live line, no config change): the same 2% grid on a $500 budget ($50 x 10 levels, 2% apart, +2% sells),
1) plain SPOT, no leverage, as XRPL DEX resting limit orders: no AMM fee, 0.05% slippage per fill + network fee
   (0.005 XRP/tx, today's high open-ledger fee, ~0.014% of a $50 fill) -> 0.064% per fill;
2) SPOT on Binance.US: 0% maker fee (https://www.binance.us/fees) + the same 0.05% slippage -> 0.05% per fill;
3) the 2x and 5x paper perps from backtest_leverage.py scaled to $500 (maker 0.02%, funding, close cost, liquidation).
Same data as backtest_leverage.py: Binance XRPUSDT perp 5-min archive (14/30/60 days) + Bitstamp Oct 2024-Mar 2025 stress file.
Spot value = cash + XRP x price (no liquidation, no funding). Baseline = keep $500 in XRP bought at the window start (0.05% cost)."""
import json, os, time, csv, datetime as dt
import levgrid, levdata
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(HERE, "config.json")))
B = 500
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
LINES = [("Spot, XRPL DEX limit orders", dict(leverage=1, maker_pct=0.064, taker_pct=0, slippage_pct=0, mmr_pct=0), False),
         ("Spot, Binance.US (0% maker)", dict(leverage=1, maker_pct=0.05, taker_pct=0, slippage_pct=0, mmr_pct=0), False),
         ("2x perp (paper)", dict(leverage=2), True), ("5x perp (paper)", dict(leverage=5), True)]

def run(sub, over, perp, fundmap):
    cfg = dict(CFG["common"], budget_usd=B, **over); st = levgrid.new_state(sub[0][1][0], cfg)
    for t, path in sub:
        if perp and t % 28800 == 0: levgrid.funding(st, cfg, t, fundmap.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        levgrid.process(st, list(path), cfg, ts=iso(t))
    v = levgrid.equity(st, sub[-1][1][-1], cfg)
    hold = B / (sub[0][1][0] * 1.0005) * sub[-1][1][-1]
    return v, hold, st

today = dt.datetime.now(dt.timezone.utc).date()
candles = []
for i in range(61, 0, -1):
    try: candles += levdata.archive_klines((today - dt.timedelta(days=i)).isoformat())
    except Exception as e: print("missing day", e)
candles.sort()
fund, _ = levdata.funding_since(candles[0][0] - 1)
for m in sorted({(today - dt.timedelta(days=i)).strftime("%Y-%m") for i in range(61, 0, -1)}):
    try: fund.update(levdata.archive_funding(m))
    except Exception: pass
old = []
for r in csv.DictReader(open(os.path.join(HERE, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
    t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
    old.append((t, (o, h, l, c) if c < o else (o, l, h, c)))
end = candles[-1][0] + 300
L = [f"PAPER backtest, $500 2% grid. Recent data {iso(candles[0][0])} -> {iso(end)} UTC (Binance XRPUSDT perp 5-min). Run {iso(time.time())} UTC.", "",
     "| Window (XRP price) | Line | End value | P/L after fees | Round trips | Max drawdown | Fees+slippage (+funding) | Keep $500 in XRP | vs keep $500 in XRP | Liquidations |",
     "|---|---|---|---|---|---|---|---|---|---|"]
def rows(sub, label):
    for name, over, perp in LINES:
        v, hold, st = run(sub, over, perp, fund if perp else {})
        L.append(f"| {label} ({sub[0][1][0]:.3f} -> {sub[-1][1][-1]:.3f}) | {name} | ${v:.2f} | {v - B:+.2f} ({(v / B - 1) * 100:+.2f}%) | {st['sells']} | {st['max_dd_pct']:.1f}% | "
                 f"${st['fees_trade_usd']:.2f}" + (f" (+${st['funding_usd']:.2f})" if perp else "") + f" | ${hold:.2f} ({(hold / B - 1) * 100:+.2f}%) | {v - hold:+.2f} | {st['liquidations']} |")
for w in (14, 30, 60):
    rows([c for c in candles if c[0] >= end - w * 86400], f"{w}d")
rows(old, "Stress, whole Oct 2024-Mar 2025")
L += ["", "### Stress test: a 14-day run starting every day, Oct 2024 - Mar 2025 (funding assumed 0.01%/8h)", "",
      "| Line | Median P/L | Worst P/L | Best P/L | Median vs keep $500 in XRP | Worst vs keep $500 in XRP | Runs with a liquidation |", "|---|---|---|---|---|---|---|"]
starts = [i for i, (t, _) in enumerate(old) if t % 86400 == 0 and t + 14 * 86400 <= old[-1][0] + 300]
for name, over, perp in LINES:
    res = [run(old[i:i + 14 * 288], over, perp, {}) for i in starts]
    pl = sorted(v - B for v, h, s in res); vh = sorted(v - h for v, h, s in res)
    L.append(f"| {name} | {pl[len(pl) // 2]:+.2f} | {pl[0]:+.2f} | {pl[-1]:+.2f} | {vh[len(vh) // 2]:+.2f} | {vh[0]:+.2f} | {sum(s['liquidations'] > 0 for v, h, s in res)} of {len(res)} |")
out = "\n".join(L); print(out)
open(os.path.join(HERE, "backtest_spot500_output.txt"), "w").write(out + "\n")
