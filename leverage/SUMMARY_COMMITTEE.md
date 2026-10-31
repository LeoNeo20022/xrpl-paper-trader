<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.53** | -1.83 (3.6%), low -1.66 | 0 | **-1.05** | -3.65 (3.6%), low -3.32 | 0 | **-5.25** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-1.37** | -4.52 (9.0%), low -4.10 | 0 | **-2.74** | -9.03 (9.0%), low -8.19 | 0 | **-13.72** | -45.16 (9.0%), low -40.96 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-0.53** | -1.83 (3.6%), low -1.66 | 0 | **-1.05** | -3.65 (3.6%), low -3.32 | 0 | **-5.25** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-1.24** | -4.39 (8.7%), low -3.97 | 0 | **-2.48** | -8.78 (8.7%), low -7.94 | 0 | **-12.39** | -43.91 (8.7%), low -39.71 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-1.36** | -1.49 (3.0%), low -1.49 | 0 | **-2.72** | -2.98 (3.0%), low -2.98 | 0 | **-13.61** | -14.88 (3.0%), low -14.88 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-3.36** | -3.67 (7.3%), low -3.67 | 0 | **-6.72** | -7.34 (7.3%), low -7.34 | 0 | **-33.61** | -36.68 (7.3%), low -36.68 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-1.36** | -1.49 (3.0%), low -1.49 | 0 | **-2.72** | -2.98 (3.0%), low -2.98 | 0 | **-13.61** | -14.88 (3.0%), low -14.88 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (0) | **-3.36** | -3.67 (7.3%), low -3.67 | 0 | **-6.72** | -7.34 (7.3%), low -7.34 | 0 | **-33.61** | -36.68 (7.3%), low -36.68 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$98.95** | -1.05 | **+2.23** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877867) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$97.26** | -2.74 | **+0.54** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502293) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.0% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.95** | -1.05 | **+2.72** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877867) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.77** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.77** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.77** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$97.52** | -2.48 | **+1.67** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502293) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 8.7% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$97.28** | -2.72 | **+0.63** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115271.210065) | 2 (0) | 0 / 3 | 0 | $0.49 | **0** | 3.0% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$93.28** | -6.72 | **-3.37** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 92216.968052) | 2 (0) | 0 / 3 | 0 | $1.21 | **0** | 7.3% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.28** | -2.72 | **+0.99** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115271.210065) | 2 (0) | 0 / 3 | 0 | $0.49 | **0** | 3.0% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.71** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.71** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.71** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$93.28** | -6.72 | **-2.70** | SHORT (77154.86327 / 77884.525376 / 75997.540321 / 92216.968052) | 2 (0) | 0 / 3 | 0 | $1.21 | **0** | 7.3% | — |
- Crowding XRPUSDT now: funding -0.0055%/8h, OI 24h 18.16%, long/short accounts 3.84 (89th pct of 7d), Fear & Greed 30 -> **longs** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 1.85%, long/short accounts 2.77 (95th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
