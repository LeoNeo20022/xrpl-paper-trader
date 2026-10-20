"""Bull-run + sideways backtest of the scalp ladder on Bitstamp XRP/USD 5-min candles,
Oct 2024 - Mar 2025 (XRP/USD stands in for XRP/RLUSD; RLUSD only launched Dec 2024)."""
import pandas as pd, sys
from scalper import new_state, process, observe, total_xrp, equity

D = pd.read_csv("data/bitstamp_5m_2024-10_2025-03.csv", parse_dates=["t"])
D["u"] = (D.t - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(seconds=1)

def run(df, label, spacing=0.5, levels=10, core=0, mode="off", days=3, rng=12, cool=24, trig=0.05, cost=0.0, save=0.5):
    cfg = dict(budget_usd=100, spacing_pct=spacing, levels=levels, core_pct=core, save_share=save,
               trigger_pct=trig, extra_cost_pct_per_fill=cost, recenter_mode=mode,
               range_days=days, range_pct=rng, recenter_cooldown_h=cool)
    st = new_state(df.o.iloc[0], cfg)
    for u, o, h, l, c in zip(df.u.values, df.o.values, df.h.values, df.l.values, df.c.values):
        process(st, (o, h, l, c) if c < o else (o, l, h, c), cfg)
        observe(st, cfg, u, h, l, c)
    px = df.c.iloc[-1]; hold = 100 / (df.o.iloc[0] * 1.0005)
    x = total_xrp(st)
    return dict(strategy=label, sp=spacing, core=core, mode=mode, days=days if mode == "range" else "", rng=rng if mode == "range" else "",
                round_trips=st["round_trips"], reanchors=st["reanchors"], open=sum(L["state"] == "sell" for L in st["levels"]),
                end_xrp=round(x, 2), hold_xrp=round(hold, 2), xrp_vs_hold=f"{(x/hold-1)*100:+.1f}%",
                kept_xrp=round(st["kept_xrp"], 2), savings=round(st["savings_usd"], 2), rlusd_trading=round(st["trading_usd"], 2),
                value=round(equity(st, px), 2), hold_value=round(hold * px, 2),
                value_vs_hold=f"{(equity(st, px)/(hold*px)-1)*100:+.1f}%")

def suite(df, title, spacings=(0.5,), extra=True):
    print(f"\n=== {title}: {df.t.iloc[0]:%Y-%m-%d} -> {df.t.iloc[-1]:%Y-%m-%d}, open {df.o.iloc[0]}, close {df.c.iloc[-1]}, bars {len(df)}")
    rows = []
    for sp in spacings:
        rows.append(run(df, "b static", sp))
        rows.append(run(df, "c trail", sp, mode="trail"))
        for days in (2, 3, 5):
            for rng in (8, 12, 20):
                rows.append(run(df, "d range", sp, mode="range", days=days, rng=rng))
        rows.append(run(df, "e core50+range3d/12%", sp, core=50, mode="range", days=3, rng=12))
        rows.append(run(df, "e core50+static", sp, core=50))
    out = pd.DataFrame(rows)
    print(out.to_string(index=False))
    return out

if __name__ == "__main__":
    pd.set_option("display.width", 260); pd.set_option("display.max_rows", 500)
    a = suite(D, "FULL Oct-2024..Mar-2025 (rally + sideways)", spacings=(0.5, 1.0, 2.0))
    side = D[D.t >= "2024-12-03"].reset_index(drop=True)
    b = suite(side, "SIDEWAYS phase only (from 2024-12-03, after the jump)", spacings=(0.5, 1.0, 2.0))
    pd.concat([a.assign(period="full"), b.assign(period="sideways")]).to_csv("backtest_bull_results.csv", index=False)
    print("\nStress (0.1% fill margin + 0.05%/fill extra cost), full period:")
    for kw in [dict(), dict(mode="trail"), dict(mode="range", days=3, rng=12), dict(core=50, mode="range", days=3, rng=12)]:
        print(run(D, "stress", 0.5, trig=0.1, cost=0.05, **kw))
