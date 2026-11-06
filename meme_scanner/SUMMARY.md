# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-06T00:36:19+00:00** (UTC) · XRP/USD 1.2180 (bitstamp) · last discovery 2026-11-06T00:36:19+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$88.40** | **-11.60** | $5.64 | 9 / $82.76 | $-4.20 | $-7.24 | 19 / 22 (46%) | 50 (41) | -4.21 | -1.21 | 72.58 | -5.45 | $5.20 (0.23748) | 1.8 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$103.81** | **+3.81** | $1.80 | 11 / $102.00 | $+12.01 | $-8.00 | 21 / 25 (46%) | 57 (46) | +8.68 | -1.68 | 85.23 | +7.20 | $6.10 (0.31691) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$89.49** | **-10.51** | $20.13 | 7 / $69.36 | $-9.37 | $-0.64 | 29 / 101 (22%) | 137 (130) | -5.04 | -0.85 | 73.47 | -4.56 | $15.30 (0.79071) | 1.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$91.73** | **-8.27** | $33.03 | 6 / $58.70 | $-6.55 | $-1.30 | 50 / 79 (39%) | 135 (129) | -2.60 | -0.70 | 75.31 | -2.79 | $14.69 (0.66033) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 72.34 | -5.76 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$109.72** | **+9.72** | $71.31 | 4 / $38.41 | $+11.89 | $-1.59 | 60 / 60 (50%) | 124 (120) | +8.09 | -0.87 | 90.08 | +11.98 | $16.59 (0.91360) | 0.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$95.04** | **-4.96** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.010000 XRP/tx = max(0.00002, live open-ledger fee 0.395731), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T18:02 | $10.00 | 1.00 | 1.00 @ 3.8h | 1.00 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 0.99 | 1.02 @ 6.8h | 0.98 | top-10 holders own 43% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-05T11:51 | $10.00 | 1.01 | 1.02 @ 3.3h | 0.99 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.94 | 1.00 @ 10.1h | 0.93 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.95 | 1.00 @ 6.8h | 0.95 | top-10 holders own 46% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.00 @ 8.3h | 0.99 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.00 @ 9.7h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T17:17 | $10.00 | 0.97 | 0.98 @ 2.0h | 0.94 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T05:45 | $10.00 | 0.97 | 1.02 @ 12.8h | 0.97 | only 28% of LP burned (liquidity can be pulled) |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-05T15:39 | $10.00 | 0.97 | 0.99 @ 2.1h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 0.99 | 1.02 @ 6.8h | 0.98 | top-10 holders own 43% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.94 | 1.00 @ 10.1h | 0.93 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.95 | 1.00 @ 6.8h | 0.95 | top-10 holders own 46% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T11:36 | $10.00 | 0.99 | 1.00 @ 3.5h | 0.99 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T14:53 | $10.00 | 1.00 | 1.03 @ 1.1h | 0.97 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-04T02:54 | $10.00 | 0.96 | 1.00 @ 0.2h | 0.95 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-04T02:54 | $10.00 | 1.00 | 1.00 @ 42.4h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 1.07 | 1.08 @ 38.9h | 0.98 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.97 | 1.02 @ 18.4h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-03T22:53 | $10.00 | 0.94 | 1.00 @ 0.2h | 0.94 |  |

### scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-06T00:08 | $10.00 | 0.98 | 0.98 @ 0.4h | 0.98 | top-10 holders own 35% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.97 | 0.98 @ 0.3h | 0.97 | top-10 holders own 43% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-06T00:03 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [FLAME](https://xrpl.to/token/rp5CUgVjAhuthJs8LdjTXFdNWJzfQqc3p2-464C414D45000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 | top-10 holders own 30% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.98 | 0.99 @ 0.5h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-06T00:03 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.98 | 0.98 @ 0.5h | 0.98 |  |

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-06T00:36 | $10.00 | 1.00 | – | – |  | slow_scalp: new/top-15 trending, round trip 0.25% <= 2.0% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-06T00:13 | $10.00 | 0.98 | 0.98 @ 0.3h | 0.98 | top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-06T00:13 | $10.00 | 0.98 | 0.98 @ 0.3h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FLAME](https://xrpl.to/token/rp5CUgVjAhuthJs8LdjTXFdNWJzfQqc3p2-464C414D45000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.98 | 0.99 @ 0.5h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.40% <= 2.0% |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | 2026-11-05T00:38 | $10.00 | 0.98 | 0.98 @ 23.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 39% | slow_scalp: new/top-15 trending, round trip 1.98% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.97 | 0.97 @ 0.1h | 0.97 | top-10 holders own 36% | dip_bounce: 33.8% below 24h high 0.0290687 XRP, age 7.4d |
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 30% | dip_bounce: 28.5% below 24h high 5.61477e-09 XRP, age 675.0d |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | 2026-11-06T00:03 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 | top-10 holders own 42% | dip_bounce: 20.3% below 24h high 4.31937e-05 XRP, age 629.2d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-05T02:09 | $10.00 | 0.93 | 1.01 @ 2.6h | 0.93 | top-10 holders own 37% | dip_bounce: 44.1% below 24h high 0.000332141 XRP, age 728.1d |

## How high do they run? (tracking only — no rule uses this)

415 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 78 | 19% |
| ≥ +20% | 27 | 7% |
| ≥ +30% | 17 | 4% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.3h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 87 of 415

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8714 |
| [DAF](https://xrpl.to/token/r3Zj53idT71Ji35Ti3ZZa9kADesUyCg12x-DAF) | FAIL_SAFETY | pool too small (xrpl.to TVL 317 XRP) | 158 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 71671 |
| [YELLOWNED](https://xrpl.to/token/r7oqe7eitxVxQm2uPbna9xp99WxGu88a5-59454C4C4F574E45440000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 276 XRP) | 138 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30403 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2046 |
| [CHAOS](https://xrpl.to/token/r9x2gBJncTSo8kK3kf7qE5qYoJCfSQoEkq-4348414F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,728 XRP) | 864 |
| [RAMP](https://xrpl.to/token/rBsaniKL1PeSLCfah8aSBscbKFPr19AGf9-52414D5000000000000000000000000000000000) | FAIL_SAFETY | pool 1,899 XRP < 2,000 | 1899 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 201 XRP too low | 62530 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2179 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 188024 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19604 |
| [DASHER](https://xrpl.to/token/rDb47Na4n1XaBW2CpuScbDJjiaWfKZJcNN-4441534845520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 265 XRP) | 132 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,020 XRP) | 1010 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5944 |
| [Chippy](https://xrpl.to/token/rEyaXNgExwKwaF8fT6CzofLqSZRtLGFbWZ-4368697070790000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 48 XRP) | 24 |
| [AOI](https://xrpl.to/token/rG1pyuQPpAKbdUHN2UG1SHYLrfavSB79Jt-AOI) | FAIL_SAFETY | pool too small (xrpl.to TVL 289 XRP) | 144 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 10236 |
| [EMPIRE](https://xrpl.to/token/rGKB7t7vaswZJUZ93DVjgkpGK5N8zenzEj-454D504952450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 321 XRP) | 160 |
| [$BUBBLES](https://xrpl.to/token/rGUKfQ2Sm35KFSZ6BuKsjHxgyKSYgV7pzs-24425542424C4553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,134 XRP) | 1067 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 15886 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | FAIL_SAFETY | top-10 holders own 50% (excl. AMM) | 2035 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 299 XRP too low | 4756 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6978 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 78% (excl. AMM) | 10344 |
| [Yoppinchuk](https://xrpl.to/token/rJrna4pnzfxSH4oAXdhGJxrM4jJgpECEZz-596F7070696E6368756B00000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 81 XRP) | 41 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 399 XRP too low | 40893 |
| [PINGU](https://xrpl.to/token/rK8HvJcbfggZPLqDyw7upGQi1wju5YnzJz-50494E4755000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,263 XRP) | 631 |
| [MYKEYS](https://xrpl.to/token/rKEYSB2osMYCdan2ce8d1e5pBdftwBCRdx-4D594B4559530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,648 XRP) | 824 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 152472 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 826 XRP) | 413 |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4998 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,988 XRP) | 1494 |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4398 |
| [CREATE](https://xrpl.to/token/rMqZY49eXVxU9rgrHVix7jkLeZcEeni9nU-4352454154450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,040 XRP) | 1520 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4427 |
| [YELLOW](https://xrpl.to/token/rPA4Y4qMfntQDF2tYr4UipkbB6HbenW3Hm-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 99 XRP) | 50 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,192 XRP) | 596 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5836 |
| [SOON](https://xrpl.to/token/rUGGWGtZT7MFt6xrVkLjK4KWiXuPmbEEUt-534F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 133 XRP) | 67 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
