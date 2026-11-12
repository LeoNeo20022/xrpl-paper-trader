<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-11-12T13:56:08+00:00 at $1.0342 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$80.92** | -19.08 | **+1.55** | 171.90 (1.14194) | 0.57472 | 10/10 | 9 | $0.28 ($0.11 + $0.16) | **0** ($0.00) | 23.1% |
| `lev_5x` (5x) | **$52.30** | -47.70 | **-27.06** | 429.75 (1.14194) | 0.91902 | 10/10 | 9 | $0.69 ($0.28 + $0.41) | **0** ($0.00) | 55.8% |
| Baseline: keep $100 in XRP | $79.37 | -20.63 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-11-12T13:56:17+00:00 at $1.0342. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **+52.22** | **+3.10** (-0.90 vs $4) | -56.84 (5.2%) | 11 (55%) | 0 | 11 (55% wins) +55.57 | 4 SHORT @ 1.033083 (stop 1.043414, TP 1.017587, liq 1.334058) | $0.84 / $-1.13 | 0 | +256.95 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **+102.53** | **+6.10** (+2.10 vs $4) | -89.71 (7.7%) | 11 (55%) | 0 | 11 (55% wins) +107.57 | 6 SHORT @ 1.033083 (stop 1.043414, TP 1.017587, liq 1.198504) | $1.38 / $-1.72 | 0 | +307.27 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->
