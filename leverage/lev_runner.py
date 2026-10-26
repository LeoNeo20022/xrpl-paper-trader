#!/usr/bin/env python3
"""PAPER-ONLY live tracker for the leveraged XRP grid (lev_2x, lev_5x). Runs after paper_runner.py in the same
GitHub Actions job. Public keyless data only; no keys, no logins, no orders, no wallet.
Each tick: catch up on closed 5-min candles, apply 8-hourly funding, simulate fills/liquidations, write
leverage/state, leverage/logs, leverage/SUMMARY_LEVERAGE.md and a section appended to the main SUMMARY.md."""
import json, os, csv, time
from datetime import datetime, timezone
import levgrid, levdata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CFG = json.load(open(os.path.join(HERE, "config.json")))
SDIR, LDIR = os.path.join(HERE, "state"), os.path.join(HERE, "logs")
MS_PATH = os.path.join(SDIR, "market.json")
EV_FIELDS = ["ts", "side", "price", "qty_xrp", "notional_usd", "margin_usd", "fee_usd", "realised_pnl_usd", "rate", "funding_usd",
             "assumed_rate", "mkt", "mkt_low", "entry", "margin_lost_usd", "levels_lost", "data_source", "label"]
BEGIN, END = "<!-- LEVERAGE-PAPER-BEGIN -->", "<!-- LEVERAGE-PAPER-END -->"

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")
def load(p): return json.load(open(p)) if os.path.exists(p) else None
def save(p, o): os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(o, open(p, "w"), indent=1)
def append(p, row, fields):
    os.makedirs(os.path.dirname(p), exist_ok=True); new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def main():
    now = time.time(); ts = iso(now)
    ms = load(MS_PATH)
    if ms is None:   # start now from the latest closed candle
        src, cs = levdata.klines_since(int(now) // 300 * 300 - 3600, now)
        t0, p0 = cs[-1][0], cs[-1][1][-1]
        ms = {"started": iso(t0 + 300), "start_price": p0, "start_source": src, "last_candle_ts": t0,
              "baseline_xrp": CFG["common"]["budget_usd"] / (p0 * (1 + CFG["baseline_cost_pct"] / 100)), "last_close": p0}
        for n, v in CFG["variants"].items():
            st = levgrid.new_state(p0, dict(CFG["common"], **v)); st["last_funding_ts"] = t0 // 28800 * 28800
            save(os.path.join(SDIR, f"{n}.json"), st)
        print(f"leverage paper line started at {p0} ({src})")
        candles = []
    else:
        src, candles = levdata.klines_since(ms["last_candle_ts"], now)
    fund, fsrc = levdata.funding_since(ms["last_candle_ts"] - 28800) if candles else ({}, "none needed")
    price = candles[-1][1][-1] if candles else ms["last_close"]
    rows = []
    for n, v in CFG["variants"].items():
        cfg = dict(CFG["common"], **v); sp = os.path.join(SDIR, f"{n}.json"); st = load(sp)
        evs = []
        for t, path in candles:
            if t % 28800 == 0 and t > (st.get("last_funding_ts") or 0):
                e = levgrid.funding(st, cfg, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t), assumed=t not in fund)
                if e: evs.append(e)
            evs += levgrid.process(st, list(path), cfg, ts=iso(t + 300))
        for e in evs:
            append(os.path.join(LDIR, f"{n}_events.csv"), dict(e, data_source=src, label="PAPER-NOT-REAL"), EV_FIELDS)
            if e["side"] == "LIQUIDATION": print(f"*** PAPER LIQUIDATION [{n}] ***", e)
            else: print(f"[{n}]", e)
        st["last_run"] = ts; save(sp, st)
        val = levgrid.equity(st, price, cfg); hold = ms["baseline_xrp"] * price
        row = {"ts": ts, "line": n, "leverage": cfg["leverage"], "price": round(price, 5), "data_source": src, "funding_source": fsrc,
               "value_usd": round(val, 4), "vs_start_usd": round(val - cfg["budget_usd"], 4), "vs_keep_xrp_usd": round(val - hold, 4),
               "cash_usd": round(st["cash"], 4), "margin_usd": round(st["margin"], 4), "position_xrp": round(st["qty"], 4),
               "avg_entry": round(st["entry"], 5), "liq_price": round(levgrid.liq_price(st, cfg), 5),
               "open_levels": sum(L["state"] == "sell" for L in st["levels"]), "round_trips": st["sells"],
               "realised_usd": round(st.get("realised_usd", 0.0), 4), "fees_trading_usd": round(st["fees_trade_usd"], 4),
               "funding_paid_usd": round(st["funding_usd"], 4), "fees_paid_usd": round(st["fees_trade_usd"] + st["funding_usd"], 4),
               "liquidations": st["liquidations"], "liq_margin_lost_usd": round(st["liq_lost_usd"], 4), "max_drawdown_pct": round(st["max_dd_pct"], 2),
               "keep_xrp_value_usd": round(hold, 4), "new_events": len(evs)}
        append(os.path.join(LDIR, f"{n}_ticks.csv"), row, list(row.keys())); rows.append(row)
    if candles: ms["last_candle_ts"] = candles[-1][0]; ms["last_close"] = price
    ms.update(last_run=ts, last_source=src, last_funding_source=fsrc, candles_this_run=len(candles))
    save(MS_PATH, ms)
    write_md(ms, rows)
    print(json.dumps(rows, indent=1))

def write_md(ms, rows):
    hold = ms["baseline_xrp"] * rows[0]["price"]
    L = [BEGIN, "## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)", "",
         f"Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **{ms['started']}** at **${ms['start_price']:.4f}**, $100 paper each, "
         f"not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update {rows[0]['ts']} at ${rows[0]['price']:.4f} "
         f"(prices: `{ms['last_source']}`, funding: `{ms['last_funding_source']}`).", "",
         "| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        L.append(f"| `{r['line']}` ({r['leverage']}x) | **${r['value_usd']:.2f}** | {r['vs_start_usd']:+.2f} | **{r['vs_keep_xrp_usd']:+.2f}** | "
                 f"{r['position_xrp']:.2f} ({r['avg_entry'] or '—'}) | {r['liq_price'] or '—'} | {r['open_levels']}/10 | {r['round_trips']} | "
                 f"${r['fees_paid_usd']:.2f} (${r['fees_trading_usd']:.2f} + ${r['funding_paid_usd']:.2f}) | **{r['liquidations']}** (${r['liq_margin_lost_usd']:.2f}) | {r['max_drawdown_pct']:.1f}% |")
    L += [f"| Baseline: keep $100 in XRP | ${hold:.2f} | {hold - 100:+.2f} | — | {ms['baseline_xrp']:.2f} | — | | | $0.05 | 0 | |", "",
          "- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. "
          "Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). "
          "Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.",
          "- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.", END]
    md = "\n".join(L) + "\n"
    open(os.path.join(HERE, "SUMMARY_LEVERAGE.md"), "w").write(md)
    p = os.path.join(ROOT, "SUMMARY.md")
    s = open(p).read() if os.path.exists(p) else ""
    if BEGIN in s: s = s[:s.index(BEGIN)].rstrip("\n") + "\n" + (s[s.index(END) + len(END):].lstrip("\n") if END in s else "")
    open(p, "w").write(s.rstrip("\n") + "\n\n" + md)

if __name__ == "__main__":
    main()
