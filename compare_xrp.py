"""Which scheme ends with the MOST XRP? Paper backtest on Bitstamp XRP/USD 5-min candles
(XRP/USD stands in for XRP/RLUSD). Scoreboard = XRP count; leftover RLUSD is also shown converted
to XRP at the last price ("XRP-equiv"). All assumptions are labeled in ASSUMPTIONS below."""
import pandas as pd, math, json
from scalper import new_state, process, total_xrp, topup

ASSUMPTIONS = dict(
    taker_cost_pct=0.05,     # market buy/sell: ~half spread + small slippage on XRP/RLUSD (spread seen 0.015-0.1%)
    maker_trigger_pct=0.05,  # limit orders fill only if price trades 0.05% through them
    lp_fee_apr_measured_recent=None,   # filled from data/amm_rlusd_yield.json (real, on-ledger)
    lp_fee_apr_assumed_2024=(3.0, 6.0, 10.0),  # ASSUMED low/central/high APR for 2024-25 (pool did not exist then)
)
AMM = json.load(open("data/amm_rlusd_yield.json"))
ASSUMPTIONS["lp_fee_apr_measured_recent"] = AMM["30d_ago"]["fee_apr_pct"]
TK = ASSUMPTIONS["taker_cost_pct"] / 100

def load(path, start=None, end=None):
    d = pd.read_csv(path, parse_dates=["t"])
    if start: d = d[d.t >= start]
    if end: d = d[d.t < end]
    return d.reset_index(drop=True)

def topup_times(d, monthly):
    if not monthly: return []
    t0, t1 = d.t.iloc[0], d.t.iloc[-1]
    out, k = [], 1
    while t0 + pd.Timedelta(days=30 * k) < t1:
        out.append(t0 + pd.Timedelta(days=30 * k)); k += 1
    return out

def idx_at(d, ts):
    return int(d.t.searchsorted(ts))

def lump(d, budget, tops):
    xrp = budget / (d.o.iloc[0] * (1 + TK)); trades = 1
    for ts in tops:
        xrp += tops[ts] / (d.o.iloc[idx_at(d, ts)] * (1 + TK)); trades += 1
    return dict(xrp=xrp, rlusd=0.0, trades=trades, xrp_sells=0)

def dca(d, budget, tops, every_days):
    t0, t1 = d.t.iloc[0], d.t.iloc[-1]
    n = max(1, math.ceil((t1 - t0) / pd.Timedelta(days=every_days)))
    sched = [t0 + pd.Timedelta(days=every_days * i) for i in range(n)]
    xrp, trades = 0.0, 0
    for ts in sched:
        xrp += budget / n / (d.o.iloc[idx_at(d, ts)] * (1 + TK)); trades += 1
    for ts, amt in tops.items():   # each top-up is DCA'd over the following 30 days
        k = max(1, round(30 / every_days))
        for i in range(k):
            j = idx_at(d, ts + pd.Timedelta(days=every_days * i))
            if j >= len(d): j = len(d) - 1
            xrp += amt / k / (d.o.iloc[j] * (1 + TK)); trades += 1
    return dict(xrp=xrp, rlusd=0.0, trades=trades, xrp_sells=0)

def dip_ladder(d, budget, tops, steps=(2, 4, 6, 8, 10), refresh_days=7):
    """Buy-only limit ladder at -2/-4/...% below the price at each weekly refresh; never sells."""
    trig = ASSUMPTIONS["maker_trigger_pct"] / 100
    cash, xrp, trades = budget, 0.0, 0
    tops_i = {idx_at(d, ts): amt for ts, amt in tops.items()}
    next_ref = d.t.iloc[0]; orders = []
    for i, (t, o, h, l, c) in enumerate(zip(d.t, d.o, d.h, d.l, d.c)):
        if i in tops_i: cash += tops_i[i]
        if t >= next_ref:
            free = cash + sum(q for _, q in orders)   # cancel + re-place with all cash
            orders = [(o * (1 - s / 100), free / len(steps)) for s in steps] if free > 0.01 else []
            cash = 0.0; next_ref = t + pd.Timedelta(days=refresh_days)
        keep = []
        for px, usd in orders:
            if l <= px * (1 - trig):
                xrp += usd / px; trades += 1
            else: keep.append((px, usd))
        orders = keep
    left = cash + sum(q for _, q in orders)
    return dict(xrp=xrp, rlusd=left, trades=trades, xrp_sells=0)

def scalp(d, budget, tops, spacing, levels=10):
    cfg = dict(budget_usd=budget, spacing_pct=spacing, levels=levels, save_share=0.0, core_pct=0,
               trigger_pct=ASSUMPTIONS["maker_trigger_pct"], recenter_mode="off", entry_cost_pct=ASSUMPTIONS["taker_cost_pct"])
    st = new_state(d.o.iloc[0], cfg)
    tops_i = {idx_at(d, ts): amt for ts, amt in tops.items()}
    for i, (o, h, l, c) in enumerate(zip(d.o.values, d.h.values, d.l.values, d.c.values)):
        if i in tops_i: topup(st, tops_i[i])
        process(st, (o, h, l, c) if c < o else (o, l, h, c), cfg)
    return dict(xrp=total_xrp(st), rlusd=st["trading_usd"] + st["savings_usd"], trades=1 + st["buys"] + st["sells"],
                xrp_sells=st["sells"], round_trips=st["round_trips"])

def lp(d, budget, tops, apr):
    """50/50 deposit into a constant-product XRP/RLUSD pool tracking the external price.
    Value of each deposit scales with sqrt(p_end/p_in) (this includes impermanent loss),
    plus fee income at `apr` (simple, pro-rata for time in pool). Withdraw at end."""
    pe = d.c.iloc[-1]; te = d.t.iloc[-1]
    deps = [(d.t.iloc[0], d.o.iloc[0], budget)] + [(ts, d.o.iloc[idx_at(d, ts)], a) for ts, a in tops.items()]
    val = fees = il_val = 0.0
    for ts, p, amt in deps:
        amt_in = amt * (1 - TK / 2)               # buy half as XRP at taker cost
        yrs = (te - ts) / pd.Timedelta(days=365)
        v = amt_in * math.sqrt(pe / p)
        hold5050 = amt_in / 2 + amt_in / 2 / p * pe
        il_val += v - hold5050
        f = v * apr / 100 * yrs; fees += f; val += v + f
    xrp_in_pool = val / 2 / pe
    return dict(xrp=xrp_in_pool, rlusd=val / 2, trades=len(deps) * 2 + 1, xrp_sells=0, il_usd=il_val, fees_usd=fees)

def hybrid(d, budget, tops):
    a = dca(d, budget / 2, {k: v / 2 for k, v in tops.items()}, 7)
    b = scalp(d, budget / 2, {k: v / 2 for k, v in tops.items()}, 2.0)
    return dict(xrp=a["xrp"] + b["xrp"], rlusd=b["rlusd"], trades=a["trades"] + b["trades"], xrp_sells=b["xrp_sells"])

def table(d, name, budget=100, monthly=0, lp_aprs=None):
    tt = topup_times(d, monthly); tops = {ts: monthly for ts in tt}
    pe = d.c.iloc[-1]; invested = budget + monthly * len(tt)
    rows = {"1 Lump sum at start": lump(d, budget, tops),
            "2a DCA weekly": dca(d, budget, tops, 7),
            "2b DCA daily": dca(d, budget, tops, 1),
            "3 Dip-buy ladder (-2..-10%, weekly refresh)": dip_ladder(d, budget, tops),
            "4a Scalp 0.5% static, 100% reinvest": scalp(d, budget, tops, 0.5),
            "4b Scalp 2% static, 100% reinvest": scalp(d, budget, tops, 2.0),
            "6 Hybrid 50% weekly DCA + 50% scalp 2%": hybrid(d, budget, tops)}
    for lab, apr in lp_aprs:
        rows[f"5 AMM LP ({lab}, {apr:.1f}% APR)"] = lp(d, budget, tops, apr)
    out = []
    for k, r in rows.items():
        eq = r["xrp"] + r["rlusd"] / (pe * (1 + TK))
        out.append(dict(scheme=k, xrp_held=round(r["xrp"], 2), rlusd_left=round(r["rlusd"], 2), xrp_equiv=round(eq, 2),
                        value_usd=round(r["xrp"] * pe + r["rlusd"], 2), trades=r["trades"], xrp_sells=r["xrp_sells"],
                        il_usd=round(r.get("il_usd", 0), 2) if "il_usd" in r else "", lp_fees_usd=round(r.get("fees_usd", 0), 2) if "fees_usd" in r else ""))
    o = pd.DataFrame(out).sort_values("xrp_equiv", ascending=False)
    lump_eq = o.loc[o.scheme.str.startswith("1 "), "xrp_equiv"].iloc[0]
    o["vs_lump"] = ((o.xrp_equiv / lump_eq - 1) * 100).round(1).astype(str) + "%"
    print(f"\n=== {name} | {d.t.iloc[0]:%Y-%m-%d} ${d.o.iloc[0]:.4f} -> {d.t.iloc[-1]:%Y-%m-%d} ${pe:.4f} | invested ${invested:.0f}"
          f"{' (incl. $%d x %d top-ups)' % (monthly, len(tt)) if tt else ''}")
    print(o.to_string(index=False))
    o.insert(0, "period", name); o.insert(1, "topups", monthly)
    return o

if __name__ == "__main__":
    pd.set_option("display.width", 250); pd.set_option("display.max_colwidth", 48)
    print("ASSUMPTIONS:", json.dumps(ASSUMPTIONS))
    rec = load("data/bitstamp_5m_30d.csv")
    full = load("data/bitstamp_5m_2024-10_2025-03.csv")
    rally = load("data/bitstamp_5m_2024-10_2025-03.csv", end="2024-12-03")
    side = load("data/bitstamp_5m_2024-10_2025-03.csv", start="2024-12-03")
    m = ASSUMPTIONS["lp_fee_apr_measured_recent"]; lo, mid, hi = ASSUMPTIONS["lp_fee_apr_assumed_2024"]
    res = [table(rec, "RECENT Sep-Oct 2026 (falling)", lp_aprs=[("0% fees = IL only", 0), ("MEASURED", m)])]
    for d, nm in [(full, "FULL Oct24-Mar25 (rally+sideways)"), (rally, "RALLY Oct1-Dec3 2024"), (side, "SIDEWAYS Dec3 2024-Mar 2025")]:
        for mo in (0, 25):
            res.append(table(d, nm, monthly=mo, lp_aprs=[("IL only", 0), ("ASSUMED low", lo), ("ASSUMED mid", mid), ("ASSUMED high", hi)]))
    pd.concat(res).to_csv("compare_xrp_results.csv", index=False)
