# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-26T01:08:50+00:00** (UTC) · XRP/USD 1.2878 (bitstamp) · last discovery 2026-10-26T01:08:50+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$109.49** | **+9.49** | $0.00 | 10 / $109.49 | $+0.00 | $+9.49 | – | 10 (0) | +0.00 | +6.98 | 85.02 | +6.98 | $0.27 (0.00012) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$117.63** | **+17.63** | $2.95 | 11 / $114.67 | $+12.96 | $+4.67 | 2 / 0 (100%) | 13 (2) | +9.89 | +3.40 | 91.34 | +13.31 | $0.79 (0.00032) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$96.59** | **-3.41** | $86.72 | 1 / $9.88 | $-3.26 | $-0.12 | 9 / 20 (31%) | 30 (29) | -2.88 | -0.05 | 75.01 | -3.03 | $2.33 (0.03226) | 0.2 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$98.55** | **-1.45** | $9.54 | 9 / $89.01 | $-0.41 | $-0.99 | 8 / 12 (40%) | 29 (20) | -0.58 | -0.39 | 76.52 | -1.58 | $2.14 (0.08169) | 1.8 |
| breakout | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$92.48** | **-7.52** | $43.54 | 5 / $48.94 | $-6.44 | $-1.06 | 2 / 9 (18%) | 16 (11) | -5.19 | -0.53 | 71.81 | -6.29 | $1.41 (0.03221) | 1.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$110.33** | **+10.33** | $90.50 | 2 / $19.83 | $+10.52 | $-0.17 | 11 / 4 (73%) | 17 (15) | +7.25 | +0.01 | 85.67 | +7.57 | $1.68 (0.02485) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$100.49** | **+0.49** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005041 XRP/tx = max(0.00002, live open-ledger fee 0.005041), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.41 | 1.75 @ 33.8h | 0.86 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.02 @ 9.8h | 0.96 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.10 | 1.15 @ 30.5h | 0.99 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.12 | 1.15 @ 34.5h | 0.95 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.15 | 1.16 @ 35.6h | 0.89 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.99 | 1.01 @ 10.0h | 0.96 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.07 @ 17.9h | 0.96 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.09 | 1.14 @ 23.9h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.97 | 1.00 @ 15.9h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.05 | 1.11 @ 7.3h | 0.98 |  |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.96 | 0.98 @ 0.1h | 0.96 | top-10 holders own 43% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.98 | 1.01 @ 0.9h | 0.98 | only 29% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.02 @ 9.8h | 0.96 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.10 | 1.15 @ 30.5h | 0.99 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.12 | 1.15 @ 34.5h | 0.95 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.15 | 1.16 @ 35.6h | 0.89 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.99 | 1.01 @ 10.0h | 0.96 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.07 @ 17.9h | 0.96 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.09 | 1.14 @ 23.9h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.97 | 1.00 @ 15.9h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.05 | 1.11 @ 7.3h | 0.98 |  |

### scalp — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-26T00:27 | $10.00 | 0.99 | 1.00 @ 0.0h | 0.99 | top-10 holders own 42% |

### slow_scalp — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-26T00:02 | $10.00 | 1.00 | 1.00 @ 0.7h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 0.99 | 1.00 @ 0.8h | 0.99 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 0.99 | 0.99 @ 1.0h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.08% <= 2.0% |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 1.00 | 1.00 @ 1.0h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.62% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-26T00:02 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.00% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-10-25T09:11 | $10.00 | 1.01 | 1.01 @ 15.9h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |

### breakout — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-25T22:45 | $10.00 | 1.01 | 1.02 @ 0.1h | 1.01 | top-10 holders own 42% | breakout: +14.2% in 1h, vol last hour 2349 vs prior 547 / 24h avg 183 XRP |
| [RIBBLE](https://xrpl.to/token/rG7jT6D4fHsipvVmPSbcnvDtFzXwwSR4qx-524942424C450000000000000000000000000000) | 2026-10-25T21:13 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  | breakout: +18.6% in 1h, vol last hour 528 vs prior 0 / 24h avg 22 XRP |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-25T21:08 | $10.00 | 0.93 | 0.99 @ 0.2h | 0.93 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | breakout: +12.3% in 1h, vol last hour 3515 vs prior 0 / 24h avg 147 XRP |
| [OPM](https://xrpl.to/token/rhdG26oZL6QKzSXsVfHGSzdXsTxR6RZ23X-OPM) | 2026-10-25T18:29 | $10.00 | 1.02 | 1.02 @ 0.2h | 0.98 | top-10 holders own 48% | breakout: +12.9% in 1h, vol last hour 663 vs prior 0 / 24h avg 29 XRP |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | 2026-10-25T06:51 | $10.00 | 0.97 | 1.01 @ 3.3h | 0.95 | top-10 holders own 36% | breakout: +14.2% in 1h, vol last hour 742 vs prior 5 / 24h avg 37 XRP |

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FLAME](https://xrpl.to/token/rp5CUgVjAhuthJs8LdjTXFdNWJzfQqc3p2-464C414D45000000000000000000000000000000) | 2026-10-25T22:14 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  | dip_bounce: 17.0% below 24h high 0.0398409 XRP, age 728.9d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-10-25T17:53 | $10.00 | 1.00 | 1.01 @ 5.0h | 0.99 |  | dip_bounce: 15.0% below 24h high 1.73015e-06 XRP, age 678.7d |

## How high do they run? (tracking only — no rule uses this)

77 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 22 | 29% |
| ≥ +20% | 5 | 6% |
| ≥ +30% | 4 | 5% |
| ≥ +50% | 3 | 4% |
| ≥ +100% | 0 | 0% |

Median peak **x1.01** · median hours to peak **1.4h** · best x1.75 · median low x0.98 · ≤ −10% at some point: 14 of 77

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9733 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9665 |
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 1643 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 27600 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,289 XRP) | 644 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,545 XRP) | 773 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 2853 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18532 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2086 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 205216 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 8310 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 11871 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,421 XRP) | 711 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 374 XRP) | 187 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 17895 |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7542 |
| [321BG](https://xrpl.to/token/rJeCmBFjiz1TBD32wSeLEGKXofYxekiwjZ-3332314247000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 177 XRP) | 89 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 79% (excl. AMM) | 10934 |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5257 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 46644 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 155076 |
| [BUZZY](https://xrpl.to/token/rLFDsYQcd7uerRnmYy3sRVTZ6P2uTjfrak-42555A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 202 XRP) | 101 |
| [KOTL](https://xrpl.to/token/rLFucYbEhZ7sLae1QMmvBCAs14eDttZWWS-4B4F544C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,922 XRP) | 961 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,960 XRP) | 980 |
| [XDNA](https://xrpl.to/token/rMKUCQ5G3YJHVJ7pEDncew2WCJpJUGuWC6-58444E4100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 460 XRP) | 230 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,357 XRP) | 679 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3583 |
| [KING](https://xrpl.to/token/rNsibHVgccpuez7iai5ZnQTqccyiLyQbuz-4B494E4700000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 6950 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4449 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,319 XRP) | 659 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4649 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 6789 |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | SKIP_ENTRY | not new and not top trending | 2059 |
| [BTCL](https://xrpl.to/token/rUgeZXZvcXX9UstkspHr1gHJKj89PqogtU-4254434C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,723 XRP < 2,000 | 1723 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 229903 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,506 XRP) | 1253 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81881 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 45884 |
| [TEMPLAR](https://xrpl.to/token/rfGrJ5R5GB1SR48LRBJrD5vkvhXVgUxX4G-54454D504C415200000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 270 XRP) | 135 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 17290 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
