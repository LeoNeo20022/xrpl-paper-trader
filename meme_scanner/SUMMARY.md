# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-15T14:33:50+00:00** (UTC) · XRP/USD 0.9604 (bitstamp) · last discovery 2026-11-15T14:33:50+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$64.86** | **-35.14** | $3.88 | 6 / $60.98 | $-35.95 | $+0.98 | 19 / 45 (30%) | 70 (64) | -14.80 | +3.13 | 67.53 | -10.50 | $6.80 (0.27912) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$73.78** | **-26.22** | $5.89 | 7 / $67.89 | $-23.88 | $-2.11 | 22 / 52 (30%) | 81 (74) | -3.51 | +1.05 | 76.82 | -1.22 | $8.08 (0.36979) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$81.15** | **-18.85** | $81.15 | 0 / $0.00 | $-18.17 | $+0.00 | 46 / 184 (20%) | 230 (230) | -12.28 | +0.00 | 84.49 | +6.46 | $26.11 (1.10592) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$67.01** | **-32.99** | $5.58 | 6 / $61.42 | $-33.75 | $+1.42 | 64 / 143 (31%) | 213 (207) | -9.39 | -0.67 | 69.77 | -8.34 | $23.37 (1.11016) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 91.74 | +13.63 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$92.52** | **-7.48** | $72.10 | 2 / $20.43 | $-7.16 | $+0.43 | 73 / 98 (43%) | 173 (171) | -0.30 | -0.08 | 96.33 | +18.23 | $23.11 (1.19781) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$74.95** | **-25.05** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | 2026-11-14T18:16 | $10.00 | 0.98 | 0.98 @ 20.3h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 38% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-14T11:58 | $10.00 | 0.96 | 1.00 @ 0.1h | 0.89 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.10 | 1.17 @ 15.0h | 0.99 | top-10 holders own 30% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.08 | 1.08 @ 26.8h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-13T17:29 | $10.00 | 1.15 | 1.15 @ 44.5h | 0.94 | top-10 holders own 31% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-13T05:52 | $10.00 | 1.04 | 1.05 @ 56.6h | 0.98 | only 29% of LP burned (liquidity can be pulled) |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-14T15:49 | $10.00 | 0.86 | 1.00 @ 0.8h | 0.82 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-14T11:43 | $10.00 | 1.00 | 1.00 @ 26.8h | 0.99 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 0.96 | 1.00 @ 0.1h | 0.89 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.17 | 1.17 @ 26.3h | 0.96 | top-10 holders own 31% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-13T02:59 | $10.00 | 0.99 | 0.99 @ 59.4h | 0.97 | only 36% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-13T00:18 | $10.00 | 1.08 | 1.08 @ 62.3h | 0.96 | only 22% of LP burned (liquidity can be pulled) |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-12T23:00 | $10.00 | 1.04 | 1.05 @ 63.5h | 0.98 | only 29% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-15T02:44 | $10.00 | 1.03 | 1.03 @ 11.8h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.18% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-15T01:54 | $10.00 | 0.98 | 0.98 @ 1.2h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-15T01:54 | $10.00 | 1.00 | 1.00 @ 12.7h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 1.66% <= 2.0% |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | 2026-11-15T00:51 | $10.00 | 0.98 | 0.98 @ 13.7h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 38% | slow_scalp: new/top-15 trending, round trip 1.98% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-15T00:20 | $10.00 | 0.98 | 1.01 @ 2.6h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-14T17:30 | $10.00 | 0.98 | 1.00 @ 4.1h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 0.10% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | 2026-11-15T13:41 | $10.00 | 0.95 | 0.99 @ 0.1h | 0.95 | top-10 holders own 38% | dip_bounce: 37.2% below 24h high 7.71565e-06 XRP, age 748.6d |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-15T01:49 | $10.00 | 1.04 | 1.04 @ 12.1h | 1.00 |  | dip_bounce: 18.4% below 24h high 1.49e-10 XRP, age 712.1d |

## How high do they run? (tracking only — no rule uses this)

664 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 98 | 15% |
| ≥ +20% | 31 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 117 of 664

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9259 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8462 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3818 |
| [EXC](https://xrpl.to/token/r3t2bLDT1bxkPLHBH1vk4BFqDPhVJyooEq-EXC) | FAIL_SAFETY | pool too small (xrpl.to TVL 762 XRP) | 381 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 61334 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 28227 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 28789 |
| [BLACKOUT](https://xrpl.to/token/rBBJjs9N54719B12jgqidAK22Z8eiiX9LM-424C41434B4F5554000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 333 XRP) | 167 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 8168 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 400 XRP) | 200 |
| [VOX🗽](https://xrpl.to/token/rBnJZMDB9HZ6UxUoeQc7eaAQHA3Y1v6Hk3-564F58F09F97BD00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,596 XRP) | 798 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 199 XRP too low | 61895 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 193841 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 174 XRP too low | 18651 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,319 XRP) | 659 |
| [EXPOSED](https://xrpl.to/token/rHfKWt7g9DvWL2av6om7jorF2sic3oQWFo-4558504F53454400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 381 XRP) | 190 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 671 XRP) | 336 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5451 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 163152 |
| [BLKSWN](https://xrpl.to/token/rKxvi3eDot8aBACcGjpVyPv7cpYF4AiETJ-424C4B53574E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 28 XRP) | 14 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2067 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,904 XRP) | 1452 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,169 XRP) | 1584 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,525 XRP) | 1263 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 4586 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5516 |
| [VOX](https://xrpl.to/token/rUiHyCL7UuFfn4gRSFFfRyVZgzRtLVQyQc-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,255 XRP) | 627 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 222943 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 308945 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 76171 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2655 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 49989 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 44952 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 25646 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 18218 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 92495 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 84633 |
| [ANCIENT](https://xrpl.to/token/rhAHUcqq28S3HHKXnkj1B2MN5vH2EBNi7b-414E4349454E5400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 236 XRP) | 118 |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 560297 |
| [COY](https://xrpl.to/token/rhVgr9LzpRmccLTKJVBnpk4sJwCYEczgd6-COY) | FAIL_SAFETY | pool too small (xrpl.to TVL 128 XRP) | 64 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
