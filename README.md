# XRP/RLUSD paper-trading experiment (XRP Ledger DEX)

**This is paper trading only.** Nothing here touches a wallet, a private key, or a real order.
The scripts read *public* price data, pretend to place orders, and write down what *would* have
happened. No money moves and no transactions are ever sent to the XRP Ledger. Not financial or tax advice.

## What it simulates ($100 of new money, goal = end with the most XRP)

| Strategy | Money | How it works |
|---|---|---|
| `dip_ladder` | $100 | Once a week it "places" 5 buy orders (about $20 each) at 2%, 4%, 6%, 8% and 10% below the current price, splitting all unspent RLUSD evenly. Unfilled orders are cancelled and re-placed at the next weekly refresh. **It never sells XRP.** |
| `scalp_2pct` | $100 | 10 buy orders (about $10 each) 2% apart below the start price. When one fills, a sell is placed 2% higher that sells only enough XRP to get the RLUSD back, so **all the profit stays as XRP**. Then the buy is re-armed. The ladder does not move (static). |
| `scalp_2pct_rlusd` | $100 | Same grid as `scalp_2pct`, but each round trip sells enough XRP to bank the **whole profit in RLUSD**; that profit is not recompounded. |
| `amm_lp` (separate line) | $100 | $100 deposited 50/50 into the XRP/RLUSD AMM pool on Oct 20, valued each tick from `amm_info` (fees included), compared with holding the same 50/50. |
| baseline: keep $100 in XRP | $100 | Simply buying $100 of XRP at the start, for comparison. |

Each strategy is compared with **keep $100 in XRP** bought at the Oct 20 start; the $300 total is compared with $300 kept in XRP. Values are in RLUSD/USD first, XRP-equivalent second. On 2026-10-24 the history was replayed from Bitstamp 5-min candles (bad XRPL book reads removed) and re-sized from $75/$25 to $100 each; `logs/summary.csv` was rebuilt from that replay, and the previous versions are kept under `state/` and `logs/archive_phantom_2026-10-24/` and `archive_resize_2026-10-24/`.

Each paper account also "buys" the XRP the ledger would lock as reserve (1 XRP base + 0.2 trust line + 0.2 per open order).
That XRP is counted as held, because it is still yours.

## How a tick works (`python paper_runner.py`)
1. Reads the live XRP/RLUSD order book from a public XRPL server (xrplcluster.com, falling back to s1/s2.ripple.com),
   plus the RLUSD issuer's transfer fee (currently 0%).
2. Reads closed Bitstamp XRP/USD 5-minute candles since the last tick, to catch dips and spikes between ticks.
3. Simulates fills. A limit order "fills" only if the price trades 0.05% through it. Then it finishes on the live XRPL price.
4. Writes:
   - `SUMMARY.md` plus `logs/summary.csv`: XRP held, RLUSD unspent, XRP-equivalent, fills and XRP sells per strategy, vs the $100 baseline.
   - `logs/<strategy>_ticks.csv` and `logs/<strategy>_fills.csv`: details.
   - `logs/tax_export.csv`: every simulated trade as Date, Type, Sent Asset/Amount, Received Asset/Amount, Fee Asset/Amount.
     Rows are marked `PAPER-NOT-ON-LEDGER` so they're never confused with real trades.
   - `state/*.json`: where each strategy is, so the next tick continues.

To restart the experiment from scratch, delete `state/`, `logs/` and `SUMMARY.md`, then run a tick.

## Automation
`.github/workflows/paper-trading.yml` runs a tick every 15 minutes on GitHub Actions and commits the updated logs.
It uses no secrets and only Python's standard library.

## Settings
Everything is in `config.json` (budgets, step sizes, refresh period, fill margin).

## Research and backtest files (not needed for the runner)
- `scalper.py` and `dipladder.py`: the strategy logic used by the runner.
- `compare_xrp.py`, `backtest_bull.py`, `backtest_scalp.py`, `amm_yield.py`: backtests and research scripts. Their outputs are in `*_output.txt` and `*_results.csv`.
- `data/`: saved public price data. `memes/`: the meme-token research. `legacy_grid/`: the first grid prototype.

## Known limits
- Bitstamp XRP/USD candles stand in for prices between ticks. The XRPL DEX price is usually within about 0.1% of them, but not always.
- Real limit orders wait in a queue and can be skipped, so simulated fills are optimistic.
- If ticks stop for more than about 3 days, only the latest 1,000 candles are caught up.

## xrp_stacker (added 2026-10-24, separate $100 line, PAPER ONLY)
Goal: more XRP over time. Starts 100% in XRP (same count as "keep $100 in XRP"). Four sell slices, each 15% of the sellable stack
(stack minus 2.0 XRP reserve), sit at +4%, +8.2%, +12.5%, +17% above a reference price. When one sells, ALL of its RLUSD is parked in a
buy-back 4% lower, so each round trip ends with ~+3.5% more XRP on that slice (4% minus 2 x 0.25% fill cost). No RLUSD is ever banked.
The ladder trails down when nothing is parked and price is 4% below the reference; a slice parked over 14 days is bought back at
market (this can lose XRP). Risk: in a sustained rally it ends with fewer XRP than holding. Scoreboard: XRP count first.
Replayed from the Oct 20 start on the same Bitstamp 5-minute candles as the other lines (book mids not used for the replay).

## Fees (as if signed in Xaman), since 2026-10-24
Every simulated transaction pays the XRPL network fee: max(0.00002 XRP, live open-ledger fee), capped at 0.01 XRP
(OfferCreate per order, OfferCancel at dip-ladder refresh, TrustSet for RLUSD, AMMDeposit/AMMWithdraw for amm_lp). Before Oct 24
fills paid 0.00001 XRP; the missed TrustSet and initial-ladder OfferCreates were charged once on Oct 24. Limit orders fill at their
limit price (maker, no AMM fee); market buys pay 0.05% taker; xrp_stacker pays 0.25% per fill (AMM 0.205% + slippage).
Owner reserves (1 XRP base + 0.2 per trust line/offer) are locked, not spent, and shown separately.
NOT included: Xaman's own 0.8% service fee on swaps, AMM deposits/withdrawals and DEX trades:
https://help.xaman.app/app/getting-started-with-xaman/understanding-the-xaman-service-fee

## xrp_stacker_6pct (added 2026-10-24, separate $100 line, PAPER ONLY)
Side-by-side copy of xrp_stacker with **6% steps instead of 4%**: same 77.19 XRP start (Oct 20), 2.0 XRP reserve never sold,
4 slices of 15% of the sellable stack at +6%, +12.4%, +19.1%, +26.2% above the reference, each rebuys 6% below its sell price
with ALL its RLUSD (~+5.5% more XRP per round trip after 2 x 0.25% fill cost). Trail-down at 6% below the reference, 14-day
forced market rebuy, same network-fee model. Replayed from Oct 20 on the same Bitstamp 5-minute candles. Not in the $300 total.
`backtest_stacker.py` compares 4% vs 6% over the last 14/30/45/60 days (output in `backtest_stacker_output.txt`).

## Leveraged XRP grid (`leverage/`, added 2026-10-26, separate $100 lines, PAPER ONLY)
A learning line that asks "would leverage have helped?". Modelled on Binance USDⓈ-M XRPUSDT perpetual futures, isolated margin,
in two variants: `lev_2x` and `lev_5x`. Same idea as `scalp_2pct`: 10 buy levels 2% apart, $10 of margin each, +2% take profit per level,
profit kept in USDT, static ladder, all levels form one long position. Costs: 0.02% maker per fill, real 8-hourly funding,
0.05% taker + 0.05% slippage to close, and **liquidation** (whole margin lost) when the 5-min low takes margin + unrealised P/L down to 0.5% of the position.
Prices come from public keyless endpoints (Binance futures API is geo-blocked in the US, so the runner falls back to Binance spot klines from
data-api.binance.vision; funding falls back to OKX's public XRP perp funding as a proxy). No keys, no accounts, no orders.
Files: `leverage/levgrid.py` (logic), `leverage/lev_runner.py` (runs after `paper_runner.py` each tick), `leverage/backtest_leverage.py`
and its output `leverage/backtest_leverage_output.txt`, `leverage/SUMMARY_LEVERAGE.md`, `leverage/logs/` (events incl. LIQUIDATION rows, ticks).
Binance.com futures are not available to US residents and Binance.US has no futures or margin, so this is not a live candidate as-is.

## Stars Aligned (added 2026-10-27, curiosity line, PAPER ONLY): `com_xrp_10x_stars_{50,100,500}`
- XRP at **10x**, long or short, opens ONLY when the team vote is **unanimous, 4 of 4** (Casey, Pip, Theo, Remy). Every other line keeps the 3-of-4 rule.
- Votes = the team committee's effective calls (`leverage/team_committee.py`): a teammate's own row in `/home/box/shared/strategy-lab/votes.csv`, else its automated proxy (`committee.proxy_votes`). Each unanimous round is logged to `leverage/team/stars_signals.csv` with how many votes were real vs proxy; totals in `leverage/team/TEAM_SUMMARY.md`.
- Note: Casey's proxy only ever votes LONG/IDLE and Pip's only SHORT/IDLE, so an all-proxy 4/4 cannot happen. The line fires only if Pip casts a real LONG or Casey a real SHORT (with the other three agreeing, real or proxy).
- Exits: take profit **+2%** price move (~ +20% on margin; raised from +1% because 4/4 trades are rare), stop **-1%** price move, isolated margin, one position at a time. At 10x a +2% win nets about +19.2% and a stop about -11.4% of margin after fees, so fees-only break-even is about a 37% win rate (+1%: 55%, +1.5%: 45%, +3%: 28%; see the backtest).
- News blackout: no new entry within 3h before/after any event in `leverage/events_calendar.csv` or any `high` item in Riley's `/home/box/shared/strategy-lab/xrp-news-events.csv` (if that file is missing or unreadable, the news check is skipped).
- Costs, funding and liquidation: same Binance-style XRPUSDT perp model as the other leverage lines (`leverage/ta.py`: taker 0.05% + 0.05% slippage, maker 0.02%, 8-hourly funding both ways, 0.5% maintenance margin; liquidation ~ -9.5% from entry at 10x).
- **Offshore-rules paper only.** Kraken US's XRP perp has a 17% maintenance margin, so 10x is not possible there; this line cannot be run as-is on a US venue.
- Runs inside the box team-committee loop, wrapped in its own try/except so an error cannot affect other lines. Backtest: `leverage/backtest_stars.py` -> `leverage/backtest_stars_output.txt` (events calendar blackout only; no news history exists).
