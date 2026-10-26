# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-26T21:36:41+00:00** (UTC) · XRP/USD 1.2931 (bitstamp) · last discovery 2026-10-26T21:36:41+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$105.48** | **+5.48** | $0.00 | 10 / $105.48 | $+0.00 | $+5.48 | – | 10 (0) | +0.00 | +3.54 | 81.57 | +3.54 | $0.27 (0.00012) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$112.01** | **+12.01** | $2.95 | 11 / $109.06 | $+12.96 | $-0.94 | 2 / 0 (100%) | 13 (2) | +9.89 | -1.31 | 86.62 | +8.59 | $0.79 (0.00032) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$96.63** | **-3.37** | $96.63 | 0 / $0.00 | $-3.35 | $+0.00 | 9 / 21 (30%) | 30 (30) | -2.92 | +0.00 | 74.72 | -3.31 | $2.35 (0.03230) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$98.32** | **-1.68** | $68.53 | 3 / $29.79 | $-1.41 | $-0.21 | 11 / 16 (41%) | 30 (27) | -1.29 | -0.13 | 76.03 | -2.07 | $2.53 (0.10222) | 0.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.02** | **-11.98** | $58.22 | 3 / $29.80 | $-11.75 | $-0.20 | 3 / 15 (17%) | 21 (18) | -9.31 | -0.13 | 68.07 | -10.04 | $2.08 (0.05298) | 0.6 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$107.40** | **+7.40** | $48.91 | 6 / $58.49 | $+8.95 | $-1.51 | 13 / 8 (62%) | 27 (21) | +5.98 | -1.11 | 83.05 | +4.95 | $2.73 (0.07556) | 1.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$100.91** | **+0.91** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.21 | 1.75 @ 33.8h | 0.86 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.02 @ 9.8h | 0.96 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 0.99 | 1.15 @ 30.5h | 0.98 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.34 | 1.35 @ 54.6h | 0.95 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.94 | 1.16 @ 35.6h | 0.89 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.01 @ 10.0h | 0.96 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.96 | 1.07 @ 17.9h | 0.94 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.07 | 1.14 @ 23.9h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.96 | 1.00 @ 15.9h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | 1.11 @ 7.3h | 0.98 |  |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.77 | 0.98 @ 0.1h | 0.77 | top-10 holders own 43% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.81 | 1.01 @ 0.9h | 0.80 | only 29% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.02 @ 9.8h | 0.96 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 0.99 | 1.15 @ 30.5h | 0.98 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.34 | 1.35 @ 54.6h | 0.95 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.94 | 1.16 @ 35.6h | 0.89 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.00 | 1.01 @ 10.0h | 0.96 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.96 | 1.07 @ 17.9h | 0.94 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.07 | 1.14 @ 23.9h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.96 | 1.00 @ 15.9h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | 1.11 @ 7.3h | 0.98 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | 2026-10-26T00:02 | $10.00 | 1.03 | 1.03 @ 21.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-26T00:02 | $10.00 | 0.99 | 0.99 @ 18.6h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.00% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | 2026-10-26T19:17 | $10.00 | 0.94 | 0.99 @ 0.1h | 0.93 | only 44% of LP burned (liquidity can be pulled); top-10 holders own 44% | breakout: +14.8% in 1h, vol last hour 581 vs prior 6 / 24h avg 149 XRP |
| [Dood](https://xrpl.to/token/rn5Y9N8APtrc7PVqXdMjkG9qvfw7FWi4kC-446F6F6400000000000000000000000000000000) | 2026-10-26T17:58 | $10.00 | 0.99 | 0.99 @ 3.6h | 0.99 | top-10 holders own 37% | breakout: +16.4% in 1h, vol last hour 600 vs prior 0 / 24h avg 26 XRP |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-26T16:53 | $10.00 | 1.06 | 1.07 @ 4.5h | 1.05 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% | breakout: +32.9% in 1h, vol last hour 3109 vs prior 3 / 24h avg 138 XRP |

### dip_bounce — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-26T20:34 | $10.00 | 1.00 | 1.00 @ 1.0h | 0.99 | top-10 holders own 30% | dip_bounce: 15.5% below 24h high 5.58147e-09 XRP, age 664.9d |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-10-26T20:18 | $10.00 | 0.98 | 0.98 @ 0.8h | 0.97 | top-10 holders own 49% | dip_bounce: 16.0% below 24h high 0.00625024 XRP, age 538.8d |
| [FADE](https://xrpl.to/token/r4Peot5JGx6KPRX147oZ2TbRSocLdzBHvy-4641444500000000000000000000000000000000) | 2026-10-26T15:55 | $10.00 | 0.99 | 0.99 @ 3.9h | 0.99 |  | dip_bounce: 22.7% below 24h high 1.07077 XRP, age 734.7d |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-26T15:25 | $10.00 | 0.97 | 1.06 @ 2.5h | 0.96 | only 29% of LP burned (liquidity can be pulled) | dip_bounce: 19.1% below 24h high 3.43635 XRP, age 739.6d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-26T15:25 | $10.00 | 0.94 | 1.03 @ 2.7h | 0.94 | top-10 holders own 42% | dip_bounce: 16.0% below 24h high 0.000184345 XRP, age 718.6d |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-26T13:48 | $10.00 | 0.98 | 1.02 @ 4.7h | 0.97 | only 19% of LP burned (liquidity can be pulled) | dip_bounce: 16.5% below 24h high 7.72181e-05 XRP, age 641.6d |

## How high do they run? (tracking only — no rule uses this)

93 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 24 | 26% |
| ≥ +20% | 6 | 6% |
| ≥ +30% | 5 | 5% |
| ≥ +50% | 3 | 3% |
| ≥ +100% | 0 | 0% |

Median peak **x1.02** · median hours to peak **2.8h** · best x1.75 · median low x0.96 · ≤ −10% at some point: 22 of 93

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9890 |
| [INU](https://xrpl.to/token/r38ghAFYDauA1V7ADEnQ5RCVbcpWvN568Z-INU) | FAIL_SAFETY | pool too small (xrpl.to TVL 228 XRP) | 114 |
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,711 XRP) | 1356 |
| [FADE](https://xrpl.to/token/r4Peot5JGx6KPRX147oZ2TbRSocLdzBHvy-4641444500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2805 |
| [XYZ](https://xrpl.to/token/r4hV1A2vEPvVV8uy6HusdXdxeV8Eb2fYxz-XYZ) | FAIL_SAFETY | pool too small (xrpl.to TVL 450 XRP) | 225 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,057 XRP) | 529 |
| [POOL](https://xrpl.to/token/r9D5RhucFjzBmdXcwc68VRbG2EYr4zqJmF-504F4F4C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,863 XRP) | 1432 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,278 XRP) | 639 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18935 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,920 XRP) | 1460 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 198365 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 474 XRP too low | 19660 |
| [WATER](https://xrpl.to/token/rESKTBrjdPoipRbwvUx78pyroj9rDQHE6i-5741544552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,908 XRP) | 954 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 316 XRP) | 158 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7488 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 255342 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 11820 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,195 XRP) | 1598 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 566 XRP) | 283 |
| [321BG](https://xrpl.to/token/rJeCmBFjiz1TBD32wSeLEGKXofYxekiwjZ-3332314247000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 186 XRP) | 93 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 79% (excl. AMM) | 10008 |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6604 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 2594 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 45203 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 155076 |
| [DROPJR](https://xrpl.to/token/rKzktV2mxZnAggmM7DXcPeS7NX4zUdEqmJ-44524F504A520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,653 XRP) | 1326 |
| [XLM](https://xrpl.to/token/rLZzuKj7Q8N9syvCvBanu85XNoSodwppa3-XLM) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,577 XRP) | 788 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10816 |
| [NFG](https://xrpl.to/token/rNFGBqAKm2xFMsrTDHHJv5Hxq3gfYYWxH1-NFG) | SKIP_ENTRY | not new and not top trending | 5164 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,600 XRP) | 1300 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4118 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3800 |
| [EAPE](https://xrpl.to/token/rPUQrzNnAurx4CckQ59NH2ECbYvRq229sD-4541504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 207 XRP) | 103 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,039 XRP) | 519 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 420 XRP too low | 42090 |
| [SIB](https://xrpl.to/token/rPz9bsto7F4adfUfE5iDQAgW2DWo74YZsw-SIB) | FAIL_SAFETY | pool too small (xrpl.to TVL 957 XRP) | 478 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7389 |
| [BRB](https://xrpl.to/token/rUkuT9TCDTP2oeAPsrCN7XKcHZfdvHvFkG-BRB) | SKIP_ENTRY | not new and not top trending | 5120 |
| [BANKER](https://xrpl.to/token/rUuDFzBDgRt22hMCs5qEwid3YGLTK679cS-42414E4B45520000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 81% (excl. AMM) | 2701 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227758 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
