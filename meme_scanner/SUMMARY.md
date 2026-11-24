# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-24T12:33:44+00:00** (UTC) · XRP/USD 0.9268 (bitstamp) · last discovery 2026-11-24T12:33:44+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$53.31** | **-46.69** | $3.04 | 5 / $50.27 | $-46.77 | $+0.27 | 25 / 57 (30%) | 87 (82) | -22.65 | +1.10 | 57.52 | -20.51 | $8.34 (0.30068) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$62.18** | **-37.82** | $4.14 | 6 / $58.04 | $-35.60 | $-1.96 | 27 / 69 (28%) | 102 (96) | -11.13 | -1.03 | 67.10 | -10.94 | $10.20 (0.41424) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$72.03** | **-27.97** | $62.27 | 1 / $9.76 | $-27.01 | $-0.24 | 74 / 242 (23%) | 317 (316) | -24.42 | -0.23 | 77.72 | -0.31 | $35.00 (1.20293) | 0.2 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$53.14** | **-46.86** | $5.81 | 5 / $47.33 | $-43.49 | $-2.67 | 83 / 178 (32%) | 266 (261) | -21.08 | -0.96 | 57.34 | -20.77 | $28.91 (1.17501) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 95.07 | +16.97 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$86.01** | **-13.99** | $38.82 | 5 / $47.19 | $-10.39 | $-2.81 | 85 / 111 (43%) | 201 (196) | -4.21 | -1.78 | 92.81 | +14.70 | $26.52 (1.28033) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$72.32** | **-27.68** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 10.4h | 0.99 |  |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 10.4h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.99 @ 0.6h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-23T04:59 | $10.00 | 1.05 | 1.14 @ 21.6h | 0.97 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T19:09 | $10.00 | 1.08 | 1.17 @ 31.0h | 0.95 | top-10 holders own 31% |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 10.4h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.99 @ 0.6h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.90 | 0.98 @ 0.2h | 0.90 |  |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.09 | 1.18 @ 21.7h | 0.96 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 0.95 | 1.00 @ 6.9h | 0.94 | only 22% of LP burned (liquidity can be pulled) |

### scalp — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-24T12:23 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 | top-10 holders own 35% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T12:23 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-24T02:10 | $10.00 | 0.99 | 1.00 @ 0.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.98 | 0.98 @ 10.4h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 0.99 | 1.00 @ 0.3h | 0.99 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.05% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 0.97 | 0.99 @ 0.1h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-24T12:23 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 42% | dip_bounce: 36.8% below 24h high 9.73178e-07 XRP, age 764.5d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-11-24T12:23 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  | dip_bounce: 26.5% below 24h high 2.01503e-06 XRP, age 708.5d |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.92 | 1.00 @ 0.1h | 0.92 | top-10 holders own 31% | dip_bounce: 22.0% below 24h high 7.21243e-07 XRP, age 123.4d |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 | top-10 holders own 45% | dip_bounce: 15.2% below 24h high 4.47354e-06 XRP, age 82.1d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.96 | top-10 holders own 31% | dip_bounce: 29.1% below 24h high 2.69848e-05 XRP, age 769.6d |

## How high do they run? (tracking only — no rule uses this)

845 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 116 | 14% |
| ≥ +20% | 36 | 4% |
| ≥ +30% | 20 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 138 of 845

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9273 |
| [Xrpump](https://xrpl.to/token/r3Y8kvAmsEqsHXBHbTvHu1s6azFrQoAN3b-587270756D700000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 933 XRP) | 466 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3924 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62313 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 762 XRP) | 381 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 428 XRP too low | 30047 |
| [RAMP](https://xrpl.to/token/rBsaniKL1PeSLCfah8aSBscbKFPr19AGf9-52414D5000000000000000000000000000000000) | FAIL_SAFETY | pool 1,720 XRP < 2,000 | 1720 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2322 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4513 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 899 XRP) | 450 |
| [NVIDIA](https://xrpl.to/token/rEnsPAKFK7LBVBciaCyQ4mCQtMzkpwsVe2-4E56494449410000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 412 XRP) | 206 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 324 XRP too low | 6696 |
| [NVIDIA](https://xrpl.to/token/rG7onSSfBzGkTCDD4rGGzngXqqYr5iLppk-4E56494449410000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 980 XRP) | 490 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12719 |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | SKIP_ENTRY | 24h volume 467 XRP too low | 33555 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 10158 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 218 XRP too low | 43409 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158755 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2192 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,968 XRP) | 1484 |
| [Exrploit](https://xrpl.to/token/rLSD1svPhf5V5ryhhqGZac6iEcNmUSHH1M-457872706C6F6974000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 85 XRP) | 43 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 419 XRP too low | 10536 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3637 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,351 XRP) | 676 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 919 XRP) | 460 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 292 XRP too low | 42272 |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 217 XRP too low | 15448 |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | SKIP_ENTRY | not new and not top trending | 2053 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228968 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 461 XRP too low | 309793 |
| [STORM](https://xrpl.to/token/rZvYqQi3icAPGTHxEGr7SSci8wPCfQWjX-53544F524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 553 XRP) | 277 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 86712 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 374 XRP too low | 11354 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11420 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51892 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41131 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 25943 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 19980 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 131227 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 82942 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
