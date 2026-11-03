# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-03T04:40:14+00:00** (UTC) · XRP/USD 1.2528 (bitstamp) · last discovery 2026-11-03T04:40:14+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$100.88** | **+0.88** | $6.26 | 10 / $94.62 | $+6.39 | $-5.38 | 15 / 16 (48%) | 41 (31) | +7.34 | -4.50 | 80.53 | +2.49 | $4.22 (0.19615) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$108.64** | **+8.64** | $9.71 | 10 / $98.93 | $+9.86 | $-1.07 | 16 / 20 (44%) | 46 (36) | +9.70 | -1.00 | 86.72 | +8.69 | $4.95 (0.22598) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$93.95** | **-6.05** | $93.95 | 0 / $0.00 | $-5.68 | $+0.00 | 27 / 83 (25%) | 110 (110) | -3.36 | +0.00 | 74.99 | -3.04 | $12.32 (0.58841) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$96.41** | **-3.59** | $27.35 | 7 / $69.06 | $-2.35 | $-0.94 | 40 / 63 (39%) | 110 (103) | -1.01 | -0.94 | 76.96 | -1.15 | $11.89 (0.46796) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.33 | -7.77 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$116.62** | **+16.62** | $65.89 | 5 / $50.73 | $+16.29 | $+0.73 | 45 / 44 (51%) | 94 (89) | +12.46 | +0.49 | 93.09 | +14.99 | $11.83 (0.61924) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.76** | **-2.24** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-02T17:58 | $10.00 | 0.84 | 0.98 @ 0.5h | 0.83 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-02T13:48 | $10.00 | 0.93 | 1.09 @ 7.7h | 0.84 | top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.02 | 1.15 @ 6.9h | 1.00 |  |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T11:47 | $10.00 | 0.94 | 0.98 @ 0.1h | 0.90 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.95 | 1.00 @ 9.5h | 0.95 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 1.00 | 1.00 @ 13.9h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 15.4h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.84 | 1.00 @ 16.0h | 0.84 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.96 | 0.98 @ 1.0h | 0.96 | only 34% of LP burned (liquidity can be pulled) |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.98 | 0.99 @ 13.1h | 0.96 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.02 | 1.15 @ 6.9h | 1.00 |  |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.98 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.91 | 1.08 @ 2.7h | 0.87 | top-10 holders own 35% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.95 | 1.00 @ 9.5h | 0.95 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 1.00 | 1.00 @ 13.9h | 0.99 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T14:51 | $10.00 | 0.96 | 0.98 @ 3.2h | 0.96 | only 34% of LP burned (liquidity can be pulled) |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T02:39 | $10.00 | 1.00 | 1.06 @ 13.1h | 0.99 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T02:39 | $10.00 | 1.21 | 1.42 @ 42.6h | 0.99 | top-10 holders own 49% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T22:51 | $10.00 | 0.86 | 1.00 @ 43.6h | 0.85 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-03T00:22 | $10.00 | 0.99 | 0.99 @ 1.1h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-03T00:11 | $10.00 | 0.99 | 1.00 @ 1.5h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-03T00:06 | $10.00 | 0.98 | 0.99 @ 0.7h | 0.97 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.24% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-03T00:06 | $10.00 | 0.99 | 1.00 @ 2.3h | 0.99 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.91% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-03T00:01 | $10.00 | 0.95 | 0.99 @ 0.2h | 0.95 | only 20% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.17% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-03T00:01 | $10.00 | 0.99 | 1.00 @ 1.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-03T00:01 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 48% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.43% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-03T01:24 | $10.00 | 1.03 | 1.03 @ 3.3h | 0.99 | top-10 holders own 30% | dip_bounce: 15.5% below 24h high 2.6961e-05 XRP, age 749.1d |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-03T00:01 | $10.00 | 0.98 | 1.01 @ 1.1h | 0.98 |  | dip_bounce: 15.2% below 24h high 7.70376e-07 XRP, age 511.6d |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-02T18:40 | $10.00 | 0.98 | 0.98 @ 10.0h | 0.98 | top-10 holders own 39% | dip_bounce: 15.6% below 24h high 0.000273498 XRP, age 511.2d |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T13:48 | $10.00 | 1.08 | 1.09 @ 6.8h | 0.99 | only 48% of LP burned (liquidity can be pulled) | dip_bounce: 17.9% below 24h high 0.0161864 XRP, age 734.6d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-11-02T05:50 | $10.00 | 0.99 | 1.00 @ 10.5h | 0.99 |  | dip_bounce: 15.7% below 24h high 9.14194e-06 XRP, age 744.2d |

## How high do they run? (tracking only — no rule uses this)

325 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 72 | 22% |
| ≥ +20% | 25 | 8% |
| ≥ +30% | 16 | 5% |
| ≥ +50% | 9 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **3.1h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 75 of 325

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9149 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9495 |
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,650 XRP) | 1325 |
| [$TRUMP](https://xrpl.to/token/r3iM2Ffe9Krgn6n3qhHj2oe8kiJMKB63s7-245452554D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2382 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 31242 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32016 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,175 XRP) | 1088 |
| [Fava](https://xrpl.to/token/r9gu97UDNkhnzRCzwZxBrxzHhEioaxtf3j-4661766100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,438 XRP) | 719 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,506 XRP) | 1253 |
| [PLATYPUS](https://xrpl.to/token/r9oHTYujRHB5SiCiPa3d2pEd4ckBFUmadk-504C415459505553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,021 XRP) | 510 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 9564 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 828 XRP) | 414 |
| [VOX🗽](https://xrpl.to/token/rBnJZMDB9HZ6UxUoeQc7eaAQHA3Y1v6Hk3-564F58F09F97BD00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 500 XRP) | 250 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 349 XRP too low | 62141 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 100 XRP too low | 19873 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,133 XRP) | 1067 |
| [XRPete](https://xrpl.to/token/rEBFKbaYRkzt9tBvV51xaW1RLYZaNyBztC-5852506574650000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,813 XRP) | 906 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5231 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7805 |
| [B2X](https://xrpl.to/token/rGGq6KDhhi8wkjBPG3QohwWGMhssu8fGtt-B2X) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,425 XRP) | 712 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12315 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,700 XRP < 2,000 | 1700 |
| [COCK](https://xrpl.to/token/rH9uUMN2bCnc8D9cFzqpEzZKuyH4vx7R5M-434F434B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,337 XRP) | 668 |
| [LOST](https://xrpl.to/token/rJLvsT5DmzhEa48u3F1coB7bKCgmkGiBQr-4C4F535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 123 XRP) | 61 |
| [XLT](https://xrpl.to/token/rJW9v4NRtuxSCbsd5ZpgkeTeFSs1NjsM33-XLT) | FAIL_SAFETY | pool too small (xrpl.to TVL 520 XRP) | 260 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 409 XRP too low | 41184 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 484 XRP) | 242 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 4523 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 155165 |
| [YELLOW](https://xrpl.to/token/rKnt6ZnCEr5CtzAi38NPAccXLgBS3inFvJ-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | pool 1,602 XRP < 2,000 | 1602 |
| [RAD](https://xrpl.to/token/rKpaNoTRdXa48W7emkKgtCLz2MuhEroU7V-RAD) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze); pool 1,829 XRP < 2,000 | 1829 |
| [WOFL](https://xrpl.to/token/rLbGxnf4F9pm3EGg1Uo4eJnYDvA7ariTTG-574F464C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 242 XRP) | 121 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 257 XRP) | 129 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool 1,681 XRP < 2,000 | 1681 |
| [XCBURN](https://xrpl.to/token/rLtzeDVMkYmWSKhR9MdUmfgY8rRst1fYJx-58434255524E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 954 XRP) | 477 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,045 XRP) | 1022 |
| [GATO](https://xrpl.to/token/rMn4JCe8FYkWjk4qhKjvuz7Pb9NXwAiMBo-4741544F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 264 XRP) | 132 |
| [TFC](https://xrpl.to/token/rN1hHRmoFDFDHEFezxRTbbfrD5WYQGLjZJ-TFC) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,614 XRP) | 807 |
| [HWR](https://xrpl.to/token/rND47ZuHb4Jq7yCT5xjJd1xwq697FPfVxv-HWR) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,442 XRP) | 721 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,453 XRP) | 727 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
