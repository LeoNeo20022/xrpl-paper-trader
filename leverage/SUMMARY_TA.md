<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-02T02:32:10+00:00 at $1.2565. 1h trend now: **down**, RSI(14) 56.22 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 5 (1) | **-1.88** | -3.03 (6.0%), low -2.78 | 0 | **-3.75** | -6.07 (6.0%), low -5.56 | 0 | **-18.75** | -30.33 (6.0%), low -27.78 | 0 |
| `lev_ta_5x` (5x) | FLAT | 5 (1) | **-4.91** | -7.40 (14.6%), low -6.77 | 0 | **-9.81** | -14.81 (14.6%), low -13.53 | 0 | **-49.07** | -74.03 (14.6%), low -67.66 | 0 |

Keep $50 / $100 / $500 in XRP: -1.47 / -2.93 / -14.66.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$96.25** | -3.75 | **-0.82** | FLAT | 5 (1) | 1 / 4 | $0.94 ($0.92 + $0.02) | **0** ($0.00) | 6.0% |
| `lev_ta_5x` (5x) | **$90.19** | -9.81 | **-6.88** | FLAT | 5 (1) | 1 / 4 | $2.27 ($2.23 + $0.04) | **0** ($0.00) | 14.6% |
| Baseline: keep $100 in XRP | $97.07 | -2.93 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
