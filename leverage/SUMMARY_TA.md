<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-27T10:22:27+00:00 at $1.2911. 1h trend now: **down**, RSI(14) 49.36 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 0 (0) | **+0.25** | -0.27 (0.5%), low -0.27 | 0 | **+0.50** | -0.54 (0.5%), low -0.54 | 0 | **+2.48** | -2.69 (0.5%), low -2.69 | 0 |
| `lev_ta_5x` (5x) | SHORT | 0 (0) | **+0.62** | -0.67 (1.3%), low -0.67 | 0 | **+1.24** | -1.34 (1.3%), low -1.34 | 0 | **+6.18** | -6.72 (1.3%), low -6.72 | 0 |

Keep $50 / $100 / $500 in XRP: -0.13 / -0.26 / -1.29.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$100.50** | +0.50 | **+0.75** | SHORT (1.29625 / 1.3108 / 1.26715 / 1.9347) | 0 (0) | 0 / 1 | $0.10 ($0.10 + $0.00) | **0** ($0.00) | 0.5% |
| `lev_ta_5x` (5x) | **$101.24** | +1.24 | **+1.49** | SHORT (1.29625 / 1.3108 / 1.26715 / 1.54776) | 0 (0) | 0 / 1 | $0.25 ($0.25 + $0.00) | **0** ($0.00) | 1.3% |
| Baseline: keep $100 in XRP | $99.74 | -0.26 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
