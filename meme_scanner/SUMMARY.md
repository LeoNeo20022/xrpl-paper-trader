# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-16T03:50:33+00:00** (UTC) · XRP/USD 0.9596 (bitstamp) · last discovery 2026-11-16T03:50:33+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$65.46** | **-34.54** | $3.88 | 6 / $61.58 | $-35.95 | $+1.58 | 19 / 45 (30%) | 70 (64) | -14.80 | +3.81 | 68.21 | -9.82 | $6.80 (0.27912) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$73.09** | **-26.91** | $5.43 | 7 / $67.66 | $-24.34 | $-2.34 | 23 / 54 (30%) | 84 (77) | -2.09 | -1.03 | 76.17 | -1.86 | $8.58 (0.37003) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$80.13** | **-19.87** | $80.13 | 0 / $0.00 | $-19.18 | $+0.00 | 49 / 191 (20%) | 240 (240) | -12.50 | +0.00 | 83.50 | +5.47 | $27.10 (1.11681) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$69.89** | **-30.11** | $9.20 | 6 / $60.69 | $-30.14 | $+0.69 | 68 / 145 (32%) | 219 (213) | -7.61 | +0.61 | 72.82 | -5.28 | $24.09 (1.11064) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 91.82 | +13.71 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$93.58** | **-6.42** | $65.45 | 3 / $28.13 | $-3.79 | $-1.87 | 75 / 98 (43%) | 176 (173) | +2.56 | -1.83 | 97.52 | +19.41 | $23.56 (1.21797) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$74.88** | **-25.12** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | 2026-11-14T18:16 | $10.00 | 0.98 | 0.98 @ 33.6h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 38% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-14T11:58 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.89 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.18 | 1.19 @ 39.4h | 0.99 | top-10 holders own 30% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.10 | 1.10 @ 37.2h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-13T17:29 | $10.00 | 1.07 | 1.19 @ 56.5h | 0.94 | top-10 holders own 31% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-13T05:52 | $10.00 | 1.07 | 1.07 @ 68.1h | 0.98 | only 29% of LP burned (liquidity can be pulled) |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-16T03:03 | $10.00 | 0.98 | 0.98 @ 0.7h | 0.98 | top-10 holders own 43% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-16T00:28 | $10.00 | 0.97 | 0.98 @ 0.5h | 0.97 |  |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-15T23:03 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 | top-10 holders own 40% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-14T15:49 | $10.00 | 0.89 | 1.03 @ 22.9h | 0.82 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-14T11:43 | $10.00 | 1.00 | 1.00 @ 40.1h | 0.99 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.89 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-14T11:43 | $10.00 | 1.10 | 1.22 @ 38.3h | 0.96 | top-10 holders own 31% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-16T01:59 | $10.00 | 1.00 | 1.00 @ 1.8h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-16T00:53 | $10.00 | 0.99 | 0.99 @ 2.2h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.91% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-16T00:28 | $10.00 | 1.02 | 1.02 @ 1.9h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-15T17:34 | $10.00 | 0.98 | 0.98 @ 0.8h | 0.98 | top-10 holders own 40% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-15T15:22 | $10.00 | 1.02 | 1.02 @ 11.3h | 0.99 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-15T14:43 | $10.00 | 1.06 | 1.06 @ 13.0h | 0.98 | top-10 holders own 44% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-16T02:43 | $10.00 | 0.92 | 1.01 @ 0.2h | 0.92 | top-10 holders own 31% | dip_bounce: 16.7% below 24h high 6.99e-07 XRP, age 115.4d |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-15T16:25 | $10.00 | 0.98 | 0.98 @ 1.9h | 0.98 | top-10 holders own 40% | dip_bounce: 16.3% below 24h high 0.000434238 XRP, age 524.1d |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | 2026-11-15T13:41 | $10.00 | 0.92 | 1.04 @ 3.0h | 0.92 | top-10 holders own 38% | dip_bounce: 37.2% below 24h high 7.71565e-06 XRP, age 748.6d |

## How high do they run? (tracking only — no rule uses this)

686 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 103 | 15% |
| ≥ +20% | 32 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.5h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 117 of 686

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9460 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8542 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3848 |
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4319 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 335 XRP too low | 7470 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63451 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 198 XRP too low | 19695 |
| [VOX🗽](https://xrpl.to/token/rBnJZMDB9HZ6UxUoeQc7eaAQHA3Y1v6Hk3-564F58F09F97BD00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,006 XRP) | 503 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,273 XRP) | 636 |
| [LKH](https://xrpl.to/token/rE2BANxWnyeyGgqyidRSQ9A54t2XVJS55v-4C4B480000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 102 XRP) | 51 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 425 XRP too low | 5535 |
| [1CELL](https://xrpl.to/token/rGCtayZogyWdKj8GAUgGSURd2ThfcyBQhP-3143454C4C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,777 XRP) | 1388 |
| [EXPOSED](https://xrpl.to/token/rHfKWt7g9DvWL2av6om7jorF2sic3oQWFo-4558504F53454400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 385 XRP) | 193 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 488 XRP too low | 44069 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 163155 |
| [BLKSWN](https://xrpl.to/token/rKxvi3eDot8aBACcGjpVyPv7cpYF4AiETJ-424C4B53574E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 27 XRP) | 13 |
| [XLM](https://xrpl.to/token/rLZzuKj7Q8N9syvCvBanu85XNoSodwppa3-XLM) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,115 XRP) | 558 |
| [$BURST](https://xrpl.to/token/rLeGXSzGpGDxBnEPzCbYiUofRTcnHMnGif-2442555253540000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 88% (excl. AMM) | 2434 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2040 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10485 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,348 XRP) | 1174 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3253 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,903 XRP) | 1452 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 4997 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5751 |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 16132 |
| [VOX](https://xrpl.to/token/rUiHyCL7UuFfn4gRSFFfRyVZgzRtLVQyQc-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 979 XRP) | 490 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 222886 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 76359 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11133 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 49883 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 45186 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 25836 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 86432 |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 121913 |
| [GTA6](https://xrpl.to/token/rhgbv9S3FeGyF2RZ3mLAusHg4nTU6H6ZQt-4754413600000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 370 XRP) | 185 |
| [LEDEGENS](https://xrpl.to/token/rhn2eHWzX7nEKhbFccK58QLU7gLsoKx9Fb-4C45444547454E53000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 456 XRP) | 228 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 6477 |
| [GEN](https://xrpl.to/token/rn72vzTgVjcGuUQ9LWfLEpsJJbNgbGZ9LA-GEN) | FAIL_SAFETY | pool too small (xrpl.to TVL 866 XRP) | 433 |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9038 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
