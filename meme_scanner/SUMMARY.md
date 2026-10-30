# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-30T21:57:37+00:00** (UTC) · XRP/USD 1.2489 (bitstamp) · last discovery 2026-10-30T21:57:37+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$101.04** | **+1.04** | $0.71 | 10 / $100.34 | $+0.82 | $+0.34 | 11 / 10 (52%) | 31 (21) | +3.21 | +0.01 | 80.91 | +2.87 | $3.07 (0.18480) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$117.76** | **+17.76** | $0.79 | 12 / $116.97 | $+20.94 | $-3.03 | 13 / 11 (54%) | 36 (24) | +17.47 | -1.22 | 94.29 | +16.26 | $4.00 (0.22510) | 2.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$95.98** | **-4.02** | $95.98 | 0 / $0.00 | $-3.81 | $+0.00 | 17 / 53 (24%) | 70 (70) | -1.74 | +0.00 | 76.85 | -1.18 | $7.85 (0.31504) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$97.92** | **-2.08** | $37.48 | 6 / $60.43 | $-2.31 | $+0.43 | 23 / 41 (36%) | 70 (64) | -0.31 | -0.39 | 78.40 | +0.30 | $7.56 (0.31226) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.55 | -7.56 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$121.64** | **+21.64** | $61.80 | 6 / $59.84 | $+22.13 | $-0.16 | 35 / 26 (57%) | 67 (61) | +17.73 | -0.59 | 97.40 | +19.29 | $8.07 (0.51881) | 1.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.46** | **-2.54** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T17:54 | $10.00 | 0.95 | 0.99 @ 0.1h | 0.95 | top-10 holders own 30% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-10-30T15:45 | $10.00 | 0.96 | 0.99 @ 0.4h | 0.96 | top-10 holders own 34% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.97 | 1.01 @ 2.5h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 0.9h | 0.99 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.06 @ 5.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 1.00 @ 7.0h | 0.98 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.09 | 1.09 @ 10.6h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 6.7h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 1.6h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### plus5 — open positions (12)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.97 | 1.01 @ 2.5h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 0.9h | 0.99 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.06 @ 5.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 1.00 @ 7.0h | 0.98 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.09 | 1.09 @ 10.6h | 1.00 |  |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.92 | 0.99 @ 6.2h | 0.92 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 1.6h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.98 | 1.16 @ 15.3h | 0.98 | only 19% of LP burned (liquidity can be pulled) |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.95 | 0.99 @ 3.6h | 0.88 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-28T22:49 | $10.00 | 0.95 | 0.99 @ 9.9h | 0.92 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.95 | 1.03 @ 21.1h | 0.95 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-30T01:25 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.14% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T00:12 | $10.00 | 0.99 | 1.00 @ 17.8h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T00:07 | $10.00 | 1.05 | 1.05 @ 12.8h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.12% <= 2.0% |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-30T00:07 | $10.00 | 1.00 | 1.03 @ 16.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.12% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.96 | 1.00 @ 0.2h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.96 | 0.99 @ 5.6h | 0.96 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-10-30T17:17 | $10.00 | 0.96 | 0.98 @ 0.4h | 0.95 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 41% | dip_bounce: 16.5% below 24h high 1.78619e-07 XRP, age 258.7d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-30T15:15 | $10.00 | 0.97 | 0.99 @ 2.3h | 0.97 |  | dip_bounce: 25.4% below 24h high 0.000225127 XRP, age 730.6d |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T03:52 | $10.00 | 1.00 | 1.06 @ 11.4h | 0.98 | top-10 holders own 30% | dip_bounce: 15.7% below 24h high 7.0907e-07 XRP, age 98.5d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-30T01:59 | $10.00 | 1.00 | 1.03 @ 18.6h | 0.98 |  | dip_bounce: 39.1% below 24h high 1.19011e-05 XRP, age 741.1d |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-30T00:02 | $10.00 | 1.00 | 1.01 @ 8.2h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 18.1% below 24h high 0.000199108 XRP, age 674.0d |
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.99 | 1.00 @ 3.1h | 0.99 | top-10 holders own 30% | dip_bounce: 17.3% below 24h high 7.59124e-09 XRP, age 668.0d |

## How high do they run? (tracking only — no rule uses this)

223 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 56 | 25% |
| ≥ +20% | 20 | 9% |
| ≥ +30% | 13 | 6% |
| ≥ +50% | 8 | 4% |
| ≥ +100% | 1 | 0% |

Median peak **x1.02** · median hours to peak **3.2h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 47 of 223

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9461 |
| [ASC](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-ASC) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,163 XRP) | 1082 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 6121 |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2895 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 497 XRP) | 248 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,092 XRP) | 546 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 31530 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,515 XRP) | 1258 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,761 XRP) | 1381 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 431 XRP too low | 19196 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 69% (excl. AMM) | 2092 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 7336 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 144 XRP too low | 62519 |
| [XRB](https://xrpl.to/token/rD9ixf7RRUKuKVFTsZa3fZGAN6HtNziPKa-XRB) | FAIL_SAFETY | pool too small (xrpl.to TVL 614 XRP) | 307 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 190128 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 64 XRP too low | 19752 |
| [CFH](https://xrpl.to/token/rDTHkzTq3Acxu6QrSLVfHrR3KadFknMkfS-CFH) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,593 XRP) | 1297 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,172 XRP) | 1586 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 429 XRP) | 214 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 399 XRP too low | 4350 |
| [RUBY](https://xrpl.to/token/rG71TpU2YZkgsGv79hbTYWMjxoKNGvAFRN-5255425900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,240 XRP) | 1120 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 17984 |
| [MILK](https://xrpl.to/token/rHjMMxnM84UGwVgABSmt3esFGxtDYK8RaZ-4D494C4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 304 XRP) | 152 |
| [OURO](https://xrpl.to/token/rHwkshB9XXd5Do3V3uqZeJv91mazdVTbEX-4F55524F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 421 XRP) | 211 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 368 XRP) | 184 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 370 XRP too low | 42745 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5977 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157498 |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4040 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 8112 |
| [JUST1](https://xrpl.to/token/rNA9GrVUYJz7XPudUVdEkMSJ15XCWhBh81-4A55535431000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 978 XRP) | 489 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,591 XRP) | 1296 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 5211 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,867 XRP) | 1434 |
| [NXS](https://xrpl.to/token/rNexusA23ZQdtejTCeHZZaiKoJRsrnXboq-NXS) | FAIL_SAFETY | pool too small (xrpl.to TVL 965 XRP) | 482 |
| [TRUMPY](https://xrpl.to/token/rPaqoKAo2ezcbKbxzu1XhAnBZ9WpowUmSW-5452554D50590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,853 XRP) | 926 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 40876 |
| [LEDG](https://xrpl.to/token/rPvKPe13jyCyVWyzGhA8obji4E57JUM3qK-4C45444700000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,175 XRP) | 588 |
| [XRT](https://xrpl.to/token/rPvuCxw1m8u2SWTqtRN6ZEcb1xPbU4cPFR-XRT) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,537 XRP) | 1268 |
| [FRIZZY](https://xrpl.to/token/rQHU5KQJytJW8Yv1JdGmdhLPNRG7T6LztR-4652495A5A590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 157 XRP) | 78 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
