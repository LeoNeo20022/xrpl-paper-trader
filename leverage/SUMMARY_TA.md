<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-04T05:26:16+00:00 at $1.2726. 1h trend now: **unclear**, RSI(14) 53.65 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 6 (1) | **-3.85** | -4.23 (8.4%), low -3.98 | 0 | **-7.70** | -8.47 (8.4%), low -7.96 | 0 | **-38.51** | -42.34 (8.4%), low -39.79 | 0 |
| `lev_ta_5x` (5x) | SHORT | 6 (1) | **-9.46** | -10.38 (20.5%), low -9.75 | 0 | **-18.91** | -20.76 (20.5%), low -19.49 | 0 | **-94.57** | -103.82 (20.5%), low -97.45 | 0 |

Keep $50 / $100 / $500 in XRP: -0.84 / -1.69 / -8.44.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$92.30** | -7.70 | **-6.01** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.88175) | 6 (1) | 1 / 6 | $1.20 ($1.21 + $-0.01) | **0** ($0.00) | 8.4% |
| `lev_ta_5x` (5x) | **$81.09** | -18.91 | **-17.23** | SHORT (1.26077 / 1.27523 / 1.23186 / 1.5054) | 6 (1) | 1 / 6 | $2.88 ($2.90 + $-0.02) | **0** ($0.00) | 20.5% |
| Baseline: keep $100 in XRP | $98.31 | -1.69 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
