<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-05T12:20:00+00:00 at $1.3141. 1h trend now: **up**, RSI(14) 62.22 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 7 (1) | **-4.94** | -5.30 (10.6%), low -5.05 | 0 | **-9.89** | -10.61 (10.6%), low -10.10 | 0 | **-49.44** | -53.03 (10.6%), low -50.48 | 0 |
| `lev_ta_5x` (5x) | LONG | 7 (1) | **-11.86** | -12.72 (25.1%), low -12.08 | 0 | **-23.71** | -25.44 (25.1%), low -24.16 | 0 | **-118.55** | -127.19 (25.1%), low -120.81 | 0 |

Keep $50 / $100 / $500 in XRP: +0.76 / +1.52 / +7.59.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$90.11** | -9.89 | **-11.41** | LONG (1.32506 / 1.30932 / 1.35655 / 0.66586) | 7 (1) | 2 / 6 | $1.39 ($1.40 + $-0.01) | **0** ($0.00) | 10.6% |
| `lev_ta_5x` (5x) | **$76.29** | -23.71 | **-25.23** | LONG (1.32506 / 1.30932 / 1.35655 / 1.06538) | 7 (1) | 2 / 6 | $3.29 ($3.32 + $-0.02) | **0** ($0.00) | 25.1% |
| Baseline: keep $100 in XRP | $101.52 | +1.52 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
