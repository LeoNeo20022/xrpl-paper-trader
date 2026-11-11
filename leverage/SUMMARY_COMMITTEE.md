<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 6 (2) | **+0.03** | -3.64 (7.2%), low -3.22 | 0 | **+0.06** | -7.28 (7.2%), low -6.43 | 0 | **+0.30** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 6 (2) | **-0.91** | -8.71 (17.1%), low -7.79 | 0 | **-1.83** | -17.41 (17.1%), low -15.58 | 0 | **-9.13** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 6 (2) | **+0.03** | -3.64 (7.2%), low -3.22 | 0 | **+0.06** | -7.28 (7.2%), low -6.43 | 0 | **+0.30** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 8 (5) | **+9.21** | -7.64 (13.3%), low -4.40 | 0 | **+18.42** | -15.27 (13.3%), low -8.81 | 0 | **+92.12** | -76.36 (13.3%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 6 (1) | **-2.05** | -3.95 (7.9%), low -3.95 | 0 | **-4.10** | -7.89 (7.9%), low -7.89 | 0 | **-20.48** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 6 (1) | **-5.24** | -9.40 (18.8%), low -9.40 | 0 | **-10.47** | -18.80 (18.8%), low -18.80 | 0 | **-52.37** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 6 (1) | **-2.05** | -3.95 (7.9%), low -3.95 | 0 | **-4.10** | -7.89 (7.9%), low -7.89 | 0 | **-20.48** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 6 (1) | **-6.52** | -9.40 (18.8%), low -9.40 | 0 | **-13.04** | -18.80 (18.8%), low -18.80 | 0 | **-65.19** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$100.06** | +0.06 | **+18.04** | SHORT (1.071364 / 1.094925 / 1.024243 / 1.599109) | 6 (2) | 0 / 7 | 0 | $1.06 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$98.17** | -1.83 | **+16.15** | SHORT (1.071364 / 1.094925 / 1.024243 / 1.279299) | 6 (2) | 0 / 7 | 0 | $2.57 | **0** | 17.1% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.06** | +0.06 | **+18.46** | SHORT (1.071364 / 1.094925 / 1.024243 / 1.599109) | 6 (2) | 0 / 7 | 0 | $1.06 | **0** | 7.2% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+18.40** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+18.40** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+18.40** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$118.42** | +18.42 | **+37.14** | FLAT | 8 (5) | 0 / 8 | 0 | $3.23 | **0** | 13.3% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$95.90** | -4.10 | **+3.83** | SHORT (73743.11 / 74624.728866 / 71979.872268 / 110181.319329) | 6 (1) | 0 / 7 | 0 | $1.06 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$89.53** | -10.47 | **-2.55** | SHORT (73743.11 / 74624.728866 / 71979.872268 / 88146.525504) | 6 (1) | 0 / 7 | 0 | $2.54 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$95.90** | -4.10 | **+4.17** | SHORT (73743.11 / 74624.728866 / 71979.872268 / 110181.319329) | 6 (1) | 0 / 7 | 0 | $1.06 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+8.26** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+8.26** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+8.26** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$86.96** | -13.04 | **-4.48** | SHORT (73743.11 / 74480.5411 / 72636.96335 / 88146.525504) | 6 (1) | 0 / 7 | 0 | $2.52 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding 0.0056%/8h, OI 24h 0.71%, long/short accounts 3.79 (23th pct of 7d), Fear & Greed 29 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 3.34%, long/short accounts 3.01 (83th pct of 7d), Fear & Greed 29 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
