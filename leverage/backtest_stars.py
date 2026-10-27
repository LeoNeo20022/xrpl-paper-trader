"""PAPER backtest of 'Stars Aligned' (stars.py): XRPUSDT 10x, opens only when all 4 voters agree: team proxies (committee.proxy_votes)
plus the Stars-only stand-ins (stars.standins); no real vote history exists, so every vote here is a proxy.
TP +3% / stop -1.5% price move, isolated margin, ta.py fees/slippage/funding/liquidation (Binance-style rules).
No news/event blackout (removed 2026-10-27). Data/loading = backtest_committee.py
(Binance perp 5-min archive + real funding for the last 60 days; Bitstamp 5-min file, funding assumed 0.01%/8h, for Oct 2024 - Mar 2025).
Output: backtest_stars_output.txt."""
import os, time
import ta, committee, levdata, stars
import backtest_committee as bc
HERE = os.path.dirname(os.path.abspath(__file__)); SYM = "XRPUSDT"

def run(sub, ctx, fund, tp=None, stop=None):
    """Proxies + Stars-only stand-ins, no news blackout (as live since 2026-10-27)."""
    accts = {b: ta.new_state(stars.cfg(bc.CC["common"], b, tp, stop)) for b in stars.BUDGETS}
    n = dict(unanimous=0, long=0, short=0, opened=0, busy=0, casey_standin=0, pip_standin=0, three=0)
    for t, path in sub:
        ts = bc.iso(t); sig = {}
        if t % 28800 == 0:
            for b, a in accts.items(): ta.funding(a, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], ts)
        if t % 900 == 0 and ctx.ready(t):
            _, PV, _, cr, trend = committee.proxy_votes(ctx, t)
            calls = stars.standins({v: {"call": PV[v][0], "proxy": True} for v in ("casey", "pip", "theo", "remy")}, cr, trend.get("ema200_4h"), bc.CC["common"])
            n["casey_standin"] += bool(calls["casey"].get("standin")); n["pip_standin"] += bool(calls["pip"].get("standin"))
            side = stars.unanimous(calls); cv = [c["call"] for c in calls.values()]
            n["three"] += max(cv.count("LONG"), cv.count("SHORT")) == 3
            if side:
                n["unanimous"] += 1; n[side.lower()] += 1
                if any(a["pos"] for a in accts.values()): n["busy"] += 1
                else: n["opened"] += 1; sig = stars.signal(t, path[0], side, "stars 4/4 proxy", stop)
        for b, a in accts.items(): ta.step(a, stars.cfg(bc.CC["common"], b, tp, stop), t, list(path), sig, ts)
    return accts, n

def be_real(a):
    w, l = a["wins"], a["trades"] - a["wins"]
    if not w or not l: return "—"
    aw, al = a["win_usd"] / w, -a["loss_usd"] / l
    return f"{al / (aw + al) * 100:.0f}%"

def main():
    rec, fund, old, ofund = bc.load(SYM); C = bc.CC["common"]; tp, sp = stars.TP_PCT, stars.STOP_PCT
    L = [f"PAPER backtest: Stars Aligned as live since 2026-10-27: 4/4 votes (team proxies + Stars-only stand-ins: Casey SHORT when 4h < EMA200 and longs crowded; "
         f"Pip LONG when 4h > EMA200, crowding clear and funding calm), XRPUSDT 10x, TP +{tp:g}% / stop -{sp:g}%, NO news blackout. Run {bc.iso(time.time())} UTC.",
         "All votes are proxies (no real vote history); crowding inputs = the existing backtest proxies (Binance daily metrics OI + long/short count ratio, "
         "Fear & Greed, funding; Oct 2024-Mar 2025 XRP funding = the existing assumed 0.01%/8h, also fed to the voters so Pip's 'funding calm' can be read). P/L after fees, slippage, funding; open positions valued as if closed at the end. Earlier TP/stop comparison: git history of this file.", "",
         "| Window (price) | Signals 4/4 (L/S) | Opened / skipped in-trade | Stand-in votes (Casey SHORT / Pip LONG rounds) | 3-of-4 rounds (near misses) | Trades (L/S) | Win rate | Break-even (fees / actual) | Liq. | $50 P/L | $100 P/L | $500 P/L | Max DD | Worst DD $500 | Fees / funding $100 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for label, cs, fm, w in (("Last 60d", rec, fund, 60), ("Stress Oct 2024-Mar 2025", old, ofund, None)):
        if not fm: fm = {t: levdata.FUNDING_ASSUMED for t, _ in cs if t % 28800 == 0}   # no XRP funding history: existing backtest assumption (0.01%/8h)
        ctx = committee.Context(cs, ta.bars_1h(cs), fm, bc.base(SYM, True, True), bc.metrics(SYM, cs), bc.FNG)
        if w: end = cs[-1][0] + 300; sub = [c for c in cs if c[0] >= end - w * 86400]
        else:
            s0 = min(t for t in ctx.t5 if ctx.ready(t)) // 86400 * 86400 + 86400; sub = [c for c in cs if c[0] >= s0]
        accts, n = run(sub, ctx, fm, tp, sp); px = sub[-1][1][-1]; a = accts[100]
        pl = {b: ta.equity(x, px, stars.cfg(C, b, tp, sp)) - b for b, x in accts.items()}
        L.append(f"| {label} {bc.iso(sub[0][0])[:10]}..{bc.iso(sub[-1][0])[:10]} ({sub[0][1][0]:.4g} -> {px:.4g}) | {n['unanimous']} ({n['long']}/{n['short']}) | "
                 f"{n['opened']} / {n['busy']} | {n['casey_standin']} / {n['pip_standin']} | {n['three']} | {a['trades']} ({a['longs']}/{a['shorts']}) | {bc.wr(a)} | "
                 f"{stars.breakeven(C, tp, sp)[2] * 100:.0f}% / {be_real(a)} | {a['liquidations']} | {pl[50]:+.2f} | {pl[100]:+.2f} | {pl[500]:+.2f} | "
                 f"{a['max_dd_pct']:.1f}% | -{accts[500].get('max_dd_usd', 0):.2f} | ${a['fees_usd']:.2f} / ${a['funding_usd']:+.2f} |")
        print(L[-1], flush=True)
    open(os.path.join(HERE, "backtest_stars_output.txt"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
