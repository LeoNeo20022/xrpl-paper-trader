# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-27T08:48:46+00:00** (UTC) · XRP/USD 0.9791 (bitstamp) · last discovery 2026-11-27T08:48:46+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$56.49** | **-43.51** | $6.22 | 5 / $50.27 | $-43.60 | $+0.27 | 27 / 60 (31%) | 92 (87) | -20.67 | -0.38 | 57.69 | -20.34 | $8.84 (0.30108) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$64.73** | **-35.27** | $4.24 | 6 / $60.48 | $-35.50 | $+0.48 | 28 / 74 (27%) | 108 (102) | -12.33 | -0.63 | 66.11 | -11.93 | $10.82 (0.41472) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$72.49** | **-27.51** | $52.75 | 2 / $19.74 | $-26.53 | $-0.26 | 85 / 254 (25%) | 341 (339) | -25.76 | -0.25 | 74.04 | -4.00 | $37.34 (1.20481) | 0.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$56.24** | **-43.76** | $5.04 | 5 / $51.20 | $-44.27 | $+1.20 | 90 / 185 (33%) | 280 (275) | -21.42 | -0.26 | 57.44 | -20.67 | $30.11 (1.17613) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 89.99 | +11.88 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$89.47** | **-10.53** | $59.51 | 3 / $29.96 | $-9.70 | $-0.04 | 89 / 117 (43%) | 209 (206) | -2.17 | -0.35 | 91.38 | +13.28 | $27.40 (1.30101) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$76.40** | **-23.60** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.4h | 1.00 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 1.01 | 1.01 @ 33.0h | 0.97 | only 22% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 0.4h | 0.99 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.4h | 1.00 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 41.3h | 0.97 | top-10 holders own 35% |

### scalp — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [WBC](https://xrpl.to/token/rnFdeZggmwKLXGaHvTL4aTwfEsPPXV5FHa-WBC) | 2026-11-27T08:33 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 |  |
| [BURN](https://xrpl.to/token/rwgNTwrsZKPe7xYCy4emjFAYpgnuioHSkd-4255524E00000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 | top-10 holders own 34% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 27% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 1.04 | 1.04 @ 8.6h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-26T15:56 | $10.00 | 0.97 | 1.00 @ 0.1h | 0.97 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.12% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-26T15:56 | $10.00 | 1.00 | 1.00 @ 16.9h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BURN](https://xrpl.to/token/rwgNTwrsZKPe7xYCy4emjFAYpgnuioHSkd-4255524E00000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 | top-10 holders own 34% | dip_bounce: 15.7% below 24h high 2.77288e-09 XRP, age 720.3d |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 50% | dip_bounce: 15.4% below 24h high 0.0273218 XRP, age 716.3d |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | 2026-11-26T15:56 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 | top-10 holders own 42% | dip_bounce: 39.9% below 24h high 5.59088e-05 XRP, age 649.9d |

## How high do they run? (tracking only — no rule uses this)

888 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 119 | 13% |
| ≥ +20% | 38 | 4% |
| ≥ +30% | 22 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 141 of 888

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9765 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 126 XRP too low | 7786 |
| [CoinMP](https://xrpl.to/token/r3VGG8wwkMfD1Lfn3D3dzEdvUcsupwLGtz-436F696E4D500000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 97 XRP) | 48 |
| [ASC](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-ASC) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,128 XRP) | 1064 |
| [MAHARISHI](https://xrpl.to/token/r43GYf7zhmTQ6xkwdWgTYzFRuxyHapoJEm-4D41484152495348490000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 232 XRP) | 116 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 65% (excl. AMM) | 3745 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63624 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32965 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2247 |
| [TNA](https://xrpl.to/token/rB54t5GDvpGc6frv2D6CpUueVJDBE6qfp3-TNA) | FAIL_SAFETY | pool too small (xrpl.to TVL 154 XRP) | 77 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,304 XRP) | 652 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 155 XRP too low | 61918 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 185792 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 201 XRP) | 101 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 245 XRP too low | 6632 |
| [XLR](https://xrpl.to/token/rG6hnGh7PS2zBQ6sXccoCVR4sTSVoqrErF-XLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 29 XRP) | 15 |
| [NVIDIA](https://xrpl.to/token/rG7onSSfBzGkTCDD4rGGzngXqqYr5iLppk-4E56494449410000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,104 XRP) | 552 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | SKIP_ENTRY | not new and not top trending | 2511 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6841 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 493 XRP too low | 42572 |
| [JELLY](https://xrpl.to/token/rKHsxmaqf2SfcyU9LRi3VyjpAtyg6ZrQMp-4A454C4C59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 22776 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156706 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending; 24h volume 300 XRP too low | 2454 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,160 XRP) | 1580 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,813 XRP) | 1406 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3772 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 429 XRP too low | 42132 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 207 XRP too low | 13637 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228590 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 309432 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 90165 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 172 XRP too low | 10742 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11215 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41186 |
| [NOMAD](https://xrpl.to/token/rfj6nPXU3j9YHA4Tvub9JeaYFrBvomJhSU-4E4F4D4144000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 40 XRP) | 20 |
| [POLICE](https://xrpl.to/token/rfjutsDJfakrhZUPMBe5E65S38eRZEP3yt-504F4C4943450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,095 XRP) | 1048 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 20860 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 130315 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 80463 |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 116525 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
