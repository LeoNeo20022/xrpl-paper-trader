<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-29T00:16:35+00:00 at $1.3252. 1h trend now: **up**, RSI(14) 52.27 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 1 (0) | **-1.93** | -2.24 (4.5%), low -1.98 | 0 | **-3.86** | -4.47 (4.5%), low -3.96 | 0 | **-19.29** | -22.36 (4.5%), low -19.81 | 0 |
| `lev_ta_5x` (5x) | LONG | 1 (0) | **-4.75** | -5.51 (10.9%), low -4.88 | 0 | **-9.50** | -11.02 (10.9%), low -9.75 | 0 | **-47.52** | -55.12 (10.9%), low -48.75 | 0 |

Keep $50 / $100 / $500 in XRP: +1.19 / +2.38 / +11.88.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$96.14** | -3.86 | **-6.23** | LONG (1.33207 / 1.31678 / 1.36263 / 0.66951) | 1 (0) | 1 / 1 | $0.32 ($0.30 + $0.02) | **0** ($0.00) | 4.5% |
| `lev_ta_5x` (5x) | **$90.50** | -9.50 | **-11.88** | LONG (1.33207 / 1.31678 / 1.36263 / 1.07114) | 1 (0) | 1 / 1 | $0.78 ($0.74 + $0.05) | **0** ($0.00) | 10.9% |
| Baseline: keep $100 in XRP | $102.38 | +2.38 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
