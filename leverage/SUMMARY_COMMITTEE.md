<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-1.58** | -1.92 (3.8%), low -1.75 | 0 | **-3.16** | -3.84 (3.8%), low -3.51 | 0 | **-15.82** | -19.21 (3.8%), low -17.53 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-3.91** | -4.74 (9.4%), low -4.32 | 0 | **-7.83** | -9.49 (9.4%), low -8.65 | 0 | **-39.13** | -47.44 (9.4%), low -43.24 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-1.58** | -1.92 (3.8%), low -1.75 | 0 | **-3.16** | -3.84 (3.8%), low -3.51 | 0 | **-15.82** | -19.21 (3.8%), low -17.53 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 1 (0) | **-3.79** | -4.62 (9.2%), low -4.20 | 0 | **-7.57** | -9.24 (9.2%), low -8.40 | 0 | **-37.87** | -46.19 (9.2%), low -41.99 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 3 (0) | **-2.07** | -2.07 (4.2%), low -2.07 | 0 | **-4.15** | -4.15 (4.2%), low -4.15 | 0 | **-20.74** | -20.74 (4.2%), low -20.74 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 3 (0) | **-5.08** | -5.08 (10.2%), low -5.08 | 0 | **-10.17** | -10.17 (10.2%), low -10.17 | 0 | **-50.84** | -50.84 (10.2%), low -50.84 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 3 (0) | **-2.07** | -2.07 (4.2%), low -2.07 | 0 | **-4.15** | -4.15 (4.2%), low -4.15 | 0 | **-20.74** | -20.74 (4.2%), low -20.74 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 3 (0) | **-5.08** | -5.08 (10.2%), low -5.08 | 0 | **-10.17** | -10.17 (10.2%), low -10.17 | 0 | **-50.84** | -50.84 (10.2%), low -50.84 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$96.84** | -3.16 | **-0.94** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877848) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$92.17** | -7.83 | **-5.60** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502275) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.4% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$96.84** | -3.16 | **-0.44** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.877848) | 1 (0) | 0 / 2 | 0 | $0.28 | **0** | 3.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.73** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.73** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.73** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$92.43** | -7.57 | **-4.47** | SHORT (1.258171 / 1.270752 / 1.239298 / 1.502275) | 1 (0) | 0 / 2 | 0 | $0.69 | **0** | 9.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$95.85** | -4.15 | **-2.50** | FLAT | 3 (0) | 0 / 3 | 0 | $0.53 | **0** | 4.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$89.83** | -10.17 | **-8.52** | FLAT | 3 (0) | 0 / 3 | 0 | $1.31 | **0** | 10.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$95.85** | -4.15 | **-2.14** | FLAT | 3 (0) | 0 / 3 | 0 | $0.53 | **0** | 4.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$89.83** | -10.17 | **-7.84** | FLAT | 3 (0) | 0 / 3 | 0 | $1.31 | **0** | 10.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding 0.0032%/8h, OI 24h 0.56%, long/short accounts 3.71 (61th pct of 7d), Fear & Greed 37 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h -1.38%, long/short accounts 2.32 (52th pct of 7d), Fear & Greed 37 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
