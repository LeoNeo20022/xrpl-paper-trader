# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-03T12:33:14+00:00** (UTC) · XRP/USD 1.2782 (bitstamp) · last discovery 2026-11-03T12:33:14+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$98.02** | **-1.98** | $6.26 | 10 / $91.76 | $+6.39 | $-8.24 | 15 / 16 (48%) | 41 (31) | +7.34 | -8.25 | 76.68 | -1.35 | $4.23 (0.19615) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$106.96** | **+6.96** | $9.71 | 10 / $97.25 | $+9.86 | $-2.75 | 16 / 20 (44%) | 46 (36) | +9.70 | -3.89 | 83.68 | +5.64 | $4.95 (0.22598) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$93.95** | **-6.05** | $93.95 | 0 / $0.00 | $-5.68 | $+0.00 | 27 / 83 (25%) | 110 (110) | -3.36 | +0.00 | 73.50 | -4.54 | $12.33 (0.58841) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$95.93** | **-4.07** | $45.90 | 5 / $50.03 | $-3.80 | $+0.03 | 40 / 65 (38%) | 110 (105) | -2.19 | -0.90 | 75.05 | -3.05 | $12.00 (0.46804) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 68.93 | -9.17 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$115.00** | **+15.00** | $24.15 | 9 / $90.85 | $+14.56 | $+0.85 | 45 / 46 (49%) | 100 (91) | +11.14 | -0.89 | 89.97 | +11.87 | $12.40 (0.63984) | 1.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$99.74** | **-0.26** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-02T17:58 | $10.00 | 0.84 | 0.98 @ 0.5h | 0.83 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-02T13:48 | $10.00 | 0.75 | 1.09 @ 7.7h | 0.69 | top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.94 | 1.15 @ 6.9h | 0.94 |  |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T11:47 | $10.00 | 0.93 | 0.98 @ 0.1h | 0.90 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.96 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.94 | 1.00 @ 9.5h | 0.93 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.98 | 1.00 @ 13.9h | 0.98 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 15.4h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.70 | 1.00 @ 16.0h | 0.67 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.95 | 0.98 @ 1.0h | 0.95 | only 34% of LP burned (liquidity can be pulled) |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.98 | 0.99 @ 13.1h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.94 | 1.15 @ 6.9h | 0.94 |  |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.96 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.90 | 1.08 @ 2.7h | 0.87 | top-10 holders own 35% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.94 | 1.00 @ 9.5h | 0.93 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.98 | 1.00 @ 13.9h | 0.98 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T14:51 | $10.00 | 0.95 | 0.98 @ 3.2h | 0.95 | only 34% of LP burned (liquidity can be pulled) |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T02:39 | $10.00 | 1.03 | 1.06 @ 13.1h | 0.99 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T02:39 | $10.00 | 0.98 | 1.42 @ 42.6h | 0.90 | top-10 holders own 49% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T22:51 | $10.00 | 0.85 | 1.00 @ 43.6h | 0.85 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-03T00:22 | $10.00 | 0.98 | 0.99 @ 1.1h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-03T00:11 | $10.00 | 0.98 | 1.00 @ 1.5h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-03T00:06 | $10.00 | 0.97 | 1.00 @ 2.3h | 0.97 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.91% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-03T00:01 | $10.00 | 0.99 | 1.00 @ 1.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-03T00:01 | $10.00 | 0.97 | 0.99 @ 0.2h | 0.96 | only 48% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.43% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-03T12:08 | $10.00 | 0.99 | 1.00 @ 0.3h | 0.99 |  | dip_bounce: 19.4% below 24h high 1.41365e-10 XRP, age 700.5d |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | 2026-11-03T11:26 | $10.00 | 0.94 | 0.94 @ 1.1h | 0.90 | only 0% of LP burned (liquidity can be pulled) | dip_bounce: 22.1% below 24h high 1.02472e-09 XRP, age 1829.5d |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-03T08:59 | $10.00 | 0.95 | 0.98 @ 1.4h | 0.95 | top-10 holders own 43% | dip_bounce: 15.5% below 24h high 7.2028e-07 XRP, age 424.9d |
| [RDL](https://xrpl.to/token/r9xvnzUWZJpDu3NA6MKHmKhKJQTRqCRgu9-RDL) | 2026-11-03T07:44 | $10.00 | 0.97 | 0.97 @ 0.2h | 0.97 | top-10 holders own 38% | dip_bounce: 24.0% below 24h high 1.50642e-05 XRP, age 539.3d |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-03T06:47 | $10.00 | 0.99 | 0.99 @ 5.8h | 0.99 | top-10 holders own 35% | dip_bounce: 21.8% below 24h high 1.35347e-05 XRP, age 730.3d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-03T01:24 | $10.00 | 1.03 | 1.03 @ 10.8h | 0.99 | top-10 holders own 30% | dip_bounce: 15.5% below 24h high 2.6961e-05 XRP, age 749.1d |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-03T00:01 | $10.00 | 0.98 | 1.01 @ 1.1h | 0.97 |  | dip_bounce: 15.2% below 24h high 7.70376e-07 XRP, age 511.6d |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-02T18:40 | $10.00 | 0.98 | 0.98 @ 17.9h | 0.98 | top-10 holders own 39% | dip_bounce: 15.6% below 24h high 0.000273498 XRP, age 511.2d |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T13:48 | $10.00 | 1.06 | 1.09 @ 6.8h | 0.99 | only 48% of LP burned (liquidity can be pulled) | dip_bounce: 17.9% below 24h high 0.0161864 XRP, age 734.6d |

## How high do they run? (tracking only — no rule uses this)

331 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 72 | 22% |
| ≥ +20% | 25 | 8% |
| ≥ +30% | 16 | 5% |
| ≥ +50% | 9 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **2.8h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 76 of 331

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9104 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 31203 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,114 XRP) | 557 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30757 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,376 XRP) | 1188 |
| [Fava](https://xrpl.to/token/r9gu97UDNkhnzRCzwZxBrxzHhEioaxtf3j-4661766100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,438 XRP) | 719 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,409 XRP) | 1204 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 419 XRP too low | 18929 |
| [RDL](https://xrpl.to/token/r9xvnzUWZJpDu3NA6MKHmKhKJQTRqCRgu9-RDL) | SKIP_ENTRY | not new and not top trending | 2861 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 821 XRP) | 410 |
| [VOX🗽](https://xrpl.to/token/rBnJZMDB9HZ6UxUoeQc7eaAQHA3Y1v6Hk3-564F58F09F97BD00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 489 XRP) | 245 |
| [CSC](https://xrpl.to/token/rCSCManTZ8ME9EoLrSHHYKW8PPwWMgkwr-CSC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 20990 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 123 XRP too low | 19877 |
| [CFH](https://xrpl.to/token/rDTHkzTq3Acxu6QrSLVfHrR3KadFknMkfS-CFH) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,438 XRP) | 719 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,488 XRP) | 744 |
| [WATER](https://xrpl.to/token/rESKTBrjdPoipRbwvUx78pyroj9rDQHE6i-5741544552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,351 XRP) | 676 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7324 |
| [AFFBAL](https://xrpl.to/token/rGu3gexApNkWR3ST7LW1mc1rZACXcxwcfi-41464642414C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,800 XRP) | 900 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,885 XRP < 2,000 | 1885 |
| [LHT](https://xrpl.to/token/rHashLabsu2H6hXDSunL8AcVDmTyE17Z35-LHT) | FAIL_SAFETY | top-10 holders own 70% (excl. AMM) | 30986 |
| [LOST](https://xrpl.to/token/rJLvsT5DmzhEa48u3F1coB7bKCgmkGiBQr-4C4F535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 123 XRP) | 61 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4725 |
| [XLT](https://xrpl.to/token/rJW9v4NRtuxSCbsd5ZpgkeTeFSs1NjsM33-XLT) | FAIL_SAFETY | pool too small (xrpl.to TVL 555 XRP) | 278 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 50% (excl. AMM) | 3793 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 40983 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 4496 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 154203 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,060 XRP) | 1530 |
| [WOFL](https://xrpl.to/token/rLbGxnf4F9pm3EGg1Uo4eJnYDvA7ariTTG-574F464C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 321 XRP) | 161 |
| [RIDDLE](https://xrpl.to/token/rLdDLeiXu9NeFLnwWWUS93XtRD9zrVuYzf-524944444C450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 860 XRP) | 430 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,012 XRP) | 1506 |
| [XCBURN](https://xrpl.to/token/rLtzeDVMkYmWSKhR9MdUmfgY8rRst1fYJx-58434255524E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,114 XRP) | 557 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,002 XRP) | 1001 |
| [GATO](https://xrpl.to/token/rMn4JCe8FYkWjk4qhKjvuz7Pb9NXwAiMBo-4741544F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 289 XRP) | 144 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,287 XRP) | 643 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4553 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,716 XRP) | 1358 |
| [CABAL](https://xrpl.to/token/rPYSbL1c4uMbpzdL8echLw7guh8o8kZsPJ-434142414C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,133 XRP) | 567 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,309 XRP) | 655 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 40475 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
