# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-23T04:44:55+00:00** (UTC) · XRP/USD 0.9316 (bitstamp) · last discovery 2026-11-23T04:44:55+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$53.61** | **-46.39** | $7.31 | 5 / $46.29 | $-42.50 | $-3.71 | 23 / 55 (29%) | 83 (78) | -16.54 | -4.97 | 57.54 | -20.49 | $8.00 (0.30036) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$62.87** | **-37.13** | $2.97 | 6 / $59.90 | $-36.78 | $-0.10 | 24 / 68 (26%) | 98 (92) | -10.21 | -1.50 | 67.49 | -10.54 | $9.77 (0.41392) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$71.13** | **-28.87** | $41.58 | 3 / $29.55 | $-27.69 | $-0.45 | 70 / 235 (23%) | 308 (305) | -25.39 | -0.39 | 76.35 | -1.68 | $34.04 (1.20213) | 0.6 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$52.21** | **-47.79** | $2.78 | 5 / $49.43 | $-46.52 | $-0.57 | 78 / 178 (30%) | 261 (256) | -22.42 | -0.77 | 56.04 | -22.06 | $28.51 (1.17461) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 94.58 | +16.47 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$87.94** | **-12.06** | $57.78 | 3 / $30.16 | $-11.44 | $+0.16 | 83 / 110 (43%) | 196 (193) | -4.17 | +0.11 | 94.40 | +16.30 | $26.07 (1.28001) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$72.69** | **-27.31** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T19:09 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.98 | top-10 holders own 31% |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 0.60 | 1.01 @ 7.5h | 0.53 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 33% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T23:05 | $10.00 | 0.97 | 1.00 @ 36.6h | 0.97 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.96 | 1.01 @ 49.4h | 0.93 | only 22% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 0.95 | 1.00 @ 6.9h | 0.95 | only 22% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T17:15 | $10.00 | 0.97 | 1.00 @ 43.0h | 0.97 |  |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.99 | 1.00 @ 50.0h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.94 | 1.00 @ 10.7h | 0.93 |  |

### scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 0.97 | 0.98 @ 0.2h | 0.97 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 22% of LP burned (liquidity can be pulled) |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.00 | 1.00 @ 0.2h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-22T23:48 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T18:39 | $10.00 | 0.99 | 1.00 @ 0.6h | 0.98 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.09% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-22T11:59 | $10.00 | 0.95 | 1.00 @ 6.7h | 0.95 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-22T11:59 | $10.00 | 0.99 | 1.00 @ 7.2h | 0.99 | only 27% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [OLX](https://xrpl.to/token/rswiX7wDL25Go4wGdLJK1ssSMpUsRGosJR-OLX) | 2026-11-23T04:29 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 |  | dip_bounce: 15.4% below 24h high 0.000571808 XRP, age 612.1d |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | 2026-11-22T23:48 | $10.00 | 0.99 | 0.99 @ 0.6h | 0.99 | top-10 holders own 50% | dip_bounce: 21.9% below 24h high 0.0309492 XRP, age 712.0d |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 1.03 | 1.03 @ 17.0h | 1.00 | top-10 holders own 34% | dip_bounce: 15.1% below 24h high 0.00365309 XRP, age 748.5d |

## How high do they run? (tracking only — no rule uses this)

826 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 111 | 13% |
| ≥ +20% | 35 | 4% |
| ≥ +30% | 20 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 137 of 826

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7890 |
| [JEZUS](https://xrpl.to/token/r4AgGS5mrckhY4bSTJwCWgpWKsEZGeWm1J-4A455A5553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,984 XRP) | 1492 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 381 XRP too low | 3732 |
| [RKITTY](https://xrpl.to/token/r4Qn3ShtyP2vyqp6TGGsASyRp824XEP7t2-524B495454590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,437 XRP) | 718 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62841 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 785 XRP) | 393 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 375 XRP too low | 30176 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,471 XRP) | 1236 |
| [HBAR](https://xrpl.to/token/rBWPqhs7YZdUN2CJcZPQTv4qAvqts3nkBw-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,778 XRP) | 1389 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 365 XRP too low | 61247 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 307 XRP too low | 4551 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6830 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | SKIP_ENTRY | not new and not top trending | 2571 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 300 XRP too low | 44102 |
| [dfgsdf](https://xrpl.to/token/rKH61s7vXBk9gMCvTtXNjGi7H5jJYkHMHY-6466677364660000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 126 XRP) | 63 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158987 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool 1,725 XRP < 2,000 | 1725 |
| [Exrploit](https://xrpl.to/token/rLSD1svPhf5V5ryhhqGZac6iEcNmUSHH1M-457872706C6F6974000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 111 XRP) | 55 |
| [LFQP](https://xrpl.to/token/rLnh3vjwgjjr6CNBq7ddsdcnCddxhsGLXN-4C46515000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 199 XRP) | 99 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 283 XRP too low | 10639 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,362 XRP) | 1181 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,190 XRP) | 1595 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 271 XRP too low | 42507 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 930 XRP) | 465 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5530 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227133 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 85904 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending; 24h volume 429 XRP too low | 74570 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,115 XRP) | 1057 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 11197 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11059 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 52034 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 43095 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13126 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26141 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 132839 |
| [mXRP](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-6D58525000000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 61170 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 81283 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 5685 |
| [SimonCat](https://xrpl.to/token/rhqsiw5Md18s9K8VJd5xqeZCSLu2zNTvi7-53696D6F6E436174000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 834 XRP) | 417 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
