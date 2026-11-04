# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-04T05:40:10+00:00** (UTC) · XRP/USD 1.2732 (bitstamp) · last discovery 2026-11-04T05:40:10+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$97.76** | **-2.24** | $6.26 | 10 / $91.50 | $+6.39 | $-8.50 | 15 / 16 (48%) | 41 (31) | +7.34 | -8.17 | 76.78 | -1.25 | $4.23 (0.19615) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$110.33** | **+10.33** | $1.58 | 11 / $108.75 | $+11.78 | $-1.25 | 17 / 23 (42%) | 51 (40) | +10.72 | -1.95 | 86.65 | +8.62 | $5.45 (0.30618) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$90.85** | **-9.15** | $90.85 | 0 / $0.00 | $-8.72 | $+0.00 | 27 / 93 (22%) | 120 (120) | -4.56 | +0.00 | 71.35 | -6.68 | $13.67 (0.66987) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$96.35** | **-3.65** | $7.08 | 9 / $89.26 | $-2.59 | $-0.74 | 43 / 67 (39%) | 119 (110) | -1.99 | -0.70 | 75.67 | -2.44 | $12.70 (0.50893) | 1.8 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 69.20 | -8.90 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$118.08** | **+18.08** | $36.80 | 8 / $81.27 | $+17.24 | $+1.27 | 50 / 49 (51%) | 107 (99) | +12.12 | +0.36 | 92.74 | +14.63 | $13.56 (0.68191) | 1.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$99.35** | **-0.65** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-02T17:58 | $10.00 | 0.87 | 0.98 @ 0.5h | 0.83 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-02T13:48 | $10.00 | 0.66 | 1.09 @ 7.7h | 0.54 | top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.00 | 1.15 @ 6.9h | 0.93 |  |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T11:47 | $10.00 | 0.92 | 0.98 @ 0.1h | 0.90 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 32.5h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.90 | 1.00 @ 9.5h | 0.88 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 1.00 @ 13.9h | 0.97 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 1.00 @ 25.5h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.71 | 1.00 @ 16.0h | 0.66 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.99 | 1.00 @ 50.2h | 0.93 | only 34% of LP burned (liquidity can be pulled) |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-04T02:54 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-04T02:54 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 1.00 | 1.01 @ 5.0h | 0.98 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.99 | 1.00 @ 1.2h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-03T22:53 | $10.00 | 0.97 | 1.00 @ 0.2h | 0.96 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.97 | 1.00 @ 23.3h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.00 | 1.15 @ 6.9h | 0.93 |  |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 32.5h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.90 | 1.00 @ 9.5h | 0.88 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 1.00 @ 13.9h | 0.97 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T14:51 | $10.00 | 0.99 | 1.00 @ 52.4h | 0.93 | only 34% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-04T01:05 | $10.00 | 1.00 | 1.00 @ 3.7h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.08% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-04T00:33 | $10.00 | 1.01 | 1.01 @ 4.2h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-04T00:13 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.96 | only 34% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.98 | 0.98 @ 5.5h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.98 | 0.98 @ 2.4h | 0.98 | top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.96 | 0.98 @ 0.2h | 0.96 | top-10 holders own 47% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-04T00:02 | $10.00 | 1.00 | 1.00 @ 3.1h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:02 | $10.00 | 1.00 | 1.01 @ 5.0h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.75% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-11-04T03:50 | $10.00 | 0.99 | 0.99 @ 1.3h | 0.99 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 31% | dip_bounce: 21.8% below 24h high 2.83948e-07 XRP, age 715.2d |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | 2026-11-04T01:30 | $10.00 | 0.98 | 0.98 @ 0.9h | 0.98 |  | dip_bounce: 17.9% below 24h high 2.87164e-07 XRP, age 476.0d |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | 2026-11-04T00:28 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 42% of LP burned (liquidity can be pulled) | dip_bounce: 28.4% below 24h high 1.28256e-07 XRP, age 695.0d |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | 2026-11-04T00:02 | $10.00 | 0.99 | 0.99 @ 3.0h | 0.99 | top-10 holders own 50% | dip_bounce: 24.8% below 24h high 1.16673e-05 XRP, age 689.0d |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-11-03T20:43 | $10.00 | 0.99 | 0.99 @ 8.9h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 15.5% below 24h high 0.000148985 XRP, age 678.9d |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-03T12:08 | $10.00 | 1.06 | 1.07 @ 8.9h | 0.99 |  | dip_bounce: 19.4% below 24h high 1.41365e-10 XRP, age 700.5d |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | 2026-11-03T11:26 | $10.00 | 1.02 | 1.04 @ 5.2h | 0.90 | only 0% of LP burned (liquidity can be pulled) | dip_bounce: 22.1% below 24h high 1.02472e-09 XRP, age 1829.5d |
| [RDL](https://xrpl.to/token/r9xvnzUWZJpDu3NA6MKHmKhKJQTRqCRgu9-RDL) | 2026-11-03T07:44 | $10.00 | 1.03 | 1.03 @ 6.9h | 0.97 | top-10 holders own 38% | dip_bounce: 24.0% below 24h high 1.50642e-05 XRP, age 539.3d |

## How high do they run? (tracking only — no rule uses this)

358 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 76 | 21% |
| ≥ +20% | 27 | 8% |
| ≥ +30% | 17 | 5% |
| ≥ +50% | 10 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **3.1h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 81 of 358

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4344 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 12586 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 895 XRP) | 447 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool 1,925 XRP < 2,000 | 1925 |
| [RDL](https://xrpl.to/token/r9xvnzUWZJpDu3NA6MKHmKhKJQTRqCRgu9-RDL) | SKIP_ENTRY | not new and not top trending | 2945 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,376 XRP) | 1188 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 9548 |
| [CSC](https://xrpl.to/token/rCSCManTZ8ME9EoLrSHHYKW8PPwWMgkwr-CSC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 20855 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 287 XRP too low | 62308 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | FAIL_SAFETY | pool 1,955 XRP < 2,000 | 1955 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 20015 |
| [CFH](https://xrpl.to/token/rDTHkzTq3Acxu6QrSLVfHrR3KadFknMkfS-CFH) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,432 XRP) | 716 |
| [DASHER](https://xrpl.to/token/rDb47Na4n1XaBW2CpuScbDJjiaWfKZJcNN-4441534845520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 322 XRP) | 161 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,215 XRP) | 1108 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,161 XRP) | 581 |
| [IOV](https://xrpl.to/token/rEQRwzSJQru4tVSywEWN4cKRK9sPfFo6t3-IOV) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,619 XRP) | 810 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5932 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 425 XRP) | 212 |
| [AOI](https://xrpl.to/token/rG1pyuQPpAKbdUHN2UG1SHYLrfavSB79Jt-AOI) | FAIL_SAFETY | pool too small (xrpl.to TVL 440 XRP) | 220 |
| [1CELL](https://xrpl.to/token/rGCtayZogyWdKj8GAUgGSURd2ThfcyBQhP-3143454C4C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,623 XRP) | 812 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12625 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 9832 |
| [AFFBAL](https://xrpl.to/token/rGu3gexApNkWR3ST7LW1mc1rZACXcxwcfi-41464642414C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,787 XRP) | 894 |
| [LHT](https://xrpl.to/token/rHashLabsu2H6hXDSunL8AcVDmTyE17Z35-LHT) | FAIL_SAFETY | top-10 holders own 70% (excl. AMM) | 28604 |
| [OURO](https://xrpl.to/token/rHwkshB9XXd5Do3V3uqZeJv91mazdVTbEX-4F55524F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 793 XRP) | 396 |
| [LOST](https://xrpl.to/token/rJLvsT5DmzhEa48u3F1coB7bKCgmkGiBQr-4C4F535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 127 XRP) | 64 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4953 |
| [XLT](https://xrpl.to/token/rJW9v4NRtuxSCbsd5ZpgkeTeFSs1NjsM33-XLT) | FAIL_SAFETY | pool too small (xrpl.to TVL 400 XRP) | 200 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 153081 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 1,189 XRP) | 594 |
| [RAD](https://xrpl.to/token/rKpaNoTRdXa48W7emkKgtCLz2MuhEroU7V-RAD) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,710 XRP) | 855 |
| [WOFL](https://xrpl.to/token/rLbGxnf4F9pm3EGg1Uo4eJnYDvA7ariTTG-574F464C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 275 XRP) | 137 |
| [RIDDLE](https://xrpl.to/token/rLdDLeiXu9NeFLnwWWUS93XtRD9zrVuYzf-524944444C450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 869 XRP) | 434 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool 1,660 XRP < 2,000 | 1660 |
| [XCBURN](https://xrpl.to/token/rLtzeDVMkYmWSKhR9MdUmfgY8rRst1fYJx-58434255524E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,083 XRP) | 541 |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2667 |
| [GATO](https://xrpl.to/token/rMn4JCe8FYkWjk4qhKjvuz7Pb9NXwAiMBo-4741544F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 243 XRP) | 122 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4627 |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6348 |
| [YELLOW](https://xrpl.to/token/rPA4Y4qMfntQDF2tYr4UipkbB6HbenW3Hm-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 165 XRP) | 83 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
