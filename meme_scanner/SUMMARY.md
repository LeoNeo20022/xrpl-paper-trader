# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-07T17:09:24+00:00** (UTC) · XRP/USD 1.1592 (bitstamp) · last discovery 2026-11-07T17:09:24+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$82.64** | **-17.36** | $4.30 | 9 / $78.34 | $-5.55 | $-11.66 | 19 / 23 (45%) | 51 (42) | -4.59 | -2.35 | 71.29 | -6.74 | $5.31 (0.23756) | 1.8 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$97.39** | **-2.61** | $6.43 | 10 / $90.96 | $+6.65 | $-9.04 | 21 / 31 (40%) | 62 (52) | +8.25 | -2.62 | 84.02 | +5.98 | $6.58 (0.33758) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$91.68** | **-8.32** | $91.68 | 0 / $0.00 | $-7.78 | $+0.00 | 33 / 117 (22%) | 150 (150) | -3.95 | +0.00 | 79.09 | +1.05 | $17.19 (0.85264) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$84.19** | **-15.81** | $7.34 | 8 / $76.85 | $-12.21 | $-3.15 | 54 / 88 (38%) | 150 (142) | -4.33 | -1.93 | 72.63 | -5.48 | $16.43 (0.69712) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 76.01 | -2.10 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$111.13** | **+11.13** | $72.02 | 4 / $39.11 | $+12.66 | $-0.89 | 65 / 68 (49%) | 137 (133) | +11.11 | -0.39 | 95.87 | +17.77 | $18.42 (0.99879) | 0.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$90.46** | **-9.54** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T05:47 | $10.00 | 0.97 | 0.98 @ 5.2h | 0.97 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T18:02 | $10.00 | 1.00 | 1.02 @ 9.8h | 0.97 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 0.91 | 1.02 @ 6.8h | 0.91 | top-10 holders own 43% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-05T11:51 | $10.00 | 0.99 | 1.02 @ 3.3h | 0.99 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.01 @ 53.0h | 0.85 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.93 | 1.00 @ 6.8h | 0.91 | top-10 holders own 46% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.95 | 1.02 @ 29.5h | 0.90 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-05T11:36 | $10.00 | 1.01 | 1.02 @ 35.2h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T17:17 | $10.00 | 0.92 | 0.98 @ 2.0h | 0.92 |  |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-07T14:58 | $10.00 | 1.00 | 1.00 @ 0.0h | 1.00 | top-10 holders own 38% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T02:55 | $10.00 | 0.96 | 0.99 @ 0.1h | 0.96 | only 21% of LP burned (liquidity can be pulled) |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-07T02:55 | $10.00 | 0.97 | 1.01 @ 0.1h | 0.87 | top-10 holders own 46% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T00:12 | $10.00 | 0.98 | 0.99 @ 10.7h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-11-06T22:54 | $10.00 | 0.96 | 0.98 @ 0.4h | 0.93 | top-10 holders own 46% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-05T15:39 | $10.00 | 0.97 | 0.99 @ 2.1h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-05T13:53 | $10.00 | 0.91 | 1.02 @ 6.8h | 0.91 | top-10 holders own 43% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 1.00 | 1.01 @ 53.0h | 0.85 | top-10 holders own 31% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-05T11:36 | $10.00 | 0.93 | 1.00 @ 6.8h | 0.91 | top-10 holders own 46% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-05T11:36 | $10.00 | 0.99 | 1.01 @ 16.2h | 0.96 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XRG](https://xrpl.to/token/rUo5UNKiRGhLq4LVgbCzvx53DH65cgk5Dp-XRG) | 2026-11-07T15:20 | $10.00 | 0.99 | 0.99 @ 1.8h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-07T13:12 | $10.00 | 0.97 | 0.98 @ 0.3h | 0.97 | only 34% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-07T02:45 | $10.00 | 0.98 | 1.00 @ 10.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-07T00:39 | $10.00 | 0.98 | 0.99 @ 0.2h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.91% <= 2.0% |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-07T00:12 | $10.00 | 0.95 | 1.00 @ 0.1h | 0.95 | top-10 holders own 38% | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T00:07 | $10.00 | 0.94 | 0.99 @ 0.1h | 0.94 | only 21% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.08% <= 2.0% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-07T00:07 | $10.00 | 0.97 | 0.98 @ 1.0h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-07T00:02 | $10.00 | 0.98 | 1.01 @ 1.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.30% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | 2026-11-07T04:31 | $10.00 | 0.96 | 0.98 @ 2.5h | 0.95 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 32% | dip_bounce: 19.2% below 24h high 0.5447 XRP, age 1806.2d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-11-07T00:02 | $10.00 | 0.99 | 0.99 @ 17.1h | 0.99 |  | dip_bounce: 24.1% below 24h high 2.14841e-06 XRP, age 691.0d |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-07T00:02 | $10.00 | 0.97 | 1.03 @ 1.1h | 0.97 |  | dip_bounce: 21.7% below 24h high 7.05336e-07 XRP, age 515.6d |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | 2026-11-07T00:02 | $10.00 | 1.04 | 1.05 @ 15.2h | 0.96 | top-10 holders own 36% | dip_bounce: 17.7% below 24h high 0.000146069 XRP, age 535.4d |

## How high do they run? (tracking only — no rule uses this)

461 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 85 | 18% |
| ≥ +20% | 29 | 6% |
| ≥ +30% | 18 | 4% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.1h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 93 of 461

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9966 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8858 |
| [RPR](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-RPR) | FAIL_SAFETY | issuer not blackholed (can still mint) | 4414 |
| [JEZUS](https://xrpl.to/token/r4AgGS5mrckhY4bSTJwCWgpWKsEZGeWm1J-4A455A5553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,278 XRP) | 1139 |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3014 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 71263 |
| [YELLOWNED](https://xrpl.to/token/r7oqe7eitxVxQm2uPbna9xp99WxGu88a5-59454C4C4F574E45440000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 299 XRP) | 150 |
| [TRENCHY](https://xrpl.to/token/r9BdC4AaxZQvydEDQHFACeWAuqDAD6mWUq-5452454E43485900000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 234 XRP) | 117 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool 1,853 XRP < 2,000 | 1853 |
| [SNFLR](https://xrpl.to/token/r9eYMjJj1tiE6NosajXz89HYZSucgq4Fjn-534E464C52000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 778 XRP) | 389 |
| [GHOST](https://xrpl.to/token/rB8FVTvTjLie6tC2kFabczgt6QedWY45k5-47484F5354000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 74 XRP) | 37 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,881 XRP) | 1440 |
| [BAY](https://xrpl.to/token/rBAYxUfBwnijbmsJdYCCNJeKULQQpjjPXa-BAY) | FAIL_SAFETY | top-10 holders own 91% (excl. AMM) | 2383 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62054 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 186429 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6573 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 237105 |
| [EMPIRE](https://xrpl.to/token/rGKB7t7vaswZJUZ93DVjgkpGK5N8zenzEj-454D504952450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 307 XRP) | 154 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,715 XRP < 2,000 | 1715 |
| [DOPAMINE](https://xrpl.to/token/rH7WnpeQrNW6fdacLfgjqFW6DLyMZaUJB-444F50414D494E45000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 64 XRP) | 32 |
| [COCK](https://xrpl.to/token/rH9uUMN2bCnc8D9cFzqpEzZKuyH4vx7R5M-434F434B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,795 XRP) | 897 |
| [ELS](https://xrpl.to/token/rHXuEaRYnnJHbDeuBH5w8yPh5uwNVh5zAg-ELS) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,193 XRP) | 1596 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7115 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,062 XRP) | 531 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 155271 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,104 XRP) | 1552 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 9887 |
| [CREATE](https://xrpl.to/token/rMqZY49eXVxU9rgrHVix7jkLeZcEeni9nU-4352454154450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,221 XRP) | 1110 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending | 14051 |
| [XVR](https://xrpl.to/token/rRCA6gnPkvpKmWwfcYxHQ845gFQ5ThYQe-XVR) | FAIL_SAFETY | pool too small (xrpl.to TVL 988 XRP) | 494 |
| [TEST](https://xrpl.to/token/rU55fFMW8kpTM5k2yWWz1oEnHjHm2CBPsE-5445535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 73 XRP) | 36 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6541 |
| [SOON](https://xrpl.to/token/rUGGWGtZT7MFt6xrVkLjK4KWiXuPmbEEUt-534F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 136 XRP) | 68 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227854 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 79959 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 77692 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 191 XRP too low | 11156 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12807 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 48543 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 46221 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
