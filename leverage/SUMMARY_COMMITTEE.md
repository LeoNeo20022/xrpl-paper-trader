<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-2.88** | -3.49 (6.9%), low -3.07 | 0 | **-5.75** | -6.98 (6.9%), low -6.13 | 0 | **-28.77** | -34.92 (6.9%), low -30.66 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 2 (0) | **-7.02** | -8.37 (16.4%), low -7.45 | 0 | **-14.04** | -16.73 (16.4%), low -14.90 | 0 | **-70.18** | -83.66 (16.4%), low -74.49 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 2 (0) | **-2.88** | -3.49 (6.9%), low -3.07 | 0 | **-5.75** | -6.98 (6.9%), low -6.13 | 0 | **-28.77** | -34.92 (6.9%), low -30.66 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 2 (1) | **+0.30** | -4.82 (9.6%), low -4.40 | 0 | **+0.60** | -9.65 (9.6%), low -8.81 | 0 | **+3.00** | -48.24 (9.6%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-3.56** | -3.84 (7.7%), low -3.84 | 0 | **-7.13** | -7.68 (7.7%), low -7.68 | 0 | **-35.63** | -38.40 (7.7%), low -38.40 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-8.53** | -9.16 (18.3%), low -9.16 | 0 | **-17.06** | -18.32 (18.3%), low -18.32 | 0 | **-85.28** | -91.58 (18.3%), low -91.58 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (0) | **-3.56** | -3.84 (7.7%), low -3.84 | 0 | **-7.13** | -7.68 (7.7%), low -7.68 | 0 | **-35.63** | -38.40 (7.7%), low -38.40 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (0) | **-8.53** | -9.16 (18.3%), low -9.16 | 0 | **-17.06** | -18.32 (18.3%), low -18.32 | 0 | **-85.28** | -91.58 (18.3%), low -91.58 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$94.25** | -5.75 | **+1.33** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.79) | 2 (0) | 0 / 3 | 0 | $0.45 | **0** | 6.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$85.96** | -14.04 | **-6.95** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.432) | 2 (0) | 0 / 3 | 0 | $1.08 | **0** | 16.4% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$94.25** | -5.75 | **+1.81** | SHORT (1.1993 / 1.218528 / 1.160843 / 1.79) | 2 (0) | 0 / 3 | 0 | $0.45 | **0** | 6.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.56** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.56** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+7.56** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$100.60** | +0.60 | **+8.52** | SHORT (1.1993 / 1.211293 / 1.181311 / 1.432) | 2 (1) | 0 / 3 | 0 | $1.01 | **0** | 9.6% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$92.87** | -7.13 | **-2.24** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113011.210152) | 4 (0) | 0 / 5 | 0 | $0.80 | **0** | 7.7% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$82.94** | -17.06 | **-12.17** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 90408.968122) | 4 (0) | 0 / 5 | 0 | $1.93 | **0** | 18.3% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$92.87** | -7.13 | **-1.89** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113011.210152) | 4 (0) | 0 / 5 | 0 | $0.80 | **0** | 7.7% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.24** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.24** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.24** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$82.94** | -17.06 | **-11.51** | SHORT (75642.169995 / 76398.591695 / 74507.537445 / 90408.968122) | 4 (0) | 0 / 5 | 0 | $1.93 | **0** | 18.3% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding 0.01%/8h, OI 24h -1.9%, long/short accounts 4.12 (99th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0027%/8h, OI 24h 5.08%, long/short accounts 3.0 (100th pct of 7d), Fear & Greed 28 -> **longs** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
