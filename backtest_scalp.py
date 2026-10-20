"""Backtest the scalp ladder on Bitstamp XRP/USD 5-minute candles (data/bitstamp_5m_30d.csv)."""
import pandas as pd, sys
from scalper import new_state, process, total_xrp, equity

df = pd.read_csv("data/bitstamp_5m_30d.csv", parse_dates=["t"])
P0, P1 = df.o.iloc[0], df.c.iloc[-1]

def path(o, h, l, c):  # red bar O-H-L-C, green bar O-L-H-C
    return (o, h, l, c) if c < o else (o, l, h, c)

def run(spacing, levels, budget=100, core=0, save=0.5, trig=0.05, cost=0.0, tp=None, start=0, trail=True):
    cfg = dict(budget_usd=budget, spacing_pct=spacing, levels=levels, core_pct=core, save_share=save,
               trigger_pct=trig, extra_cost_pct_per_fill=cost, trail=trail)
    if tp: cfg["tp_pct"] = tp
    d = df.iloc[start:]
    st = new_state(d.o.iloc[0], cfg)
    for o, h, l, c in zip(d.o.values, d.h.values, d.l.values, d.c.values):
        process(st, path(o, h, l, c), cfg)
    px = d.c.iloc[-1]
    hold_xrp = budget / (d.o.iloc[0] * 1.0005)          # buy-and-hold (same 0.05% entry cost)
    open_pos = sum(1 for L in st["levels"] if L["state"] == "sell")
    return dict(spacing=spacing, levels=levels, core=core, trig=trig, cost=cost, round_trips=st["round_trips"],
                open_pos=open_pos, reanch=st["reanchors"], xrp_kept=round(st["kept_xrp"], 3),
                savings=round(st["savings_usd"], 2), trading_usd=round(st["trading_usd"], 2),
                total_xrp=round(total_xrp(st), 2), hold_xrp=round(hold_xrp, 2),
                value=round(equity(st, px), 2), hold_value=round(hold_xrp * px, 2))

if __name__ == "__main__":
    pd.set_option("display.width", 250)
    print(f"Bitstamp 5m {df.t.iloc[0]} -> {df.t.iloc[-1]}, open {P0}, close {P1}, bars {len(df)}")
    rows = []
    for sp, n in [(0.3, 20), (0.5, 12), (1.0, 6), (0.3, 10), (0.5, 10), (1.0, 10)]:
        for core in (0, 50):
            for trig in (0.0, 0.05, 0.1):
                rows.append(run(sp, n, core=core, trig=trig))
    out = pd.DataFrame(rows); out.to_csv("backtest_scalp_results.csv", index=False)
    print(out.to_string(index=False))
    print("\nStress: +0.05% per fill (DEX vs CEX price gap / adverse fills), trigger 0.05%")
    for sp, n in [(0.3, 20), (0.5, 12), (1.0, 6)]:
        print(run(sp, n, core=50, cost=0.05))
    print("\nNo trailing anchor (fixed ladder under start price), core 50%")
    for sp, n in [(0.3, 20), (0.5, 12), (1.0, 6)]:
        print(run(sp, n, core=50, trail=False))
    print("\nHalves: first 15d (rally+chop) / last 15d (decline), 0.5%x12 core 50")
    h = len(df) // 2
    d0 = df; df = d0.iloc[:h].reset_index(drop=True); print(run(0.5, 12, core=50))
    df = d0.iloc[h:].reset_index(drop=True); print(run(0.5, 12, core=50))
