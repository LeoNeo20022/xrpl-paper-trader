# XRP/RLUSD paper-trading experiment: SUMMARY

> **PAPER ONLY.** Simulated trades from public prices. No wallet, no keys, no real orders. Not financial or tax advice.

- Started: **2026-10-20T08:43:56+00:00** at XRPL mid **$1.2948**
- Last update: **2026-10-20T10:41:05+00:00**, XRPL XRP/RLUSD mid **$1.2912** (bid 1.2907 / ask 1.2916, node https://xrplcluster.com, ledger 107782151)
- RLUSD issuer transfer fee (live): 0.0000%  |  candles processed this run: 8

| Strategy | Budget | XRP held | RLUSD unspent | XRP-equivalent* | Fills | XRP sells (taxable) |
|---|---|---|---|---|---|---|
| Weekly dip-buy ladder, never sells (`dip_ladder`) | $75 | 61.5320 | $0.00 | 61.5320 | 6 | 0 |
| Static 2% scalp ladder, all profit kept as XRP (`scalp_2pct`) | $25 | 5.1646 | $18.77 | 19.6940 | 20 | 9 |
| **Total** | $100 | **66.6966** | $18.77 | **81.2260** | | |
| Baseline: $100 lump-sum XRP bought at start | $100 | 77.1917 | $0.00 | 77.1917 | 1 | 0 |

**Experiment vs baseline (XRP-equivalent): +5.23%**

\* XRP-equivalent = XRP held + unspent RLUSD converted at the current mid with a 0.05% taker cost. XRP held includes the XRP locked as ledger reserve (it is still yours).

- Dip ladder open buy orders: none (reference 1.2948290358744394, next refresh 2026-10-27T08:43:56+00:00)
- `scalp_2pct`: 9 buy orders waiting, 1 sell orders waiting, XRP kept from scalps 0.321287

Logs: `logs/summary.csv`, `logs/<strategy>_ticks.csv`, `logs/<strategy>_fills.csv`, `logs/tax_export.csv`.
