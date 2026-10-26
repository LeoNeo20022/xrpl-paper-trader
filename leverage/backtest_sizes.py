"""PAPER backtest: every leverage_ta and committee line at $50, $100 and $500 starting budgets, side by side, plus the
'get on base' quick-take-profit variants (5x, and as an option on mix's 5x trades): take profit at +1% or +1.5% underlying
move (+5% / +7.5% on margin at 5x), stop = the tighter of 1% underlying or 1.5x ATR, isolated margin.
Same data, rules, costs and windows as backtest_committee.py (imported from it). Profit = after trading fees, slippage and
funding; open positions valued as if closed at the end. Worst drawdown = biggest peak-to-trough drop in dollars (and %).
Low = lowest account value seen vs the start (max loss). No extra slippage for size: at 5x, $500 controls $2,500 of
XRPUSDT/BTCUSDT perps, far inside Binance's top-of-book, so the 0.05% slippage already charged covers it.
Usage: python3 backtest_sizes.py [XRPUSDT|BTCUSDT]  -> backtest_sizes_<sym>.txt; no argument = merge into backtest_sizes_output.txt."""
import os, sys
ARG = sys.argv[1] if len(sys.argv) > 1 else None
sys.argv = sys.argv[:1]
from backtest_committee import *   # noqa: F401,F403 (data loaders, run_com, run_ta, VARIANTS, CC)

SIZES = (50, 100, 500)
Q = lambda tp, minlev=0: {"quick_tp_pct": tp, "quick_stop_pct": 1.0, "quick_tp_min_lev": minlev}
LINES = [("Committee+Theo 2x", "c", VARIANTS[0], None), ("Committee+Theo 5x (regular)", "c", VARIANTS[1], None),
         ("Committee+Theo 5x get-on-base TP +1%", "c", VARIANTS[1], Q(1.0)), ("Committee+Theo 5x get-on-base TP +1.5%", "c", VARIANTS[1], Q(1.5)),
         ("Committee+Theo mix (regular)", "c", VARIANTS[2], None), ("Committee+Theo mix, quick TP +1% on its 5x trades", "c", VARIANTS[2], Q(1.0, 5)),
         ("Committee+Theo mix, quick TP +1.5% on its 5x trades", "c", VARIANTS[2], Q(1.5, 5)),
         ("Proxy team 2x", "c", VARIANTS[5], None), ("Proxy team 5x (regular)", "c", VARIANTS[6], None),
         ("Proxy team 5x get-on-base TP +1%", "c", VARIANTS[6], Q(1.0)), ("Proxy team 5x get-on-base TP +1.5%", "c", VARIANTS[6], Q(1.5)),
         ("Proxy team mix", "c", VARIANTS[7], None),
         ("leverage_ta 2x", "t", 2, None), ("leverage_ta 5x (regular)", "t", 5, None),
         ("leverage_ta 5x get-on-base TP +1%", "t", 5, Q(1.0)), ("leverage_ta 5x get-on-base TP +1.5%", "t", 5, Q(1.5))]

def stats(st, b):
    n = st["trades"]; w = st["wins"]; aw = st.get("win_usd", 0) / w if w else 0; al = st.get("loss_usd", 0) / (n - w) if n - w else 0
    return n, (f"{w / n * 100:.0f}%" if n else "—"), f"{aw / b * 100:+.1f}% / {al / b * 100:+.1f}%" if n else "—"

def cell(v, st, b):
    return f"**{v - b:+.2f}** | -{st.get('max_dd_usd', 0):.2f} ({st['max_dd_pct']:.0f}%), low {min(0, st.get('min_equity', b) - b):+.2f} | {st['liquidations']}"

def run(sym):
    coin = [c for c, s in CC["coins"].items() if s == sym][0]
    rec, fund, old, ofund = load(sym)
    ctx_r, ind_r, _ = prep(rec, fund, sym); ctx_o, ind_o, _ = prep(old, ofund, sym)
    end = rec[-1][0] + 300
    s0 = min(t for t in ctx_o[(True, True)].t5 if ctx_o[(True, True)].ready(t)) // 86400 * 86400 + 86400
    wins = [(f"Last {w} days", [c for c in rec if c[0] >= end - w * 86400], ctx_r, ind_r, fund) for w in (14, 30, 60)]
    wins.append(("Stress Oct 2024 - Mar 2025", [c for c in old if c[0] >= s0], ctx_o, ind_o, ofund))
    L = []
    for label, sub, ctxs, ind, fm in wins:
        h = hold(sub)
        L += [f"## {sym} — {label} ({sub[0][1][0]:.4g} -> {sub[-1][1][-1]:.4g})", "",
              "| Line | Trades | Win rate | Avg win / avg loss (% of account) | " + " | ".join(f"**${b}: profit** | ${b}: worst drawdown, low | ${b}: liq." for b in SIZES) + " |",
              "|---|---|---|---|" + "---|---|---|" * len(SIZES)]
        for name, kind, x, ex in LINES:
            r = {b: (run_com(sub, ctxs, fm, x, sym, budget=b, extra=ex) if kind == "c" else run_ta(sub, ind, fm, x, sym, budget=b, extra=ex)) for b in SIZES}
            n, wr_, awl = stats(r[100][1], 100)
            L.append(f"| {name} | {n} | {wr_} | {awl} | " + " | ".join(cell(*r[b], b) for b in SIZES) + " |")
        L.append(f"| Just hold {coin.upper()} | — | — | — | " + " | ".join(f"**{(h - 100) * b / 100:+.2f}** | | 0" for b in SIZES) + " |")
        L.append(""); print("\n".join(L[-20:]), flush=True)
    open(os.path.join(HERE, f"backtest_sizes_{sym}.txt"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    if ARG: run(ARG)
    else:
        head = __doc__.split("Usage:")[0].strip()
        parts = [open(os.path.join(HERE, f"backtest_sizes_{s}.txt")).read() for s in CC["coins"].values()]
        open(os.path.join(HERE, "backtest_sizes_output.txt"), "w").write(f"PAPER backtest, run {iso(time.time())} UTC.\n{head}\n\n" + "\n".join(parts))
