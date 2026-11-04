<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-04T03:52:58+00:00 at $1.2595. 1h trend now: **down**, RSI(14) 36.05 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 6 (1) | **-2.87** | -3.36 (6.7%), low -3.10 | 0 | **-5.74** | -6.72 (6.7%), low -6.21 | 0 | **-28.71** | -33.58 (6.7%), low -31.03 | 0 |
| `lev_ta_5x` (5x) | SHORT | 6 (1) | **-7.23** | -8.40 (16.6%), low -7.76 | 0 | **-14.47** | -16.79 (16.6%), low -15.52 | 0 | **-72.33** | -83.96 (16.6%), low -77.59 | 0 |

Keep $50 / $100 / $500 in XRP: -1.35 / -2.70 / -13.50.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$94.26** | -5.74 | **-3.04** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.88175) | 6 (1) | 1 / 6 | $1.20 ($1.21 + $-0.01) | **0** ($0.00) | 6.7% |
| `lev_ta_5x` (5x) | **$85.53** | -14.47 | **-11.77** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.5054) | 6 (1) | 1 / 6 | $2.88 ($2.90 + $-0.02) | **0** ($0.00) | 16.6% |
| Baseline: keep $100 in XRP | $97.30 | -2.70 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
