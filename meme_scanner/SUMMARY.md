# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-25T05:31:28+00:00** (UTC) · XRP/USD 0.9153 (bitstamp) · last discovery 2026-11-25T05:31:28+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$52.74** | **-47.26** | $3.04 | 5 / $49.70 | $-46.77 | $-0.30 | 25 / 57 (30%) | 87 (82) | -22.65 | +1.16 | 57.62 | -20.41 | $8.34 (0.30068) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$61.18** | **-38.82** | $4.14 | 6 / $57.03 | $-35.60 | $-2.97 | 27 / 69 (28%) | 102 (96) | -11.13 | -1.34 | 66.84 | -11.19 | $10.19 (0.41424) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$70.71** | **-29.29** | $31.16 | 4 / $39.55 | $-28.12 | $-0.45 | 74 / 246 (23%) | 324 (320) | -25.41 | -0.35 | 77.26 | -0.78 | $35.74 (1.20337) | 0.8 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$51.76** | **-48.24** | $3.04 | 5 / $48.72 | $-46.27 | $-1.28 | 83 / 182 (31%) | 270 (265) | -21.94 | -0.94 | 56.55 | -21.55 | $29.25 (1.17533) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 96.27 | +18.16 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$87.38** | **-12.62** | $57.83 | 3 / $29.55 | $-11.39 | $-0.45 | 86 / 114 (43%) | 203 (200) | -3.75 | -0.18 | 95.47 | +17.37 | $26.88 (1.28057) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$71.42** | **-28.58** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 1.00 @ 10.7h | 0.98 |  |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 26.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 27.3h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-23T04:59 | $10.00 | 1.03 | 1.14 @ 21.6h | 0.97 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T19:09 | $10.00 | 1.12 | 1.17 @ 31.0h | 0.95 | top-10 holders own 31% |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 26.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 27.3h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.88 | 0.98 @ 0.2h | 0.88 |  |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.99 @ 0.1h | 0.98 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.13 | 1.18 @ 21.7h | 0.96 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 0.91 | 1.00 @ 6.9h | 0.91 | only 22% of LP burned (liquidity can be pulled) |

### scalp — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-25T05:31 | $10.00 | 1.00 | – | – | only 37% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.99 | top-10 holders own 32% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 1.00 | 1.00 @ 0.5h | 1.00 |  |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.99 | top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 0.12% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 27% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 1.00 | 1.00 @ 6.9h | 0.98 | top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 0.98 | 0.99 @ 0.5h | 0.98 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T12:23 | $10.00 | 0.95 | 0.99 @ 10.2h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 1.01 | 1.01 @ 0.1h | 1.01 | top-10 holders own 34% | dip_bounce: 35.4% below 24h high 1.12577e-05 XRP, age 752.2d |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 0.98 | 0.99 @ 0.6h | 0.98 | top-10 holders own 37% | dip_bounce: 18.4% below 24h high 1.87645e-05 XRP, age 540.2d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-11-24T12:23 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  | dip_bounce: 26.5% below 24h high 2.01503e-06 XRP, age 708.5d |

## How high do they run? (tracking only — no rule uses this)

855 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 117 | 14% |
| ≥ +20% | 36 | 4% |
| ≥ +30% | 20 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 139 of 855

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9416 |
| [MEKUAI](https://xrpl.to/token/r3URUgK1WDecKUTPA94s3Pmz6697RdTPWg-4D454B5541490000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,518 XRP) | 759 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 68% (excl. AMM) | 5896 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 447 XRP too low | 3547 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62574 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29360 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,369 XRP) | 1185 |
| [LOVE](https://xrpl.to/token/rBQftsx8vp5ymLv9pJC188BDrZQdZKNYUW-4C4F564500000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 70% (excl. AMM) | 2314 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | 24h volume 466 XRP too low | 62452 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 190952 |
| [NVIDIA](https://xrpl.to/token/rG7onSSfBzGkTCDD4rGGzngXqqYr5iLppk-4E56494449410000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 998 XRP) | 499 |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | SKIP_ENTRY | 24h volume 399 XRP too low | 33527 |
| [OWL](https://xrpl.to/token/rH8oHtbNDueptu9Djoee8J97sTP9hecBww-OWL) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,720 XRP) | 1360 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157618 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2411 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,978 XRP) | 1489 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2042 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,199 XRP) | 1600 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3642 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,271 XRP) | 635 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 891 XRP) | 445 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 374 XRP too low | 42155 |
| [SCRxrp](https://xrpl.to/token/rPyq5PomtBALYQvLVBS2JjUwh9YwmWkPef-5343527872700000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 694 XRP) | 347 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5800 |
| [TOMATO](https://xrpl.to/token/rUBnSCEXo6TRFJNYTYwyAjCPbE6pU2UYmB-544F4D41544F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 520 XRP) | 260 |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | SKIP_ENTRY | not new and not top trending | 2053 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228553 |
| [STORM](https://xrpl.to/token/rZvYqQi3icAPGTHxEGr7SSci8wPCfQWjX-53544F524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 547 XRP) | 274 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 88304 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,350 XRP) | 1175 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51893 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41598 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 20168 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 131745 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 81910 |
| [Phantom](https://xrpl.to/token/rfwDHEbmc28ocKY7KxMa6XgddnUnpYWytg-5068616E746F6D00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 132 XRP) | 66 |
| [xSPECTAR](https://xrpl.to/token/rh5jzTCdMRCVjQ7LT6zucjezC47KATkuvv-7853504543544152000000000000000000000000) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 8234 |
| [WARP](https://xrpl.to/token/rhuQ5tKUHG77J5ovRN4GVSwZJT5SDTZZCD-5741525000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 190 XRP) | 95 |
| [WBC](https://xrpl.to/token/rnFdeZggmwKLXGaHvTL4aTwfEsPPXV5FHa-WBC) | SKIP_ENTRY | not new and not top trending; 24h volume 118 XRP too low | 8208 |
| [SPY](https://xrpl.to/token/rnmJEi7hzEL34R7x48e732qvSnmF5wsLtQ-SPY) | FAIL_SAFETY | top-10 holders own 79% (excl. AMM) | 8812 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
