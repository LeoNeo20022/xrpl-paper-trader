<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.67** | -1.83 (3.6%), low -1.66 | 0 | **-1.33** | -3.65 (3.6%), low -3.32 | 0 | **-6.66** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-1.71** | -4.52 (9.0%), low -4.10 | 0 | **-3.42** | -9.03 (9.0%), low -8.19 | 0 | **-17.11** | -45.16 (9.0%), low -40.96 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-0.67** | -1.83 (3.6%), low -1.66 | 0 | **-1.33** | -3.65 (3.6%), low -3.32 | 0 | **-6.66** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-1.58** | -4.39 (8.7%), low -3.97 | 0 | **-3.16** | -8.78 (8.7%), low -7.94 | 0 | **-15.79** | -43.91 (8.7%), low -39.71 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-1.66** | -1.92 (3.8%), low -1.92 | 0 | **-3.31** | -3.83 (3.8%), low -3.83 | 0 | **-16.56** | -19.17 (3.8%), low -19.17 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-4.07** | -4.70 (9.4%), low -4.70 | 0 | **-8.15** | -9.41 (9.4%), low -9.41 | 0 | **-40.74** | -47.04 (9.4%), low -47.04 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-1.66** | -1.92 (3.8%), low -1.92 | 0 | **-3.31** | -3.83 (3.8%), low -3.83 | 0 | **-16.56** | -19.17 (3.8%), low -19.17 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (0) | **-4.07** | -4.70 (9.4%), low -4.70 | 0 | **-8.15** | -9.41 (9.4%), low -9.41 | 0 | **-40.74** | -47.04 (9.4%), low -47.04 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$98.67** | -1.33 | **+1.81** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877847) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$96.58** | -3.42 | **-0.28** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502274) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.0% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.67** | -1.33 | **+2.30** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877847) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$96.84** | -3.16 | **+0.85** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502274) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 8.7% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$96.69** | -3.31 | **-0.26** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115278.914846) | 2 (0) | 0 / 3 | 0 | $0.48 | **0** | 3.8% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$91.85** | -8.15 | **-5.10** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 92224.672833) | 2 (0) | 0 / 3 | 0 | $1.17 | **0** | 9.4% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$96.69** | -3.31 | **+0.10** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115278.914846) | 2 (0) | 0 / 3 | 0 | $0.48 | **0** | 3.8% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$91.85** | -8.15 | **-4.42** | SHORT (77154.86327 / 77884.525376 / 75997.540321 / 92224.672833) | 2 (0) | 0 / 3 | 0 | $1.17 | **0** | 9.4% | — |
- Crowding XRPUSDT now: funding -0.0016%/8h, OI 24h 14.04%, long/short accounts 3.8 (82th pct of 7d), Fear & Greed 30 -> **longs** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 0.48%, long/short accounts 2.67 (85th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
