# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-27T00:46:15+00:00** (UTC) · XRP/USD 0.9451 (bitstamp) · last discovery 2026-11-27T00:46:15+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$54.94** | **-45.06** | $6.47 | 5 / $48.47 | $-43.34 | $-1.53 | 27 / 57 (32%) | 89 (84) | -19.38 | -1.47 | 58.13 | -19.90 | $8.59 (0.30084) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$63.16** | **-36.84** | $6.09 | 6 / $57.07 | $-33.66 | $-2.93 | 28 / 70 (29%) | 104 (98) | -9.07 | -3.39 | 66.83 | -11.20 | $10.43 (0.41440) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$71.75** | **-28.25** | $42.06 | 3 / $29.69 | $-27.21 | $-0.31 | 82 / 254 (24%) | 339 (336) | -25.21 | -0.44 | 75.92 | -2.11 | $36.97 (1.20461) | 0.6 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$54.38** | **-45.62** | $5.19 | 5 / $49.19 | $-44.11 | $-0.81 | 90 / 184 (33%) | 279 (274) | -21.03 | -0.74 | 57.54 | -20.56 | $29.99 (1.17605) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 93.23 | +15.13 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$89.33** | **-10.67** | $79.51 | 1 / $9.82 | $-9.70 | $-0.18 | 89 / 117 (43%) | 207 (206) | -2.17 | -0.17 | 94.52 | +16.41 | $27.31 (1.30093) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$73.75** | **-26.25** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 0.97 | 0.99 @ 6.6h | 0.97 | only 22% of LP burned (liquidity can be pulled) |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 1.00 @ 52.2h | 0.97 |  |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 0.98 @ 26.9h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 1.00 @ 37.4h | 0.97 | only 27% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 32.9h | 0.97 | top-10 holders own 35% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 0.98 @ 26.9h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 1.00 @ 37.4h | 0.97 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.87 | 0.98 @ 0.2h | 0.85 |  |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.90 | 0.99 @ 0.1h | 0.89 |  |

### scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-27T00:16 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 27% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T00:11 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 0.99 | 0.99 @ 0.6h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-27T00:11 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-26T15:56 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.97 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.12% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-26T15:56 | $10.00 | 1.00 | 1.00 @ 8.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.97 | 0.99 @ 0.6h | 0.97 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.09% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | 2026-11-26T15:56 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 | top-10 holders own 42% | dip_bounce: 39.9% below 24h high 5.59088e-05 XRP, age 649.9d |

## How high do they run? (tracking only — no rule uses this)

880 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 119 | 14% |
| ≥ +20% | 38 | 4% |
| ≥ +30% | 22 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.1h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 141 of 880

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 160 XRP too low | 7791 |
| [CoinMP](https://xrpl.to/token/r3VGG8wwkMfD1Lfn3D3dzEdvUcsupwLGtz-436F696E4D500000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 106 XRP) | 53 |
| [ASC](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-ASC) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,130 XRP) | 1065 |
| [MAHARISHI](https://xrpl.to/token/r43GYf7zhmTQ6xkwdWgTYzFRuxyHapoJEm-4D41484152495348490000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 297 XRP) | 148 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 65% (excl. AMM) | 3924 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62260 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32979 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2247 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,373 XRP) | 687 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | 24h volume 452 XRP too low | 62020 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 188897 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 173 XRP) | 87 |
| [$ALEX](https://xrpl.to/token/rEwd8T3xMrhJwybaEPCMYY9NeDnxdmpiYw-24414C4558000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,149 XRP) | 1574 |
| [XLR](https://xrpl.to/token/rG6hnGh7PS2zBQ6sXccoCVR4sTSVoqrErF-XLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 40 XRP) | 20 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6856 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 9612 |
| [JELLY](https://xrpl.to/token/rKHsxmaqf2SfcyU9LRi3VyjpAtyg6ZrQMp-4A454C4C59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 22776 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157193 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending; 24h volume 321 XRP too low | 2453 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,972 XRP) | 1486 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,752 XRP) | 1376 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3817 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,793 XRP < 2,000 | 1793 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 274 XRP too low | 42275 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 197 XRP too low | 13616 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228513 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 309432 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 90165 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 195 XRP too low | 10742 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11474 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 40458 |
| [NOMAD](https://xrpl.to/token/rfj6nPXU3j9YHA4Tvub9JeaYFrBvomJhSU-4E4F4D4144000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 43 XRP) | 21 |
| [POLICE](https://xrpl.to/token/rfjutsDJfakrhZUPMBe5E65S38eRZEP3yt-504F4C4943450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,321 XRP) | 1160 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 21624 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 130313 |
| [mXRP](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-6D58525000000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 61151 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 82124 |
| [xSPECTAR](https://xrpl.to/token/rh5jzTCdMRCVjQ7LT6zucjezC47KATkuvv-7853504543544152000000000000000000000000) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 7500 |
| [BOX](https://xrpl.to/token/rhLJ2ma5pScsxVhL5EQr71w3FgASVLwP84-BOX) | SKIP_ENTRY | not new and not top trending | 7364 |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 116470 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
