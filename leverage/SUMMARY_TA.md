<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-08T21:46:24+00:00 at $1.1443. 1h trend now: **down**, RSI(14) 38.65 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 8 (1) | **-4.59** | -6.24 (12.4%), low -5.99 | 0 | **-9.19** | -12.49 (12.4%), low -11.98 | 0 | **-45.94** | -62.44 (12.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | SHORT | 8 (1) | **-11.15** | -14.70 (29.0%), low -14.07 | 0 | **-22.31** | -29.41 (29.0%), low -28.13 | 0 | **-111.54** | -147.03 (29.0%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -5.80 / -11.60 / -58.00.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$90.81** | -9.19 | **+2.41** | SHORT (1.15482 / 1.16512 / 1.13422 / 1.72362) | 8 (1) | 2 / 7 | $1.57 ($1.58 + $-0.01) | **0** ($0.00) | 12.4% |
| `lev_ta_5x` (5x) | **$77.69** | -22.31 | **-10.71** | SHORT (1.15482 / 1.16512 / 1.13422 / 1.37889) | 8 (1) | 2 / 7 | $3.68 ($3.70 + $-0.02) | **0** ($0.00) | 29.0% |
| Baseline: keep $100 in XRP | $88.40 | -11.60 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
