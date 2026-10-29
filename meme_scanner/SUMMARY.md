# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-29T00:11:31+00:00** (UTC) · XRP/USD 1.3239 (bitstamp) · last discovery 2026-10-29T00:11:31+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$111.24** | **+11.24** | $2.57 | 10 / $108.67 | $+2.68 | $+8.67 | 6 / 4 (60%) | 20 (10) | +0.88 | +5.57 | 84.03 | +5.99 | $1.67 (0.16382) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$117.88** | **+17.88** | $8.71 | 11 / $109.17 | $+18.84 | $-0.83 | 9 / 6 (60%) | 26 (15) | +12.79 | -1.53 | 89.04 | +11.00 | $2.83 (0.20426) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$96.21** | **-3.79** | $7.99 | 9 / $88.22 | $-1.81 | $-1.78 | 14 / 36 (28%) | 59 (50) | -1.55 | -1.29 | 72.67 | -5.36 | $6.03 (0.30340) | 1.8 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$95.81** | **-4.19** | $7.65 | 9 / $88.16 | $-2.19 | $-1.84 | 17 / 32 (35%) | 58 (49) | -2.57 | -1.37 | 72.37 | -5.74 | $5.90 (0.25573) | 1.8 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 66.55 | -11.55 | $2.27 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$109.99** | **+9.99** | $60.14 | 5 / $49.85 | $+10.40 | $-0.15 | 26 / 19 (58%) | 50 (45) | +6.36 | -0.04 | 83.08 | +4.98 | $5.92 (0.39939) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$103.31** | **+3.31** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.010000 XRP/tx = max(0.00002, live open-ledger fee 0.050181), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | 2026-10-27T17:51 | $10.00 | 1.17 | 1.57 @ 29.1h | 0.73 | top-10 holders own 47% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-10-27T15:40 | $10.00 | 0.92 | 0.98 @ 0.1h | 0.92 | only 35% of LP burned (liquidity can be pulled) |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 29.7h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.97 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.21 | 1.31 @ 14.9h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.74 | 0.99 @ 0.1h | 0.74 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.47 | 1.62 @ 30.4h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.14 | 1.25 @ 31.7h | 0.85 | top-10 holders own 47% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 1.14 | 1.23 @ 29.4h | 0.62 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 32.6h | 0.98 | top-10 holders own 35% |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-28T22:49 | $10.00 | 0.99 | 0.99 @ 1.3h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.78 | 1.15 @ 0.2h | 0.78 | top-10 holders own 32% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 29.7h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.97 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.21 | 1.31 @ 14.9h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.74 | 0.99 @ 0.1h | 0.74 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.14 | 1.25 @ 31.7h | 0.85 | top-10 holders own 47% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.87 | 1.00 @ 14.7h | 0.72 | top-10 holders own 30% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 1.14 | 1.23 @ 29.4h | 0.62 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 32.6h | 0.98 | top-10 holders own 35% |

### scalp — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 34% |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.97 | 0.97 @ 0.1h | 0.97 | top-10 holders own 32% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 45% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 19% of LP burned (liquidity can be pulled) |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 49% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.97 | 0.99 @ 0.1h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  |

### slow_scalp — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T00:11 | $10.00 | 1.00 | – | – | only 19% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.49% <= 2.0% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 45% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.97 | 0.97 @ 0.1h | 0.97 | top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 0.45% <= 2.0% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 1.79% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.58% <= 2.0% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-28T00:12 | $10.00 | 0.98 | 0.98 @ 19.2h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  | dip_bounce: 20.8% below 24h high 8.43202e-06 XRP, age 740.0d |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% | dip_bounce: 17.8% below 24h high 8.35659e-08 XRP, age 709.0d |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 30% | dip_bounce: 17.1% below 24h high 6.85046e-07 XRP, age 97.3d |
| [RIBBLE](https://xrpl.to/token/rG7jT6D4fHsipvVmPSbcnvDtFzXwwSR4qx-524942424C450000000000000000000000000000) | 2026-10-28T01:27 | $10.00 | 0.99 | 1.00 @ 17.4h | 0.99 |  | dip_bounce: 17.5% below 24h high 2.26085e-05 XRP, age 653.1d |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-28T01:27 | $10.00 | 1.03 | 1.04 @ 19.6h | 0.97 | only 28% of LP burned (liquidity can be pulled) | dip_bounce: 15.1% below 24h high 2.62997 XRP, age 741.1d |

## How high do they run? (tracking only — no rule uses this)

173 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 42 | 24% |
| ≥ +20% | 12 | 7% |
| ≥ +30% | 9 | 5% |
| ≥ +50% | 6 | 3% |
| ≥ +100% | 0 | 0% |

Median peak **x1.01** · median hours to peak **1.6h** · best x1.75 · median low x0.97 · ≤ −10% at some point: 38 of 173

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,828 XRP) | 1414 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 6853 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,011 XRP) | 505 |
| [$PBLU](https://xrpl.to/token/r9JVUKhSQDfMLDXiXWrkNgn4gazWAP7KEA-2450424C55000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,675 XRP) | 1337 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,080 XRP) | 540 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 28497 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 130 XRP too low | 19022 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 71% (excl. AMM) | 2295 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62934 |
| [XRB](https://xrpl.to/token/rD9ixf7RRUKuKVFTsZa3fZGAN6HtNziPKa-XRB) | FAIL_SAFETY | pool too small (xrpl.to TVL 824 XRP) | 412 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 188942 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 106 XRP too low | 19769 |
| [IOV](https://xrpl.to/token/rEQRwzSJQru4tVSywEWN4cKRK9sPfFo6t3-IOV) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,549 XRP) | 775 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4483 |
| [0FF](https://xrpl.to/token/rGVYRZVjDG8YwVF69dPbB4vv6qrr66hono-0FF) | FAIL_SAFETY | pool too small (xrpl.to TVL 615 XRP) | 307 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 3776 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 154302 |
| [KNIGHT](https://xrpl.to/token/rKsJ4b1rnUPxN8B11UQQj752MxqmYiR3Nv-4B4E494748540000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 386 XRP) | 193 |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2884 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9305 |
| [Ledgy](https://xrpl.to/token/rMPU2n4L46xav5xcNYTivAM5pgmcJVEAtq-4C65646779000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 492 XRP) | 246 |
| [TRAINXRP](https://xrpl.to/token/rMsvvbgfKHQhw7gwQYkkdkRfgqoU2UzhdE-545241494E585250000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 467 XRP) | 234 |
| [HBAR](https://xrpl.to/token/rN8fAmQNJvvpb1Cga2hm7amqEhs4ioUvgp-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,348 XRP) | 1174 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,223 XRP) | 1112 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4164 |
| [EAPE](https://xrpl.to/token/rPUQrzNnAurx4CckQ59NH2ECbYvRq229sD-4541504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 50 XRP) | 25 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42100 |
| [LEDG](https://xrpl.to/token/rPvKPe13jyCyVWyzGhA8obji4E57JUM3qK-4C45444700000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,123 XRP) | 561 |
| [BBB](https://xrpl.to/token/rQDeP83vnYhiSSxgBqcdkGNRLQ1y5auW5h-BBB) | FAIL_SAFETY | pool too small (xrpl.to TVL 221 XRP) | 111 |
| [FRIZZY](https://xrpl.to/token/rQHU5KQJytJW8Yv1JdGmdhLPNRG7T6LztR-4652495A5A590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 350 XRP) | 175 |
| [PHASER](https://xrpl.to/token/rQLfUoZNafhTTJCoCt64isgCcmXdL5a5cp-5048415345520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,949 XRP) | 1474 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7719 |
| [AUDD](https://xrpl.to/token/rUN5Zxt3K1AnMRJgEWywDJT8QDMMeLH5ok-4155444400000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Stablecoin; not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,390 XRP) | 1195 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 230071 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 309768 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,984 XRP) | 992 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 77598 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 81875 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending | 6342 |
| [SMQKE](https://xrpl.to/token/racaUo2hNNk7vTWKA912t8jTqp9wcxFW89-534D514B45000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 486 XRP) | 243 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
