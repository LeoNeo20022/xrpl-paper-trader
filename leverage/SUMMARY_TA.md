<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-29T15:39:45+00:00 at $1.3095. 1h trend now: **down**, RSI(14) 48.66 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 2 (0) | **-2.54** | -2.80 (5.6%), low -2.54 | 0 | **-5.09** | -5.60 (5.6%), low -5.09 | 0 | **-25.44** | -27.99 (5.6%), low -25.44 | 0 |
| `lev_ta_5x` (5x) | FLAT | 2 (0) | **-6.23** | -6.86 (13.6%), low -6.23 | 0 | **-12.45** | -13.73 (13.6%), low -12.45 | 0 | **-62.27** | -68.64 (13.6%), low -62.27 | 0 |

Keep $50 / $100 / $500 in XRP: +0.58 / +1.16 / +5.81.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$94.91** | -5.09 | **-6.25** | FLAT | 2 (0) | 1 / 1 | $0.41 ($0.39 + $0.02) | **0** ($0.00) | 5.6% |
| `lev_ta_5x` (5x) | **$87.55** | -12.45 | **-13.62** | FLAT | 2 (0) | 1 / 1 | $1.01 ($0.97 + $0.05) | **0** ($0.00) | 13.6% |
| Baseline: keep $100 in XRP | $101.16 | +1.16 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
