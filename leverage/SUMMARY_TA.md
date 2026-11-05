<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-05T10:09:12+00:00 at $1.3177. 1h trend now: **up**, RSI(14) 63.9 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | LONG | 7 (1) | **-4.70** | -5.19 (10.3%), low -4.94 | 0 | **-9.39** | -10.39 (10.3%), low -9.87 | 0 | **-46.95** | -51.93 (10.3%), low -49.37 | 0 |
| `lev_ta_5x` (5x) | LONG | 7 (1) | **-11.31** | -12.48 (24.6%), low -11.84 | 0 | **-22.62** | -24.95 (24.6%), low -23.68 | 0 | **-113.12** | -124.77 (24.6%), low -118.40 | 0 |

Keep $50 / $100 / $500 in XRP: +0.90 / +1.80 / +8.98.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$90.61** | -9.39 | **-11.19** | LONG (1.32506 / 1.30932 / 1.35655 / 0.66586) | 7 (1) | 2 / 6 | $1.39 ($1.40 + $-0.01) | **0** ($0.00) | 10.3% |
| `lev_ta_5x` (5x) | **$77.38** | -22.62 | **-24.42** | LONG (1.32506 / 1.30932 / 1.35655 / 1.06538) | 7 (1) | 2 / 6 | $3.29 ($3.32 + $-0.02) | **0** ($0.00) | 24.6% |
| Baseline: keep $100 in XRP | $101.80 | +1.80 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
