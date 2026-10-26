# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-26T15:46:00+00:00**, XRPL XRP/RLUSD mid **$1.3009** (bid 1.3003 / ask 1.3015, node https://xrplcluster.com, ledger 107918168)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 2

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$100.50** | +0.50 | **+0.08** (+0.08%) | 17.5119 | $77.72 | 77.2258 | +0.04% | 2 | 0 | $0.00 (0.00014) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$100.21** | +0.21 | **-0.21** (-0.21%) | 3.3479 | $95.85 | 76.9948 | -0.26% | 3 | 1 | $0.00 (0.00026) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$100.21** | +0.21 | **-0.21** (-0.21%) | 3.1997 | $96.05 | 76.9940 | -0.26% | 3 | 1 | $0.00 (0.00026) | 3.2 |
| **Experiment total** (all 3) | $300 | **$300.92** | +0.92 | **-0.33** (-0.11%) | 24.0595 | $269.62 | 231.2145 | -0.16% | | | $0.01 (0.00066) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $100.42 | +0.42 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $301.25 | +1.25 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: -0.33 USD (-0.11%)** · XRP-equivalent: -0.16%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.005081 XRP per tx = max(0.00002, live open-ledger fee 0.005081) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.2430 1.2171 1.1912 1.1653 (reference 1.294829, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.148117
- `scalp_2pct_rlusd`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **77.5841** | **+0.3924** (+0.51%) | +0.51% | $100.93 | +0.51 | 1 | 0 | $0.00 |
| `xrp_stacker_6pct` | 6% | **77.8086** | **+0.6169** (+0.80%) | +0.80% | $101.22 | +0.80 | 1 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $100.42 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **77.5841** | **+0.3924** (+0.51%) | $0.00 | 77.5841 (+0.51%) | $100.93 | +0.51 | 1 | +0.3925 | 0 (+0.0000) | $0.13 (0.00014) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $100.42 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.294829): sell 1.3466 sell 1.4005 sell 1.4565 sell 1.5148
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **77.8086** | **+0.6169** (+0.80%) | $0.00 | 77.8086 (+0.80%) | $101.22 | +0.80 | 1 | +0.6170 | 0 (+0.0000) | $0.13 (0.00014) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $100.42 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.294829): sell 1.3725 sell 1.4549 sell 1.5422 sell 1.6347
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$100.27** | +0.27 | 38.5237 | $50.16 | 77.0594 |
| Hold the same 50/50 (no pool) | $100.21 | +0.21 | 38.5793 | $50.02 | 77.0126 |
| Baseline: keep $100 in XRP | $100.42 | +0.42 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.061%** = impermanent loss -0.000% + fees earned ≈ +0.061% (pool fee 0.214%, pool share 0.002101%)
- LP vs keep $100 in XRP: **-0.15 USD** · XRP-equivalent: -0.17%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-10-26T15:46:02+00:00 at $1.3024 (prices: `binance_spot_data_api`, funding: `none needed`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$100.00** | +0.00 | **+0.05** | 0.00 (—) | — | 0/10 | 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| `lev_5x` (5x) | **$100.00** | +0.00 | **+0.05** | 0.00 (—) | — | 0/10 | 0 | $0.00 ($0.00 + $0.00) | **0** ($0.00) | 0.0% |
| Baseline: keep $100 in XRP | $99.95 | -0.05 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->
