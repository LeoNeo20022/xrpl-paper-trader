<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-18T03:06:09+00:00 at $0.9781. 1h trend now: **down**, RSI(14) 55.98 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 18 (6) | **-0.92** | -7.64 (13.5%), low -5.99 | 0 | **-1.83** | -15.27 (13.5%), low -11.98 | 0 | **-9.15** | -76.35 (13.5%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | SHORT | 18 (6) | **-5.03** | -20.13 (31.0%), low -14.07 | 0 | **-10.07** | -40.26 (31.0%), low -28.13 | 0 | **-50.34** | -201.32 (31.0%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -12.22 / -24.44 / -122.19.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$98.17** | -1.83 | **+22.61** | SHORT (0.97771 / 0.99431 / 0.94451 / 1.45927) | 18 (6) | 2 / 17 | $3.28 ($3.29 + $-0.02) | **0** ($0.00) | 13.5% |
| `lev_ta_5x` (5x) | **$89.93** | -10.07 | **+14.37** | SHORT (0.97771 / 0.99431 / 0.94451 / 1.16742) | 18 (6) | 2 / 17 | $7.88 ($7.91 + $-0.03) | **0** ($0.00) | 31.0% |
| Baseline: keep $100 in XRP | $75.56 | -24.44 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
