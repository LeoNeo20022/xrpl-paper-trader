# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-28T17:05:14+00:00**, XRPL XRP/RLUSD mid **$1.3128** (bid 1.3122 / ask 1.3135, node https://xrplcluster.com, ledger 107962466)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 3

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$100.71** | +0.71 | **-0.63** (-0.62%) | 17.5118 | $77.72 | 76.6821 | -0.66% | 2 | 0 | $0.00 (0.00032) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$100.25** | +0.25 | **-1.09** (-1.08%) | 3.3479 | $95.85 | 76.3244 | -1.12% | 3 | 1 | $0.00 (0.00026) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$100.25** | +0.25 | **-1.09** (-1.08%) | 3.1997 | $96.05 | 76.3223 | -1.13% | 3 | 1 | $0.00 (0.00026) | 3.2 |
| **Experiment total** (all 3) | $300 | **$301.21** | +1.21 | **-2.81** (-0.93%) | 24.0594 | $269.62 | 229.3288 | -0.97% | | | $0.01 (0.00084) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $101.34 | +1.34 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $304.02 | +4.02 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: -2.81 USD (-0.93%)** · XRP-equivalent: -0.97%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.000020 XRP per tx = max(0.00002, live open-ledger fee 1e-05) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.2725 1.2465 1.2205 1.1945 1.1686 (reference 1.29842, next refresh 2026-11-03T08:45:00+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.148117
- `scalp_2pct_rlusd`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **77.5841** | **+0.3924** (+0.51%) | +0.51% | $101.86 | +0.52 | 1 | 0 | $0.00 |
| `xrp_stacker_6pct` | 6% | **77.8086** | **+0.6169** (+0.80%) | +0.80% | $102.15 | +0.81 | 1 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $101.34 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **77.5841** | **+0.3924** (+0.51%) | $0.00 | 77.5841 (+0.51%) | $101.86 | +0.52 | 1 | +0.3925 | 0 (+0.0000) | $0.13 (0.00014) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $101.34 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.294829): sell 1.3466 sell 1.4005 sell 1.4565 sell 1.5148
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **77.8086** | **+0.6169** (+0.80%) | $0.00 | 77.8086 (+0.80%) | $102.15 | +0.81 | 1 | +0.6170 | 0 (+0.0000) | $0.13 (0.00014) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $101.34 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.294829): sell 1.3725 sell 1.4549 sell 1.5422 sell 1.6347
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$100.74** | +0.74 | 38.3730 | $50.37 | 76.7179 |
| Hold the same 50/50 (no pool) | $100.67 | +0.67 | 38.5793 | $50.02 | 76.6628 |
| Baseline: keep $100 in XRP | $101.34 | +1.34 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.072%** = impermanent loss -0.002% + fees earned ≈ +0.074% (pool fee 0.214%, pool share 0.002100%)
- LP vs keep $100 in XRP: **-0.60 USD** · XRP-equivalent: -0.61%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-10-28T17:05:17+00:00 at $1.3146 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$100.00** | +0.00 | **-0.89** | 0.00 (—) | — | 0/10 | 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| `lev_5x` (5x) | **$100.00** | +0.00 | **-0.89** | 0.00 (—) | — | 0/10 | 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| Baseline: keep $100 in XRP | $100.89 | +0.89 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-28T17:05:18+00:00 at $1.3146. 1h trend now: **up**, RSI(14) 43.66 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 1 (0) | **-1.27** | -1.53 (3.0%), low -1.27 | 0 | **-2.54** | -3.06 (3.0%), low -2.54 | 0 | **-12.72** | -15.28 (3.0%), low -12.72 | 0 |
| `lev_ta_5x` (5x) | FLAT | 1 (0) | **-3.18** | -3.81 (7.5%), low -3.18 | 0 | **-6.35** | -7.63 (7.5%), low -6.35 | 0 | **-31.76** | -38.14 (7.5%), low -31.76 | 0 |

Keep $50 / $100 / $500 in XRP: +0.78 / +1.56 / +7.78.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$97.46** | -2.54 | **-4.10** | FLAT | 1 (0) | 0 / 1 | $0.20 ($0.20 + $0.00) | **0** ($0.00) | 3.0% |
| `lev_ta_5x` (5x) | **$93.65** | -6.35 | **-7.91** | FLAT | 1 (0) | 0 / 1 | $0.50 ($0.50 + $0.00) | **0** ($0.00) | 7.5% |
| Baseline: keep $100 in XRP | $101.56 | +1.56 | — | | | | $0.05 | 0 | |

- Rules: 1h trend = EMA50 vs EMA200 + price vs EMA200. Uptrend: long when RSI(14) turns up from under 40 or MACD crosses up. Downtrend: short when RSI turns down from over 60 or MACD crosses down. Unclear trend: flat. Stop 1.5x ATR(14), target 3x ATR, one position at a time, whole balance as isolated margin. Costs: market entry/stop 0.05% taker + 0.05% slippage, target 0.02% maker, 8-hourly funding (longs pay / shorts receive when positive), liquidation at 0.5% maintenance. Backtest: `leverage/backtest_ta_output.txt`.
<!-- LEVERAGE-TA-END -->

<!-- COMMITTEE-BEGIN -->
## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)

Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie (stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). Every line runs at $100 plus $50 and $500 twins (`_50`, `_500`), isolated margin; `com_*_5x_quick` = 'get on base' 5x: take profit at +1.5% underlying (about +7.5% on margin; +1.5% backtested better than +1%, see `leverage/backtest_sizes_output.txt`), stop the tighter of 1% or 1.5x ATR; same costs/funding/liquidation as leverage_ta.

### $50 / $100 / $500 side by side (profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Started | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | FLAT | 1 (0) | **-0.86** | -0.86 (1.7%), low -0.86 | 0 | **-1.72** | -1.72 (1.7%), low -1.72 | 0 | **-8.58** | -8.58 (1.7%), low -8.58 | 0 |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | FLAT | 1 (0) | **-2.14** | -2.14 (4.3%), low -2.14 | 0 | **-4.28** | -4.28 (4.3%), low -4.28 | 0 | **-21.41** | -21.41 (4.3%), low -21.41 | 0 |
| `com_btc_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 1 (0) | **-0.86** | -0.86 (1.7%), low -0.86 | 0 | **-1.72** | -1.72 (1.7%), low -1.72 | 0 | **-8.58** | -8.58 (1.7%), low -8.58 | 0 |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_proxy_mix` | 2026-10-26T17:00:00+00:00 | FLAT | 0 (0) | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 | **+0.00** | -0.00 (0.0%), low +0.00 | 0 |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | FLAT | 1 (0) | **-2.14** | -2.14 (4.3%), low -2.14 | 0 | **-4.28** | -4.28 (4.3%), low -4.28 | 0 | **-21.41** | -21.41 (4.3%), low -21.41 | 0 |

### Details ($100 lines; the `_50` / `_500` twins hold the same positions at 0.5x / 5x the size)

| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$100.00** | +0.00 | **-1.90** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$100.00** | +0.00 | **-1.90** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-1.38** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-1.38** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-1.38** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-1.38** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "IDLE", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$100.00** | +0.00 | **-0.99** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$98.28** | -1.72 | **-2.42** | FLAT | 1 (0) | 0 / 1 | 0 | $0.20 | **0** | 1.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$95.72** | -4.28 | **-4.98** | FLAT | 1 (0) | 0 / 1 | 0 | $0.50 | **0** | 4.3% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$98.28** | -1.72 | **-2.04** | FLAT | 1 (0) | 0 / 1 | 0 | $0.20 | **0** | 1.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-0.33** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-0.33** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **-0.33** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "IDLE"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$95.72** | -4.28 | **-4.28** | FLAT | 1 (0) | 0 / 1 | 0 | $0.50 | **0** | 4.3% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "SHORT", "chart_reader": "IDLE"} |
- Crowding XRPUSDT now: funding 0.01%/8h, OI 24h 1.1%, long/short accounts 3.37 (35th pct of 7d), Fear & Greed 51 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0066%/8h, OI 24h -2.07%, long/short accounts 2.05 (23th pct of 7d), Fear & Greed 51 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-10-28T17:05:26+00:00 at $1.3146. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **+0.00** | **+0.00** (-4.00 vs $4) | -0.00 (0.0%) | 0 (—) | 0 | 0 | 0 (FLAT) | $0.00 / $+0.00 | 0 | -10.88 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **+0.00** | **+0.00** (-4.00 vs $4) | -0.00 (0.0%) | 0 (—) | 0 | 0 | 0 (FLAT) | $0.00 / $+0.00 | 0 | -10.88 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->

<!-- SIZES:BEGIN -->
## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)

$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth (pool 1,827,220 XRP / 2,398,276 RLUSD from https://xrplcluster.com). Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.

| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |
|---|---|---|---|---|---|
| `dip_ladder` | **+0.71** | -0.70 | **+3.55** | -3.48 | $0.0032 (2 fills) |
| `scalp_2pct` | **+0.25** | -0.54 | **+1.25** | -2.68 | $0.0017 (3 fills) |
| `scalp_2pct_rlusd` | **+0.25** | -0.54 | **+1.23** | -2.68 | $0.0017 (3 fills) |
| `xrp_stacker` | **+1.86** | -3.08 | **+9.19** | -15.40 | $0.0872 (3 fills) |
| `xrp_stacker_6pct` | **+2.15** | -3.09 | **+10.66** | -15.45 | $0.0874 (3 fills) |
| `amm_lp` | **+0.74** | -1.53 | **+3.72** | -7.63 | $0.0000 (0 fills) |
| `lev_2x` | **+0.00** | -0.00 | **+0.00** | -0.00 | $0.0000 (0 fills) |
| `lev_5x` | **+0.00** | -0.00 | **+0.00** | -0.00 | $0.0000 (0 fills) |

Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.
<!-- SIZES:END -->
