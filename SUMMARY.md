# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-29T22:37:17+00:00**, XRPL XRP/RLUSD mid **$1.2508** (bid 1.2501 / ask 1.2514, node https://xrplcluster.com, ledger 107988948)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 2

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$99.41** | -0.59 | **+2.86** (+2.97%) | 42.1978 | $46.63 | 79.4622 | +2.94% | 4 | 0 | $0.00 (0.00036) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$99.96** | -0.04 | **+3.41** (+3.53%) | 18.6099 | $76.68 | 79.8891 | +3.49% | 5 | 1 | $0.00 (0.00030) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$99.97** | -0.03 | **+3.42** (+3.54%) | 18.4618 | $76.88 | 79.8942 | +3.50% | 5 | 1 | $0.00 (0.00030) | 3.2 |
| **Experiment total** (all 3) | $300 | **$299.34** | -0.66 | **+9.69** (+3.35%) | 79.2694 | $200.19 | 239.2456 | +3.31% | | | $0.01 (0.00096) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $96.55 | -3.45 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $289.64 | -10.36 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: +9.69 USD (+3.35%)** · XRP-equivalent: +3.31%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.000020 XRP per tx = max(0.00002, live open-ledger fee 1e-05) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.2205 1.1945 1.1686 (reference 1.29842, next refresh 2026-11-03T08:45:00+00:00)
- `scalp_2pct`: 8 buy orders waiting, 2 sell orders waiting, XRP kept from scalps 0.148117
- `scalp_2pct_rlusd`: 8 buy orders waiting, 2 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **77.5839** | **+0.3923** (+0.51%) | +0.51% | $97.04 | +0.49 | 1 | 0 | $0.00 |
| `xrp_stacker_6pct` | 6% | **77.8086** | **+0.6169** (+0.80%) | +0.80% | $97.32 | +0.77 | 1 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $96.55 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **77.5839** | **+0.3923** (+0.51%) | $0.00 | 77.5839 (+0.51%) | $97.04 | +0.49 | 1 | +0.3925 | 0 (+0.0000) | $0.13 (0.00030) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $96.55 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.23045): sell 1.2797 sell 1.3309 sell 1.3841 sell 1.4395
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **77.8086** | **+0.6169** (+0.80%) | $0.00 | 77.8086 (+0.80%) | $97.32 | +0.77 | 1 | +0.6170 | 0 (+0.0000) | $0.13 (0.00014) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $96.55 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.294829): sell 1.3725 sell 1.4549 sell 1.5422 sell 1.6347
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$98.35** | -1.65 | 39.3428 | $49.15 | 78.6155 |
| Hold the same 50/50 (no pool) | $98.28 | -1.72 | 38.5793 | $50.02 | 78.5532 |
| Baseline: keep $100 in XRP | $96.55 | -3.45 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.079%** = impermanent loss -0.017% + fees earned ≈ +0.096% (pool fee 0.214%, pool share 0.002100%)
- LP vs keep $100 in XRP: **+1.81 USD** · XRP-equivalent: +1.84%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-10-29T22:37:20+00:00 at $1.2506 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$99.94** | -0.06 | **+3.96** | 31.66 (1.25066) | 0.62847 | 2/10 | 1 | $0.02 ($0.02 + $0.00) | **0** ($0.00) | 1.5% |
| `lev_5x` (5x) | **$99.84** | -0.16 | **+3.87** | 79.15 (1.25066) | 1.00555 | 2/10 | 1 | $0.04 ($0.04 + $0.00) | **0** ($0.00) | 3.6% |
| Baseline: keep $100 in XRP | $95.97 | -4.03 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-29T22:37:21+00:00 at $1.2506. 1h trend now: **down**, RSI(14) 32.73 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 3 (1) | **-0.19** | -3.03 (6.0%), low -2.78 | 0 | **-0.39** | -6.07 (6.0%), low -5.56 | 0 | **-1.93** | -30.33 (6.0%), low -27.78 | 0 |
| `lev_ta_5x` (5x) | FLAT | 3 (1) | **-0.81** | -7.40 (14.6%), low -6.77 | 0 | **-1.63** | -14.81 (14.6%), low -13.53 | 0 | **-8.14** | -74.03 (14.6%), low -67.66 | 0 |

Keep $50 / $100 / $500 in XRP: -1.69 / -3.39 / -16.94.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$99.61** | -0.39 | **+3.00** | FLAT | 3 (1) | 1 / 2 | $0.55 ($0.53 + $0.02) | **0** ($0.00) | 6.0% |
| `lev_ta_5x` (5x) | **$98.37** | -1.63 | **+1.76** | FLAT | 3 (1) | 1 / 2 | $1.32 ($1.27 + $0.05) | **0** ($0.00) | 14.6% |
| Baseline: keep $100 in XRP | $96.61 | -3.39 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->

<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 1 (0) | **-1.19** | -1.36 (2.7%), low -1.19 | 0 | **-2.38** | -2.72 (2.7%), low -2.38 | 0 | **-11.91** | -13.60 (2.7%), low -11.91 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 1 (0) | **-2.97** | -3.39 (6.7%), low -2.97 | 0 | **-5.95** | -6.79 (6.7%), low -5.95 | 0 | **-29.74** | -33.94 (6.7%), low -29.74 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 1 (0) | **-1.19** | -1.36 (2.7%), low -1.19 | 0 | **-2.38** | -2.72 (2.7%), low -2.38 | 0 | **-11.91** | -13.60 (2.7%), low -11.91 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 1 (0) | **-2.85** | -3.27 (6.5%), low -2.85 | 0 | **-5.69** | -6.53 (6.5%), low -5.69 | 0 | **-28.45** | -32.65 (6.5%), low -28.45 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 2 (0) | **-1.03** | -1.34 (2.7%), low -1.34 | 0 | **-2.06** | -2.67 (2.7%), low -2.67 | 0 | **-10.30** | -13.37 (2.7%), low -13.37 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 2 (0) | **-2.56** | -3.31 (6.6%), low -3.31 | 0 | **-5.12** | -6.61 (6.6%), low -6.61 | 0 | **-25.60** | -33.07 (6.6%), low -33.07 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 2 (0) | **-1.03** | -1.34 (2.7%), low -1.34 | 0 | **-2.06** | -2.67 (2.7%), low -2.67 | 0 | **-10.30** | -13.37 (2.7%), low -13.37 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 2 (0) | **-2.56** | -3.31 (6.6%), low -3.31 | 0 | **-5.12** | -6.61 (6.6%), low -6.61 | 0 | **-25.60** | -33.07 (6.6%), low -33.07 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$97.62** | -2.38 | **+0.67** | FLAT | 1 (0) | 0 / 1 | 0 | $0.18 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$94.05** | -5.95 | **-2.89** | FLAT | 1 (0) | 0 / 1 | 0 | $0.45 | **0** | 6.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.62** | -2.38 | **+1.17** | FLAT | 1 (0) | 0 / 1 | 0 | $0.18 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.55** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$94.31** | -5.69 | **-1.77** | FLAT | 1 (0) | 0 / 1 | 0 | $0.45 | **0** | 6.5% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$97.94** | -2.06 | **-0.92** | FLAT | 2 (0) | 0 / 2 | 0 | $0.40 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$94.88** | -5.12 | **-3.98** | FLAT | 2 (0) | 0 / 2 | 0 | $0.98 | **0** | 6.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.94** | -2.06 | **-0.56** | FLAT | 2 (0) | 0 / 2 | 0 | $0.40 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+1.50** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+1.50** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+1.50** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$94.88** | -5.12 | **-3.30** | FLAT | 2 (0) | 0 / 2 | 0 | $0.98 | **0** | 6.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding 0.01%/8h, OI 24h 3.31%, long/short accounts 4.15 (99th pct of 7d), Fear & Greed 51 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0096%/8h, OI 24h 6.45%, long/short accounts 2.12 (32th pct of 7d), Fear & Greed 51 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-10-29T22:37:29+00:00 at $1.2506. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **-20.42** | **-6.42** (-10.42 vs $4) | -25.60 (2.5%) | 1 (0%) | 0 | 1 (0% wins) -20.42 | 0 (FLAT) | $0.07 / $-0.20 | 0 | +17.91 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **-27.23** | **-8.56** (-12.56 vs $4) | -34.14 (3.4%) | 1 (0%) | 0 | 1 (0% wins) -27.23 | 0 (FLAT) | $0.09 / $-0.26 | 0 | +11.10 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->

<!-- SIZES:BEGIN -->
## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)

$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth (pool 1,873,393 XRP / 2,340,147 RLUSD from https://xrplcluster.com). Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.

| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |
|---|---|---|---|---|---|
| `dip_ladder` | **-0.59** | -2.07 | **-2.95** | -10.36 | $0.0074 (4 fills) |
| `scalp_2pct` | **-0.04** | -0.54 | **-0.20** | -2.68 | $0.0033 (5 fills) |
| `scalp_2pct_rlusd` | **-0.03** | -0.54 | **-0.17** | -2.68 | $0.0033 (5 fills) |
| `xrp_stacker` | **-2.96** | -7.52 | **-14.90** | -37.59 | $0.0894 (3 fills) |
| `xrp_stacker_6pct` | **-2.68** | -7.54 | **-13.49** | -37.70 | $0.0896 (3 fills) |
| `amm_lp` | **-1.65** | -3.73 | **-8.23** | -18.64 | $0.0000 (0 fills) |
| `lev_2x` | **-0.06** | -0.61 | **-0.32** | -3.03 | $0.0000 (0 fills) |
| `lev_5x` | **-0.16** | -1.52 | **-0.79** | -7.58 | $0.0000 (0 fills) |

Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.
<!-- SIZES:END -->
