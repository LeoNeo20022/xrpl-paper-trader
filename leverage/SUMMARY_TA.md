<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-28T23:06:12+00:00 at $1.3258. 1h trend now: **up**, RSI(14) 53.72 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 1 (0) | **-1.88** | -2.22 (4.4%), low -1.96 | 0 | **-3.75** | -4.44 (4.4%), low -3.93 | 0 | **-18.76** | -22.19 (4.4%), low -19.64 | 0 |
| `lev_ta_5x` (5x) | LONG | 1 (0) | **-4.62** | -5.47 (10.8%), low -4.83 | 0 | **-9.25** | -10.94 (10.8%), low -9.67 | 0 | **-46.24** | -54.71 (10.8%), low -48.34 | 0 |

Keep $50 / $100 / $500 in XRP: +1.21 / +2.42 / +12.11.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$96.25** | -3.75 | **-6.17** | LONG (1.33207 / 1.31678 / 1.36263 / 0.66938) | 1 (0) | 1 / 1 | $0.30 ($0.30 + $0.00) | **0** ($0.00) | 4.4% |
| `lev_ta_5x` (5x) | **$90.75** | -9.25 | **-11.67** | LONG (1.33207 / 1.31678 / 1.36263 / 1.07101) | 1 (0) | 1 / 1 | $0.74 ($0.74 + $0.00) | **0** ($0.00) | 10.8% |
| Baseline: keep $100 in XRP | $102.42 | +2.42 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
