<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-28T04:36:36+00:00 at $1.3317. 1h trend now: **unclear**, RSI(14) 68.62 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 1 (0) | **-1.27** | -1.53 (3.0%), low -1.27 | 0 | **-2.54** | -3.06 (3.0%), low -2.54 | 0 | **-12.72** | -15.28 (3.0%), low -12.72 | 0 |
| `lev_ta_5x` (5x) | FLAT | 1 (0) | **-3.18** | -3.81 (7.5%), low -3.18 | 0 | **-6.35** | -7.63 (7.5%), low -6.35 | 0 | **-31.76** | -38.14 (7.5%), low -31.76 | 0 |

Keep $50 / $100 / $500 in XRP: +1.44 / +2.88 / +14.39.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$97.46** | -2.54 | **-5.42** | FLAT | 1 (0) | 0 / 1 | $0.20 ($0.20 + $0.00) | **0** ($0.00) | 3.0% |
| `lev_ta_5x` (5x) | **$93.65** | -6.35 | **-9.23** | FLAT | 1 (0) | 0 / 1 | $0.50 ($0.50 + $0.00) | **0** ($0.00) | 7.5% |
| Baseline: keep $100 in XRP | $102.88 | +2.88 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
