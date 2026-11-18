<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-18T08:41:30+00:00 at $1.0018. 1h trend now: **down**, RSI(14) 72.18 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 19 (6) | **-2.55** | -9.22 (16.3%), low -5.99 | 0 | **-5.10** | -18.44 (16.3%), low -11.98 | 0 | **-25.50** | -92.19 (16.3%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | FLAT | 19 (6) | **-8.79** | -23.77 (36.6%), low -14.07 | 0 | **-17.58** | -47.55 (36.6%), low -28.13 | 0 | **-87.92** | -237.74 (36.6%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -11.30 / -22.61 / -113.04.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$94.90** | -5.10 | **+17.51** | FLAT | 19 (6) | 2 / 17 | $3.38 ($3.40 + $-0.02) | **0** ($0.00) | 16.3% |
| `lev_ta_5x` (5x) | **$82.42** | -17.58 | **+5.02** | FLAT | 19 (6) | 2 / 17 | $8.11 ($8.14 + $-0.03) | **0** ($0.00) | 36.6% |
| Baseline: keep $100 in XRP | $77.39 | -22.61 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
