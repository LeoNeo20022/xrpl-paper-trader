# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-27T18:43:54+00:00** (UTC) · XRP/USD 0.9455 (bitstamp) · last discovery 2026-11-27T18:43:54+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$55.52** | **-44.48** | $6.22 | 5 / $49.30 | $-43.60 | $-0.70 | 27 / 60 (31%) | 92 (87) | -20.67 | +0.42 | 58.72 | -19.31 | $8.84 (0.30108) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$63.46** | **-36.54** | $4.24 | 6 / $59.22 | $-35.50 | $-0.78 | 28 / 74 (27%) | 108 (102) | -12.33 | +0.23 | 67.12 | -10.91 | $10.81 (0.41472) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$71.75** | **-28.25** | $51.90 | 2 / $19.85 | $-27.38 | $-0.15 | 85 / 256 (25%) | 343 (341) | -25.97 | -0.11 | 75.88 | -2.15 | $37.48 (1.20497) | 0.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$54.64** | **-45.36** | $5.41 | 5 / $49.24 | $-43.90 | $-0.76 | 92 / 185 (33%) | 282 (277) | -21.04 | -0.47 | 57.79 | -20.31 | $30.18 (1.17629) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 93.19 | +15.09 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$88.01** | **-11.99** | $59.23 | 3 / $28.78 | $-9.97 | $-1.22 | 89 / 118 (43%) | 210 (207) | -2.47 | -0.51 | 93.09 | +14.98 | $27.46 (1.30109) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$73.78** | **-26.22** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.01 | 1.01 @ 10.4h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 10.2h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.07 | 1.07 @ 10.4h | 1.00 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 1.00 | 1.01 @ 33.1h | 0.97 | only 22% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 0.98 | 0.99 @ 0.4h | 0.98 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.01 | 1.01 @ 10.4h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 0.99 | 0.99 @ 10.2h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.07 | 1.07 @ 10.4h | 1.00 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 51.2h | 0.97 | top-10 holders own 35% |

### scalp — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-27T18:18 | $10.00 | 1.00 | 1.00 @ 0.4h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T18:18 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 22% of LP burned (liquidity can be pulled) |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T18:18 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |
| [BURN](https://xrpl.to/token/rwgNTwrsZKPe7xYCy4emjFAYpgnuioHSkd-4255524E00000000000000000000000000000000) | 2026-11-27T18:18 | $10.00 | 1.00 | 1.00 @ 0.4h | 1.00 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.10% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.97 | only 27% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 1.03 | 1.04 @ 8.7h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-27T18:18 | $10.00 | 0.97 | 0.99 @ 0.1h | 0.97 | top-10 holders own 31% | dip_bounce: 24.7% below 24h high 1.85909e-05 XRP, age 773.8d |
| [BURN](https://xrpl.to/token/rwgNTwrsZKPe7xYCy4emjFAYpgnuioHSkd-4255524E00000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 10.4h | 1.00 | top-10 holders own 34% | dip_bounce: 15.7% below 24h high 2.77288e-09 XRP, age 720.3d |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | 2026-11-27T08:18 | $10.00 | 0.98 | 0.99 @ 0.2h | 0.98 | top-10 holders own 50% | dip_bounce: 15.4% below 24h high 0.0273218 XRP, age 716.3d |

## How high do they run? (tracking only — no rule uses this)

893 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 119 | 13% |
| ≥ +20% | 38 | 4% |
| ≥ +30% | 22 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.1h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 141 of 893

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9758 |
| [BG123HEART](https://xrpl.to/token/r3LXwcvxiENopYX9UuFcKxmRJ1Q6YZAczx-4247313233484541525400000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 273 XRP) | 137 |
| [CoinMP](https://xrpl.to/token/r3VGG8wwkMfD1Lfn3D3dzEdvUcsupwLGtz-436F696E4D500000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 83 XRP) | 41 |
| [MAHARISHI](https://xrpl.to/token/r43GYf7zhmTQ6xkwdWgTYzFRuxyHapoJEm-4D41484152495348490000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 186 XRP) | 93 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 65% (excl. AMM) | 3314 |
| [XNODE](https://xrpl.to/token/r4CSnJij8KscghxxY4nybuBXiexdQgxn31-584E4F4445000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 42 XRP) | 21 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63760 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32792 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29486 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2392 |
| [TNA](https://xrpl.to/token/rB54t5GDvpGc6frv2D6CpUueVJDBE6qfp3-TNA) | FAIL_SAFETY | pool too small (xrpl.to TVL 151 XRP) | 76 |
| [BG123OLIVE](https://xrpl.to/token/rBWguRQdj4m7gCr1GJJgJ9Xa5pK5jK8U2M-42473132334F4C49564500000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 228 XRP) | 114 |
| [XBAR](https://xrpl.to/token/rBbpmcuvmokBb7yFR6ZE8fNHbBLskyR8Ar-5842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,797 XRP) | 899 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 140 XRP too low | 61921 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | FAIL_SAFETY | pool 1,990 XRP < 2,000 | 1990 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 186318 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 105 XRP too low | 19791 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 180 XRP) | 90 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 285 XRP too low | 6650 |
| [XLR](https://xrpl.to/token/rG6hnGh7PS2zBQ6sXccoCVR4sTSVoqrErF-XLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 13 XRP) | 6 |
| [NVIDIA](https://xrpl.to/token/rG7onSSfBzGkTCDD4rGGzngXqqYr5iLppk-4E56494449410000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 565 XRP) | 283 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | SKIP_ENTRY | not new and not top trending | 2504 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 9713 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42585 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 969 XRP) | 484 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156592 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,146 XRP) | 1573 |
| [XRdoge](https://xrpl.to/token/rLqUC2eCPohYvJCEBJ77eCCqVL2uEiczjA-5852646F67650000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10029 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3788 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,274 XRP) | 637 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 303 XRP too low | 42137 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227983 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 90928 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 194 XRP too low | 10753 |
| [RACC](https://xrpl.to/token/ratLwDashNhXpNHP8XEhX2bf8CF1tGtUvu-5241434300000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,170 XRP) | 585 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11184 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51146 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41186 |
| [NOMAD](https://xrpl.to/token/rfj6nPXU3j9YHA4Tvub9JeaYFrBvomJhSU-4E4F4D4144000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 24 XRP) | 12 |
| [POLICE](https://xrpl.to/token/rfjutsDJfakrhZUPMBe5E65S38eRZEP3yt-504F4C4943450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,419 XRP) | 1209 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
