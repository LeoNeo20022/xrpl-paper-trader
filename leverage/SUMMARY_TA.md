<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-04T04:25:06+00:00 at $1.2628. 1h trend now: **down**, RSI(14) 46.02 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 6 (1) | **-3.12** | -3.99 (8.0%), low -3.74 | 0 | **-6.24** | -7.99 (8.0%), low -7.48 | 0 | **-31.18** | -39.94 (8.0%), low -37.39 | 0 |
| `lev_ta_5x` (5x) | SHORT | 6 (1) | **-7.79** | -9.84 (19.4%), low -9.20 | 0 | **-15.59** | -19.68 (19.4%), low -18.40 | 0 | **-77.93** | -98.39 (19.4%), low -92.02 | 0 |

Keep $50 / $100 / $500 in XRP: -1.22 / -2.44 / -12.22.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$93.76** | -6.24 | **-3.79** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.88175) | 6 (1) | 1 / 6 | $1.20 ($1.21 + $-0.01) | **0** ($0.00) | 8.0% |
| `lev_ta_5x` (5x) | **$84.41** | -15.59 | **-13.14** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.5054) | 6 (1) | 1 / 6 | $2.88 ($2.90 + $-0.02) | **0** ($0.00) | 19.4% |
| Baseline: keep $100 in XRP | $97.56 | -2.44 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
