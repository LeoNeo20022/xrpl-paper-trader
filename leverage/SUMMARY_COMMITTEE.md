<!-- COMMITTEE-BEGIN -->
## Separate lines: rule-based COMMITTEE, paper perps on XRP and BTC (`com_*`, PAPER-NOT-REAL)

Four rule-based voters (long scout, short scout, idle guard, chart reader) vote every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). $100 each, isolated margin; same costs/funding/liquidation as leverage_ta.

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 @ 1.2894 | **$100.00** | +0.00 | **+0.15** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 @ 1.2894 | **$100.00** | +0.00 | **+0.15** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 @ 79940 | **$100.00** | +0.00 | **+0.12** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 @ 79940 | **$100.00** | +0.00 | **+0.12** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
