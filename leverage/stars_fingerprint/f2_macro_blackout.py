"""PAPER research only. F2 squeeze LONG (10x, TP +3%/stop -1.5%, $100/trade, fees/slippage/funding/liquidation) baseline vs
macro blackout: no NEW entry within 12h before a scheduled FOMC decision or US CPI release (variant B: also 2h after).
Reuses the per-hour simulated outcomes in candidates_*.csv written by fingerprint.py (same engine, no new data pulls).
Event times = FOMC + CPI rows of ../events_calendar.csv (FOMC dates checked vs federalreserve.gov/monetarypolicy/fomccalendars.htm)."""
import os, csv, datetime as dt
H = os.path.dirname(os.path.abspath(__file__))
ts = lambda s: int(dt.datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp())
EV = sorted((ts(r["datetime_utc"]), r["event"]) for r in csv.DictReader(open(os.path.join(H, "..", "events_calendar.csv"))) if r["event"] in ("FOMC", "CPI"))
def load(f):
    out = []
    for r in csv.DictReader(open(os.path.join(H, f))):
        out.append(dict(t=int(r["t"]), crowded=r["crowded"], ema=r["ema200_4h"], oi=float(r["oi24_pct"] or 0), win=r["LONG_win"] == "True",
                        kind=r["LONG_kind"], ret=float(r["LONG_ret"]), exit_t=int(r["LONG_exit_t"]), minq=float(r["LONG_minq"])))
    return out
f2 = lambda r: r["crowded"] == "shorts" or (r["oi"] >= 5 and r["ema"] == "above")
def blocked(t, before, after): return any(e - before * 3600 <= t < e + after * 3600 for e, _ in EV)
def seq(rows, cond):
    pl = peak = dd = 0.0; busy = 0; taken = []
    for r in rows:
        if r["t"] < busy or not cond(r) or r["kind"] == "OPEN_AT_END": continue
        dd = max(dd, peak - (pl - 100 * (1 - r["minq"]))); pl += 100 * r["ret"]; peak = max(peak, pl); dd = max(dd, peak - pl)
        busy = r["exit_t"]; taken.append(r)
    n = len(taken); w = sum(r["win"] for r in taken)
    return dict(n=n, w=w, pl=pl, dd=dd, liq=sum(r["kind"] == "LIQUIDATION" for r in taken), taken=taken)
O = load("candidates_rally_2024_25.csv"); R = load("candidates_last60d.csv"); cut = ts("2025-01-01T00:00:00Z")
P = [("Oct-Dec 2024", [r for r in O if r["t"] < cut]), ("Jan-Mar 2025", [r for r in O if r["t"] >= cut]), ("Last 60 days (Aug 27-Oct 25 2026)", R)]
V = [("Baseline F2", 0, 0), ("Blackout 12h before", 12, 0), ("Blackout 12h before + 2h after", 12, 2)]
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
L = ["# F2 macro blackout test (PAPER). F2 squeeze LONG 10x, TP +3% / stop -1.5%, $100 per trade, one at a time, after fees/slippage/funding/liquidation.",
     "Blackout = skip new entries from 12h before a scheduled FOMC decision or CPI release (variant: until 2h after). Events: " + ", ".join(f"{iso(e)} {k}" for e, k in EV if e < ts("2026-10-26T00:00:00Z")), "",
     "| Period | Variant | Trades | Win rate | P/L after fees | Worst drawdown | Liquidations |", "|---|---|---|---|---|---|---|"]
notes = []
for pn, rows in P:
    base = seq(rows, f2)
    for vn, b, a in V:
        s = seq(rows, (lambda b, a: lambda r: f2(r) and not blocked(r["t"], b, a))(b, a)) if b else base
        L.append(f"| {pn} | {vn} | {s['n']} | {s['w'] / s['n'] * 100 if s['n'] else 0:.0f}% | ${s['pl']:+.0f} | -${s['dd']:.0f} | {s['liq']} |")
        if b:
            bt = {r["t"] for r in s["taken"]}; rem = [r for r in base["taken"] if r["t"] not in bt]; add = [r for r in s["taken"] if r["t"] not in {x["t"] for x in base["taken"]}]
            notes.append(f"- {pn}, {vn}: removed {len(rem)} baseline trades (net ${sum(100 * r['ret'] for r in rem):+.0f}; {sum(r['win'] for r in rem)} won / {sum(not r['win'] for r in rem)} lost)"
                         f"; {len(add)} different trades taken instead (net ${sum(100 * r['ret'] for r in add):+.0f}). Removed: " + (", ".join(f"{iso(r['t'])} {r['kind']} ${100 * r['ret']:+.0f}" for r in rem) or "none"))
L += ["", "## What the blackout removed", *notes]
open(os.path.join(H, "f2_macro_blackout.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
