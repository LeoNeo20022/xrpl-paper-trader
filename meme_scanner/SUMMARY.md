# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-31T01:01:12+00:00** (UTC) · XRP/USD 1.2577 (bitstamp) · last discovery 2026-10-31T01:01:12+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$98.84** | **-1.16** | $0.71 | 10 / $98.14 | $+0.82 | $-1.86 | 11 / 10 (52%) | 31 (21) | +3.21 | -2.31 | 78.59 | +0.55 | $3.07 (0.18480) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$117.80** | **+17.80** | $0.79 | 12 / $117.01 | $+20.94 | $-2.99 | 13 / 11 (54%) | 36 (24) | +17.47 | -1.84 | 93.66 | +15.63 | $4.00 (0.22510) | 2.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$95.82** | **-4.18** | $45.98 | 5 / $49.84 | $-3.81 | $-0.16 | 17 / 53 (24%) | 75 (70) | -1.74 | -0.19 | 76.18 | -1.85 | $8.04 (0.31524) | 1.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$97.33** | **-2.67** | $18.10 | 8 / $79.23 | $-1.69 | $-0.77 | 26 / 43 (38%) | 77 (69) | -0.51 | -1.02 | 77.39 | -0.72 | $8.19 (0.32285) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.05 | -8.05 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$120.16** | **+20.16** | $51.34 | 7 / $68.82 | $+21.67 | $-1.18 | 36 / 27 (57%) | 70 (63) | +17.11 | -1.50 | 95.54 | +17.43 | $8.40 (0.51901) | 1.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$98.15** | **-1.85** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T17:54 | $10.00 | 0.91 | 0.99 @ 0.1h | 0.91 | top-10 holders own 30% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-10-30T15:45 | $10.00 | 0.74 | 0.99 @ 0.4h | 0.74 | top-10 holders own 34% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.97 | 1.01 @ 2.5h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 0.9h | 0.99 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.03 | 1.06 @ 5.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.98 | 1.00 @ 7.0h | 0.98 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.08 | 1.09 @ 11.3h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 6.7h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.02 | 1.02 @ 13.7h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### plus5 — open positions (12)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.97 | 1.01 @ 2.5h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 0.9h | 0.99 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.03 | 1.06 @ 5.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.98 | 1.00 @ 7.0h | 0.98 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.08 | 1.09 @ 11.3h | 1.00 |  |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.92 | 0.99 @ 6.2h | 0.92 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.02 | 1.02 @ 13.7h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.97 | 1.16 @ 15.3h | 0.96 | only 19% of LP burned (liquidity can be pulled) |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.92 | 0.99 @ 3.6h | 0.88 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-28T22:49 | $10.00 | 0.95 | 0.99 @ 9.9h | 0.92 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.94 | 1.03 @ 21.1h | 0.94 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |

### scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-31T00:09 | $10.00 | 0.98 | 0.99 @ 0.0h | 0.98 | only 19% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-31T00:04 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.9h | 1.00 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.6h | 1.00 | top-10 holders own 49% |

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-31T00:09 | $10.00 | 0.98 | 0.99 @ 0.0h | 0.98 | only 19% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.22% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T00:09 | $10.00 | 0.98 | 0.98 @ 0.9h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 0.98 | 0.98 @ 0.7h | 0.98 | top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 0.96 | 0.99 @ 0.1h | 0.96 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.9h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-30T01:25 | $10.00 | 0.99 | 1.00 @ 21.8h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.14% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-31T00:04 | $10.00 | 1.00 | 1.00 @ 0.6h | 1.00 | top-10 holders own 49% | dip_bounce: 44.4% below 24h high 0.000131068 XRP, age 6.8d |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 0.98 | 0.98 @ 0.9h | 0.98 | top-10 holders own 41% | dip_bounce: 18.6% below 24h high 0.000112847 XRP, age 528.4d |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | 2026-10-31T00:04 | $10.00 | 0.98 | 0.99 @ 0.3h | 0.98 | top-10 holders own 31% | dip_bounce: 15.2% below 24h high 2.23684e-05 XRP, age 522.2d |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-10-30T17:17 | $10.00 | 0.95 | 0.98 @ 0.4h | 0.95 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 41% | dip_bounce: 16.5% below 24h high 1.78619e-07 XRP, age 258.7d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-30T15:15 | $10.00 | 0.91 | 0.99 @ 2.3h | 0.91 |  | dip_bounce: 25.4% below 24h high 0.000225127 XRP, age 730.6d |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T03:52 | $10.00 | 0.96 | 1.06 @ 11.4h | 0.96 | top-10 holders own 30% | dip_bounce: 15.7% below 24h high 7.0907e-07 XRP, age 98.5d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-30T01:59 | $10.00 | 1.03 | 1.03 @ 18.6h | 0.98 |  | dip_bounce: 39.1% below 24h high 1.19011e-05 XRP, age 741.1d |

## How high do they run? (tracking only — no rule uses this)

234 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 56 | 24% |
| ≥ +20% | 20 | 9% |
| ≥ +30% | 13 | 6% |
| ≥ +50% | 8 | 3% |
| ≥ +100% | 1 | 0% |

Median peak **x1.01** · median hours to peak **2.8h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 48 of 234

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9461 |
| [SOCKS](https://xrpl.to/token/r3D3XjfF9xSoSsRKHMrZ6RTV6SJvucMoon-534F434B53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 759 XRP) | 380 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 6099 |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2891 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 530 XRP) | 265 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,137 XRP) | 569 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,329 XRP) | 665 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,389 XRP) | 1195 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,797 XRP) | 1398 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19187 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 69% (excl. AMM) | 2091 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 7843 |
| [BEARTARDIO](https://xrpl.to/token/rBaqA4jccYewn1Rq1dP5TD2GTWuZgf3DBi-4245415254415244494F00000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,046 XRP) | 523 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 108 XRP too low | 62505 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 189429 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 95 XRP too low | 19777 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,156 XRP) | 1578 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 314 XRP) | 157 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 359 XRP too low | 4372 |
| [RUBY](https://xrpl.to/token/rG71TpU2YZkgsGv79hbTYWMjxoKNGvAFRN-5255425900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,240 XRP) | 1120 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 17982 |
| [MILK](https://xrpl.to/token/rHjMMxnM84UGwVgABSmt3esFGxtDYK8RaZ-4D494C4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 293 XRP) | 147 |
| [OURO](https://xrpl.to/token/rHwkshB9XXd5Do3V3uqZeJv91mazdVTbEX-4F55524F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 398 XRP) | 199 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 284 XRP) | 142 |
| [CMAI](https://xrpl.to/token/rJUTeaho7z77FV2pnG2Lw9szZUktvXt2mW-434D414900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,022 XRP) | 511 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42545 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5957 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157843 |
| [CIRCLE](https://xrpl.to/token/rKtZqPGaiW8ejjaUccf13WuZLEXdzSz2CE-434952434C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4040 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 468 XRP) | 234 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7890 |
| [JUST1](https://xrpl.to/token/rNA9GrVUYJz7XPudUVdEkMSJ15XCWhBh81-4A55535431000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 956 XRP) | 478 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,600 XRP) | 1300 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 5211 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,865 XRP) | 1433 |
| [NXS](https://xrpl.to/token/rNexusA23ZQdtejTCeHZZaiKoJRsrnXboq-NXS) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,032 XRP) | 516 |
| [TRUMPY](https://xrpl.to/token/rPaqoKAo2ezcbKbxzu1XhAnBZ9WpowUmSW-5452554D50590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,854 XRP) | 927 |
| [LEDG](https://xrpl.to/token/rPvKPe13jyCyVWyzGhA8obji4E57JUM3qK-4C45444700000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,135 XRP) | 567 |
| [XRT](https://xrpl.to/token/rPvuCxw1m8u2SWTqtRN6ZEcb1xPbU4cPFR-XRT) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,516 XRP) | 1258 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending | 16215 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
