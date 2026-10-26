#!/usr/bin/env python3
"""PAPER-ONLY live tracker for leverage_ta (lev_ta_2x, lev_ta_5x): trend-pullback long/short on a simulated Binance
XRPUSDT perp. Runs after lev_runner.py in the paper-trading workflow; failure-isolated. Public keyless data only:
no keys, no logins, no orders, no wallet. Rules: see ta.py. State/logs: leverage/state/lev_ta_*.json, leverage/logs/lev_ta_*."""
import json, os, csv, time
from datetime import datetime, timezone
import ta, levdata

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TC = json.load(open(os.path.join(HERE, "ta_config.json")))
SDIR, LDIR = os.path.join(HERE, "state"), os.path.join(HERE, "logs")
MS = os.path.join(SDIR, "ta_market.json")
EV = ["ts", "event", "price", "qty_xrp", "notional_usd", "margin_usd", "fee_usd", "stop", "target", "liq_price", "why",
      "trade_net_usd", "funding_usd", "rate", "mkt", "margin_lost_usd", "data_source", "label"]
BEGIN, END = "<!-- LEVERAGE-TA-BEGIN -->", "<!-- LEVERAGE-TA-END -->"

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")
def load(p): return json.load(open(p)) if os.path.exists(p) else None
def save(p, o): os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(o, open(p, "w"), indent=1)
def append(p, row, fields):
    os.makedirs(os.path.dirname(p), exist_ok=True); new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def hourly(now):
    """Closed 1h candles (>= 250 for the EMA200): Binance futures -> Binance spot data-api -> OKX perp."""
    for name, url in [("binance_futures_perp", "https://fapi.binance.com/fapi/v1/klines?symbol=XRPUSDT&interval=1h&limit=500"),
                      ("binance_spot_data_api", "https://data-api.binance.vision/api/v3/klines?symbol=XRPUSDT&interval=1h&limit=500")]:
        try:
            rows = json.loads(levdata._get(url))
            return name, [(int(r[0]) // 1000, *map(float, r[1:5])) for r in rows if int(r[0]) // 1000 + 3600 <= now]
        except Exception as e: print(name, "1h unavailable:", str(e)[:100])
    rows = json.loads(levdata._get("https://www.okx.com/api/v5/market/candles?instId=XRP-USDT-SWAP&bar=1H&limit=300"))["data"]
    return "okx_swap", sorted((int(r[0]) // 1000, *map(float, r[1:5])) for r in rows if r[8] == "1")

def main():
    now = time.time(); ts = iso(now); ms = load(MS)
    src5, c5 = levdata.klines_since((ms or {}).get("last_candle_ts", int(now) // 300 * 300 - 3600), now)
    if ms is None:
        t0, p0 = c5[-1][0], c5[-1][1][-1]
        ms = {"started": iso(t0 + 300), "start_price": p0, "last_candle_ts": t0, "last_close": p0,
              "baseline_xrp": TC["common"]["budget_usd"] / (p0 * (1 + TC["baseline_cost_pct"] / 100))}
        for n, v in TC["variants"].items(): save(os.path.join(SDIR, f"{n}.json"), ta.new_state(dict(TC["common"], **v)))
        c5 = []; print("leverage_ta started at", p0, src5)
    src1, bars = hourly(now)
    ind = ta.indicators(bars, TC["common"])
    fund, fsrc = levdata.funding_since(ms["last_candle_ts"] - 28800) if c5 else ({}, "none needed")
    price = c5[-1][1][-1] if c5 else ms["last_close"]
    last = ind[max(ind)] if ind else {}
    rows = []
    for n, v in TC["variants"].items():
        cfg = dict(TC["common"], **v); sp = os.path.join(SDIR, f"{n}.json"); st = load(sp); evs = []
        for t, path in c5:
            if t % 28800 == 0 and t > (st.get("last_funding_ts") or 0):
                e = ta.funding(st, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
                if e: evs.append(dict(e, why="assumed rate" if t not in fund else fsrc))
            evs += ta.step(st, cfg, t, list(path), ind, iso(t))
        for e in evs:
            append(os.path.join(LDIR, f"{n}_events.csv"), dict(e, data_source=src5, label="PAPER-NOT-REAL"), EV)
            print(("*** PAPER LIQUIDATION " if e["event"].startswith("LIQ") else "") + f"[{n}]", e)
        st["last_run"] = ts; save(sp, st)
        val = ta.equity(st, price, cfg); p = st["pos"]
        row = {"ts": ts, "line": n, "leverage": cfg["leverage"], "price": round(price, 5), "prices_5m": src5, "prices_1h": src1, "funding_source": fsrc,
               "trend_1h": last.get("trend"), "rsi_1h": last.get("rsi"), "value_usd": round(val, 4), "vs_start_usd": round(val - cfg["budget_usd"], 4),
               "vs_keep_xrp_usd": round(val - ms["baseline_xrp"] * price, 4), "position": p["side"] if p else "FLAT",
               "entry": round(p["entry"], 5) if p else "", "stop": round(p["stop"], 5) if p else "", "target": round(p["target"], 5) if p else "",
               "liq_price": round(ta.liq_price(p, cfg), 5) if p else "", "trades": st["trades"], "wins": st["wins"], "longs": st["longs"], "shorts": st["shorts"],
               "fees_usd": round(st["fees_usd"], 4), "funding_usd": round(st["funding_usd"], 4), "fees_paid_usd": round(st["fees_usd"] + st["funding_usd"], 4),
               "liquidations": st["liquidations"], "liq_margin_lost_usd": round(st["liq_lost_usd"], 4), "max_drawdown_pct": round(st["max_dd_pct"], 2),
               "keep_xrp_value_usd": round(ms["baseline_xrp"] * price, 4), "new_events": len(evs)}
        append(os.path.join(LDIR, f"{n}_ticks.csv"), row, list(row.keys())); rows.append(row)
    if c5: ms["last_candle_ts"] = c5[-1][0]; ms["last_close"] = price
    ms.update(last_run=ts, last_source_5m=src5, last_source_1h=src1, last_funding_source=fsrc, candles_this_run=len(c5)); save(MS, ms)
    write_md(ms, rows); print(json.dumps(rows, indent=1))

def write_md(ms, rows):
    r0 = rows[0]; hold = ms["baseline_xrp"] * r0["price"]
    L = [BEGIN, "## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)", "",
         f"Started **{ms['started']}** at **${ms['start_price']:.4f}**, $100 paper each, not in the $300 total. Last update {r0['ts']} at ${r0['price']:.4f}. "
         f"1h trend now: **{r0['trend_1h']}**, RSI(14) {r0['rsi_1h']} (prices `{r0['prices_5m']}`, funding `{r0['funding_source']}`).", "",
         "| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        pos = f"{r['position']} ({r['entry']} / {r['stop']} / {r['target']} / {r['liq_price']})" if r["position"] != "FLAT" else "FLAT"
        L.append(f"| `{r['line']}` ({r['leverage']}x) | **${r['value_usd']:.2f}** | {r['vs_start_usd']:+.2f} | **{r['vs_keep_xrp_usd']:+.2f}** | {pos} | {r['trades']} ({r['wins']}) | "
                 f"{r['longs']} / {r['shorts']} | ${r['fees_paid_usd']:.2f} (${r['fees_usd']:.2f} + ${r['funding_usd']:.2f}) | **{r['liquidations']}** (${r['liq_margin_lost_usd']:.2f}) | {r['max_drawdown_pct']:.1f}% |")
    L += [f"| Baseline: keep $100 in XRP | ${hold:.2f} | {hold - 100:+.2f} | — | | | | $0.05 | 0 | |", "",
          "- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down "
          "from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. "
          "Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. "
          "Backtest: `leverage/backtest_ta_output.txt`.", END]
    md = "\n".join(L) + "\n"
    open(os.path.join(HERE, "SUMMARY_TA.md"), "w").write(md)
    p = os.path.join(ROOT, "SUMMARY.md"); s = open(p).read() if os.path.exists(p) else ""
    if BEGIN in s: s = s[:s.index(BEGIN)].rstrip("\n") + "\n" + (s[s.index(END) + len(END):].lstrip("\n") if END in s else "")
    open(p, "w").write(s.rstrip("\n") + "\n\n" + md)

if __name__ == "__main__":
    main()
