<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-29T01:07:15+00:00 at $1.3182. 1h trend now: **up**, RSI(14) 47.5 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 1 (0) | **-2.44** | -2.72 (5.4%), low -2.46 | 0 | **-4.88** | -5.44 (5.4%), low -4.92 | 0 | **-24.41** | -27.18 (5.4%), low -24.62 | 0 |
| `lev_ta_5x` (5x) | LONG | 1 (0) | **-5.98** | -6.67 (13.2%), low -6.03 | 0 | **-11.96** | -13.34 (13.2%), low -12.06 | 0 | **-59.78** | -66.68 (13.2%), low -60.31 | 0 |

Keep $50 / $100 / $500 in XRP: +0.92 / +1.83 / +9.17.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$95.12** | -4.88 | **-6.72** | LONG (1.33207 / 1.31678 / 1.36263 / 0.66951) | 1 (0) | 1 / 1 | $0.32 ($0.30 + $0.02) | **0** ($0.00) | 5.4% |
| `lev_ta_5x` (5x) | **$88.04** | -11.96 | **-13.79** | LONG (1.33207 / 1.31678 / 1.36263 / 1.07114) | 1 (0) | 1 / 1 | $0.78 ($0.74 + $0.05) | **0** ($0.00) | 13.2% |
| Baseline: keep $100 in XRP | $101.83 | +1.83 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
