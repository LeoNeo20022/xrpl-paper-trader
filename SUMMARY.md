# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-23T00:24:21+00:00**, XRPL XRP/RLUSD mid **$1.3061** (bid 1.3052 / ask 1.3069, node https://xrplcluster.com, ledger 107838109)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 6

| Strategy | Budget | XRP held | RLUSD unspent | XRP-equivalent* | Fills | XRP sells (taxable) |
|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $75 | 61.5320 | $0.00 | 61.5320 | 6 | 0 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $25 | 3.9066 | $20.85 | 19.8660 | 41 | 20 |
| **Total** | $100 | **65.4386** | $20.85 | **81.3980** | | |
| Baseline: $100 lump-sum XRP bought at start | $100 | 77.1917 | $0.00 | 77.1917 | 1 | 0 |

**Experiment vs baseline (XRP-equivalent): +5.45%**

\* XRP-equivalent = XRP held + unspent RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

- Dip ladder open buy orders: none (reference 1.2948290358744394, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 10 buy orders waiting, 0 sell orders waiting, XRP kept from scalps 0.707024

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/tax_export.csv`.
