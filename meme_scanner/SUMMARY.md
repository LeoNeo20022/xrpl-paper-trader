# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-29T04:31:24+00:00** (UTC) · XRP/USD 1.2882 (bitstamp) · last discovery 2026-10-29T04:31:24+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$109.45** | **+9.45** | $2.57 | 10 / $106.88 | $+2.68 | $+6.88 | 6 / 4 (60%) | 20 (10) | +0.88 | +6.46 | 84.96 | +6.93 | $1.66 (0.16382) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$122.28** | **+22.28** | $3.65 | 12 / $118.63 | $+23.79 | $-1.37 | 10 / 6 (62%) | 28 (16) | +16.85 | +0.12 | 94.92 | +16.89 | $3.04 (0.20438) | 2.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$98.08** | **-1.92** | $98.08 | 0 / $0.00 | $-1.72 | $+0.00 | 16 / 44 (27%) | 60 (60) | -1.02 | +0.00 | 76.14 | -1.90 | $6.80 (0.30384) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$100.81** | **+0.81** | $52.72 | 5 / $48.09 | $+2.90 | $-1.91 | 21 / 34 (38%) | 60 (55) | +1.86 | -0.46 | 78.25 | +0.15 | $6.62 (0.26650) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 68.40 | -9.71 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$117.55** | **+17.55** | $69.25 | 5 / $48.30 | $+19.53 | $-1.70 | 30 / 21 (59%) | 56 (51) | +14.22 | -0.58 | 91.25 | +13.14 | $6.73 (0.42032) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$100.52** | **+0.52** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005020 XRP/tx = max(0.00002, live open-ledger fee 0.00502), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | 2026-10-27T17:51 | $10.00 | 1.49 | 1.80 @ 33.3h | 0.73 | top-10 holders own 47% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-10-27T15:40 | $10.00 | 0.92 | 0.98 @ 0.1h | 0.92 | only 35% of LP burned (liquidity can be pulled) |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 29.7h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.97 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.22 | 1.31 @ 14.9h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.74 | 0.99 @ 0.1h | 0.74 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.40 | 1.62 @ 30.4h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.12 | 1.25 @ 31.7h | 0.85 | top-10 holders own 47% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 0.99 | 1.23 @ 29.4h | 0.62 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 32.6h | 0.98 | top-10 holders own 35% |

### plus5 — open positions (12)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 1.00 | 1.00 @ 0.5h | 0.98 | only 19% of LP burned (liquidity can be pulled) |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-28T22:49 | $10.00 | 0.99 | 0.99 @ 3.0h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.98 | 0.98 @ 5.7h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 29.7h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.97 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.22 | 1.31 @ 14.9h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.74 | 0.99 @ 0.1h | 0.74 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.12 | 1.25 @ 31.7h | 0.85 | top-10 holders own 47% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.02 | 1.10 @ 40.6h | 0.72 | top-10 holders own 30% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 0.99 | 1.23 @ 29.4h | 0.62 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 32.6h | 0.98 | top-10 holders own 35% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-29T00:57 | $10.00 | 0.99 | 0.99 @ 3.3h | 0.98 | top-10 holders own 47% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T00:11 | $10.00 | 1.00 | 1.00 @ 3.0h | 0.98 | only 19% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.49% <= 2.0% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.99 | 0.99 @ 4.3h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-10-29T00:06 | $10.00 | 0.97 | 0.98 @ 0.2h | 0.97 | top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.98 @ 4.4h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 1.79% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-29T01:53 | $10.00 | 1.01 | 1.01 @ 2.4h | 0.92 |  | dip_bounce: 16.5% below 24h high 0.000341 XRP, age 368.2d |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-29T01:48 | $10.00 | 1.03 | 1.03 @ 1.3h | 0.98 | top-10 holders own 45% | dip_bounce: 18.0% below 24h high 7.19505e-07 XRP, age 419.6d |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-29T01:07 | $10.00 | 0.91 | 0.99 @ 1.3h | 0.91 | top-10 holders own 49% | dip_bounce: 15.3% below 24h high 0.000112529 XRP, age 4.9d |
| [XRPBR](https://xrpl.to/token/rfnMuYiECGMAHUkZdDw5K1c7gVdoiqkmJC-5852504252000000000000000000000000000000) | 2026-10-29T00:26 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 | only 36% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 16.3% below 24h high 0.0126757 XRP, age 551.4d |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-29T00:01 | $10.00 | 0.98 | 0.99 @ 0.3h | 0.98 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% | dip_bounce: 17.8% below 24h high 8.35659e-08 XRP, age 709.0d |

## How high do they run? (tracking only — no rule uses this)

185 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 48 | 26% |
| ≥ +20% | 18 | 10% |
| ≥ +30% | 11 | 6% |
| ≥ +50% | 8 | 4% |
| ≥ +100% | 0 | 0% |

Median peak **x1.01** · median hours to peak **2.6h** · best x1.80 · median low x0.97 · ≤ −10% at some point: 39 of 185

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,783 XRP) | 1392 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 6858 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 477 XRP) | 238 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,057 XRP) | 528 |
| [$PBLU](https://xrpl.to/token/r9JVUKhSQDfMLDXiXWrkNgn4gazWAP7KEA-2450424C55000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,675 XRP) | 1337 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,065 XRP) | 532 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 28530 |
| [SCHWATOSHI](https://xrpl.to/token/rB1xGmTgqF8WSRbyaRD3AR4PkyTC1eyErL-5343485741544F53484900000000000000000000) | FAIL_SAFETY | pool 1,710 XRP < 2,000 | 1710 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 71% (excl. AMM) | 2288 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62929 |
| [XRB](https://xrpl.to/token/rD9ixf7RRUKuKVFTsZa3fZGAN6HtNziPKa-XRB) | FAIL_SAFETY | pool too small (xrpl.to TVL 769 XRP) | 384 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2377 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 189380 |
| [MMX](https://xrpl.to/token/rDYEH6EW7R1usTfRZ3KoC87qSxktFX1obK-MMX) | FAIL_SAFETY | pool too small (xrpl.to TVL 310 XRP) | 155 |
| [IOV](https://xrpl.to/token/rEQRwzSJQru4tVSywEWN4cKRK9sPfFo6t3-IOV) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,552 XRP) | 776 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4440 |
| [0FF](https://xrpl.to/token/rGVYRZVjDG8YwVF69dPbB4vv6qrr66hono-0FF) | FAIL_SAFETY | pool too small (xrpl.to TVL 394 XRP) | 197 |
| [CBIRD](https://xrpl.to/token/rHcU3JWTp7fnea3xgvbV8pCbEp9S3HjSUz-4342495244000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10474 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 3755 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 154519 |
| [KNIGHT](https://xrpl.to/token/rKsJ4b1rnUPxN8B11UQQj752MxqmYiR3Nv-4B4E494748540000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 363 XRP) | 181 |
| [LockIn](https://xrpl.to/token/rM2SU1Ct2fu1Bm6cKEBojf2763JNm43Tv6-4C6F636B496E0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2689 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 478 XRP too low | 9325 |
| [Ledgy](https://xrpl.to/token/rMPU2n4L46xav5xcNYTivAM5pgmcJVEAtq-4C65646779000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 477 XRP) | 239 |
| [TRAINXRP](https://xrpl.to/token/rMsvvbgfKHQhw7gwQYkkdkRfgqoU2UzhdE-545241494E585250000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 298 XRP) | 149 |
| [HBAR](https://xrpl.to/token/rN8fAmQNJvvpb1Cga2hm7amqEhs4ioUvgp-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,349 XRP) | 1174 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,519 XRP) | 1260 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4158 |
| [NXS](https://xrpl.to/token/rNexusA23ZQdtejTCeHZZaiKoJRsrnXboq-NXS) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,333 XRP) | 667 |
| [EAPE](https://xrpl.to/token/rPUQrzNnAurx4CckQ59NH2ECbYvRq229sD-4541504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 66 XRP) | 33 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42128 |
| [LEDG](https://xrpl.to/token/rPvKPe13jyCyVWyzGhA8obji4E57JUM3qK-4C45444700000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,169 XRP) | 584 |
| [BBB](https://xrpl.to/token/rQDeP83vnYhiSSxgBqcdkGNRLQ1y5auW5h-BBB) | FAIL_SAFETY | pool too small (xrpl.to TVL 222 XRP) | 111 |
| [FRIZZY](https://xrpl.to/token/rQHU5KQJytJW8Yv1JdGmdhLPNRG7T6LztR-4652495A5A590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 252 XRP) | 126 |
| [PHASER](https://xrpl.to/token/rQLfUoZNafhTTJCoCt64isgCcmXdL5a5cp-5048415345520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,659 XRP) | 1329 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7595 |
| [AUDD](https://xrpl.to/token/rUN5Zxt3K1AnMRJgEWywDJT8QDMMeLH5ok-4155444400000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Stablecoin; not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 2,422 XRP) | 1211 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 230088 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 309751 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,540 XRP) | 770 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
