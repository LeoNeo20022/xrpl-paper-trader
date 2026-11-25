# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-25T15:36:17+00:00** (UTC) · XRP/USD 0.8980 (bitstamp) · last discovery 2026-11-25T15:36:17+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$53.65** | **-46.35** | $3.04 | 5 / $50.61 | $-46.77 | $+0.61 | 25 / 57 (30%) | 87 (82) | -22.65 | +3.21 | 59.74 | -18.29 | $8.34 (0.30068) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$60.84** | **-39.16** | $2.90 | 6 / $57.94 | $-36.85 | $-2.06 | 27 / 70 (28%) | 103 (97) | -12.12 | +0.47 | 67.75 | -10.28 | $10.33 (0.41432) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$71.08** | **-28.92** | $41.19 | 3 / $29.89 | $-28.08 | $-0.11 | 75 / 249 (23%) | 327 (324) | -24.25 | -0.24 | 79.15 | +1.12 | $35.97 (1.20365) | 0.6 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$52.41** | **-47.59** | $3.38 | 5 / $49.03 | $-45.92 | $-0.97 | 84 / 183 (31%) | 272 (267) | -20.84 | -0.28 | 58.36 | -19.74 | $29.41 (1.17549) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 98.12 | +20.01 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$87.55** | **-12.45** | $67.35 | 2 / $20.20 | $-11.86 | $+0.20 | 86 / 115 (43%) | 203 (201) | -3.87 | +0.78 | 97.50 | +19.39 | $26.92 (1.28061) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$70.08** | **-29.92** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.99 | 1.00 @ 10.7h | 0.98 |  |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 26.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 37.4h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-23T04:59 | $10.00 | 1.02 | 1.14 @ 21.6h | 0.97 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T19:09 | $10.00 | 1.31 | 1.31 @ 68.4h | 0.95 | top-10 holders own 31% |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 35% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 26.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 37.4h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.87 | 0.98 @ 0.2h | 0.87 |  |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.89 | 0.99 @ 0.1h | 0.89 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.32 | 1.32 @ 59.1h | 0.96 | top-10 holders own 31% |

### scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-25T15:31 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 27% of LP burned (liquidity can be pulled) |
| [JELLY](https://xrpl.to/token/rKHsxmaqf2SfcyU9LRi3VyjpAtyg6ZrQMp-4A454C4C59000000000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-25T15:31 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |
| [JELLY](https://xrpl.to/token/rKHsxmaqf2SfcyU9LRi3VyjpAtyg6ZrQMp-4A454C4C59000000000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 1.00 | 1.00 @ 10.6h | 0.99 | only 27% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 1.01 | 1.01 @ 17.0h | 0.98 | top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 0.98 | 0.99 @ 0.5h | 0.98 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-25T05:01 | $10.00 | 1.00 | 1.01 @ 0.1h | 1.00 | top-10 holders own 34% | dip_bounce: 35.4% below 24h high 1.12577e-05 XRP, age 752.2d |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | 2026-11-24T22:38 | $10.00 | 1.07 | 1.07 @ 16.9h | 0.98 | top-10 holders own 37% | dip_bounce: 18.4% below 24h high 1.87645e-05 XRP, age 540.2d |

## How high do they run? (tracking only — no rule uses this)

860 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 118 | 14% |
| ≥ +20% | 38 | 4% |
| ≥ +30% | 22 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 140 of 860

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9403 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 68% (excl. AMM) | 5790 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3638 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62490 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 33025 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29459 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19666 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,386 XRP) | 1193 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,152 XRP) | 576 |
| [HBAR](https://xrpl.to/token/rBWPqhs7YZdUN2CJcZPQTv4qAvqts3nkBw-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,876 XRP) | 1438 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 395 XRP too low | 62453 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 191821 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 239 XRP) | 119 |
| [XRPuffin](https://xrpl.to/token/rGAxsQvcFuydfwSYEAkovZobp5R2fHZSyH-585250756666696E000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,562 XRP) | 781 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 362 XRP too low | 12885 |
| [OWL](https://xrpl.to/token/rH8oHtbNDueptu9Djoee8J97sTP9hecBww-OWL) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,697 XRP) | 1348 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157603 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2408 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool 1,619 XRP < 2,000 | 1619 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2130 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,171 XRP) | 1585 |
| [CHIMPS](https://xrpl.to/token/rMdQw9azZu94CedtczEpNwXMjB1jCrZMia-4348494D50530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 734 XRP) | 367 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3732 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 994 XRP) | 497 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,096 XRP) | 548 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2679404 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 862 XRP) | 431 |
| [TOMATO](https://xrpl.to/token/rUBnSCEXo6TRFJNYTYwyAjCPbE6pU2UYmB-544F4D41544F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 525 XRP) | 263 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 229208 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 143 XRP too low | 309783 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 88974 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 74689 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 210 XRP too low | 10756 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,365 XRP) | 1183 |
| [CORE](https://xrpl.to/token/rcoreNywaoz2ZCQ8Lg2EbSLnGuRBmun6D-434F524500000000000000000000000000000000) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 10832 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11673 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51740 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41900 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 14057 |
| [NOMAD](https://xrpl.to/token/rfj6nPXU3j9YHA4Tvub9JeaYFrBvomJhSU-4E4F4D4144000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 59 XRP) | 30 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
