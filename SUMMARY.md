# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD** (goal: grow dollars; can swap to XRP later). XRP-equivalent is shown second.

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-24T12:22:41+00:00**, XRPL XRP/RLUSD mid **$1.2835** (bid 1.2827 / ask 1.2844, node https://xrplcluster.com, ledger 107871240)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 3

| Strategy | Start | **Value (RLUSD/USD)** | **Change vs start** | XRP held | RLUSD | XRP-equivalent* | Fills | XRP sells (taxable) |
|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $75 | **$74.97** | **-0.03** (-0.03%) | 2.2000 | $72.15 | 58.3832 | 1 | 0 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $25 | **$24.96** | **-0.04** (-0.15%) | 3.2000 | $20.85 | 19.4394 | 1 | 0 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $25 | **$24.96** | **-0.04** (-0.15%) | 3.2000 | $20.85 | 19.4394 | 1 | 0 |
| **Experiment total** (dip_ladder + scalp_2pct) | $100 | **$99.94** | **-0.06** | 5.4000 | $93.00 | 77.8225 | | |
| Alt total (dip_ladder + scalp_2pct_rlusd) | $100 | $99.94 | -0.06 | | | | | |
| Baseline: hold RLUSD (do nothing in dollars) | $100 | $100.00 | +0.00 | 0 | $100.00 | 77.8700 | 0 | 0 |
| Baseline: $100 lump-sum XRP bought at start | $100 | $99.08 | -0.92 | 77.1917 | $0.00 | 77.1917 | 1 | 0 |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed (old state/fills archived under `*/archive_phantom_2026-10-24/`)._

**Experiment vs $100 in RLUSD: -0.06 USD** · vs lump-sum XRP (XRP-equivalent): +0.82%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

- Note: `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` (paper variant, not in the experiment total) runs the same 2% grid but banks each round trip's whole profit in RLUSD and does not recompound it; it was backfilled from the experiment start using the same 5-min candles (same replay as the original).

- Dip ladder open buy orders: 1.2689 1.2430 1.2171 1.1912 1.1653 (reference 1.294829, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0
- `scalp_2pct_rlusd`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Not included in the totals above.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$99.58** | -0.42 | 38.8162 | $49.75 | 77.5588 |
| Hold the same 50/50 (no pool) | $99.54 | -0.46 | 38.5793 | $50.02 | 77.5319 |
| Hold RLUSD | $100.00 | +0.00 | 0 | $100.00 | |
| $100 lump-sum XRP baseline | $99.08 | -0.92 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.035%** = impermanent loss -0.002% + fees earned ≈ +0.036% (pool fee 0.205%, pool share 0.002125%)
- LP vs lump-sum XRP (XRP-equivalent): **+0.48%**

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.
