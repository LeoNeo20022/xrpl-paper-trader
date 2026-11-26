<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-26T03:14:13+00:00 at $0.9552. 1h trend now: **unclear**, RSI(14) 68.94 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 27 (10) | **+2.52** | -9.84 (17.4%), low -5.99 | 0 | **+5.05** | -19.67 (17.4%), low -11.98 | 0 | **+25.24** | -98.36 (17.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | FLAT | 27 (10) | **+0.57** | -25.11 (38.6%), low -14.07 | 0 | **+1.14** | -50.22 (38.6%), low -28.13 | 0 | **+5.71** | -251.12 (38.6%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -13.10 / -26.21 / -131.04.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$105.05** | +5.05 | **+31.26** | FLAT | 27 (10) | 2 / 25 | $4.80 ($4.85 + $-0.05) | **0** ($0.00) | 17.4% |
| `lev_ta_5x` (5x) | **$101.14** | +1.14 | **+27.35** | FLAT | 27 (10) | 2 / 25 | $11.74 ($11.86 + $-0.12) | **0** ($0.00) | 38.6% |
| Baseline: keep $100 in XRP | $73.79 | -26.21 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
