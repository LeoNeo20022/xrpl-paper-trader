# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD** (goal: grow dollars; can swap to XRP later). XRP-equivalent is shown second.

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-24T12:06:54+00:00**, XRPL XRP/RLUSD mid **$1.2791** (bid 1.2783 / ask 1.2798, node https://xrplcluster.com, ledger 107870997)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 2

| Strategy | Start | **Value (RLUSD/USD)** | **Change vs start** | XRP held | RLUSD | XRP-equivalent* | Fills | XRP sells (taxable) |
|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $75 | **$78.70** | **+3.70** (+4.94%) | 61.5320 | $0.00 | 61.5320 | 6 | 0 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $25 | **$25.85** | **+0.85** (+3.41%) | 3.9066 | $20.85 | 20.2029 | 41 | 20 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $25 | **$24.95** | **-0.05** (-0.21%) | 3.2000 | $20.85 | 19.4963 | 1 | 0 |
| **Experiment total** (dip_ladder + scalp_2pct) | $100 | **$104.55** | **+4.55** | 65.4386 | $20.85 | 81.7350 | | |
| Alt total (dip_ladder + scalp_2pct_rlusd) | $100 | $103.65 | +3.65 | | | | | |
| Baseline: hold RLUSD (do nothing in dollars) | $100 | $100.00 | +0.00 | 0 | $100.00 | 78.1430 | 0 | 0 |
| Baseline: $100 lump-sum XRP bought at start | $100 | $98.73 | -1.27 | 77.1917 | $0.00 | 77.1917 | 1 | 0 |

> ⚠️ **Data issue found 2026-10-24:** the XRPL book snapshots at 2026-10-20 08:54 UTC (mid $0.646) and 2026-10-22 21:22 UTC (mid $0.679) were bad reads (crossed book from dust offers). They triggered phantom fills in `dip_ladder` and `scalp_2pct`, so their results above are overstated. A guard now rejects such snapshots. The backfilled `scalp_2pct_rlusd` and `amm_lp` lines are not affected.

**Experiment vs $100 in RLUSD: +4.55 USD** · vs lump-sum XRP (XRP-equivalent): +5.89%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

- Note: `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` (paper variant, not in the experiment total) runs the same 2% grid but banks each round trip's whole profit in RLUSD and does not recompound it; it was backfilled from the experiment start using the same 5-min candles (the original scalper's extra fills came from the bad snapshots noted above; by the candles, price never fell 2% below the start, so no ladder level should have filled yet).

- Dip ladder open buy orders: none (reference 1.2948290358744394, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.707024
- `scalp_2pct_rlusd`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Not included in the totals above.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$99.40** | -0.60 | 38.8466 | $49.71 | 77.6946 |
| Hold the same 50/50 (no pool) | $99.37 | -0.63 | 38.5793 | $50.02 | 77.6684 |
| Hold RLUSD | $100.00 | +0.00 | 0 | $100.00 | |
| $100 lump-sum XRP baseline | $98.73 | -1.27 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.034%** = impermanent loss -0.002% + fees earned ≈ +0.036% (pool fee 0.205%, pool share 0.002125%)
- LP vs lump-sum XRP (XRP-equivalent): **+0.65%**

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.
