<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-29T00:52:16+00:00 at $1.3228. 1h trend now: **up**, RSI(14) 52.27 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 1 (0) | **-2.10** | -2.42 (4.8%), low -2.16 | 0 | **-4.21** | -4.84 (4.8%), low -4.33 | 0 | **-21.05** | -24.18 (4.8%), low -21.63 | 0 |
| `lev_ta_5x` (5x) | LONG | 1 (0) | **-5.17** | -5.95 (11.8%), low -5.31 | 0 | **-10.35** | -11.90 (11.8%), low -10.63 | 0 | **-51.73** | -59.50 (11.8%), low -53.13 | 0 |

Keep $50 / $100 / $500 in XRP: +1.10 / +2.19 / +10.95.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$95.79** | -4.21 | **-6.40** | LONG (1.33207 / 1.31678 / 1.36263 / 0.66951) | 1 (0) | 1 / 1 | $0.32 ($0.30 + $0.02) | **0** ($0.00) | 4.8% |
| `lev_ta_5x` (5x) | **$89.65** | -10.35 | **-12.54** | LONG (1.33207 / 1.31678 / 1.36263 / 1.07114) | 1 (0) | 1 / 1 | $0.78 ($0.74 + $0.05) | **0** ($0.00) | 11.8% |
| Baseline: keep $100 in XRP | $102.19 | +2.19 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
