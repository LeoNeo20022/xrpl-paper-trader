<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-26T17:01:42+00:00 at $1.2960. 1h trend now: **down**, RSI(14) 51.62 (prices `binance_spot_data_api`, funding `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$100.00** | +0.00 | **-0.12** | FLAT | 0 (0) | 0 / 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| `lev_ta_5x` (5x) | **$100.00** | +0.00 | **-0.12** | FLAT | 0 (0) | 0 / 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| Baseline: keep $100 in XRP | $100.12 | +0.12 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->
