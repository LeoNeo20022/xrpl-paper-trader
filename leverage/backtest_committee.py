"""PAPER backtest: committee (4 voters + crowding + Fear & Greed + Theo's rules R1-R6) vs leverage_ta vs holding the coin,
XRPUSDT and BTCUSDT, $100 per line. Parameters fixed up front in committee_config.json / ta_config.json (no tuning).
Data: recent = real Binance USDⓈ-M perp 5-min klines (data.binance.vision, 75 days; first ~15 days warm-up), real Binance funding
(monthly files) + OKX proxy for the current month. Stress Oct 2024 - Mar 2025: XRP = saved Bitstamp 5-min file (funding assumed
0.01%/8h), BTC = Binance perp monthly archive with real funding. Crowding history = Binance daily 'metrics' (count long/short ratio,
open interest in coins). Fear & Greed = alternative.me daily history. News events = events_calendar.csv (CPI/PPI/FOMC).
Caveat: live uses OKX's long/short ACCOUNT ratio, the backtest Binance's count ratio, so the R2 thresholds (1.8 / 0.55) do not
mean exactly the same thing in both. Output: backtest_committee_output.txt."""
import json, os, csv, time, datetime as dt
from concurrent.futures import ThreadPoolExecutor
import ta, committee, levdata
HERE = os.path.dirname(os.path.abspath(__file__))
CC = json.load(open(os.path.join(HERE, "committee_config.json"))); TC = json.load(open(os.path.join(HERE, "ta_config.json")))
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
today = dt.datetime.now(dt.timezone.utc).date()
FNG, _ = levdata.fear_greed()
THEO = [k for k in CC["common"] if k.startswith("theo_r")]
VARIANTS = [("Committee+Theo 2x", 2, True, True), ("Committee+Theo 5x", 5, True, True), ("Committee+Theo mix", "mix", True, True),
            ("Committee 2x, no Theo rules", 2, False, True), ("Committee 2x, no Theo, no crowding/F&G", 2, False, False),
            ("Proxy team (Casey/Pip/Theo/Remy) 2x", 2, True, True, "proxy"), ("Proxy team 5x", 5, True, True, "proxy"), ("Proxy team mix", "mix", True, True, "proxy")]
ROLL = [0, 1, 2, 3, 5, 7]

def base(sym, theo, crowd):
    c = dict(CC["common"], mmr_pct=CC["common"]["mmr_pct"][sym], crowding=crowd)
    for k in THEO: c[k] = theo
    return c

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
        old, ofund = [], {}
        for r in csv.DictReader(open(os.path.join(HERE, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
            t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
            old.append((t, (o, h, l, c) if c < o else (o, l, h, c)))
    else:
        old, ofund = [], {}
        for m in ("2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03"):
            old += levdata.archive_klines(m, sym, "monthly"); ofund.update(levdata.archive_funding(m, sym))
    return sorted(rec), fund, sorted(old), ofund

def metrics(sym, cs):
    days = sorted({dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat() for t, _ in cs}); out = {}
    def one(d):
        try: return levdata.archive_metrics(d, sym)
        except Exception: return {}
    with ThreadPoolExecutor(16) as ex:
        for r in ex.map(one, days): out.update(r)
    return out

def prep(c5, fund, sym):
    bars = ta.bars_1h(c5); crowd = metrics(sym, c5)
    ctx = {(th, cr): committee.Context(c5, bars, fund, base(sym, th, cr), crowd if cr else None, FNG if cr else None) for th, cr in {(v[2], v[3]) for v in VARIANTS}}
    return ctx, ta.indicators(bars, TC["common"]), len(crowd)

def run_com(sub, ctxs, fund, var, sym, ties=None):
    _, lev, th, cr = var[:4]; c = base(sym, th, cr)
    cfg = dict(c, leverage=c["mix_base"], sizing="mix") if lev == "mix" else dict(c, leverage=lev)
    if len(var) > 4: cfg["voters"] = var[4]
    st = committee.new_state(cfg); ctx = ctxs[(th, cr)]
    for t, path in sub: committee.step(st, cfg, ctx, t, path, iso(t), fund.get(t, levdata.FUNDING_ASSUMED), None, ties)
    return ta.equity(st, sub[-1][1][-1], cfg), st

def run_ta(sub, ind, fund, lev, sym):
    cfg = dict(TC["common"], leverage=lev, mmr_pct=CC["common"]["mmr_pct"][sym]); st = ta.new_state(cfg)
    for t, path in sub:
        if t % 28800 == 0: ta.funding(st, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        ta.step(st, cfg, t, list(path), ind, iso(t))
    return ta.equity(st, sub[-1][1][-1], cfg), st

def hold(sub): return 100 / (sub[0][1][0] * 1.0005) * sub[-1][1][-1]
def wr(st): return f"{st['wins'] / st['trades'] * 100:.0f}%" if st["trades"] else "—"

L = [f"PAPER backtest: committee (+crowding, F&G, Theo R1-R6) vs leverage_ta vs hold. Run {iso(time.time())} UTC. "
     "P/L after fees, slippage, funding; open positions valued as if closed at the end. Votes every 15 min.", ""]
for coin, sym in CC["coins"].items():
    rec, fund, old, ofund = load(sym)
    ctx_r, ind_r, nm_r = prep(rec, fund, sym); ctx_o, ind_o, nm_o = prep(old, ofund, sym)
    end = rec[-1][0] + 300
    L += [f"## {sym} (recent data to {iso(end)} UTC; crowding metrics hours: recent {nm_r}, stress {nm_o})", "",
          "| Window (price) | Line | P/L | Closed trades (entries L/S) | Trades/day | Win rate | Liquidations | Max drawdown | Fees / funding | Decisions L/S/tie/idle | Rules fired (votes) | vs hold |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def window(sub, ctxs, ind, fm, label):
        h = hold(sub); days = len(sub) / 288
        for var in VARIANTS:
            ties = []; v, st = run_com(sub, ctxs, fm, var, sym, ties); d = st["decisions"]
            rf = ", ".join(f"{k}:{n}" for k, n in sorted(st.get("rules_fired", {}).items()))
            extra = f" [5x trades {st.get('mix_high_trades', 0)}]" if var[1] == "mix" else ""
            L.append(f"| {label} ({sub[0][1][0]:.4g} -> {sub[-1][1][-1]:.4g}) | {var[0]}{extra} | {v - 100:+.2f} | {st['trades']} ({st['longs']}/{st['shorts']}) | "
                     f"{(st['longs'] + st['shorts']) / days:.2f} | {wr(st)} | {st['liquidations']} | {st['max_dd_pct']:.1f}% | ${st['fees_usd']:.2f} / ${st['funding_usd']:+.2f} | "
                     f"{d['LONG']}/{d['SHORT']}/{d['TIE']}/{d['IDLE']} | {rf or '—'}; news flats {st.get('news_flats', 0)}; crowded votes {st.get('crowded_votes', 0)} | {v - h:+.2f} |")
        for lev in (2, 5):
            v, st = run_ta(sub, ind, fm, lev, sym)
            L.append(f"| | leverage_ta {lev}x | {v - 100:+.2f} | {st['trades']} ({st['longs']}/{st['shorts']}) | {(st['longs'] + st['shorts']) / days:.2f} | {wr(st)} | "
                     f"{st['liquidations']} | {st['max_dd_pct']:.1f}% | ${st['fees_usd']:.2f} / ${st['funding_usd']:+.2f} | — | — | {v - h:+.2f} |")
        L.append(f"| | Hold $100 of {coin.upper()} | {h - 100:+.2f} | — | — | — | 0 | — | $0.05 | — | — | — |")
    for w in (14, 30, 60): window([c for c in rec if c[0] >= end - w * 86400], ctx_r, ind_r, fund, f"{w}d")
    s0 = min(t for t in ctx_o[(True, True)].t5 if ctx_o[(True, True)].ready(t)) // 86400 * 86400 + 86400
    window([c for c in old if c[0] >= s0], ctx_o, ind_o, ofund, "Stress whole")
    def rolling(cs, ctxs, ind, fm, title):
        first = min(t for t in ctxs[(True, True)].t5 if ctxs[(True, True)].ready(t))
        starts = [i for i, (t, _) in enumerate(cs) if t % 86400 == 0 and t >= first and t + 14 * 86400 <= cs[-1][0] + 300]
        R = ["", f"14-day runs, one starting every day: {sym} {title} ({len(starts)} runs)", "",
             "| Line | Median P/L | Worst run | Best run | Losing runs | Runs with a liquidation | Median trades | Median vs hold |", "|---|---|---|---|---|---|---|---|"]
        lines = [(VARIANTS[i][0], ("c", VARIANTS[i])) for i in ROLL] + [(f"leverage_ta {l}x", ("t", l)) for l in (2, 5)]
        for name, (kind, x) in lines:
            res = []
            for i in starts:
                sub = cs[i:i + 14 * 288]
                v, st = run_com(sub, ctxs, fm, x, sym) if kind == "c" else run_ta(sub, ind, fm, x, sym)
                res.append((v - 100, v - hold(sub), st["liquidations"], st["trades"]))
            pl = sorted(r[0] for r in res); vh = sorted(r[1] for r in res); nt = sorted(r[3] for r in res)
            R.append(f"| {name} | {pl[len(pl) // 2]:+.2f} | {pl[0]:+.2f} | {pl[-1]:+.2f} | {sum(r[0] < 0 for r in res)} of {len(res)} | "
                     f"{sum(r[2] > 0 for r in res)} | {nt[len(nt) // 2]} | {vh[len(vh) // 2]:+.2f} |")
        return R
    L += rolling(rec, ctx_r, ind_r, fund, "last 60 days")
    L += rolling(old, ctx_o, ind_o, ofund, "STRESS Oct 2024 - Mar 2025")
    L.append(""); print("\n".join(L[-45:]), flush=True)
    open(os.path.join(HERE, "backtest_committee_output.txt"), "w").write("\n".join(L) + "\n")
