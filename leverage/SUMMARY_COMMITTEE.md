<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-1.34** | -2.01 (4.0%), low -1.84 | 0 | **-2.69** | -4.01 (4.0%), low -3.68 | 0 | **-13.43** | -20.06 (4.0%), low -18.38 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 1 (0) | **-3.34** | -4.95 (9.8%), low -4.53 | 0 | **-6.68** | -9.90 (9.8%), low -9.06 | 0 | **-33.39** | -49.49 (9.8%), low -45.29 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 1 (0) | **-1.34** | -2.01 (4.0%), low -1.84 | 0 | **-2.69** | -4.01 (4.0%), low -3.68 | 0 | **-13.43** | -20.06 (4.0%), low -18.38 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 2 (1) | **+0.53** | -4.82 (9.6%), low -4.40 | 0 | **+1.06** | -9.65 (9.6%), low -8.81 | 0 | **+5.31** | -48.24 (9.6%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 3 (0) | **-2.39** | -2.59 (5.2%), low -2.59 | 0 | **-4.78** | -5.18 (5.2%), low -5.18 | 0 | **-23.89** | -25.91 (5.2%), low -25.91 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 3 (0) | **-5.82** | -6.29 (12.6%), low -6.29 | 0 | **-11.64** | -12.59 (12.6%), low -12.59 | 0 | **-58.21** | -62.95 (12.6%), low -62.95 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 3 (0) | **-2.39** | -2.59 (5.2%), low -2.59 | 0 | **-4.78** | -5.18 (5.2%), low -5.18 | 0 | **-23.89** | -25.91 (5.2%), low -25.91 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 3 (0) | **-5.82** | -6.29 (12.6%), low -6.29 | 0 | **-11.64** | -12.59 (12.6%), low -12.59 | 0 | **-58.21** | -62.95 (12.6%), low -62.95 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$97.31** | -2.69 | **-0.23** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.878026) | 1 (0) | 0 / 2 | 0 | $0.25 | **0** | 4.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$93.32** | -6.68 | **-4.22** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.502453) | 1 (0) | 0 / 2 | 0 | $0.63 | **0** | 9.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.31** | -2.69 | **+0.26** | SHORT (1.258171 / 1.27706 / 1.220392 / 1.878026) | 1 (0) | 0 / 2 | 0 | $0.25 | **0** | 4.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.95** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.95** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+2.95** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$101.06** | +1.06 | **+4.38** | FLAT | 2 (1) | 0 / 2 | 0 | $0.76 | **0** | 9.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$95.22** | -4.78 | **-1.25** | SHORT (77013.474 / 77560.963278 / 75918.495444 / 115067.623462) | 3 (0) | 0 / 4 | 0 | $0.61 | **0** | 5.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$88.36** | -11.64 | **-8.12** | SHORT (77013.474 / 77560.963278 / 75918.495444 / 92055.629239) | 3 (0) | 0 / 4 | 0 | $1.49 | **0** | 12.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$95.22** | -4.78 | **-0.89** | SHORT (77013.474 / 77560.963278 / 75918.495444 / 115067.623462) | 3 (0) | 0 / 4 | 0 | $0.61 | **0** | 5.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.88** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.88** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.88** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$88.36** | -11.64 | **-7.45** | SHORT (77013.474 / 77560.963278 / 75858.27189 / 92055.629239) | 3 (0) | 0 / 4 | 0 | $1.49 | **0** | 12.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding 0.0056%/8h, OI 24h -3.15%, long/short accounts 3.65 (36th pct of 7d), Fear & Greed 26 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 2.11%, long/short accounts 2.76 (88th pct of 7d), Fear & Greed 26 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
