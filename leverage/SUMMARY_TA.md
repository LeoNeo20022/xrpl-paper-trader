<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-28T22:34:12+00:00 at $1.3271. 1h trend now: **up**, RSI(14) 58.64 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 1 (0) | **-1.78** | -2.18 (4.3%), low -1.92 | 0 | **-3.56** | -4.35 (4.3%), low -3.84 | 0 | **-17.81** | -21.75 (4.3%), low -19.20 | 0 |
| `lev_ta_5x` (5x) | LONG | 1 (0) | **-4.40** | -5.37 (10.6%), low -4.73 | 0 | **-8.79** | -10.73 (10.6%), low -9.46 | 0 | **-43.96** | -53.66 (10.6%), low -47.29 | 0 |

Keep $50 / $100 / $500 in XRP: +1.26 / +2.52 / +12.61.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$96.44** | -3.56 | **-6.08** | LONG (1.33207 / 1.31678 / 1.36263 / 0.66938) | 1 (0) | 1 / 1 | $0.30 ($0.30 + $0.00) | **0** ($0.00) | 4.3% |
| `lev_ta_5x` (5x) | **$91.21** | -8.79 | **-11.32** | LONG (1.33207 / 1.31678 / 1.36263 / 1.07101) | 1 (0) | 1 / 1 | $0.74 ($0.74 + $0.00) | **0** ($0.00) | 10.6% |
| Baseline: keep $100 in XRP | $102.52 | +2.52 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
