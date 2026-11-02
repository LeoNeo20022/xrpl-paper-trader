# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-02T16:41:25+00:00** (UTC) · XRP/USD 1.2490 (bitstamp) · last discovery 2026-11-02T16:41:25+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$102.76** | **+2.76** | $7.84 | 10 / $94.92 | $+7.97 | $-5.08 | 15 / 15 (50%) | 40 (30) | +8.59 | -4.01 | 82.27 | +4.24 | $4.10 (0.19607) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$109.79** | **+9.79** | $9.71 | 10 / $100.08 | $+9.86 | $+0.08 | 16 / 20 (44%) | 46 (36) | +9.70 | +0.16 | 87.91 | +9.87 | $4.95 (0.22598) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$92.87** | **-7.13** | $92.87 | 0 / $0.00 | $-6.76 | $+0.00 | 24 / 76 (24%) | 100 (100) | -4.24 | +0.00 | 74.36 | -3.67 | $11.50 (0.57717) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$93.44** | **-6.56** | $23.64 | 7 / $69.80 | $-6.11 | $-0.20 | 36 / 57 (39%) | 100 (93) | -4.20 | -0.13 | 74.81 | -3.29 | $10.82 (0.38489) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.54 | -7.56 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$115.62** | **+15.62** | $45.50 | 7 / $70.12 | $+15.88 | $+0.12 | 41 / 39 (51%) | 87 (80) | +12.18 | +0.13 | 92.57 | +14.47 | $10.64 (0.58144) | 1.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.46** | **-2.54** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-02T13:48 | $10.00 | 0.94 | 1.00 @ 1.2h | 0.94 | top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T11:47 | $10.00 | 0.91 | 0.98 @ 0.1h | 0.91 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.90 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 0.99 @ 0.5h | 0.97 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.99 | 1.00 @ 2.3h | 0.99 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.99 | 0.99 @ 4.8h | 0.97 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.97 | 0.98 @ 1.0h | 0.97 | only 34% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T17:54 | $10.00 | 0.84 | 0.99 @ 0.1h | 0.69 | top-10 holders own 30% |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T13:48 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T11:32 | $10.00 | 0.90 | 0.99 @ 1.6h | 0.90 | only 48% of LP burned (liquidity can be pulled) |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.96 | 1.08 @ 2.7h | 0.96 | top-10 holders own 35% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.97 | 0.99 @ 0.5h | 0.97 | only 20% of LP burned (liquidity can be pulled) |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T11:32 | $10.00 | 0.99 | 1.00 @ 2.3h | 0.99 |  |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T14:51 | $10.00 | 0.97 | 0.98 @ 3.2h | 0.97 | only 34% of LP burned (liquidity can be pulled) |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T02:39 | $10.00 | 1.03 | 1.06 @ 13.1h | 0.99 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T02:39 | $10.00 | 1.23 | 1.32 @ 23.0h | 0.99 | top-10 holders own 49% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T22:51 | $10.00 | 0.98 | 1.00 @ 10.5h | 0.88 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-02T02:49 | $10.00 | 1.00 | 1.07 @ 8.2h | 0.94 |  | slow_scalp: new/top-15 trending, round trip 0.18% <= 2.0% |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | 2026-11-02T02:39 | $10.00 | 1.00 | 1.00 @ 3.8h | 1.00 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.05% <= 2.0% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-02T00:49 | $10.00 | 0.95 | 0.99 @ 0.0h | 0.95 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.39% <= 2.0% |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-02T00:13 | $10.00 | 1.05 | 1.05 @ 13.7h | 0.97 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.15% <= 2.0% |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | 2026-11-02T00:03 | $10.00 | 0.99 | 1.00 @ 1.3h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-02T00:03 | $10.00 | 1.01 | 1.01 @ 16.6h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-11-02T00:03 | $10.00 | 0.99 | 1.06 @ 11.6h | 0.98 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-02T13:48 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 48% of LP burned (liquidity can be pulled) | dip_bounce: 17.9% below 24h high 0.0161864 XRP, age 734.6d |
| [Opulence](https://xrpl.to/token/rs5wxrBTSErywDDfPs5NY4Zorrca5QMGVd-4F70756C656E6365000000000000000000000000) | 2026-11-02T10:00 | $10.00 | 0.98 | 0.99 @ 3.8h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 39% | dip_bounce: 33.9% below 24h high 6.0216e-05 XRP, age 1240.0d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-11-02T05:50 | $10.00 | 1.00 | 1.00 @ 10.5h | 0.99 |  | dip_bounce: 15.7% below 24h high 9.14194e-06 XRP, age 744.2d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-02T00:39 | $10.00 | 1.06 | 1.06 @ 16.0h | 0.96 | top-10 holders own 43% | dip_bounce: 17.2% below 24h high 0.000125324 XRP, age 725.0d |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | 2026-11-02T00:08 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 | top-10 holders own 31% | dip_bounce: 17.3% below 24h high 2.06085e-05 XRP, age 524.2d |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-01T20:49 | $10.00 | 1.02 | 1.02 @ 19.5h | 0.95 |  | dip_bounce: 16.4% below 24h high 0.000196076 XRP, age 372.0d |
| [WALRUS](https://xrpl.to/token/rHYYwa8esP5eJCiWnSVY7STTHVH1iQVKqR-57414C5255530000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.97 | 0.99 @ 0.1h | 0.97 | top-10 holders own 35% | dip_bounce: 29.9% below 24h high 0.000459695 XRP, age 428.8d |

## How high do they run? (tracking only — no rule uses this)

302 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 66 | 22% |
| ≥ +20% | 23 | 8% |
| ≥ +30% | 15 | 5% |
| ≥ +50% | 9 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **3.2h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 67 of 302

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [SOCKS](https://xrpl.to/token/r3D3XjfF9xSoSsRKHMrZ6RTV6SJvucMoon-534F434B53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 260 XRP) | 130 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4699 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,803 XRP) | 1402 |
| [Fava](https://xrpl.to/token/r9gu97UDNkhnzRCzwZxBrxzHhEioaxtf3j-4661766100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,367 XRP) | 684 |
| [PLATYPUS](https://xrpl.to/token/r9oHTYujRHB5SiCiPa3d2pEd4ckBFUmadk-504C415459505553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,097 XRP) | 548 |
| [CHAOS](https://xrpl.to/token/r9x2gBJncTSo8kK3kf7qE5qYoJCfSQoEkq-4348414F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,546 XRP) | 773 |
| [VOX🗽](https://xrpl.to/token/rBnJZMDB9HZ6UxUoeQc7eaAQHA3Y1v6Hk3-564F58F09F97BD00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 633 XRP) | 317 |
| [FUZZYB](https://xrpl.to/token/rCiqVyZRZsdEAcoitSeE5Hqd6dxmkX5Kp-46555A5A59420000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,009 XRP) | 1504 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2409 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 190288 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 91 XRP too low | 19846 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool 1,838 XRP < 2,000 | 1838 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 213 XRP) | 107 |
| [XRPete](https://xrpl.to/token/rEBFKbaYRkzt9tBvV51xaW1RLYZaNyBztC-5852506574650000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,601 XRP) | 801 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7941 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 241677 |
| [COCK](https://xrpl.to/token/rH9uUMN2bCnc8D9cFzqpEzZKuyH4vx7R5M-434F434B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,324 XRP) | 662 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 16280 |
| [WALRUS](https://xrpl.to/token/rHYYwa8esP5eJCiWnSVY7STTHVH1iQVKqR-57414C5255530000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2769 |
| [LOST](https://xrpl.to/token/rJLvsT5DmzhEa48u3F1coB7bKCgmkGiBQr-4C4F535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 159 XRP) | 79 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 4761 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157660 |
| [WOFL](https://xrpl.to/token/rLbGxnf4F9pm3EGg1Uo4eJnYDvA7ariTTG-574F464C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 729 XRP) | 364 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 286 XRP) | 143 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2331 |
| [XCBURN](https://xrpl.to/token/rLtzeDVMkYmWSKhR9MdUmfgY8rRst1fYJx-58434255524E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,246 XRP) | 623 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 341 XRP too low | 7746 |
| [GATO](https://xrpl.to/token/rMn4JCe8FYkWjk4qhKjvuz7Pb9NXwAiMBo-4741544F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 525 XRP) | 262 |
| [TFC](https://xrpl.to/token/rN1hHRmoFDFDHEFezxRTbbfrD5WYQGLjZJ-TFC) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,614 XRP) | 807 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,721 XRP) | 861 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 4955 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,925 XRP) | 963 |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6952 |
| [YZZUF](https://xrpl.to/token/rPzDvACffFYezttfbbeGcje5qCXK8R2uxB-595A5A5546000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,951 XRP) | 975 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2696456 |
| [ELEVNFIVE](https://xrpl.to/token/rU4gxrLrgZAEEPQuTQ3KhaT1hD8DGXKyTi-454C45564E464956450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,684 XRP) | 1342 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7206 |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 16897 |
| [BTCL](https://xrpl.to/token/rUgeZXZvcXX9UstkspHr1gHJKj89PqogtU-4254434C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,942 XRP) | 1471 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228790 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
