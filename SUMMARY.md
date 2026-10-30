# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-30T11:45:18+00:00**, XRPL XRP/RLUSD mid **$1.2463** (bid 1.2460 / ask 1.2465, node https://xrplcluster.com, ledger 108000851)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 3

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$99.55** | -0.45 | **+3.35** (+3.48%) | 54.9334 | $31.09 | 79.8656 | +3.46% | 5 | 0 | $0.00 (0.00038) | 2.2 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$100.25** | +0.25 | **+4.05** (+4.21%) | 18.9100 | $76.68 | 80.4095 | +4.17% | 9 | 3 | $0.01 (0.00550) | 3.2 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$100.26** | +0.26 | **+4.06** (+4.22%) | 18.4566 | $77.26 | 80.4173 | +4.18% | 9 | 3 | $0.01 (0.00550) | 3.2 |
| **Experiment total** (all 3) | $300 | **$300.06** | +0.06 | **+11.46** (+3.97%) | 92.3000 | $185.03 | 240.6924 | +3.94% | | | $0.02 (0.01138) | 8.6 |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $96.20 | -3.80 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 | $0.05 | — |
| Baseline for the total: keep $300 in XRP | $300 | $288.61 | -11.39 | — | 231.5750 | $0.00 | 231.5750 | — | | | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: +11.46 USD (+3.97%)** · XRP-equivalent: +3.94%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

**All values and P/L are after fees.** Fees paid = taker/AMM cost on market buys + XRPL network fee on every transaction, as if each were a plain OfferCreate/OfferCancel/TrustSet/AMMDeposit signed in Xaman. Network fee this tick: 0.005041 XRP per tx = max(0.00002, live open-ledger fee 0.005041) capped at 0.01. Grid limit orders fill at their limit price (maker, no AMM fee). Before Oct 24 fills paid 0.00001 XRP; the TrustSet and initial-ladder OfferCreates were charged once on Oct 24 (catch-up), dip-ladder refresh cancels/creates from then on. Reserve locked = 1 XRP base + 0.2 per trust line/offer, held by the ledger (not spent). **Not included:** Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades (see README).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.1945 1.1686 (reference 1.29842, next refresh 2026-11-03T08:45:00+00:00)
- `scalp_2pct`: 8 buy orders waiting, 2 sell orders waiting, XRP kept from scalps 0.45348
- `scalp_2pct_rlusd`: 8 buy orders waiting, 2 sell orders waiting, XRP kept from scalps 0.0

## XRP stacker side by side (separate $100 lines, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

| Line | Step | **XRP held** | **vs keep $100 in XRP (XRP)** | XRP-equivalent* vs holding | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | Forced rebuys | RLUSD parked |
|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | 4% | **77.5839** | **+0.3923** (+0.51%) | +0.51% | $96.69 | +0.49 | 1 | 0 | $0.00 |
| `xrp_stacker_6pct` | 6% | **77.8084** | **+0.6167** (+0.80%) | +0.80% | $96.97 | +0.77 | 1 | 0 | $0.00 |
| Baseline: keep $100 in XRP | — | 77.1917 | — | — | $96.20 | — | | | |

## Separate line: XRP stacker, 4% steps (`xrp_stacker`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker: sell slices high, buy back lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker` | **77.5839** | **+0.3923** (+0.51%) | $0.00 | 77.5839 (+0.51%) | $96.69 | +0.49 | 1 | +0.3925 | 0 (+0.0000) | $0.13 (0.00030) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $96.20 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +4% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (4%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 4% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.23045): sell 1.2797 sell 1.3309 sell 1.3841 sell 1.4395
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: XRP stacker, 6% steps (`xrp_stacker_6pct`, PAPER-NOT-ON-LEDGER) — scoreboard is XRP COUNT

XRP stacker 6% steps (side-by-side test): sell slices high, buy back 6% lower with all the RLUSD (goal: more XRP). Separate $100 line, not included in the $300 total. Started 2026-10-20T08:43:56+00:00 at $1.2948 with **77.1917 XRP** (= keep $100 in XRP).

| | **XRP held** | vs start XRP | RLUSD parked (waiting to rebuy) | XRP-equivalent* | Value (RLUSD/USD) | vs keep $100 in XRP (USD) | Round trips | XRP gained from trips | Forced rebuys (XRP lost) | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `xrp_stacker_6pct` | **77.8084** | **+0.6167** (+0.80%) | $0.00 | 77.8084 (+0.80%) | $96.97 | +0.77 | 1 | +0.6170 | 0 (+0.0000) | $0.13 (0.00030) | 2.0 |
| Baseline: keep $100 in XRP | 77.1917 | +0.0000 | $0.00 | 77.1917 | $96.20 | — | | | | | |

- Rules: 4 sell slices of 15% of the sellable stack at +6% steps above the reference; each sold slice rebuys with ALL its RLUSD one step (6%) lower, so each round trip ends with more XRP. No RLUSD profit is banked. Cost 0.25% per fill (AMM 0.205% + slippage) + network fee. Ladder trails down when nothing is parked and price is 6% below the reference. A slice parked over 14 days is bought back at market (can lose XRP).
- Orders now (reference 1.20913): sell 1.2817 sell 1.3586 sell 1.4401 sell 1.5265
- Risk: in a sustained rally the RLUSD stays parked or is rebought higher, so it ends with **fewer XRP than just holding**.

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$98.19** | -1.81 | 39.3617 | $49.14 | 78.7702 |
| Hold the same 50/50 (no pool) | $98.10 | -1.90 | 38.5793 | $50.02 | 78.6969 |
| Baseline: keep $100 in XRP | $96.20 | -3.80 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.093%** = impermanent loss -0.018% + fees earned ≈ +0.111% (pool fee 0.214%, pool share 0.002103%)
- LP vs keep $100 in XRP: **+1.99 USD** · XRP-equivalent: +2.04%
- Fees paid: $0.03 (taker cost on the XRP half + 0.00008 XRP network fees for TrustSet, OfferCreate, AMMDeposit and the future AMMWithdraw, already deducted). Reserve locked: 1.4 XRP (base + RLUSD line + LP-token line), not spent.

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.

<!-- LEVERAGE-PAPER-BEGIN -->
## Separate line: LEVERAGED XRP grid, paper perpetual futures (`lev_2x`, `lev_5x`, PAPER-NOT-REAL)

Modelled on Binance USDⓈ-M XRPUSDT perps, isolated margin. Started **2026-10-26T15:45:00+00:00** at **$1.3024**, $100 paper each, not in the $300 total. Scoreboard: USD vs keep $100 in XRP bought at the same start. Last update 2026-10-30T11:45:21+00:00 at $1.2470 (prices: `binance_spot_data_api`, funding: `okx_proxy`).

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position XRP (avg entry) | Liquidation price | Open levels | Round trips | Fees paid (trading + funding) | **Liquidations (margin lost)** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|---|
| `lev_2x` (2x) | **$100.61** | +0.61 | **+4.91** | 31.66 (1.23167) | 0.61873 | 2/10 | 3 | $0.03 ($0.03 + $-0.01) | **0** ($0.00) | 2.5% |
| `lev_5x` (5x) | **$101.53** | +1.53 | **+5.83** | 79.15 (1.23167) | 0.99009 | 2/10 | 3 | $0.07 ($0.08 + $-0.02) | **0** ($0.00) | 6.3% |
| Baseline: keep $100 in XRP | $95.70 | -4.30 | — | 76.74 | — | | | $0.05 | 0 | |

- Rules: 10 buy levels 2% apart below the start, $10 margin each (2x = $20 of XRP, 5x = $50), take profit +2% per level, profit kept in USDT, static ladder. Costs: 0.02% maker per fill, 8-hourly funding, and the value assumes a market close (0.05% taker + 0.05% slippage). Liquidation when margin + unrealised P/L falls to 0.5% of the position; the whole margin is lost. Backtest: `leverage/backtest_leverage_output.txt`.
- Not available to US residents on Binance.com; Binance.US has no futures or margin. This line is for learning only.
<!-- LEVERAGE-PAPER-END -->

<!-- LEVERAGE-TA-BEGIN -->
## Separate line: TA long/short on leverage, paper perpetual futures (`lev_ta_2x`, `lev_ta_5x`, PAPER-NOT-REAL)

Started **2026-10-26T16:15:00+00:00** at **$1.2938**, $100 paper each, not in the $300 total. Last update 2026-10-30T11:45:22+00:00 at $1.2470. 1h trend now: **down**, RSI(14) 47.32 (prices `binance_spot_data_api`, funding `okx_proxy`).

### $50 / $100 / $500 side by side (`_50` / `_500` lines are the same strategy with $50 / $500; profit after fees + funding; worst drawdown = biggest drop from a high; max loss = lowest value vs start)

| Line | Position | Trades (wins) | **$50: profit** | $50: worst drawdown, low | $50: liq. | **$100: profit** | $100: worst drawdown, low | $100: liq. | **$500: profit** | $500: worst drawdown, low | $500: liq. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | FLAT | 3 (1) | **-0.19** | -3.03 (6.0%), low -2.78 | 0 | **-0.39** | -6.07 (6.0%), low -5.56 | 0 | **-1.93** | -30.33 (6.0%), low -27.78 | 0 |
| `lev_ta_5x` (5x) | FLAT | 3 (1) | **-0.81** | -7.40 (14.6%), low -6.77 | 0 | **-1.63** | -14.81 (14.6%), low -13.53 | 0 | **-8.14** | -74.03 (14.6%), low -67.66 | 0 |

Keep $50 / $100 / $500 in XRP: -1.83 / -3.67 / -18.33.

### Details ($100 lines)

| Line | **Value (USD, if closed now)** | Change vs $100 | **vs keep $100 in XRP** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Fees paid (trading + funding) | **Liquidations** | Max drawdown |
|---|---|---|---|---|---|---|---|---|---|
| `lev_ta_2x` (2x) | **$99.61** | -0.39 | **+3.28** | FLAT | 3 (1) | 1 / 2 | $0.55 ($0.53 + $0.02) | **0** ($0.00) | 6.0% |
| `lev_ta_5x` (5x) | **$98.37** | -1.63 | **+2.04** | FLAT | 3 (1) | 1 / 2 | $1.32 ($1.27 + $0.05) | **0** ($0.00) | 14.6% |
| Baseline: keep $100 in XRP | $96.33 | -3.67 | — | | | | $0.05 | 0 | |

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
| `com_xrp_2x` | 2026-10-26T16:40:00+00:00 | **$97.62** | -2.38 | **+0.95** | FLAT | 1 (0) | 0 / 1 | 0 | $0.18 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_5x` | 2026-10-26T16:40:00+00:00 | **$94.05** | -5.95 | **-2.61** | FLAT | 1 (0) | 0 / 1 | 0 | $0.45 | **0** | 6.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.62** | -2.38 | **+1.45** | FLAT | 1 (0) | 0 / 1 | 0 | $0.18 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_xrp_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.83** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.83** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.83** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_xrp_5x_quick` | 2026-10-26T17:15:00+00:00 | **$94.31** | -5.69 | **-1.49** | FLAT | 1 (0) | 0 / 1 | 0 | $0.45 | **0** | 6.5% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_2x` | 2026-10-26T16:40:00+00:00 | **$97.94** | -2.06 | **+1.10** | FLAT | 2 (0) | 0 / 2 | 0 | $0.40 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_5x` | 2026-10-26T16:40:00+00:00 | **$94.88** | -5.12 | **-1.96** | FLAT | 2 (0) | 0 / 2 | 0 | $0.98 | **0** | 6.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$97.94** | -2.06 | **+1.46** | FLAT | 2 (0) | 0 / 2 | 0 | $0.40 | **0** | 2.7% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
| `com_btc_proxy_2x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.52** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_5x` | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.52** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_proxy_mix` (5x trades: 0) | 2026-10-26T17:00:00+00:00 | **$100.00** | +0.00 | **+3.52** | FLAT | 0 (0) | 0 / 0 | 0 | $0.00 | **0** | 0.0% | {"casey": "IDLE", "pip": "IDLE", "theo": "SHORT", "remy": "SHORT"} |
| `com_btc_5x_quick` | 2026-10-26T17:15:00+00:00 | **$94.88** | -5.12 | **-1.29** | FLAT | 2 (0) | 0 / 2 | 0 | $0.98 | **0** | 6.6% | {"long_scout": "IDLE", "short_scout": "IDLE", "idle_guard": "IDLE", "chart_reader": "SHORT"} |
- Crowding XRPUSDT now: funding -0.0155%/8h, OI 24h -6.21%, long/short accounts 3.53 (43th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)
- Crowding BTCUSDT now: funding 0.0055%/8h, OI 24h 2.4%, long/short accounts 2.45 (96th pct of 7d), Fear & Greed 30 -> **not crowded** (sources: okx_rubik, alternative.me)

Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.

Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.
<!-- COMMITTEE-END -->

<!-- KRAKEN-1K-BEGIN -->
## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps

Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`okx_proxy`), liquidation at 17% maintenance margin + $10 fee. Last update 2026-10-30T11:45:29+00:00 at $1.2470. Target: $4/day after fees.

| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `com_xrp_kraken_1k_2x` (2x cap) | 2026-10-26T18:15:00+00:00 | **-20.42** | **-5.48** (-9.48 vs $4) | -25.60 (2.5%) | 1 (0%) | 0 | 1 (0% wins) -20.42 | 0 (FLAT) | $0.07 / $-0.20 | 0 | +20.68 |
| `com_xrp_kraken_1k_3x` (3x cap) | 2026-10-26T18:15:00+00:00 | **-27.23** | **-7.30** (-11.30 vs $4) | -34.14 (3.4%) | 1 (0%) | 0 | 1 (0% wins) -27.23 | 0 (FLAT) | $0.09 / $-0.26 | 0 | +13.87 |

- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).
<!-- KRAKEN-1K-END -->

<!-- SIZES:BEGIN -->
## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)

$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth (pool 1,871,416 XRP / 2,336,237 RLUSD from https://xrplcluster.com). Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.

| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |
|---|---|---|---|---|---|
| `dip_ladder` | **-0.45** | -3.99 | **-2.26** | -19.97 | $0.0095 (5 fills) |
| `scalp_2pct` | **+0.25** | -1.38 | **+1.25** | -6.89 | $0.0064 (9 fills) |
| `scalp_2pct_rlusd` | **+0.26** | -1.36 | **+1.30** | -6.79 | $0.0065 (9 fills) |
| `xrp_stacker` | **-3.31** | -10.66 | **-16.64** | -53.29 | $0.0895 (3 fills) |
| `xrp_stacker_6pct` | **-3.03** | -10.69 | **-15.24** | -53.44 | $0.0897 (3 fills) |
| `amm_lp` | **-1.81** | -5.33 | **-9.03** | -26.63 | $0.0000 (0 fills) |
| `lev_2x` | **+0.61** | -2.05 | **+3.06** | -10.23 | $0.0000 (0 fills) |
| `lev_5x` | **+1.53** | -5.12 | **+7.65** | -25.59 | $0.0000 (0 fills) |

Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.
<!-- SIZES:END -->
