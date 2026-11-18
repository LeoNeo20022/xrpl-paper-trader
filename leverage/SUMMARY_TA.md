<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-18T12:41:11+00:00 at $0.9826. 1h trend now: **down**, RSI(14) 57.03 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 19 (6) | **-1.12** | -9.84 (17.4%), low -5.99 | 0 | **-2.25** | -19.67 (17.4%), low -11.98 | 0 | **-11.24** | -98.36 (17.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | SHORT | 19 (6) | **-5.70** | -25.11 (38.6%), low -14.07 | 0 | **-11.41** | -50.22 (38.6%), low -28.13 | 0 | **-57.03** | -251.12 (38.6%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -12.05 / -24.09 / -120.46.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$97.75** | -2.25 | **+21.84** | SHORT (0.9991 / 1.015 / 0.96731 / 1.49119) | 19 (6) | 2 / 18 | $3.47 ($3.49 + $-0.02) | **0** ($0.00) | 17.4% |
| `lev_ta_5x` (5x) | **$88.59** | -11.41 | **+12.69** | SHORT (0.9991 / 1.015 / 0.96731 / 1.19296) | 19 (6) | 2 / 18 | $8.32 ($8.34 + $-0.03) | **0** ($0.00) | 38.6% |
| Baseline: keep $100 in XRP | $75.91 | -24.09 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
