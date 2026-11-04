# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-04T23:23:02+00:00** (UTC) · XRP/USD 1.3075 (bitstamp) · last discovery 2026-11-04T23:23:02+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$95.38** | **-4.62** | $0.33 | 10 / $95.05 | $+0.47 | $-4.95 | 16 / 17 (48%) | 43 (33) | +2.22 | -6.86 | 72.95 | -5.08 | $4.41 (0.21656) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$112.76** | **+12.76** | $1.77 | 11 / $110.99 | $+11.97 | $+0.99 | 18 / 23 (44%) | 52 (41) | +10.52 | -2.13 | 86.25 | +8.21 | $5.58 (0.30626) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$90.85** | **-9.15** | $90.85 | 0 / $0.00 | $-8.72 | $+0.00 | 27 / 93 (22%) | 120 (120) | -4.56 | +0.00 | 69.48 | -8.55 | $13.68 (0.66987) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$100.75** | **+0.75** | $19.60 | 8 / $81.15 | $-0.08 | $+1.15 | 45 / 67 (40%) | 120 (112) | -0.56 | -0.61 | 77.06 | -1.05 | $12.93 (0.50905) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 67.39 | -10.71 | $2.27 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$120.12** | **+20.12** | $59.14 | 6 / $60.98 | $+19.60 | $+0.98 | 55 / 50 (52%) | 111 (105) | +13.10 | -0.78 | 91.87 | +13.76 | $14.63 (0.72239) | 1.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$102.02** | **+2.02** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T17:17 | $10.00 | 0.98 | 0.98 @ 2.0h | 0.97 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T05:45 | $10.00 | 1.00 | 1.02 @ 12.8h | 0.98 | only 28% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-02T17:58 | $10.00 | 0.87 | 0.98 @ 0.5h | 0.83 |  |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.04 | 1.15 @ 6.9h | 0.93 |  |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T11:47 | $10.00 | 0.92 | 0.98 @ 0.1h | 0.90 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.88 | 0.99 @ 32.5h | 0.88 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.89 | 1.00 @ 9.5h | 0.88 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 1.00 @ 13.9h | 0.97 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.96 | 1.00 @ 25.5h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.63 | 1.00 @ 16.0h | 0.62 |  |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-04T14:53 | $10.00 | 1.01 | 1.03 @ 1.1h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-04T02:54 | $10.00 | 0.97 | 1.00 @ 0.2h | 0.95 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-04T02:54 | $10.00 | 0.99 | 0.99 @ 14.4h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 1.06 | 1.06 @ 18.1h | 0.98 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.99 | 1.02 @ 18.4h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-03T22:53 | $10.00 | 0.97 | 1.00 @ 0.2h | 0.96 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.96 | 1.00 @ 23.3h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.04 | 1.15 @ 6.9h | 0.93 |  |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.88 | 0.99 @ 32.5h | 0.88 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.89 | 1.00 @ 9.5h | 0.88 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 1.00 @ 13.9h | 0.97 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-11-04T15:39 | $10.00 | 0.96 | 1.00 @ 1.9h | 0.96 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-04T01:05 | $10.00 | 0.99 | 1.07 @ 14.4h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.08% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-04T00:33 | $10.00 | 1.01 | 1.02 @ 5.5h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.94 | 0.98 @ 0.1h | 0.94 | only 34% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.99 | 1.00 @ 15.4h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-04T00:08 | $10.00 | 0.97 | 0.98 @ 2.4h | 0.97 | top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | 2026-11-04T00:02 | $10.00 | 1.00 | 1.00 @ 21.4h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-04T00:02 | $10.00 | 1.06 | 1.06 @ 18.2h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.75% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [OPM](https://xrpl.to/token/rhdG26oZL6QKzSXsVfHGSzdXsTxR6RZ23X-OPM) | 2026-11-04T07:02 | $10.00 | 0.99 | 0.99 @ 14.5h | 0.98 | top-10 holders own 46% | dip_bounce: 16.7% below 24h high 3.32458e-05 XRP, age 459.4d |
| [Sketch](https://xrpl.to/token/rKqoG3EJLokTMVEjyFMmTaz9DX2cgJFaLu-536B657463680000000000000000000000000000) | 2026-11-04T05:45 | $10.00 | 0.97 | 0.97 @ 9.9h | 0.97 | top-10 holders own 37% | dip_bounce: 15.2% below 24h high 1.16762e-06 XRP, age 529.4d |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-11-04T03:50 | $10.00 | 0.94 | 0.99 @ 1.3h | 0.93 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 31% | dip_bounce: 21.8% below 24h high 2.83948e-07 XRP, age 715.2d |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | 2026-11-04T01:30 | $10.00 | 0.98 | 0.98 @ 0.9h | 0.98 |  | dip_bounce: 17.9% below 24h high 2.87164e-07 XRP, age 476.0d |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | 2026-11-04T00:28 | $10.00 | 1.02 | 1.02 @ 18.7h | 0.98 | only 42% of LP burned (liquidity can be pulled) | dip_bounce: 28.4% below 24h high 1.28256e-07 XRP, age 695.0d |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | 2026-11-04T00:02 | $10.00 | 1.01 | 1.01 @ 23.0h | 0.99 | top-10 holders own 50% | dip_bounce: 24.8% below 24h high 1.16673e-05 XRP, age 689.0d |

## How high do they run? (tracking only — no rule uses this)

366 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 77 | 21% |
| ≥ +20% | 27 | 7% |
| ≥ +30% | 17 | 5% |
| ≥ +50% | 10 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **3.4h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 82 of 366

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9242 |
| [SirPEPE](https://xrpl.to/token/r3H7UVBHS4W71EjxYBD9gegRP5G8c8hDrg-5369725045504500000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,405 XRP) | 703 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 363 XRP too low | 4384 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 66241 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 31923 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 821 XRP) | 410 |
| [YELLOWNED](https://xrpl.to/token/r7oqe7eitxVxQm2uPbna9xp99WxGu88a5-59454C4C4F574E45440000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 275 XRP) | 137 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,165 XRP) | 582 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30713 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool 1,850 XRP < 2,000 | 1850 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2385 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 20528 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,377 XRP) | 1188 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 329 XRP too low | 62383 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 137 XRP too low | 19948 |
| [DASHER](https://xrpl.to/token/rDb47Na4n1XaBW2CpuScbDJjiaWfKZJcNN-4441534845520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 242 XRP) | 121 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,106 XRP) | 1053 |
| [AOI](https://xrpl.to/token/rG1pyuQPpAKbdUHN2UG1SHYLrfavSB79Jt-AOI) | FAIL_SAFETY | pool too small (xrpl.to TVL 366 XRP) | 183 |
| [1CELL](https://xrpl.to/token/rGCtayZogyWdKj8GAUgGSURd2ThfcyBQhP-3143454C4C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,867 XRP) | 934 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12565 |
| [AWU](https://xrpl.to/token/rGrxMm95RzEcfWBAYgYrkvN8ajge9PanGH-AWU) | SKIP_ENTRY | not new and not top trending | 3342 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,685 XRP < 2,000 | 1685 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4617 |
| [XLT](https://xrpl.to/token/rJW9v4NRtuxSCbsd5ZpgkeTeFSs1NjsM33-XLT) | FAIL_SAFETY | pool too small (xrpl.to TVL 223 XRP) | 111 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 10995 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 153447 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 706 XRP) | 353 |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5342 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,195 XRP) | 1598 |
| [XCBURN](https://xrpl.to/token/rLtzeDVMkYmWSKhR9MdUmfgY8rRst1fYJx-58434255524E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,187 XRP) | 593 |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2712 |
| [GATO](https://xrpl.to/token/rMn4JCe8FYkWjk4qhKjvuz7Pb9NXwAiMBo-4741544F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 237 XRP) | 119 |
| [YELLOW](https://xrpl.to/token/rPA4Y4qMfntQDF2tYr4UipkbB6HbenW3Hm-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam; pool too small (xrpl.to TVL 99 XRP) | 50 |
| [XRT](https://xrpl.to/token/rPvuCxw1m8u2SWTqtRN6ZEcb1xPbU4cPFR-XRT) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,640 XRP) | 1320 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,212 XRP) | 606 |
| [ELEVNFIVE](https://xrpl.to/token/rU4gxrLrgZAEEPQuTQ3KhaT1hD8DGXKyTi-454C45564E464956450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,397 XRP) | 1199 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5315 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5347 |
| [SOON](https://xrpl.to/token/rUGGWGtZT7MFt6xrVkLjK4KWiXuPmbEEUt-534F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 192 XRP) | 96 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 80539 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
