# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

**Scoreboard: value in RLUSD/USD**, XRP-equivalent second. Each strategy has its own **$100** (paper total **$300**) and is compared with **keep $100 in XRP** (bought at the start).

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-24T14:10:28+00:00**, XRPL XRP/RLUSD mid **$1.2844** (bid 1.2842 / ask 1.2845, node https://xrplcluster.com, ledger 107872853)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 3

| Strategy | Start | **Value (RLUSD/USD)** | Change vs start | **vs keep $100 in XRP** | XRP held | RLUSD | XRP-equivalent* | vs XRP baseline (XRP-eq.) | Fills | XRP sells (taxable) |
|---|---|---|---|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $100 | **$99.98** | -0.02 | **+0.83** (+0.84%) | 2.2000 | $97.15 | 77.8031 | +0.79% | 1 | 0 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $100 | **$99.96** | -0.04 | **+0.82** (+0.83%) | 3.2000 | $95.85 | 77.7949 | +0.78% | 1 | 0 |
| Static 2% scalp ladder, profit banked in RLUSD (variant) (`scalp_2pct_rlusd`) | $100 | **$99.96** | -0.04 | **+0.82** (+0.83%) | 3.2000 | $95.85 | 77.7949 | +0.78% | 1 | 0 |
| **Experiment total** (all 3) | $300 | **$299.90** | -0.10 | **+2.48** (+0.83%) | 8.6000 | $288.86 | 233.3930 | +0.79% | | |
| **Baseline: keep $100 in XRP** (bought at start) | $100 | $99.14 | -0.86 | — | 77.1917 | $0.00 | 77.1917 | — | 1 | 0 |
| Baseline for the total: keep $300 in XRP | $300 | $297.43 | -2.57 | — | 231.5750 | $0.00 | 231.5750 | — | | |

_History replayed on 2026-10-24 from Bitstamp 5-min candles after bad XRPL book data was removed, then re-sized to $100 per strategy (earlier versions archived under `*/archive_phantom_2026-10-24/` and `*/archive_resize_2026-10-24/`)._

**Experiment ($300) vs keep $300 in XRP: +2.48 USD (+0.83%)** · XRP-equivalent: +0.79%

\* Value = XRP held × current mid + RLUSD. XRP-equivalent = XRP held + RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

- `dip_ladder` is an **XRP-accumulation** strategy (it only buys and never sells), so it only grows dollar value if XRP rises.
- `scalp_2pct_rlusd` runs the same 2% grid as `scalp_2pct` but banks each round trip's whole profit in RLUSD and does not recompound it.

- Dip ladder open buy orders: 1.2689 1.2430 1.2171 1.1912 1.1653 (reference 1.294829, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0
- `scalp_2pct_rlusd`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.0

## Separate line: AMM liquidity provider (`amm_lp`, PAPER-NOT-ON-LEDGER)

$100 deposited 50/50 into the XRP/RLUSD AMM pool on 2026-10-20T08:43:56+00:00 at $1.2948 (38.5793 XRP + 50.02 RLUSD; backdated from historical pool state). Separate $100 line, not included in the $300 total.

| | **Value (RLUSD/USD)** | Change vs $100 | XRP | RLUSD | XRP-equivalent* |
|---|---|---|---|---|---|
| AMM LP position now (fees included) | **$99.61** | -0.39 | 38.7971 | $49.78 | 77.5370 |
| Hold the same 50/50 (no pool) | $99.57 | -0.43 | 38.5793 | $50.02 | 77.5074 |
| Baseline: keep $100 in XRP | $99.14 | -0.86 | 77.1917 | $0.00 | 77.1917 |

- LP vs hold-50/50: **+0.038%** = impermanent loss -0.001% + fees earned ≈ +0.040% (pool fee 0.205%, pool share 0.002125%)
- LP vs keep $100 in XRP: **+0.47 USD** · XRP-equivalent: +0.45%

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/amm_lp_ticks.csv`, `logs/tax_export.csv`.
