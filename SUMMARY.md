# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-11-13T00:26:56+00:00**, XRPL XRP/RLUSD mid **$1.0388** (bid 1.0384 / ask 1.0391, node https://xrplcluster.com, ledger 108292653)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 3

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$84.52** | -15.48 | **+4.33** (+5.40%) | 81.3620 | $0.00 | 81.3620 | +5.40% | 10 | 0 | $0.05 (0.04663) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$90.68** | -9.32 | **+10.50** (+13.09%) | 87.2950 | $0.00 | 87.2950 | +13.09% | 27 | 8 | $0.02 (0.02174) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$90.92** | -9.08 | **+10.73** (+13.38%) | 86.0464 | $1.53 | 87.5221 | +13.38% | 27 | 8 | $0.02 (0.02174) | 3.2 |
| **Experiment total** (all 3) | $300 | **$266.11** | -33.89 | **+25.56** (+10.62%) | 254.7033 | $1.53 | 256.1790 | +10.62% | | | $0.10 (0.09011) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $80.18 | -19.82 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $240.55 | -59.45 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: +25.56 USD (+10.62%)** · XRP-equivalent: +10.62%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.000020 XRP per tx = max(0.00002, live open-ledger fee 1e-05) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: none (reference 1.08488, next refresh 2026-11-17T08:45:00+00:00)
- `scalp_2pct`: 0 buy orders waiting, 10 sell orders waiting, XRP kept from scalps 1.24859
- `scalp_2pct_rlusd`: 0 buy orders waiting, 10 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **78.7183** | **+1.5266** (+1.98%) | +1.98% | $81.77 | +1.59 | 4 | 0 | $-0.00 |
| `xrp_stacker_6pct` | 6% | **78.3782** | **+1.1865** (+1.54%) | +1.54% | $81.42 | +1.23 | 2 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $80.18 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **78.7183** | **+1.5266** (+1.98%) | $-0.00 | 78.7183 (+1.98%) | $81.77 | +1.59 | 4 | +1.5588 | 0 (+0.0000) | $0.39 (0.05370) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $80.18 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.03015): sell 1.0714 sell 1.1142 sell 1.1588 sell 1.2051
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **78.3782** | **+1.1865** (+1.54%) | $0.00 | 78.3782 (+1.54%) | $81.42 | +1.23 | 2 | +1.2191 | 0 (+0.0000) | $0.25 (0.05259) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $80.18 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.04899): sell 1.1119 sell 1.1786 sell 1.2494 sell 1.3243
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$89.82** | -10.18 | 43.2091 | $44.93 | 86.4434 |
| Hold the same 50/50 (no pool) | $90.10 | -9.90 | 38.5793 | $50.02 | 86.7109 |
| Baseline: keep $100 in XRP | $80.18 | -19.82 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **-0.311%** = impermanent loss -0.606% + fees earned ≈ +0.296% (pool fee 0.315%, pool share 0.002282%)
- LP vs keep $100 in XRP: **+9.63 USD** · XRP-equivalent: +11.98%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-11-13T00:26:58+00:00 at $1.0392 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$81.75** | -18.25 | **+2.00** | 171.90 (1.14194) | 0.57487 | 10/10 | 9 | $0.30 ($0.11 + $0.19) | **0** ($0.00) | 24.0% |
| `lev_5x` (5x) | **$54.38** | -45.62 | **-25.37** | 429.75 (1.14194) | 0.91918 | 10/10 | 9 | $0.76 ($0.28 + $0.48) | **0** ($0.00) | 57.9% |
| Baseline: keep $100 in XRP | $79.75 | -20.25 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-11-13T00:27:00+00:00 at $1.0392. 1h trend now: **down**, RSI(14) 49.75 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 12 (4) | **+0.37** | -6.24 (12.4%), low -5.99 | 0 | **+0.75** | -12.49 (12.4%), low -11.98 | 0 | **+3.75** | -62.44 (12.4%), low -59.88 | 0 |
| `lev_ta_5x` (5x) | FLAT | 12 (4) | **-0.59** | -14.70 (29.0%), low -14.07 | 0 | **-1.18** | -29.41 (29.0%), low -28.13 | 0 | **-5.89** | -147.03 (29.0%), low -140.66 | 0 |

Keep $50 / $100 / $500 in XRP: -9.86 / -19.72 / -98.59.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$100.75** | +0.75 | **+20.47** | FLAT | 12 (4) | 2 / 10 | $2.02 ($2.07 + $-0.05) | **0** ($0.00) | 12.4% |
| `lev_ta_5x` (5x) | **$98.82** | -1.18 | **+18.54** | FLAT | 12 (4) | 2 / 10 | $4.71 ($4.82 + $-0.11) | **0** ($0.00) | 29.0% |
| Baseline: keep $100 in XRP | $80.28 | -19.72 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->

<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 8 (3) | **+1.55** | -3.64 (7.2%), low -3.22 | 0 | **+3.09** | -7.28 (7.2%), low -6.43 | 0 | **+15.45** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 8 (3) | **+2.20** | -8.71 (17.1%), low -7.79 | 0 | **+4.40** | -17.41 (17.1%), low -15.58 | 0 | **+22.02** | -87.07 (17.1%), low -77.91 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 8 (3) | **+1.55** | -3.64 (7.2%), low -3.22 | 0 | **+3.09** | -7.28 (7.2%), low -6.43 | 0 | **+15.45** | -36.42 (7.2%), low -32.16 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 12 (7) | **+10.45** | -8.47 (13.7%), low -4.40 | 0 | **+20.89** | -16.94 (13.7%), low -8.81 | 0 | **+104.46** | -84.71 (13.7%), low -44.05 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 7 (1) | **-3.31** | -3.95 (7.9%), low -3.95 | 0 | **-6.62** | -7.89 (7.9%), low -7.89 | 0 | **-33.10** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 7 (1) | **-8.18** | -9.40 (18.8%), low -9.40 | 0 | **-16.36** | -18.80 (18.8%), low -18.80 | 0 | **-81.79** | -94.02 (18.8%), low -94.02 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 7 (1) | **-3.31** | -3.95 (7.9%), low -3.95 | 0 | **-6.62** | -7.89 (7.9%), low -7.89 | 0 | **-33.10** | -39.47 (7.9%), low -39.47 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 7 (1) | **-8.95** | -9.40 (18.8%), low -9.40 | 0 | **-17.90** | -18.80 (18.8%), low -18.80 | 0 | **-89.52** | -94.02 (18.8%), low -94.02 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$103.09** | +3.09 | **+22.54** | FLAT | 8 (3) | 0 / 8 | 0 | $1.23 | **0** | 7.2% | {"long_scout": "LONG", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$104.40** | +4.40 | **+23.85** | FLAT | 8 (3) | 0 / 8 | 0 | $3.04 | **0** | 17.1% | {"long_scout": "LONG", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$103.09** | +3.09 | **+22.95** | FLAT | 8 (3) | 0 / 8 | 0 | $1.23 | **0** | 7.2% | {"long_scout": "LONG", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+19.85** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+19.85** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+19.85** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$120.89** | +20.89 | **+41.05** | FLAT | 12 (7) | 0 / 12 | 0 | $5.09 | **0** | 13.7% | {"long_scout": "LONG", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$93.38** | -6.62 | **+4.14** | FLAT | 7 (1) | 0 / 7 | 0 | $1.13 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$83.64** | -16.36 | **-5.59** | FLAT | 7 (1) | 0 / 7 | 0 | $2.70 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$93.38** | -6.62 | **+4.47** | FLAT | 7 (1) | 0 / 7 | 0 | $1.13 | **0** | 7.9% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.09** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.09** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+11.09** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$82.10** | -17.90 | **-6.52** | FLAT | 7 (1) | 0 / 7 | 0 | $2.68 | **0** | 18.8% | {"long_scout": "IDLE", "short_scout": "SHORT", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding 0.01%/8h, OI 24h 8.15%, long/short accounts 3.54 (1th pct of 7d), Fear & Greed 28 -> **shorts** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.01%/8h, OI 24h 6.18%, long/short accounts 3.27 (98th pct of 7d), Fear & Greed 28 -> **longs** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-11-13T00:27:08+00:00 at $1.0392. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **+86.48** | **+5.01** (+1.01 vs $4) | -56.84 (5.2%) | 12 (58%) | 0 | 12 (58% wins) +86.48 | 0 (FLAT) | $0.88 / $-1.13 | 0 | +287.37 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **+153.92** | **+8.92** (+4.92 vs $4) | -89.71 (7.7%) | 12 (58%) | 0 | 12 (58% wins) +153.92 | 0 (FLAT) | $1.45 / $-1.72 | 0 | +354.81 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->

<!-- SIZES:BEGIN -->
## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)

$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth (pool 1,893,493 XRP / 1,969,030 RLUSD from https://xrplcluster.com). Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.

| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |
|---|---|---|---|---|---|
| `dip_ladder` | **-15.48** | -21.39 | **-77.43** | -106.97 | $0.0132 (10 fills) |
| `scalp_2pct` | **-9.32** | -12.38 | **-46.63** | -61.91 | $0.0244 (27 fills) |
| `scalp_2pct_rlusd` | **-9.08** | -12.07 | **-45.45** | -60.33 | $0.0247 (27 fills) |
| `xrp_stacker` | **-18.23** | -23.84 | **-91.27** | -119.22 | $0.1182 (9 fills) |
| `xrp_stacker_6pct` | **-18.58** | -24.49 | **-93.03** | -122.45 | $0.1107 (5 fills) |
| `amm_lp` | **-10.18** | -12.87 | **-50.91** | -64.37 | $0.0000 (0 fills) |
| `lev_2x` | **-18.25** | -23.82 | **-91.23** | -119.08 | $0.0000 (0 fills) |
| `lev_5x` | **-45.62** | -59.54 | **-228.08** | -297.71 | $0.0000 (0 fills) |

Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.
<!-- SIZES:END -->
