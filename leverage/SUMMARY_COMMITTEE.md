<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-2.77** | -3.61 (7.2%), low -3.18 | 0 | **-5.53** | -7.22 (7.2%), low -6.37 | 0 | **-27.67** | -36.10 (7.2%), low -31.84 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-6.77** | -8.64 (17.0%), low -7.72 | 0 | **-13.53** | -17.27 (17.0%), low -15.44 | 0 | **-67.66** | -86.36 (17.0%), low -77.19 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-2.77** | -3.61 (7.2%), low -3.18 | 0 | **-5.53** | -7.22 (7.2%), low -6.37 | 0 | **-27.67** | -36.10 (7.2%), low -31.84 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (1) | **+0.59** | -4.82 (9.6%), low -4.40 | 0 | **+1.19** | -9.65 (9.6%), low -8.81 | 0 | **+5.94** | -48.24 (9.6%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-3.62** | -3.84 (7.7%), low -3.84 | 0 | **-7.23** | -7.68 (7.7%), low -7.68 | 0 | **-36.16** | -38.40 (7.7%), low -38.40 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-8.65** | -9.16 (18.3%), low -9.16 | 0 | **-17.29** | -18.32 (18.3%), low -18.32 | 0 | **-86.47** | -91.58 (18.3%), low -91.58 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (0) | **-3.62** | -3.84 (7.7%), low -3.84 | 0 | **-7.23** | -7.68 (7.7%), low -7.68 | 0 | **-36.16** | -38.40 (7.7%), low -38.40 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (0) | **-8.65** | -9.16 (18.3%), low -9.16 | 0 | **-17.29** | -18.32 (18.3%), low -18.32 | 0 | **-86.47** | -91.58 (18.3%), low -91.58 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$94.47** | -5.53 | **+1.66** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.79) | 2 (0) | 0 / 3 | 0 | $0.45 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$86.47** | -13.53 | **-6.34** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.432) | 2 (0) | 0 / 3 | 0 | $1.08 | **0** | 17.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$94.47** | -5.53 | **+2.14** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.79) | 2 (0) | 0 / 3 | 0 | $0.45 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.67** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.67** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.67** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$101.19** | +1.19 | **+9.21** | SHORT (1.1993 / 1.211293 / 1.181311 / 1.432) | 2 (1) | 0 / 3 | 0 | $1.01 | **0** | 9.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$92.77** | -7.23 | **-2.40** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113011.210152) | 4 (0) | 0 / 5 | 0 | $0.80 | **0** | 7.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$82.71** | -17.29 | **-12.46** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 90408.968122) | 4 (0) | 0 / 5 | 0 | $1.93 | **0** | 18.3% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$92.77** | -7.23 | **-2.04** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113011.210152) | 4 (0) | 0 / 5 | 0 | $0.80 | **0** | 7.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.19** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.19** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.19** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$82.71** | -17.29 | **-11.80** | SHORT (75642.169995 / 76398.591695 / 74507.537445 / 90408.968122) | 4 (0) | 0 / 5 | 0 | $1.93 | **0** | 18.3% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding 0.01%/8h, OI 24h -0.65%, long/short accounts 4.06 (98th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0027%/8h, OI 24h 4.64%, long/short accounts 3.02 (100th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
