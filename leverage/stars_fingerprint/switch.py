"""PAPER research: Pip's regime-switch line. Same engine and candidates as fingerprint.py (10x, TP +3% / stop -1.5%, $100 per trade).
Regime UP = last closed 4h candle above the 4h EMA200 AND that EMA200 is RISING (higher than 24h ago; variant: 72h ago).
UP -> take only F2 longs; otherwise -> take only F3 shorts. One position at a time.
Lag cost = trades opened within 48h after the regime label flipped (the label is late by design), vs all other trades.
Output: switch.md."""
import os, datetime as dt
import fingerprint as fp

F2 = fp.FINGERPRINTS[1][2]; F3 = fp.FINGERPRINTS[2][2]
def regime(r, key): return r["ema200_4h"] == "above" and bool(r[key])

def run(rows, key, lagwin=48 * 3600):
    pl, peak, dd, busy, n, w = 0.0, 0.0, 0.0, 0, 0, 0; flips, last = [], None; lag = [0, 0, 0.0]
    for r in rows:
        g = regime(r, key) if r[key] is not None else None
        if g is not None and last is not None and g != last: flips.append(r["t"])
        if g is not None: last = g
        if r["t"] < busy or g is None: continue
        side, fn = ("LONG", F2) if g else ("SHORT", F3)
        if not fn(r) or r[side + "_kind"] == "OPEN_AT_END": continue
        n += 1; w += r[side + "_win"]; ret = 100 * r[side + "_ret"]
        dd = max(dd, peak - (pl - 100 * (1 - r[side + "_minq"]))); pl += ret; peak = max(peak, pl); dd = max(dd, peak - pl)
        busy = r[side + "_exit_t"]
        if flips and r["t"] - flips[-1] <= lagwin: lag[0] += 1; lag[1] += r[side + "_win"]; lag[2] += ret
    return dict(trades=n, wins=w, wr=w / n if n else 0, pl=pl, dd=dd, liq=0), len(flips), lag

def main():
    d = fp.load(); end = d["rec"][-1][0] + 300
    R = fp.period("last60d", d["rec"], d["rvol"], d["fund"], d["rmet"], end - 60 * 86400, end - 3600)
    O = fp.period("rally", d["old"], d["ovol"], d["ofund"], d["omet"], d["old"][0][0], d["old"][-1][0] - 3600)
    cut = int(dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc).timestamp())
    parts = [("Oct-Dec 2024", [r for r in O if r["t"] < cut]), ("Jan-Mar 2025", [r for r in O if r["t"] >= cut]), ("Last 60 days", R)]
    L = ["# Regime switch (PAPER): UP (4h close above a rising 4h EMA200) -> F2 longs only, else F3 shorts only. 10x, TP +3% / stop -1.5%, $100 per trade, after fees/funding.", "",
         "Oct-Dec 2024 has no EMA200 slope until about Nov 7 (the 4h EMA200 needs ~37 days of warm-up), so hours before that are skipped by the switch.", "",
         "| Line | " + " | ".join(p for p, _ in parts) + " |", "|---|" + "---|" * len(parts)]
    res = {}
    for key, lab in (("ema200_4h_rising24", "Switch, EMA200 rising vs 24h ago"), ("ema200_4h_rising72", "Switch, EMA200 rising vs 72h ago")):
        cells = []
        for pn, rows in parts:
            s, nf, lag = run(rows, key); res[(key, pn)] = s
            cells.append(fp.fmt_seq(s) + f"; regime flips {nf}; trades within 48h of a flip: {lag[0]} ({lag[1]} won), ${lag[2]:+.0f}")
        L.append(f"| {lab} | " + " | ".join(cells) + " |")
    for lab, side, fn in (("F2 alone (longs)", "LONG", F2), ("F3 alone (shorts)", "SHORT", F3)):
        cells = []
        for pn, rows in parts:
            s = fp.seq([r for r in rows], side, fn); res[(lab, pn)] = s; cells.append(fp.fmt_seq(s))
        L.append(f"| {lab} | " + " | ".join(cells) + " |")
    # gate: beats both standalone (P/L) in >= 2 of 3 periods and worst drawdown not above the worse standalone
    for key in ("ema200_4h_rising24", "ema200_4h_rising72"):
        wins = sum(res[(key, pn)]["pl"] > max(res[("F2 alone (longs)", pn)]["pl"], res[("F3 alone (shorts)", pn)]["pl"]) for pn, _ in parts)
        ddok = all(res[(key, pn)]["dd"] <= max(res[("F2 alone (longs)", pn)]["dd"], res[("F3 alone (shorts)", pn)]["dd"]) for pn, _ in parts)
        L.append(f"\nGate {key}: beats both standalone in {wins} of 3 periods; drawdown never worse than the worse standalone: {ddok} -> {'PASS' if wins >= 2 and ddok else 'FAIL'}")
    open(os.path.join(fp.HERE, "switch.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))

if __name__ == "__main__":
    main()
