# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-05T22:26:06+00:00** (UTC) · XRP/USD 1.2205 (bitstamp) · last discovery 2026-11-05T22:26:06+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$89.14** | **-10.86** | $5.64 | 9 / $83.50 | $-4.20 | $-6.50 | 19 / 22 (46%) | 50 (41) | -4.21 | -0.75 | 73.03 | -5.00 | $5.20 (0.23748) | 1.8 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$104.66** | **+4.66** | $1.80 | 11 / $102.86 | $+12.01 | $-7.14 | 21 / 25 (46%) | 57 (46) | +8.68 | -1.15 | 85.75 | +7.72 | $6.10 (0.31691) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$90.13** | **-9.87** | $90.13 | 0 / $0.00 | $-9.37 | $+0.00 | 29 / 101 (22%) | 130 (130) | -5.04 | +0.00 | 73.84 | -4.19 | $14.85 (0.79043) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$92.89** | **-7.11** | $18.12 | 8 / $74.77 | $-1.50 | $-5.23 | 50 / 72 (41%) | 130 (122) | -2.52 | -0.05 | 76.10 | -2.00 | $14.03 (0.59993) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 72.19 | -5.91 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$110.69** | **+10.69** | $65.10 | 5 / $45.59 | $+15.69 | $-4.41 | 60 / 56 (52%) | 121 (116) | +8.88 | -0.96 | 90.69 | +12.59 | $16.24 (0.91332) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$95.24** | **-4.76** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T18:02 | $10.00 | 1.00 | 1.00 @ 3.8h | 1.00 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 1.01 | 1.02 @ 6.8h | 0.98 | top-10 holders own 43% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-05T11:51 | $10.00 | 1.02 | 1.02 @ 3.3h | 0.99 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.94 | 1.00 @ 10.1h | 0.93 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.98 | 1.00 @ 6.8h | 0.95 | top-10 holders own 46% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.00 @ 8.3h | 0.99 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.00 @ 9.7h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T17:17 | $10.00 | 0.97 | 0.98 @ 2.0h | 0.94 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T05:45 | $10.00 | 0.98 | 1.02 @ 12.8h | 0.97 | only 28% of LP burned (liquidity can be pulled) |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-05T15:39 | $10.00 | 0.98 | 0.99 @ 2.1h | 0.98 | only 23% of LP burned (liquidity can be pulled) |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 1.01 | 1.02 @ 6.8h | 0.98 | top-10 holders own 43% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.94 | 1.00 @ 10.1h | 0.93 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.98 | 1.00 @ 6.8h | 0.95 | top-10 holders own 46% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T11:36 | $10.00 | 0.99 | 1.00 @ 3.5h | 0.99 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T14:53 | $10.00 | 1.00 | 1.03 @ 1.1h | 0.97 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-04T02:54 | $10.00 | 0.96 | 1.00 @ 0.2h | 0.95 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-04T02:54 | $10.00 | 1.00 | 1.00 @ 42.4h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 1.07 | 1.08 @ 38.9h | 0.98 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.98 | 1.02 @ 18.4h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-03T22:53 | $10.00 | 0.94 | 1.00 @ 0.2h | 0.94 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | 2026-11-05T00:38 | $10.00 | 0.98 | 0.98 @ 21.8h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 39% | slow_scalp: new/top-15 trending, round trip 1.98% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-05T00:33 | $10.00 | 1.00 | 1.00 @ 21.2h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.25% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-05T00:15 | $10.00 | 0.99 | 1.00 @ 14.8h | 0.96 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-05T00:15 | $10.00 | 0.98 | 0.99 @ 14.7h | 0.98 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.12% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-05T00:10 | $10.00 | 0.98 | 0.99 @ 14.9h | 0.97 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-05T00:05 | $10.00 | 1.00 | 1.00 @ 2.6h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T00:05 | $10.00 | 1.04 | 1.05 @ 21.6h | 0.94 | top-10 holders own 43% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-05T00:00 | $10.00 | 1.03 | 1.07 @ 15.3h | 0.99 | only 20% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.43% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-05T02:09 | $10.00 | 0.95 | 1.01 @ 2.6h | 0.95 | top-10 holders own 37% | dip_bounce: 44.1% below 24h high 0.000332141 XRP, age 728.1d |
| [Dood](https://xrpl.to/token/rn5Y9N8APtrc7PVqXdMjkG9qvfw7FWi4kC-446F6F6400000000000000000000000000000000) | 2026-11-05T00:00 | $10.00 | 0.99 | 0.99 @ 15.3h | 0.98 | top-10 holders own 37% | dip_bounce: 20.8% below 24h high 1.49954e-08 XRP, age 732.0d |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-05T00:00 | $10.00 | 1.00 | 1.00 @ 21.8h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | dip_bounce: 20.6% below 24h high 0.000226047 XRP, age 745.0d |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T00:00 | $10.00 | 0.94 | 0.98 @ 0.1h | 0.91 | top-10 holders own 46% | dip_bounce: 19.7% below 24h high 0.01 XRP, age 547.9d |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-05T00:00 | $10.00 | 1.00 | 1.00 @ 22.4h | 1.00 |  | dip_bounce: 15.4% below 24h high 0.000130802 XRP, age 749.0d |

## How high do they run? (tracking only — no rule uses this)

403 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 78 | 19% |
| ≥ +20% | 27 | 7% |
| ≥ +30% | 17 | 4% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.01** · median hours to peak **3.4h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 87 of 403

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8904 |
| [DAF](https://xrpl.to/token/r3Zj53idT71Ji35Ti3ZZa9kADesUyCg12x-DAF) | FAIL_SAFETY | pool too small (xrpl.to TVL 317 XRP) | 158 |
| [XMEME](https://xrpl.to/token/r4UPddYeGeZgDhSGPkooURsQtmGda4oYQW-584D454D45000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 261 XRP too low | 8125 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 71067 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32032 |
| [YELLOWNED](https://xrpl.to/token/r7oqe7eitxVxQm2uPbna9xp99WxGu88a5-59454C4C4F574E45440000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 271 XRP) | 136 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 371 XRP too low | 30483 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2085 |
| [CHAOS](https://xrpl.to/token/r9x2gBJncTSo8kK3kf7qE5qYoJCfSQoEkq-4348414F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,728 XRP) | 864 |
| [DRGSLR](https://xrpl.to/token/rBRUGYxmu5Lr9L246JzybRoE7TaL9VznSh-445247534C520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 668 XRP) | 334 |
| [RAMP](https://xrpl.to/token/rBsaniKL1PeSLCfah8aSBscbKFPr19AGf9-52414D5000000000000000000000000000000000) | FAIL_SAFETY | pool 1,893 XRP < 2,000 | 1893 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 321 XRP too low | 62528 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2179 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 187950 |
| [DASHER](https://xrpl.to/token/rDb47Na4n1XaBW2CpuScbDJjiaWfKZJcNN-4441534845520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 265 XRP) | 132 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,020 XRP) | 1010 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5937 |
| [Chippy](https://xrpl.to/token/rEyaXNgExwKwaF8fT6CzofLqSZRtLGFbWZ-4368697070790000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 48 XRP) | 24 |
| [AOI](https://xrpl.to/token/rG1pyuQPpAKbdUHN2UG1SHYLrfavSB79Jt-AOI) | FAIL_SAFETY | pool too small (xrpl.to TVL 292 XRP) | 146 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 10236 |
| [EMPIRE](https://xrpl.to/token/rGKB7t7vaswZJUZ93DVjgkpGK5N8zenzEj-454D504952450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 411 XRP) | 206 |
| [$BUBBLES](https://xrpl.to/token/rGUKfQ2Sm35KFSZ6BuKsjHxgyKSYgV7pzs-24425542424C4553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,129 XRP) | 1065 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | FAIL_SAFETY | top-10 holders own 50% (excl. AMM) | 2035 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 346 XRP too low | 4759 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6978 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 78% (excl. AMM) | 10351 |
| [Yoppinchuk](https://xrpl.to/token/rJrna4pnzfxSH4oAXdhGJxrM4jJgpECEZz-596F7070696E6368756B00000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 81 XRP) | 41 |
| [PINGU](https://xrpl.to/token/rK8HvJcbfggZPLqDyw7upGQi1wju5YnzJz-50494E4755000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,263 XRP) | 631 |
| [MYKEYS](https://xrpl.to/token/rKEYSB2osMYCdan2ce8d1e5pBdftwBCRdx-4D594B4559530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,849 XRP) | 924 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 151660 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 814 XRP) | 407 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,964 XRP) | 1482 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 229 XRP too low | 8546 |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4350 |
| [CREATE](https://xrpl.to/token/rMqZY49eXVxU9rgrHVix7jkLeZcEeni9nU-4352454154450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,010 XRP) | 1505 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4427 |
| [YELLOW](https://xrpl.to/token/rPA4Y4qMfntQDF2tYr4UipkbB6HbenW3Hm-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 99 XRP) | 50 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,192 XRP) | 596 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5835 |
| [SOON](https://xrpl.to/token/rUGGWGtZT7MFt6xrVkLjK4KWiXuPmbEEUt-534F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 133 XRP) | 67 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
