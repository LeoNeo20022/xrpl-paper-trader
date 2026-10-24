# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Token data by <a href="https://xrpl.to">xrpl.to</a>; safety checks and prices from the public XRP Ledger.

Last run: **2026-10-24T11:19:59+00:00** (UTC) · XRP/USD 1.2817 (bitstamp) · this run: 45 tokens seen, 13 passed, 0 paper-bought · buys today 10/10

**Source warnings this run:** daily buy cap reached; skipped further buys

## Results per exit strategy (closed trades, each buy scored separately under all 3)

| Strategy | Rule | Closed | Win rate | P&L XRP gross | P&L XRP net | P&L USD gross | P&L USD net | Open |
|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 0 | – | +0.000 | +0.000 | +0.00 | +0.00 | 10 |
| plus5 | all at +50%, stop −50%, 72h | 0 | – | +0.000 | +0.000 | +0.00 | +0.00 | 10 |
| scalp | +20% / −10% / 60 min | 0 | – | +0.000 | +0.000 | +0.00 | +0.00 | 10 |

Gross = at pool spot price with no fees/slippage. Net = simulated AMM swaps incl. pool trading fee, price impact, issuer transfer fee and network fee. USD P&L also moves with XRP/USD. Exits fire at the price seen at each ~15-min poll, so real fills could be better or worse than the trigger level.

## Open paper positions (10/20)

| Token | Bought (UTC) | Cost | Buy cost vs spot | Now (net, x) | Strategies still open | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.29% | 0.99 | hold, plus5, scalp | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.53% | 0.99 | hold, plus5, scalp | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.01% | 1.00 | hold, plus5, scalp |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.58% | 0.99 | hold, plus5, scalp | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.15% | 1.00 | hold, plus5, scalp | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.12% | 1.00 | hold, plus5, scalp | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.00% | 1.00 | hold, plus5, scalp |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.33% | 0.99 | hold, plus5, scalp |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.47% | 0.99 | hold, plus5, scalp | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10 = 7.80 XRP | 0.22% | 1.00 | hold, plus5, scalp |  |

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9202 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9122 |
| [RIPTARD](https://xrpl.to/token/r37NJszgETCmYqUkPH7PmtkpVdsYBfMYSc-5249505441524400000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10725 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 26495 |
| [POOL](https://xrpl.to/token/r9D5RhucFjzBmdXcwc68VRbG2EYr4zqJmF-504F4F4C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,042 XRP) | 1521 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18267 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7607 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12970 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 472 XRP) | 236 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157172 |
| [BUZZY](https://xrpl.to/token/rLFDsYQcd7uerRnmYy3sRVTZ6P2uTjfrak-42555A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 339 XRP) | 169 |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3868 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4192 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4168 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,527 XRP) | 1263 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8061 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 80956 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13482 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 46775 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 14336 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26820 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 91244 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 84618 |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 748854 |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 139240 |
| [WARP](https://xrpl.to/token/rhuQ5tKUHG77J5ovRN4GVSwZJT5SDTZZCD-5741525000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 923 XRP) | 462 |
| [XRP.EXE](https://xrpl.to/token/rndx27LVQUEe3KvVDiBDz8DaqBwWJzFPP4-5852502E45584500000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,807 XRP) | 903 |
| [aura](https://xrpl.to/token/rpjuvqrH37RGzb88UVibzCQYSNrM9FxJDy-6175726100000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6215 |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 24177 |
| [XAH](https://xrpl.to/token/rswh1fvyLqHizBS2awu1vs6QcmwTBd9qiv-XAH) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 47385 |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 120853 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 497 XRP too low | 12127 |
| [WIND](https://xrpl.to/token/rnh3kiVFSBJxhwa7RJmmafQrqhyn9SKyCj-57494E4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,050 XRP) | 1525 |

Logs: `logs/candidates.csv`, `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
