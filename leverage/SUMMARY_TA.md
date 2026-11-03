<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-03T02:52:02+00:00 at $1.2498. 1h trend now: **down**, RSI(14) 49.58 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 5 (1) | **-1.71** | -3.06 (6.1%), low -2.81 | 0 | **-3.43** | -6.13 (6.1%), low -5.62 | 0 | **-17.14** | -30.65 (6.1%), low -28.09 | 0 |
| `lev_ta_5x` (5x) | SHORT | 5 (1) | **-4.53** | -7.73 (15.3%), low -7.09 | 0 | **-9.06** | -15.46 (15.3%), low -14.18 | 0 | **-45.30** | -77.29 (15.3%), low -70.92 | 0 |

Keep $50 / $100 / $500 in XRP: -1.72 / -3.45 / -17.25.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$96.57** | -3.43 | **+0.02** | SHORT (1.25367 / 1.26434 / 1.23235 / 1.87126) | 5 (1) | 1 / 5 | $1.02 ($1.02 + $0.00) | **0** ($0.00) | 6.1% |
| `lev_ta_5x` (5x) | **$90.94** | -9.06 | **-5.61** | SHORT (1.25367 / 1.26434 / 1.23235 / 1.49703) | 5 (1) | 1 / 5 | $2.46 ($2.46 + $0.00) | **0** ($0.00) | 15.3% |
| Baseline: keep $100 in XRP | $96.55 | -3.45 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
