"""PAPER backtest: backtest_contracts.py models at $500 and $1,000 budgets (whole contracts, US fee schedules).
Models: Kraken $0.0113/contract/side at up to 5x, and with leverage capped at 3x and 2x (Kraken's PXRPUH margin is unverified);
Coinbase 0.02% + $0.15/contract capped by ~$370 overnight margin per XPP contract (~57% of notional, third-party figure).
Same data/rules/windows as backtest_contracts.py. Usage: python3 backtest_contracts_1k.py -> backtest_contracts_1k_output.txt"""
import os, time
import backtest_contracts as bc
from backtest_committee import load, prep, run_com, hold, iso, CC, VARIANTS, HERE

BUDGETS = (500, 1000)
KR = dict(pct=0.0, per=0.0113)
MODELS = [("Kraken, up to 5x", dict(KR)), ("Kraken, capped 3x", dict(KR, lev_cap=3)), ("Kraken, capped 2x", dict(KR, lev_cap=2)),
          ("Coinbase 0.02%+$0.15, overnight-margin cap", dict(pct=0.02, per=0.15, margin_pct=57.0))]
LINES = [("Committee 5x get-on-base +1.5%", VARIANTS[1], bc.QUICK), ("Committee 2x", VARIANTS[0], None)]

def main():
    L = [f"PAPER backtest, run {iso(time.time())} UTC. " + __doc__.split("Usage:")[0].strip(), ""]
    tot = {}
    for coin, sym in CC["coins"].items():
        rec, fund, old, ofund = load(sym)
        ctx_r, _, _ = prep(rec, fund, sym); ctx_o, _, _ = prep(old, ofund, sym)
        end = rec[-1][0] + 300
        s0 = min(t for t in ctx_o[(True, True)].t5 if ctx_o[(True, True)].ready(t)) // 86400 * 86400 + 86400
        wins = [(f"Last {w} days", [c for c in rec if c[0] >= end - w * 86400], ctx_r, fund) for w in (14, 30, 60)]
        wins.append(("Oct 2024 - Mar 2025", [c for c in old if c[0] >= s0], ctx_o, ofund))
        for label, sub, ctxs, fm in wins:
            days = len(sub) / 288
            L += [f"## {sym} - {label} ({sub[0][1][0]:.4g} -> {sub[-1][1][-1]:.4g}, {days:.0f} days)", "",
                  "| Budget | Line | Model | P/L after fees+funding | Per day | Worst drawdown | Trades | Win rate | Fees | Contracts (eff. lev) | Skipped | Longs: n, win%, P/L | Shorts: n, win%, P/L |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for B in BUDGETS:
                h = (hold(sub) - 100) * B / 100; tot.setdefault((B, sym, "hold"), []).append(h)
                for name, var, ex in LINES:
                    for mn, mv in MODELS:
                        if name == "Committee 2x" and mv.get("lev_cap") in (2, 3): continue   # caps >= 2x do not change the 2x line
                        bc.MODEL["fee"] = mv; bc.MODEL["csize"] = bc.CSIZE[sym]
                        v, st = run_com(sub, ctxs, fm, var, sym, budget=B, extra=ex); bc.MODEL["fee"] = None
                        pl = v - B; n = st["trades"]; cn = st.get("contracts", []); el = st.get("eff_lev", [])
                        tot.setdefault((B, sym, name, mn), []).append(pl)
                        L.append(f"| ${B} | {name} | {mn} | **{pl:+.2f}** | {pl / days:+.2f} | -{st.get('max_dd_usd', 0):.2f} ({st['max_dd_pct']:.0f}%) | {n} | "
                                 f"{(st['wins'] / n * 100 if n else 0):.0f}% | ${st['fees_usd']:.2f} | "
                                 f"{(f'{min(cn)}-{max(cn)} ({min(el):.1f}x-{max(el):.1f}x)') if cn else '—'} | {st.get('skipped', 0)} | {' | '.join(bc.sides(st))} |")
                L.append(f"| ${B} | Just hold {coin.upper()} | — | **{h:+.2f}** | {h / days:+.2f} | | | | | | | | |")
            L.append(""); print("\n".join(L[-20:]), flush=True)
    L += ["## Totals: 4 windows per coin (overlapping) and 8-window total", "", "| Budget | Line | Model | XRP 4-window | BTC 4-window | 8-window |", "|---|---|---|---|---|---|"]
    for k in sorted({k for k in tot if len(k) == 4 and k[1] == "XRPUSDT"}):
        B, _, name, mn = k; x = sum(tot[k]); b = sum(tot[(B, "BTCUSDT", name, mn)])
        L.append(f"| ${B} | {name} | {mn} | {x:+.2f} | {b:+.2f} | {x + b:+.2f} |")
    for B in BUDGETS:
        x = sum(tot[(B, "XRPUSDT", "hold")]); b = sum(tot[(B, "BTCUSDT", "hold")])
        L.append(f"| ${B} | Just hold | — | {x:+.2f} | {b:+.2f} | {x + b:+.2f} |")
    open(os.path.join(HERE, "backtest_contracts_1k_output.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[-20:]))

if __name__ == "__main__":
    main()
