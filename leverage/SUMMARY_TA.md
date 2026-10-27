<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-27T12:19:19+00:00 at $1.3030. 1h trend now: **down**, RSI(14) 54.16 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 0 (0) | **-0.67** | -1.36 (2.7%), low -1.10 | 0 | **-1.34** | -2.72 (2.7%), low -2.21 | 0 | **-6.70** | -13.58 (2.7%), low -11.02 | 0 |
| `lev_ta_5x` (5x) | SHORT | 0 (0) | **-1.67** | -3.39 (6.7%), low -2.75 | 0 | **-3.35** | -6.78 (6.7%), low -5.50 | 0 | **-16.74** | -33.89 (6.7%), low -27.52 | 0 |

Keep $50 / $100 / $500 in XRP: +0.33 / +0.66 / +3.30.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$98.66** | -1.34 | **-2.00** | SHORT (1.29625 / 1.3108 / 1.26715 / 1.9347) | 0 (0) | 0 / 1 | $0.10 ($0.10 + $0.00) | **0** ($0.00) | 2.7% |
| `lev_ta_5x` (5x) | **$96.65** | -3.35 | **-4.01** | SHORT (1.29625 / 1.3108 / 1.26715 / 1.54776) | 0 (0) | 0 / 1 | $0.25 ($0.25 + $0.00) | **0** ($0.00) | 6.7% |
| Baseline: keep $100 in XRP | $100.66 | +0.66 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
