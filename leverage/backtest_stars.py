"""PAPER backtest of 'Stars Aligned' (stars.py): XRPUSDT 10x, opens only when all 4 PROXY voters agree (committee.proxy_votes,
the same stand-ins the team ledger uses for missing votes; no real vote history exists, so every vote here is a proxy).
TP +2% (live; backtest compares +1/+1.5/+2/+3%) / stop -1% price move, isolated margin, ta.py fees/slippage/funding/liquidation (Binance-style rules).
News blackout: events_calendar.csv only (+-3h); Riley's news log has no history. Data/loading = backtest_committee.py
(Binance perp 5-min archive + real funding for the last 60 days; Bitstamp 5-min file, funding assumed 0.01%/8h, for Oct 2024 - Mar 2025).
Output: backtest_stars_output.txt."""
import os, time
import ta, committee, levdata, stars
import backtest_committee as bc
HERE = os.path.dirname(os.path.abspath(__file__)); SYM = "XRPUSDT"

def run(sub, ctx, fund, times, whatif=False, tp=None, stop=None):
    accts = {b: ta.new_state(stars.cfg(bc.CC["common"], b, tp, stop)) for b in stars.BUDGETS}
    n = dict(unanimous=0, long=0, short=0, opened=0, blackout=0, busy=0, near_long=0, near_short=0)
    for t, path in sub:
        ts = bc.iso(t); sig = {}
        if t % 28800 == 0:
            for b, a in accts.items(): ta.funding(a, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], ts)
        if t % 900 == 0 and ctx.ready(t):
            _, PV, _, _, _ = committee.proxy_votes(ctx, t)
            cv = {v: PV[v][0] for v in ("casey", "pip", "theo", "remy")}
            n["near_long"] += cv["casey"] == cv["theo"] == cv["remy"] == "LONG"     # 3/3 non-Pip LONG: only a real Pip LONG makes it 4/4
            n["near_short"] += cv["pip"] == cv["theo"] == cv["remy"] == "SHORT"    # 3/3 non-Casey SHORT: only a real Casey SHORT makes it 4/4
            side = stars.unanimous({v: {"call": PV[v][0]} for v in ("casey", "pip", "theo", "remy")})
            if whatif and not side:   # WHAT-IF: pretend the missing side voter (Pip on longs, Casey on shorts) agreed for real
                side = "LONG" if cv["casey"] == cv["theo"] == cv["remy"] == "LONG" else "SHORT" if cv["pip"] == cv["theo"] == cv["remy"] == "SHORT" else None
            if side:
                n["unanimous"] += 1; n[side.lower()] += 1
                if any(a["pos"] for a in accts.values()): n["busy"] += 1
                elif stars.in_blackout(t, times): n["blackout"] += 1
                else: n["opened"] += 1; sig = stars.signal(t, path[0], side, "stars 4/4 proxy", stop)
        for b, a in accts.items(): ta.step(a, stars.cfg(bc.CC["common"], b, tp, stop), t, list(path), sig, ts)
    return accts, n

COMBOS = ((1.0, 1.0), (1.5, 1.0), (2.0, 1.0), (3.0, 1.0), (3.0, 1.5), (5.0, 2.0))   # (take profit %, stop %)

def be_real(a):
    """Break-even win rate from this run's own average win / average loss (fees + funding included)."""
    w, l = a["wins"], a["trades"] - a["wins"]
    if not w or not l: return "—"
    aw, al = a["win_usd"] / w, -a["loss_usd"] / l
    return f"{al / (aw + al) * 100:.0f}%"

def main():
    rec, fund, old, ofund = bc.load(SYM)
    times = sorted(committee.EVENTS); C = bc.CC["common"]
    L = [f"PAPER backtest: Stars Aligned (4/4 votes, XRPUSDT 10x, TP/stop combos +1/-1, +1.5/-1, +2/-1, +3/-1, +3/-1.5, +5/-2; live line uses +2/-1; +-3h events-calendar blackout). Run {bc.iso(time.time())} UTC.",
         "All votes are proxies (no real vote history). NOTE: Casey's proxy only votes LONG/IDLE and Pip's only SHORT/IDLE, so an all-proxy 4/4 is "
         "impossible by construction; Stars Aligned can only fire when Pip casts a real LONG or Casey a real SHORT. WHAT-IF rows assume that missing "
         "voter agreed whenever the other three did (hypothetical, upper bound on signals). P/L after fees, slippage, funding; open positions valued as if closed at the end. "
         "Break-even (fees) = one clean TP win vs one stop loss at 10x; break-even (actual) = from the run's own average win / loss incl. funding and gaps.", "",
         "| Window (price) | TP / stop | Unanimous rounds (L/S) | Opened / skipped news / skipped in-trade | Trades (L/S) | **Win rate** | **Break-even (fees / actual)** | Liq. | $50 P/L | $100 P/L | $500 P/L | Max DD | Worst DD $500 | Fees / funding $100 |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for label, cs, fm, w in (("Last 60d", rec, fund, 60), ("Stress Oct 2024-Mar 2025", old, ofund, None)):
        ctx = committee.Context(cs, ta.bars_1h(cs), fm, bc.base(SYM, True, True), bc.metrics(SYM, cs), bc.FNG)
        if w: end = cs[-1][0] + 300; sub = [c for c in cs if c[0] >= end - w * 86400]
        else:
            s0 = min(t for t in ctx.t5 if ctx.ready(t)) // 86400 * 86400 + 86400; sub = [c for c in cs if c[0] >= s0]
        for wi, tp, sp in [(False, stars.TP_PCT, stars.STOP_PCT)] + [(True, x, y) for x, y in COMBOS]:
            accts, n = run(sub, ctx, fm, times, wi, tp, sp); px = sub[-1][1][-1]; a = accts[100]
            pl = {b: ta.equity(x, px, stars.cfg(C, b, tp, sp)) - b for b, x in accts.items()}
            L.append(f"| {'WHAT-IF ' if wi else 'Proxies as-is '}{label} {bc.iso(sub[0][0])[:10]}..{bc.iso(sub[-1][0])[:10]} ({sub[0][1][0]:.4g} -> {px:.4g}) | +{tp:g}% / -{sp:g}% | {n['unanimous']} ({n['long']}/{n['short']}) | "
                     f"{n['opened']} / {n['blackout']} / {n['busy']} | {a['trades']} ({a['longs']}/{a['shorts']}) | {bc.wr(a)} | {stars.breakeven(C, tp, sp)[2] * 100:.0f}% / {be_real(a)} | {a['liquidations']} | "
                     f"{pl[50]:+.2f} | {pl[100]:+.2f} | {pl[500]:+.2f} | {a['max_dd_pct']:.1f}% | -{accts[500].get('max_dd_usd', 0):.2f} | ${a['fees_usd']:.2f} / ${a['funding_usd']:+.2f} |")
            if not wi: L.append(f"|  ↳ near misses: Casey+Theo+Remy LONG {n['near_long']} rounds (needs a real Pip LONG), Pip+Theo+Remy SHORT {n['near_short']} rounds (needs a real Casey SHORT) | | | | | | | | | | | | | |")
            print(*L[-1 if wi else -2:], sep="\n", flush=True)
    open(os.path.join(HERE, "backtest_stars_output.txt"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
