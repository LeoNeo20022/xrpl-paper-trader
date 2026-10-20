# XRP/RLUSD paper-trading experiment (XRP Ledger DEX)

**This is paper trading only.** Nothing here touches a wallet, a private key, or a real order.
The scripts read *public* price data, pretend to place orders, and write down what *would* have
happened. No money moves and no transactions are ever sent to the XRP Ledger. Not financial or tax advice.

## What it simulates ($100 of new money, goal = end with the most XRP)

| Strategy | Money | How it works |
|---|---|---|
| `dip_ladder` | $75 | Once a week it "places" 5 buy orders at 2%, 4%, 6%, 8% and 10% below the current price, splitting all unspent RLUSD evenly. Unfilled orders are cancelled and re-placed at the next weekly refresh. **It never sells XRP.** |
| `scalp_2pct` | $25 | 10 buy orders 2% apart below the start price. When one fills, a sell is placed 2% higher that sells only enough XRP to get the RLUSD back, so **all the profit stays as XRP**. Then the buy is re-armed. The ladder does not move (static). |
| baseline | $100 | Simply buying $100 of XRP at the start, for comparison. |

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
