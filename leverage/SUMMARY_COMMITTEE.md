<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-0.58** | -1.83 (3.6%), low -1.66 | 0 | **-1.16** | -3.65 (3.6%), low -3.32 | 0 | **-5.81** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-1.51** | -4.52 (9.0%), low -4.10 | 0 | **-3.01** | -9.03 (9.0%), low -8.19 | 0 | **-15.06** | -45.16 (9.0%), low -40.96 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-0.58** | -1.83 (3.6%), low -1.66 | 0 | **-1.16** | -3.65 (3.6%), low -3.32 | 0 | **-5.81** | -18.26 (3.6%), low -16.58 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-1.37** | -4.39 (8.7%), low -3.97 | 0 | **-2.75** | -8.78 (8.7%), low -7.94 | 0 | **-13.74** | -43.91 (8.7%), low -39.71 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-1.55** | -1.65 (3.3%), low -1.65 | 0 | **-3.10** | -3.30 (3.3%), low -3.30 | 0 | **-15.48** | -16.52 (3.3%), low -16.52 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-3.81** | -4.06 (8.1%), low -4.06 | 0 | **-7.62** | -8.13 (8.1%), low -8.13 | 0 | **-38.12** | -40.65 (8.1%), low -40.65 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-1.55** | -1.65 (3.3%), low -1.65 | 0 | **-3.10** | -3.30 (3.3%), low -3.30 | 0 | **-15.48** | -16.52 (3.3%), low -16.52 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (0) | **-3.81** | -4.06 (8.1%), low -4.06 | 0 | **-7.62** | -8.13 (8.1%), low -8.13 | 0 | **-38.12** | -40.65 (8.1%), low -40.65 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$98.84** | -1.16 | **+2.07** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877847) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$96.99** | -3.01 | **+0.22** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502274) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.0% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.84** | -1.16 | **+2.56** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877847) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.6% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.72** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.72** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.72** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "IDLE"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$97.25** | -2.75 | **+1.34** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502274) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 8.7% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$96.90** | -3.10 | **+0.06** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115278.914846) | 2 (0) | 0 / 3 | 0 | $0.48 | **0** | 3.3% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$92.38** | -7.62 | **-4.47** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 92224.672833) | 2 (0) | 0 / 3 | 0 | $1.17 | **0** | 8.1% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$96.90** | -3.10 | **+0.42** | SHORT (77154.86327 / 77884.525376 / 75695.539057 / 115278.914846) | 2 (0) | 0 / 3 | 0 | $0.48 | **0** | 3.3% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.51** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.51** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.51** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$92.38** | -7.62 | **-3.80** | SHORT (77154.86327 / 77884.525376 / 75997.540321 / 92224.672833) | 2 (0) | 0 / 3 | 0 | $1.17 | **0** | 8.1% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding -0.0016%/8h, OI 24h 17.83%, long/short accounts 3.92 (93th pct of 7d), Fear & Greed 30 -> **longs** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 4.14%, long/short accounts 2.74 (91th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
