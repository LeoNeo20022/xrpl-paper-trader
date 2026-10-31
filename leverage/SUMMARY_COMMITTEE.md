<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.87** | -1.83 (3.6%), low -1.66 | 0 | **-1.75** | -3.65 (3.6%), low -3.32 | 0 | **-8.74** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-2.21** | -4.52 (9.0%), low -4.10 | 0 | **-4.42** | -9.03 (9.0%), low -8.19 | 0 | **-22.11** | -45.16 (9.0%), low -40.96 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-0.87** | -1.83 (3.6%), low -1.66 | 0 | **-1.75** | -3.65 (3.6%), low -3.32 | 0 | **-8.74** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-2.08** | -4.39 (8.7%), low -3.97 | 0 | **-4.16** | -8.78 (8.7%), low -7.94 | 0 | **-20.80** | -43.91 (8.7%), low -39.71 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-1.65** | -1.97 (3.9%), low -1.97 | 0 | **-3.30** | -3.94 (3.9%), low -3.94 | 0 | **-16.48** | -19.71 (3.9%), low -19.71 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-4.05** | -4.84 (9.7%), low -4.84 | 0 | **-8.11** | -9.67 (9.7%), low -9.67 | 0 | **-40.54** | -48.36 (9.7%), low -48.36 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-1.65** | -1.97 (3.9%), low -1.97 | 0 | **-3.30** | -3.94 (3.9%), low -3.94 | 0 | **-16.48** | -19.71 (3.9%), low -19.71 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (0) | **-4.05** | -4.84 (9.7%), low -4.84 | 0 | **-8.11** | -9.67 (9.7%), low -9.67 | 0 | **-40.54** | -48.36 (9.7%), low -48.36 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$98.25** | -1.75 | **+1.19** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877872) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$95.58** | -4.42 | **-1.49** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502298) | 1 (0) | 0 / 2 | 0 | $0.68 | **0** | 9.0% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.25** | -1.75 | **+1.68** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877872) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.43** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.43** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.43** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$95.84** | -4.16 | **-0.36** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502298) | 1 (0) | 0 / 2 | 0 | $0.68 | **0** | 8.7% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$96.70** | -3.30 | **-0.25** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115286.646122) | 2 (0) | 0 / 3 | 0 | $0.46 | **0** | 3.9% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$91.89** | -8.11 | **-5.06** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 92232.404109) | 2 (0) | 0 / 3 | 0 | $1.12 | **0** | 9.7% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$96.70** | -3.30 | **+0.11** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115286.646122) | 2 (0) | 0 / 3 | 0 | $0.46 | **0** | 3.9% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.41** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$91.89** | -8.11 | **-4.39** | SHORT (77154.86327 / 77884.525376 / 75997.540321 / 92232.404109) | 2 (0) | 0 / 3 | 0 | $1.12 | **0** | 9.7% | — |
- Crowding XRPUSDT now: funding 0.002%/8h, OI 24h 3.55%, long/short accounts 3.78 (82th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h -0.22%, long/short accounts 2.62 (79th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
