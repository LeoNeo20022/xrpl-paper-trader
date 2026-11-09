<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 6 (2) | **-1.04** | -3.64 (7.2%), low -3.22 | 0 | **-2.08** | -7.28 (7.2%), low -6.43 | 0 | **-10.41** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 6 (2) | **-3.45** | -8.71 (17.1%), low -7.79 | 0 | **-6.91** | -17.41 (17.1%), low -15.58 | 0 | **-34.55** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 6 (2) | **-1.04** | -3.64 (7.2%), low -3.22 | 0 | **-2.08** | -7.28 (7.2%), low -6.43 | 0 | **-10.41** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 7 (4) | **+5.27** | -7.64 (13.3%), low -4.40 | 0 | **+10.54** | -15.27 (13.3%), low -8.81 | 0 | **+52.70** | -76.36 (13.3%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 5 (1) | **-1.75** | -3.95 (7.9%), low -3.95 | 0 | **-3.50** | -7.89 (7.9%), low -7.89 | 0 | **-17.52** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 5 (1) | **-4.52** | -9.40 (18.8%), low -9.40 | 0 | **-9.04** | -18.80 (18.8%), low -18.80 | 0 | **-45.21** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 5 (1) | **-1.75** | -3.95 (7.9%), low -3.95 | 0 | **-3.50** | -7.89 (7.9%), low -7.89 | 0 | **-17.52** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 5 (1) | **-5.90** | -9.40 (18.8%), low -9.40 | 0 | **-11.79** | -18.80 (18.8%), low -18.80 | 0 | **-58.96** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$97.92** | -2.08 | **+12.03** | FLAT | 6 (2) | 0 / 6 | 0 | $0.97 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$93.09** | -6.91 | **+7.20** | FLAT | 6 (2) | 0 / 6 | 0 | $2.37 | **0** | 17.1% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.92** | -2.08 | **+12.47** | FLAT | 6 (2) | 0 / 6 | 0 | $0.97 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+14.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+14.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+14.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$110.54** | +10.54 | **+25.42** | FLAT | 7 (4) | 0 / 7 | 0 | $2.85 | **0** | 13.3% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$96.50** | -3.50 | **+2.79** | SHORT (74402.78 / 75169.945313 / 72868.449373 / 111159.531873) | 5 (1) | 0 / 6 | 0 | $0.88 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$90.96** | -9.04 | **-2.75** | SHORT (74402.78 / 75169.945313 / 72868.449373 / 88927.625498) | 5 (1) | 0 / 6 | 0 | $2.12 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$96.50** | -3.50 | **+3.13** | SHORT (74402.78 / 75169.945313 / 72868.449373 / 111159.531873) | 5 (1) | 0 / 6 | 0 | $0.88 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.64** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$88.21** | -11.79 | **-4.85** | SHORT (74402.78 / 75146.8078 / 73286.7383 / 88927.625498) | 5 (1) | 0 / 6 | 0 | $2.11 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding 0.0008%/8h, OI 24h -4.72%, long/short accounts 3.92 (49th pct of 7d), Fear & Greed 29 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0096%/8h, OI 24h 1.22%, long/short accounts 2.98 (78th pct of 7d), Fear & Greed 29 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
