<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-14T15:52:38+00:00 at $0.9704. 1h trend now: **down**, RSI(14) 34.61 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 14 (5) | **+1.99** | -6.24 (12.4%), low -5.99 | 0 | **+3.97** | -12.49 (12.4%), low -11.98 | 0 | **+19.85** | -62.44 (12.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | FLAT | 14 (5) | **+2.85** | -14.70 (29.0%), low -14.07 | 0 | **+5.69** | -29.41 (29.0%), low -28.13 | 0 | **+28.46** | -147.03 (29.0%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -12.52 / -25.03 / -125.17.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$103.97** | +3.97 | **+29.00** | FLAT | 14 (5) | 2 / 12 | $2.36 ($2.41 + $-0.05) | **0** ($0.00) | 12.4% |
| `lev_ta_5x` (5x) | **$105.69** | +5.69 | **+30.73** | FLAT | 14 (5) | 2 / 12 | $5.51 ($5.63 + $-0.12) | **0** ($0.00) | 29.0% |
| Baseline: keep $100 in XRP | $74.97 | -25.03 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
