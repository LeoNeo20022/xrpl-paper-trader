<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-05T06:46:03+00:00 at $1.3086. 1h trend now: **up**, RSI(14) 57.57 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 7 (1) | **-4.05** | -4.30 (8.6%), low -4.05 | 0 | **-8.10** | -8.61 (8.6%), low -8.10 | 0 | **-40.48** | -43.03 (8.6%), low -40.48 | 0 |
| `lev_ta_5x` (5x) | FLAT | 7 (1) | **-9.90** | -10.54 (20.8%), low -9.90 | 0 | **-19.80** | -21.08 (20.8%), low -19.80 | 0 | **-99.02** | -105.40 (20.8%), low -99.02 | 0 |

Keep $50 / $100 / $500 in XRP: +0.55 / +1.09 / +5.47.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$91.90** | -8.10 | **-9.19** | FLAT | 7 (1) | 1 / 6 | $1.29 ($1.31 + $-0.01) | **0** ($0.00) | 8.6% |
| `lev_ta_5x` (5x) | **$80.20** | -19.80 | **-20.90** | FLAT | 7 (1) | 1 / 6 | $3.09 ($3.12 + $-0.02) | **0** ($0.00) | 20.8% |
| Baseline: keep $100 in XRP | $101.09 | +1.09 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
