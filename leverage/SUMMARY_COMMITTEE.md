<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (1) | **-0.97** | -3.64 (7.2%), low -3.22 | 0 | **-1.94** | -7.28 (7.2%), low -6.43 | 0 | **-9.69** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (1) | **-2.95** | -8.71 (17.1%), low -7.79 | 0 | **-5.90** | -17.41 (17.1%), low -15.58 | 0 | **-29.51** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (1) | **-0.97** | -3.64 (7.2%), low -3.22 | 0 | **-1.94** | -7.28 (7.2%), low -6.43 | 0 | **-9.69** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (2) | **+2.31** | -7.64 (13.3%), low -4.40 | 0 | **+4.61** | -15.27 (13.3%), low -8.81 | 0 | **+23.07** | -76.36 (13.3%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-3.45** | -3.95 (7.9%), low -3.95 | 0 | **-6.90** | -7.89 (7.9%), low -7.89 | 0 | **-34.52** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-8.28** | -9.40 (18.8%), low -9.40 | 0 | **-16.55** | -18.80 (18.8%), low -18.80 | 0 | **-82.75** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (0) | **-3.45** | -3.95 (7.9%), low -3.95 | 0 | **-6.90** | -7.89 (7.9%), low -7.89 | 0 | **-34.52** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (0) | **-8.28** | -9.40 (18.8%), low -9.40 | 0 | **-16.55** | -18.80 (18.8%), low -18.80 | 0 | **-82.75** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$98.06** | -1.94 | **+8.25** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.740369) | 4 (1) | 0 / 5 | 0 | $0.73 | **0** | 7.2% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$94.10** | -5.90 | **+4.29** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.392334) | 4 (1) | 0 / 5 | 0 | $1.76 | **0** | 17.1% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.06** | -1.94 | **+8.71** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.740369) | 4 (1) | 0 / 5 | 0 | $0.73 | **0** | 7.2% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+10.65** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+10.65** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+10.65** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$104.61** | +4.61 | **+15.60** | SHORT (1.165917 / 1.177576 / 1.148428 / 1.392334) | 4 (2) | 0 / 5 | 0 | $1.78 | **0** | 13.3% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$93.10** | -6.90 | **-1.93** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113034.201593) | 4 (0) | 0 / 5 | 0 | $0.74 | **0** | 7.9% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$83.45** | -16.55 | **-11.58** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 90431.959562) | 4 (0) | 0 / 5 | 0 | $1.80 | **0** | 18.8% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$93.10** | -6.90 | **-1.58** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113034.201593) | 4 (0) | 0 / 5 | 0 | $0.74 | **0** | 7.9% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.32** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.32** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.32** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$83.45** | -16.55 | **-10.92** | SHORT (75642.169995 / 76398.591695 / 74507.537445 / 90431.959562) | 4 (0) | 0 / 5 | 0 | $1.80 | **0** | 18.8% | — |
- Crowding XRPUSDT now: funding 0.0055%/8h, OI 24h 1.61%, long/short accounts 4.18 (96th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0013%/8h, OI 24h 0.79%, long/short accounts 2.96 (71th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->
