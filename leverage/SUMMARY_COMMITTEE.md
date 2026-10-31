<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.36** | -1.83 (3.6%), low -1.66 | 0 | **-0.72** | -3.65 (3.6%), low -3.32 | 0 | **-3.62** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.98** | -4.52 (9.0%), low -4.10 | 0 | **-1.96** | -9.03 (9.0%), low -8.19 | 0 | **-9.80** | -45.16 (9.0%), low -40.96 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-0.36** | -1.83 (3.6%), low -1.66 | 0 | **-0.72** | -3.65 (3.6%), low -3.32 | 0 | **-3.62** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-0.85** | -4.39 (8.7%), low -3.97 | 0 | **-1.69** | -8.78 (8.7%), low -7.94 | 0 | **-8.46** | -43.91 (8.7%), low -39.71 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-1.25** | -1.37 (2.8%), low -1.37 | 0 | **-2.51** | -2.75 (2.8%), low -2.75 | 0 | **-12.55** | -13.73 (2.8%), low -13.73 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-3.10** | -3.39 (6.8%), low -3.39 | 0 | **-6.21** | -6.78 (6.8%), low -6.78 | 0 | **-31.03** | -33.89 (6.8%), low -33.89 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-1.25** | -1.37 (2.8%), low -1.37 | 0 | **-2.51** | -2.75 (2.8%), low -2.75 | 0 | **-12.55** | -13.73 (2.8%), low -13.73 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (0) | **-3.10** | -3.39 (6.8%), low -3.39 | 0 | **-6.21** | -6.78 (6.8%), low -6.78 | 0 | **-31.03** | -33.89 (6.8%), low -33.89 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$99.28** | -0.72 | **+2.72** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877867) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$98.04** | -1.96 | **+1.49** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502293) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.0% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$99.28** | -0.72 | **+3.21** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877867) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.94** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.94** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.94** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$98.31** | -1.69 | **+2.61** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502293) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 8.7% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$97.49** | -2.51 | **+0.95** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115271.210065) | 2 (0) | 0 / 3 | 0 | $0.49 | **0** | 2.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$93.79** | -6.21 | **-2.75** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 92216.968052) | 2 (0) | 0 / 3 | 0 | $1.21 | **0** | 6.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.49** | -2.51 | **+1.30** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115271.210065) | 2 (0) | 0 / 3 | 0 | $0.49 | **0** | 2.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.81** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.81** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.81** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$93.79** | -6.21 | **-2.08** | SHORT (77154.86327 / 77884.525376 / 75997.540321 / 92216.968052) | 2 (0) | 0 / 3 | 0 | $1.21 | **0** | 6.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding -0.0055%/8h, OI 24h 18.97%, long/short accounts 3.83 (86th pct of 7d), Fear & Greed 30 -> **longs** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 1.19%, long/short accounts 2.76 (95th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
