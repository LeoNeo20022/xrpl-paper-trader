"""Backtest grid configs on Kraken XRP/USD hourly candles (data/kraken_1h_30d.csv)."""
import pandas as pd, copy, itertools, sys
from grid import make_levels, init_state, step, equity

df = pd.read_csv("data/kraken_1h_30d.csv", parse_dates=["t"])
p0, p1 = df.o.iloc[0], df.c.iloc[-1]

def path(r):  # intrabar path guess: red candle O-H-L-C, green candle O-L-H-C
    return [r.o, r.h, r.l, r.c] if r.c < r.o else [r.o, r.l, r.h, r.c]

def run(lo, hi, sp, budget, trigger=0.1, fee=0.0, start=0):
    d = df.iloc[start:]
    st = init_state(make_levels(lo, hi, sp), d.o.iloc[0], budget)
    for r in d.itertuples():
        step(st, path(r), fee_pct=fee, trigger_pct=trigger, ts=str(r.t))
    e = equity(st, d.c.iloc[-1])
    hold = budget / d.o.iloc[0] * d.c.iloc[-1]
    half = budget / 2 + budget / 2 / d.o.iloc[0] * d.c.iloc[-1]
    return dict(lo=lo, hi=hi, sp=sp, levels=len(st["slots"]) + 1, budget=budget, fills=st["fills"],
                round_trips=st["round_trips"], grid_profit=round(st["realized_usd"], 2),
                entry_cost=round(st["entry_cost_usd"], 3), fees=round(st["fees_usd"], 4),
                final=round(e, 2), pnl=round(e - budget, 2), hold_xrp=round(hold - budget, 2),
                hold_5050=round(half - budget, 2), end_usd=round(st["usd"], 2), end_xrp=round(st["xrp"], 2))

if __name__ == "__main__":
    print("period", df.t.iloc[0], "->", df.t.iloc[-1], "open", p0, "close", p1)
    rows = []
    for budget in (100, 500):
        for lo, hi in [(1.10, 1.50), (1.20, 1.70), (1.25, 1.70)]:
            for sp in (1.0, 1.5, 2.0, 3.0):
                rows.append(run(lo, hi, sp, budget))
    out = pd.DataFrame(rows); pd.set_option("display.width", 250)
    print(out.to_string(index=False)); out.to_csv("backtest_results.csv", index=False)
    print("\nStress: same grid, stricter fills (0.3% trade-through) and 0.05%/fill extra cost")
    for b in (100, 500):
        print(run(1.20, 1.70, 1.5, b, trigger=0.3, fee=0.05))
    print("\nSecond half only (falling market, start ~Oct 5)")
    for b in (100, 500):
        print(run(1.20, 1.70, 1.5, b, start=360))
