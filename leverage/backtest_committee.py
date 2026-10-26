"""PAPER backtest: committee (4 voters) vs leverage_ta vs holding the coin, XRPUSDT and BTCUSDT, 2x and 5x, $100 each.
Recent: real Binance USDⓈ-M perp 5-min klines (data.binance.vision, 75 days; the first ~15 days only warm up indicators), real
Binance monthly funding + OKX proxy for the current month. Stress Oct 2024 - Mar 2025: XRP = the saved Bitstamp 5-min file
(funding assumed 0.01%/8h, same as earlier backtests); BTC = Binance perp monthly archive with real Binance funding.
Parameters fixed up front in committee_config.json / ta_config.json. Outputs backtest_committee_output.txt."""
import json, os, csv, time, datetime as dt
import ta, committee, levdata
HERE = os.path.dirname(os.path.abspath(__file__))
CC = json.load(open(os.path.join(HERE, "committee_config.json"))); TC = json.load(open(os.path.join(HERE, "ta_config.json")))
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
today = dt.datetime.now(dt.timezone.utc).date()

def load(sym):
    rec = []
    for i in range(75, 0, -1):
        try: rec += levdata.archive_klines((today - dt.timedelta(days=i)).isoformat(), sym)
        except Exception as e: print("missing", sym, i, e)
    fund, _ = levdata.funding_since(rec[0][0] - 1, sym)
    for m in sorted({(today - dt.timedelta(days=i)).strftime("%Y-%m") for i in range(75, 0, -1)}):
        try: fund.update(levdata.archive_funding(m, sym))
        except Exception: pass
    if sym == "XRPUSDT":
        old = []
        for r in csv.DictReader(open(os.path.join(HERE, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
            t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
            old.append((t, (o, h, l, c) if c < o else (o, l, h, c)))
        ofund = {}
    else:
        old, ofund = [], {}
        for m in ("2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"):
            old += levdata.archive_klines(m, sym, "monthly"); ofund.update(levdata.archive_funding(m, sym))
    return sorted(rec), fund, sorted(old), ofund

def prep(c5, fund, sym):
    bars = ta.bars_1h(c5)
    return committee.Context(c5, bars, fund, dict(CC["common"], mmr_pct=CC["common"]["mmr_pct"][sym])), ta.indicators(bars, TC["common"])

def run_com(sub, ctx, fund, lev, sym, logs=None):
    cfg = dict(CC["common"], leverage=lev, mmr_pct=CC["common"]["mmr_pct"][sym]); st = committee.new_state(cfg)
    for t, path in sub: committee.step(st, cfg, ctx, t, path, iso(t), fund.get(t, levdata.FUNDING_ASSUMED), None, logs)
    return ta.equity(st, sub[-1][1][-1], cfg), st

def run_ta(sub, ind, fund, lev, sym):
    cfg = dict(TC["common"], leverage=lev, mmr_pct=CC["common"]["mmr_pct"][sym]); st = ta.new_state(cfg)
    for t, path in sub:
        if t % 28800 == 0: ta.funding(st, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        ta.step(st, cfg, t, list(path), ind, iso(t))
    return ta.equity(st, sub[-1][1][-1], cfg), st

def hold(sub): return 100 / (sub[0][1][0] * 1.0005) * sub[-1][1][-1]
def wr(st): return f"{st['wins'] / st['trades'] * 100:.0f}%" if st["trades"] else "—"

L = [f"PAPER backtest: committee vs leverage_ta vs hold. Run {iso(time.time())} UTC. P/L after fees, slippage, funding; open positions valued as if closed at the end.", ""]
for coin, sym in CC["coins"].items():
    rec, fund, old, ofund = load(sym)
    ctx_r, ind_r = prep(rec, fund, sym); ctx_o, ind_o = prep(old, ofund, sym)
    end = rec[-1][0] + 300
    L += [f"## {sym} (recent data to {iso(end)} UTC)", "",
          "| Window (price) | Line | P/L | Closed trades (entries L/S) | Win rate | Liquidations | Max drawdown | Fees / funding | Committee decisions L/S/tie/idle | vs hold |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    def window(sub, ctx, ind, fm, label):
        h = hold(sub); rows = []
        for lev in CC["leverages"]:
            ties = []
            v, st = run_com(sub, ctx, fm, lev, sym, ties)
            sl = sum(x.get("if_long_usd", 0) for x in ties); ss = sum(x.get("if_short_usd", 0) for x in ties)
            d = st["decisions"]
            rows.append(f"| {label} ({sub[0][1][0]:.4g} -> {sub[-1][1][-1]:.4g}) | Committee {lev}x | {v - 100:+.2f} | {st['trades']} ({st['longs']}/{st['shorts']}) | {wr(st)} | {st['liquidations']} | "
                        f"{st['max_dd_pct']:.1f}% | ${st['fees_usd']:.2f} / ${st['funding_usd']:+.2f} | {d['LONG']}/{d['SHORT']}/{d['TIE']}/{d['IDLE']} (ties: if-long {sl:+.2f}, if-short {ss:+.2f}) | {v - h:+.2f} |")
        for lev in CC["leverages"]:
            v, st = run_ta(sub, ind, fm, lev, sym)
            rows.append(f"| | leverage_ta {lev}x | {v - 100:+.2f} | {st['trades']} ({st['longs']}/{st['shorts']}) | {wr(st)} | {st['liquidations']} | {st['max_dd_pct']:.1f}% | "
                        f"${st['fees_usd']:.2f} / ${st['funding_usd']:+.2f} | — | {v - h:+.2f} |")
        rows.append(f"| | Hold $100 of {coin.upper()} | {h - 100:+.2f} | — | — | 0 | — | $0.05 | — | — |")
        L.extend(rows)
    for w in (14, 30, 60): window([c for c in rec if c[0] >= end - w * 86400], ctx_r, ind_r, fund, f"{w}d")
    s0 = min(t for t in ctx_o.t5 if ctx_o.ready(t)) // 86400 * 86400 + 86400
    window([c for c in old if c[0] >= s0], ctx_o, ind_o, ofund, "Stress whole")
    def rolling(cs, ctx, ind, fm, title):
        first = min(t for t in ctx.t5 if ctx.ready(t))
        starts = [i for i, (t, _) in enumerate(cs) if t % 86400 == 0 and t >= first and t + 14 * 86400 <= cs[-1][0] + 300]
        R = ["", f"14-day runs, one starting every day: {sym} {title} ({len(starts)} runs)", "",
             "| Line | Median P/L | Worst run | Best run | Losing runs | Runs with a liquidation | Median trades | Median vs hold |", "|---|---|---|---|---|---|---|---|"]
        for kind in ("Committee", "leverage_ta"):
            for lev in CC["leverages"]:
                res = []
                for i in starts:
                    sub = cs[i:i + 14 * 288]
                    v, st = run_com(sub, ctx, fm, lev, sym) if kind == "Committee" else run_ta(sub, ind, fm, lev, sym)
                    res.append((v - 100, v - hold(sub), st["liquidations"], st["trades"]))
                pl = sorted(r[0] for r in res); vh = sorted(r[1] for r in res); nt = sorted(r[3] for r in res)
                R.append(f"| {kind} {lev}x | {pl[len(pl) // 2]:+.2f} | {pl[0]:+.2f} | {pl[-1]:+.2f} | {sum(r[0] < 0 for r in res)} of {len(res)} | "
                         f"{sum(r[2] > 0 for r in res)} | {nt[len(nt) // 2]} | {vh[len(vh) // 2]:+.2f} |")
        return R
    L += rolling(rec, ctx_r, ind_r, fund, "last 60 days")
    L += rolling(old, ctx_o, ind_o, ofund, "STRESS Oct 2024 - Mar 2025")
    L.append(""); print("\n".join(L[-40:]), flush=True)
out = "\n".join(L)
open(os.path.join(HERE, "backtest_committee_output.txt"), "w").write(out + "\n")
