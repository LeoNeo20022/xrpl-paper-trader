# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-24T16:47:21+00:00** (UTC) · XRP/USD 1.2698 (bitstamp) · last discovery 2026-10-24T16:47:21+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 9

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$100.62** | **+0.62** | $0.00 | 10 / $100.62 | $+0.00 | $+0.62 | – | 10 (0) | +0.00 | +1.21 | 79.24 | +1.21 | $0.27 (0.00012) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$100.62** | **+0.62** | $0.00 | 10 / $100.62 | $+0.00 | $+0.62 | – | 10 (0) | +0.00 | +1.21 | 79.24 | +1.21 | $0.27 (0.00012) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$99.22** | **-0.78** | $99.22 | 0 / $0.00 | $-0.78 | $+0.00 | 3 / 7 (30%) | 10 (10) | -0.72 | +0.00 | 78.14 | +0.11 | $0.54 (0.00024) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 6h | 2026-10-24 13:37 | **$100.52** | **+0.52** | $21.18 | 8 / $79.34 | $+1.18 | $-0.66 | 1 / 1 (50%) | 10 (2) | +1.00 | -0.00 | 79.17 | +1.06 | $0.36 (0.00017) | 1.6 |
| breakout | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$98.26** | **-1.74** | $88.92 | 1 / $9.34 | $-1.07 | $-0.66 | 0 / 1 (0%) | 2 (1) | -0.72 | -0.55 | 77.39 | -0.72 | $0.12 (0.01765) | 0.2 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$100.14** | **+0.14** | $0.00 | 10 / $100.14 | $+0.00 | $+0.14 | – | 10 (0) | +0.00 | +0.76 | 78.86 | +0.76 | $0.43 (0.00012) | 2.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$99.08** | **-0.92** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings |
|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.15 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.00 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.01 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.97 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.04 |  |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings |
|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.15 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.00 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.01 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.97 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.04 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T13:37 | $10.00 | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T13:37 | $10.00 | 1.00 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.00% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.98 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.08% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.05 |  | slow_scalp: new/top-15 trending, round trip 0.43% <= 2.0% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.00 | top-10 holders own 37% | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.99 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% | slow_scalp: new/top-15 trending, round trip 0.91% <= 2.0% |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.00 | top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |

### breakout — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T16:31 | $10.00 | 0.93 | top-10 holders own 31% | breakout: +42.4% in 1h, vol last hour 5107 vs prior 1353 / 24h avg 549 XRP |

### dip_bounce — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.01 | top-10 holders own 44% | dip_bounce: 39.9% below 24h high 1.09353e-06 XRP, age 415.1d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.99 |  | dip_bounce: 32.3% below 24h high 5.5575e-06 XRP, age 735.6d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.00 | top-10 holders own 42% | dip_bounce: 27.2% below 24h high 0.000211242 XRP, age 716.6d |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-10-24T13:37 | $10.00 | 1.03 | only 48% of LP burned (liquidity can be pulled) | dip_bounce: 22.5% below 24h high 0.0133504 XRP, age 725.6d |
| [NOX](https://xrpl.to/token/rBbu9c7zyuiDH4bq7uJhdLhzsRdEkSrYFX-NOX) | 2026-10-24T13:37 | $10.00 | 1.00 |  | dip_bounce: 21.8% below 24h high 0.0341682 XRP, age 691.6d |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.00 |  | dip_bounce: 21.7% below 24h high 4.16006e-06 XRP, age 733.6d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.05 | top-10 holders own 31% | dip_bounce: 19.5% below 24h high 2.83763e-05 XRP, age 739.6d |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.99 |  | dip_bounce: 18.7% below 24h high 0.000211392 XRP, age 733.6d |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.98 |  | dip_bounce: 17.2% below 24h high 5.8921e-07 XRP, age 502.2d |
| [BOX](https://xrpl.to/token/rhLJ2ma5pScsxVhL5EQr71w3FgASVLwP84-BOX) | 2026-10-24T13:37 | $10.00 | 1.04 | top-10 holders own 35% | dip_bounce: 16.2% below 24h high 0.00153201 XRP, age 669.6d |

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9175 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9383 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | FAIL_SAFETY | top-10 holders own 50% (excl. AMM) | 4022 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 26545 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 884 XRP) | 442 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,645 XRP) | 822 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18248 |
| [BEAR](https://xrpl.to/token/rBEARGUAsyu7tUw53rufQzFdWmJHpJEqFW-4245415200000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 99907 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 8245 |
| [NOX](https://xrpl.to/token/rBbu9c7zyuiDH4bq7uJhdLhzsRdEkSrYFX-NOX) | SKIP_ENTRY | not new and not top trending | 3416 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7513 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 257222 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13011 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 12495 |
| [AFFBAL](https://xrpl.to/token/rGu3gexApNkWR3ST7LW1mc1rZACXcxwcfi-41464642414C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,774 XRP) | 887 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 709 XRP) | 354 |
| [XPUNK](https://xrpl.to/token/rHEL3bM4RFsvF8kbQj3cya8YiDvjoEmxLq-5850554E4B000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 53 XRP) | 27 |
| [WOX](https://xrpl.to/token/rHSinRYo7V3h2769zueW3ke7V62zyvFwzu-WOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 349 XRP) | 174 |
| [LHT](https://xrpl.to/token/rHashLabsu2H6hXDSunL8AcVDmTyE17Z35-LHT) | FAIL_SAFETY | top-10 holders own 70% (excl. AMM) | 29533 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156887 |
| [DROPJR](https://xrpl.to/token/rKzktV2mxZnAggmM7DXcPeS7NX4zUdEqmJ-44524F504A520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,072 XRP) | 1536 |
| [BUZZY](https://xrpl.to/token/rLFDsYQcd7uerRnmYy3sRVTZ6P2uTjfrak-42555A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 294 XRP) | 147 |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3883 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4585 |
| [SIB](https://xrpl.to/token/rPz9bsto7F4adfUfE5iDQAgW2DWo74YZsw-SIB) | FAIL_SAFETY | pool too small (xrpl.to TVL 671 XRP) | 336 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 769 XRP) | 385 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,463 XRP) | 1232 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7193 |
| [VOX](https://xrpl.to/token/rUiHyCL7UuFfn4gRSFFfRyVZgzRtLVQyQc-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,310 XRP) | 655 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 234406 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 307880 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 80946 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11541 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 46688 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 14370 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 91192 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 84178 |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3437 |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 772848 |
| [BOX](https://xrpl.to/token/rhLJ2ma5pScsxVhL5EQr71w3FgASVLwP84-BOX) | SKIP_ENTRY | not new and not top trending | 6841 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
