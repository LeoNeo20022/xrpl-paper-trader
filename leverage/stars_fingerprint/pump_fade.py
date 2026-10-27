"""PAPER research only (no keys, no orders, no wallets): Riley's 'fade the big pump' idea, counting ALL signals.
Signal: on a 1h close, XRP close >= +15% vs (a) the lowest low of the prior 72 1h bars, or (b) the 1h close 72h earlier.
Theo variant: (a) AND longs crowded (committee crowding: >= 2 of funding >= +0.03%/8h, OI +5%/24h, L/S ratio top 20% of 7d).
Trade: 10x isolated SHORT at the next open, TP +3% / stop -1.5% on price, 24h time limit, same ta.py engine/costs/real funding
as fingerprint.py (fp.simulate with MAXH=24), one position at a time, 12h cooldown after exit, $100 per trade (no compounding).
'Further rise' = from the entry open, price rose +3% before it fell -1.5% (within 24h), counted over every signal hour.
News: signals within 12h after a news_found=yes, tone=bullish row of Riley's stars_top_moves_news.csv (biased list: big moves only).
Data: the cached files fingerprint.py uses (/tmp/stars_fp_cache.pkl); no Binance calls. Output: pump_fade.md."""
import os, csv, pickle, datetime as dt
import fingerprint as fp
fp.MAXH = 24
import ta, committee, backtest_committee as bc
COOL = 12 * 3600; NEWS = "/home/box/shared/strategy-lab/stars_top_moves_news.csv"

def further_rise(cs, i):
    e = cs[i][1][0]
    for _, path in cs[i:i + 288]:
        for p in path:
            if p >= e * 1.03: return True
            if p <= e * 0.985: return False
    return False

def signals(cs, fund, met, start, end):
    bars = ta.bars_1h(cs); ctx = committee.Context(cs, bars, fund, bc.base(fp.SYM, True, True), met, bc.FNG)
    pos = {t: i for i, (t, _) in enumerate(cs)}; out = []
    for t in range(start // 3600 * 3600, end, 3600):
        k = ctx.hour_idx(t)
        if t not in pos or k is None or k < 72: continue
        c = bars[k][4]; lo = min(b[3] for b in bars[k - 72:k]); c72 = bars[k - 72][4]
        A, B = c >= lo * 1.15, c >= c72 * 1.15
        if not (A or B): continue
        crowd = ctx.crowding(t, fund.get(t // 28800 * 28800))["crowded"] if ctx.ready(t) else None
        o = fp.simulate(cs, pos[t], fund, "SHORT")
        out.append(dict(t=t, A=A, B=B, crowded=crowd == "longs", rise=further_rise(cs, pos[t]), **o))
    return out

def seq(rows, cond):
    pl = peak = dd = 0.0; busy = 0; n = w = liq = 0; taken = []
    for r in rows:
        if r["t"] < busy or not cond(r) or r["kind"] == "OPEN_AT_END": continue
        n += 1; w += r["win"]; liq += r["kind"] == "LIQUIDATION"; taken.append(r)
        dd = max(dd, peak - (pl - 100 * (1 - r["minq"]))); pl += 100 * r["ret"]; peak = max(peak, pl); dd = max(dd, peak - pl)
        busy = r["exit_t"] + COOL
    return dict(trades=n, wins=w, pl=pl, dd=dd, liq=liq, taken=taken)

def main():
    d = pickle.load(open(fp.CACHE, "rb"))                         # cached data only (Binance is geo-blocked here)
    end = d["rec"][-1][0] + 300; cut = int(dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc).timestamp())
    O = signals(d["old"], d["ofund"], d["omet"], d["old"][0][0], d["old"][-1][0] - 3600)
    R = signals(d["rec"], d["fund"], d["rmet"], end - 60 * 86400, end - 3600)
    parts = [("Oct-Dec 2024", [r for r in O if r["t"] < cut]), ("Jan-Mar 2025", [r for r in O if r["t"] >= cut]), ("Last 60 days", R)]
    lines = [("A: +15% vs 72h low", lambda r: r["A"]), ("B: +15% vs close 72h ago", lambda r: r["B"]), ("A + longs crowded (Theo)", lambda r: r["A"] and r["crowded"])]
    L = ["# Pump fade (PAPER): 10x SHORT after a +15% pump, TP +3% / stop -1.5%, 24h limit, 12h cooldown, $100/trade, after fees, slippage and real funding", "",
         "| Variant | " + " | ".join(p for p, _ in parts) + " |", "|---|---|---|---|"]
    res = {}
    for lab, fn in lines:
        cells = []
        for pn, rows in parts:
            s = seq(rows, fn); res[(lab, pn)] = s; sig = [r for r in rows if fn(r)]
            cells.append(f"{s['trades']} trades, {s['wins'] / s['trades'] * 100 if s['trades'] else 0:.0f}% wins, ${s['pl']:+.0f}, DD -${s['dd']:.0f}, {s['liq']} liq; "
                         f"signal hours {len(sig)}, further +3% first {sum(r['rise'] for r in sig)} ({sum(r['rise'] for r in sig) / len(sig) * 100 if sig else 0:.0f}%)")
        L.append(f"| {lab} | " + " | ".join(cells) + " |")
    L += ["| ref: retired pop fade | -$542 | -$137 | -$10 |", "| ref: F3 | -$432 | +$204 | +$145 |", ""]
    # news overlap
    bull = [int(dt.datetime.fromisoformat(r["move_timestamp_utc"]).replace(tzinfo=dt.timezone.utc).timestamp())
            for r in csv.DictReader(open(NEWS)) if r["news_found"].strip() == "yes" and r["tone"].strip() == "bullish"]
    near = lambda t: any(0 <= t - b <= 12 * 3600 for b in bull)
    taken = [r for lab, _ in lines[:1] for pn, _ in parts for r in res[(lab, pn)]["taken"]]
    hit = [r for r in taken if near(r["t"])]; rest = [r for r in taken if not near(r["t"])]
    f = lambda xs: f"{len(xs)} trades, {sum(r['win'] for r in xs)} won, ${sum(100 * r['ret'] for r in xs):+.0f}"
    L += [f"## News overlap (variant A trades; {len(bull)} bullish news moves in Riley's file)", "",
          f"- Within 12h after a bullish headline move: {f(hit)}" + "".join(f"\n  - {fp.iso(r['t'])} UTC: {r['kind']}, ${100 * r['ret']:+.1f}" for r in hit),
          f"- All other A trades: {f(rest)}", "",
          "Caveat: biased subset. Riley's list only holds the 48 biggest moves, so bullish headlines never followed by a big move are missing; this cannot test 'short after bullish news' in general.", ""]
    ok = sum(res[("A: +15% vs 72h low", pn)]["pl"] > 0 for pn, _ in parts); enough = all(res[("A: +15% vs 72h low", pn)]["trades"] >= 8 for pn, _ in parts)
    L.append(f"Gate (variant A): positive in {ok} of 3 periods, >= 8 trades in every period: {enough} -> {'PASS' if ok >= 2 and enough else 'FAIL'}")
    L.append("Notes: 'prior 72h low' excludes the signal bar. Timeouts are marked at the 24h close (engine equity). No live paper line added.")
    open(os.path.join(fp.HERE, "pump_fade.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))

if __name__ == "__main__":
    main()
