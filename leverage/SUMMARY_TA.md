<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-06T21:29:24+00:00 at $1.1796. 1h trend now: **down**, RSI(14) 27.61 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 8 (1) | **-5.28** | -5.53 (11.0%), low -5.28 | 0 | **-10.55** | -11.06 (11.0%), low -10.55 | 0 | **-52.75** | -55.31 (11.0%), low -52.75 | 0 |
| `lev_ta_5x` (5x) | FLAT | 8 (1) | **-12.58** | -13.21 (26.1%), low -12.58 | 0 | **-25.15** | -26.43 (26.1%), low -25.15 | 0 | **-125.76** | -132.13 (26.1%), low -125.76 | 0 |

Keep $50 / $100 / $500 in XRP: -4.44 / -8.87 / -44.36.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$89.45** | -10.55 | **-1.68** | FLAT | 8 (1) | 2 / 6 | $1.48 ($1.49 + $-0.01) | **0** ($0.00) | 11.0% |
| `lev_ta_5x` (5x) | **$74.85** | -25.15 | **-16.28** | FLAT | 8 (1) | 2 / 6 | $3.49 ($3.51 + $-0.02) | **0** ($0.00) | 26.1% |
| Baseline: keep $100 in XRP | $91.13 | -8.87 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
