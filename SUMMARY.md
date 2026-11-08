# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-11-08T21:46:20+00:00**, XRPL XRP/RLUSD mid **$1.1431** (bid 1.1425 / ask 1.1436, node https://xrplcluster.com, ledger 108204505)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 2

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$92.91** | -7.09 | **+4.67** (+5.30%) | 75.8419 | $6.22 | 81.2786 | +5.29% | 9 | 0 | $0.05 (0.04137) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$97.55** | -2.45 | **+9.32** (+10.56%) | 51.7982 | $38.34 | 85.3243 | +10.54% | 19 | 6 | $0.01 (0.00570) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$97.67** | -2.33 | **+9.43** (+10.69%) | 50.8943 | $39.49 | 85.4263 | +10.67% | 19 | 6 | $0.01 (0.00570) | 3.2 |
| **Experiment total** (all 3) | $300 | **$288.13** | -11.87 | **+23.42** (+8.85%) | 178.5344 | $84.05 | 252.0292 | +8.83% | | | $0.07 (0.05277) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $88.24 | -11.76 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $264.71 | -35.29 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: +23.42 USD (+8.85%)** · XRP-equivalent: +8.83%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.000020 XRP per tx = max(0.00002, live open-ledger fee 1e-05) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.1253 (reference 1.25033, next refresh 2026-11-10T08:45:00+00:00)
- `scalp_2pct`: 4 buy orders waiting, 6 sell orders waiting, XRP kept from scalps 0.903875
- `scalp_2pct_rlusd`: 4 buy orders waiting, 6 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **78.3679** | **+1.1762** (+1.52%) | +1.52% | $89.58 | +1.34 | 3 | 0 | $-0.00 |
| `xrp_stacker_6pct` | 6% | **78.4205** | **+1.2288** (+1.59%) | +1.59% | $89.64 | +1.40 | 2 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $88.24 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **78.3679** | **+1.1762** (+1.52%) | $-0.00 | 78.3679 (+1.52%) | $89.58 | +1.34 | 3 | +1.1716 | 0 (+0.0000) | $0.28 (0.00559) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $88.24 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.17967): sell 1.2269 sell 1.2759 sell 1.3270 sell 1.3800
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **78.4205** | **+1.2288** (+1.59%) | $0.00 | 78.4205 (+1.59%) | $89.64 | +1.40 | 2 | +1.2191 | 0 (+0.0000) | $0.21 (0.01032) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $88.24 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.20913): sell 1.2817 sell 1.3586 sell 1.4401 sell 1.5265
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$94.12** | -5.88 | 41.1640 | $47.07 | 82.3198 |
| Hold the same 50/50 (no pool) | $94.12 | -5.88 | 38.5793 | $50.02 | 82.3191 |
| Baseline: keep $100 in XRP | $88.24 | -11.76 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **-0.001%** = impermanent loss -0.197% + fees earned ≈ +0.197% (pool fee 0.308%, pool share 0.002104%)
- LP vs keep $100 in XRP: **+5.89 USD** · XRP-equivalent: +6.64%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-11-08T21:46:23+00:00 at $1.1443 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$95.78** | -4.22 | **+7.97** | 98.95 (1.20242) | 0.60466 | 6/10 | 7 | $0.13 ($0.08 + $0.04) | **0** ($0.00) | 6.8% |
| `lev_5x` (5x) | **$89.46** | -10.54 | **+1.65** | 247.37 (1.20242) | 0.9672 | 6/10 | 7 | $0.31 ($0.20 + $0.11) | **0** ($0.00) | 16.3% |
| Baseline: keep $100 in XRP | $87.82 | -12.18 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-08T21:46:24+00:00 at $1.1443. 1h trend now: **down**, RSI(14) 38.65 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | SHORT | 8 (1) | **-4.59** | -6.24 (12.4%), low -5.99 | 0 | **-9.19** | -12.49 (12.4%), low -11.98 | 0 | **-45.94** | -62.44 (12.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | SHORT | 8 (1) | **-11.15** | -14.70 (29.0%), low -14.07 | 0 | **-22.31** | -29.41 (29.0%), low -28.13 | 0 | **-111.54** | -147.03 (29.0%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -5.80 / -11.60 / -58.00.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$90.81** | -9.19 | **+2.41** | SHORT (1.15482 / 1.16512 / 1.13422 / 1.72362) | 8 (1) | 2 / 7 | $1.57 ($1.58 + $-0.01) | **0** ($0.00) | 12.4% |
| `lev_ta_5x` (5x) | **$77.69** | -22.31 | **-10.71** | SHORT (1.15482 / 1.16512 / 1.13422 / 1.37889) | 8 (1) | 2 / 7 | $3.68 ($3.70 + $-0.02) | **0** ($0.00) | 29.0% |
| Baseline: keep $100 in XRP | $88.40 | -11.60 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->

<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (1) | **+0.22** | -3.64 (7.2%), low -3.22 | 0 | **+0.44** | -7.28 (7.2%), low -6.43 | 0 | **+2.22** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (1) | **-0.14** | -8.71 (17.1%), low -7.79 | 0 | **-0.28** | -17.41 (17.1%), low -15.58 | 0 | **-1.39** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (1) | **+0.22** | -3.64 (7.2%), low -3.22 | 0 | **+0.44** | -7.28 (7.2%), low -6.43 | 0 | **+2.22** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 5 (3) | **+4.78** | -7.64 (13.3%), low -4.40 | 0 | **+9.56** | -15.27 (13.3%), low -8.81 | 0 | **+47.81** | -76.36 (13.3%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-2.96** | -3.95 (7.9%), low -3.95 | 0 | **-5.92** | -7.89 (7.9%), low -7.89 | 0 | **-29.58** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | SHORT | 4 (0) | **-7.15** | -9.40 (18.8%), low -9.40 | 0 | **-14.30** | -18.80 (18.8%), low -18.80 | 0 | **-71.48** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | SHORT | 4 (0) | **-2.96** | -3.95 (7.9%), low -3.95 | 0 | **-5.92** | -7.89 (7.9%), low -7.89 | 0 | **-29.58** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | SHORT | 4 (0) | **-7.15** | -9.40 (18.8%), low -9.40 | 0 | **-14.30** | -18.80 (18.8%), low -18.80 | 0 | **-71.48** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$100.44** | +0.44 | **+11.74** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.740369) | 4 (1) | 0 / 5 | 0 | $0.73 | **0** | 7.2% | — |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$99.72** | -0.28 | **+11.02** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.392334) | 4 (1) | 0 / 5 | 0 | $1.76 | **0** | 17.1% | — |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.44** | +0.44 | **+12.19** | SHORT (1.165917 / 1.180672 / 1.136407 / 1.740369) | 4 (1) | 0 / 5 | 0 | $0.73 | **0** | 7.2% | — |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.75** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.75** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.75** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$109.56** | +9.56 | **+21.65** | SHORT (1.146227 / 1.156632 / 1.129033 / 1.368629) | 5 (3) | 0 / 6 | 0 | $2.15 | **0** | 13.3% | — |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$94.08** | -5.92 | **-0.45** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113034.201593) | 4 (0) | 0 / 5 | 0 | $0.74 | **0** | 7.9% | — |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$85.70** | -14.30 | **-8.83** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 90431.959562) | 4 (0) | 0 / 5 | 0 | $1.80 | **0** | 18.8% | — |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$94.08** | -5.92 | **-0.10** | SHORT (75642.169995 / 76463.101563 / 74000.306858 / 113034.201593) | 4 (0) | 0 / 5 | 0 | $0.74 | **0** | 7.9% | — |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.82** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.82** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+5.82** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | — |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$85.70** | -14.30 | **-8.17** | SHORT (75642.169995 / 76398.591695 / 74507.537445 / 90431.959562) | 4 (0) | 0 / 5 | 0 | $1.80 | **0** | 18.8% | — |
- Crowding XRPUSDT now: funding 0.0055%/8h, OI 24h 2.07%, long/short accounts 4.12 (89th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0013%/8h, OI 24h 1.02%, long/short accounts 2.95 (66th pct of 7d), Fear & Greed 28 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-11-08T21:46:32+00:00 at $1.1443. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **+44.91** | **+3.42** (-0.58 vs $4) | -48.31 (4.6%) | 5 (60%) | 0 | 5 (60% wins) +42.95 | 3 SHORT @ 1.146227 (stop 1.156632, TP 1.129033, liq 1.573932) | $0.37 / $-0.71 | 0 | +164.98 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **+72.21** | **+5.49** (+1.49 vs $4) | -80.51 (7.4%) | 5 (60%) | 0 | 5 (60% wins) +68.94 | 5 SHORT @ 1.146227 (stop 1.156632, TP 1.129033, liq 1.34511) | $0.58 / $-1.09 | 0 | +192.28 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->

<!-- SIZES:BEGIN -->
## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)

$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth (pool 1,956,712 XRP / 2,237,318 RLUSD from https://xrplcluster.com). Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.

| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |
|---|---|---|---|---|---|
| `dip_ladder` | **-7.09** | -11.38 | **-35.46** | -56.88 | $0.0113 (9 fills) |
| `scalp_2pct` | **-2.45** | -3.77 | **-12.26** | -18.84 | $0.0149 (19 fills) |
| `scalp_2pct_rlusd` | **-2.33** | -3.60 | **-11.68** | -17.98 | $0.0151 (19 fills) |
| `xrp_stacker` | **-10.42** | -14.46 | **-52.20** | -72.31 | $0.1013 (7 fills) |
| `xrp_stacker_6pct` | **-10.36** | -14.70 | **-51.90** | -73.52 | $0.0975 (5 fills) |
| `amm_lp` | **-5.88** | -7.70 | **-29.40** | -38.48 | $0.0000 (0 fills) |
| `lev_2x` | **-4.22** | -6.57 | **-21.08** | -32.83 | $0.0000 (0 fills) |
| `lev_5x` | **-10.54** | -16.42 | **-52.69** | -82.08 | $0.0000 (0 fills) |

Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.
<!-- SIZES:END -->
