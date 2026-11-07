<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 4 (1) | **-1.45** | -3.64 (7.2%), low -3.22 | 0 | **-2.90** | -7.28 (7.2%), low -6.43 | 0 | **-14.49** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 4 (1) | **-4.08** | -8.71 (17.1%), low -7.79 | 0 | **-8.17** | -17.41 (17.1%), low -15.58 | 0 | **-40.84** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 4 (1) | **-1.45** | -3.64 (7.2%), low -3.22 | 0 | **-2.90** | -7.28 (7.2%), low -6.43 | 0 | **-14.49** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 4 (2) | **+1.05** | -6.41 (11.2%), low -4.40 | 0 | **+2.09** | -12.82 (11.2%), low -8.81 | 0 | **+10.47** | -64.12 (11.2%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-3.44** | -3.95 (7.9%), low -3.95 | 0 | **-6.87** | -7.89 (7.9%), low -7.89 | 0 | **-34.36** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-8.24** | -9.40 (18.8%), low -9.40 | 0 | **-16.47** | -18.80 (18.8%), low -18.80 | 0 | **-82.37** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (0) | **-3.44** | -3.95 (7.9%), low -3.95 | 0 | **-6.87** | -7.89 (7.9%), low -7.89 | 0 | **-34.36** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (0) | **-8.24** | -9.40 (18.8%), low -9.40 | 0 | **-16.47** | -18.80 (18.8%), low -18.80 | 0 | **-82.37** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$97.10** | -2.90 | **+6.19** | FLAT | 4 (1) | 0 / 4 | 0 | $0.66 | **0** | 7.2% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$91.83** | -8.17 | **+0.92** | FLAT | 4 (1) | 0 / 4 | 0 | $1.61 | **0** | 17.1% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.10** | -2.90 | **+6.65** | FLAT | 4 (1) | 0 / 4 | 0 | $0.66 | **0** | 7.2% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+9.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+9.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+9.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$102.09** | +2.09 | **+11.99** | FLAT | 4 (2) | 0 / 4 | 0 | $1.61 | **0** | 11.2% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$93.13** | -6.87 | **-1.86** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113018.873134) | 4 (0) | 0 / 5 | 0 | $0.78 | **0** | 7.9% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$83.53** | -16.47 | **-11.47** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 90416.631104) | 4 (0) | 0 / 5 | 0 | $1.89 | **0** | 18.8% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$93.13** | -6.87 | **-1.51** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113018.873134) | 4 (0) | 0 / 5 | 0 | $0.78 | **0** | 7.9% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.36** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.36** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.36** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$83.53** | -16.47 | **-10.81** | SHORT (75642.169995 / 76398.591695 / 74507.537445 / 90416.631104) | 4 (0) | 0 / 5 | 0 | $1.89 | **0** | 18.8% | — |
- Crowding XRPUSDT now: funding 0.0072%/8h, OI 24h 1.27%, long/short accounts 3.96 (80th pct of 7d), Fear & Greed 25 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding -0.0004%/8h, OI 24h -1.68%, long/short accounts 2.93 (82th pct of 7d), Fear & Greed 25 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
