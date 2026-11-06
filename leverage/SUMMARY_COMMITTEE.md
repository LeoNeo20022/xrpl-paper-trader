<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 2 (0) | **-2.79** | -3.22 (6.4%), low -2.79 | 0 | **-5.58** | -6.43 (6.4%), low -5.58 | 0 | **-27.91** | -32.17 (6.4%), low -27.91 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 2 (0) | **-6.82** | -7.74 (15.2%), low -6.82 | 0 | **-13.64** | -15.47 (15.2%), low -13.64 | 0 | **-68.21** | -77.37 (15.2%), low -68.21 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 2 (0) | **-2.79** | -3.22 (6.4%), low -2.79 | 0 | **-5.58** | -6.43 (6.4%), low -5.58 | 0 | **-27.91** | -32.17 (6.4%), low -27.91 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 2 (1) | **+0.53** | -4.82 (9.6%), low -4.40 | 0 | **+1.06** | -9.65 (9.6%), low -8.81 | 0 | **+5.31** | -48.24 (9.6%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 4 (0) | **-2.89** | -2.89 (5.8%), low -2.89 | 0 | **-5.78** | -5.78 (5.8%), low -5.78 | 0 | **-28.89** | -28.89 (5.8%), low -28.89 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 4 (0) | **-6.99** | -6.99 (14.0%), low -6.99 | 0 | **-13.98** | -13.98 (14.0%), low -13.98 | 0 | **-69.92** | -69.92 (14.0%), low -69.92 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 4 (0) | **-2.89** | -2.89 (5.8%), low -2.89 | 0 | **-5.78** | -5.78 (5.8%), low -5.78 | 0 | **-28.89** | -28.89 (5.8%), low -28.89 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 4 (0) | **-6.99** | -6.99 (14.0%), low -6.99 | 0 | **-13.98** | -13.98 (14.0%), low -13.98 | 0 | **-69.92** | -69.92 (14.0%), low -69.92 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$94.42** | -5.58 | **+0.38** | FLAT | 2 (0) | 0 / 2 | 0 | $0.35 | **0** | 6.4% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$86.36** | -13.64 | **-7.68** | FLAT | 2 (0) | 0 / 2 | 0 | $0.86 | **0** | 15.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$94.42** | -5.58 | **+0.85** | FLAT | 2 (0) | 0 / 2 | 0 | $0.35 | **0** | 6.4% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.44** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.44** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+6.44** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$101.06** | +1.06 | **+7.86** | FLAT | 2 (1) | 0 / 2 | 0 | $0.76 | **0** | 9.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$94.22** | -5.78 | **-1.12** | FLAT | 4 (0) | 0 / 4 | 0 | $0.71 | **0** | 5.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$86.02** | -13.98 | **-9.33** | FLAT | 4 (0) | 0 / 4 | 0 | $1.72 | **0** | 14.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$94.22** | -5.78 | **-0.77** | FLAT | 4 (0) | 0 / 4 | 0 | $0.71 | **0** | 5.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.01** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$86.02** | -13.98 | **-8.67** | FLAT | 4 (0) | 0 / 4 | 0 | $1.72 | **0** | 14.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding 0.0024%/8h, OI 24h -1.55%, long/short accounts 4.12 (98th pct of 7d), Fear & Greed 50 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0028%/8h, OI 24h 4.68%, long/short accounts 2.87 (96th pct of 7d), Fear & Greed 50 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
