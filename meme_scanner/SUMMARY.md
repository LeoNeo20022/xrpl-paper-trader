# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-27T20:52:55+00:00** (UTC) · XRP/USD 1.3189 (bitstamp) · last discovery 2026-10-27T20:52:55+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$100.44** | **+0.44** | $2.57 | 10 / $97.87 | $+2.68 | $-2.13 | 6 / 4 (60%) | 20 (10) | +0.88 | -2.31 | 76.15 | -1.88 | $1.67 (0.16382) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$104.21** | **+4.21** | $4.12 | 11 / $100.09 | $+14.22 | $-9.91 | 7 / 4 (64%) | 22 (11) | +9.81 | -8.56 | 79.01 | +0.98 | $1.98 (0.16394) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$95.63** | **-4.37** | $95.63 | 0 / $0.00 | $-4.25 | $+0.00 | 10 / 30 (25%) | 40 (40) | -3.35 | +0.00 | 72.51 | -5.53 | $4.06 (0.19139) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$100.89** | **+0.89** | $70.36 | 3 / $30.53 | $+0.46 | $+0.53 | 15 / 22 (41%) | 40 (37) | -0.27 | +0.10 | 76.49 | -1.61 | $4.13 (0.15446) | 0.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 66.80 | -11.30 | $2.27 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$105.10** | **+5.10** | $55.09 | 5 / $50.01 | $+5.29 | $+0.01 | 18 / 14 (56%) | 37 (32) | +2.92 | -0.31 | 79.69 | +1.58 | $4.07 (0.30386) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$102.92** | **+2.92** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | 2026-10-27T17:51 | $10.00 | 0.90 | 0.99 @ 0.1h | 0.89 | top-10 holders own 47% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-10-27T15:40 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 | only 35% of LP burned (liquidity can be pulled) |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.98 @ 4.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 0.98 | 1.16 @ 3.8h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.90 | 0.99 @ 0.1h | 0.89 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.05 | 1.10 @ 7.6h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.87 | 0.98 @ 0.9h | 0.87 | top-10 holders own 47% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 1.10 | 1.15 @ 1.1h | 0.87 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 9.5h | 0.98 | top-10 holders own 35% |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.98 @ 4.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 0.98 | 1.16 @ 3.8h | 0.96 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.90 | 0.99 @ 0.1h | 0.89 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 1.05 | 1.10 @ 7.6h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.87 | 0.98 @ 0.9h | 0.87 | top-10 holders own 47% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.74 | 0.99 @ 0.1h | 0.73 | top-10 holders own 30% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 1.10 | 1.15 @ 1.1h | 0.87 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 9.5h | 0.98 | top-10 holders own 35% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.60 | 0.98 @ 0.1h | 0.51 | top-10 holders own 43% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.72 | 1.01 @ 0.9h | 0.69 | only 29% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-27T03:35 | $10.00 | 1.02 | 1.06 @ 9.4h | 1.00 | top-10 holders own 37% | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T02:39 | $10.00 | 1.03 | 1.08 @ 16.2h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [NFG](https://xrpl.to/token/rNFGBqAKm2xFMsrTDHHJv5Hxq3gfYYWxH1-NFG) | 2026-10-27T00:10 | $10.00 | 0.96 | 0.98 @ 13.4h | 0.96 | only 27% of LP burned (liquidity can be pulled); top-10 holders own 39% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-10-27T00:35 | $10.00 | 1.03 | 1.03 @ 14.2h | 1.00 |  | dip_bounce: 15.9% below 24h high 1.41367e-10 XRP, age 693.0d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-27T00:00 | $10.00 | 0.96 | 1.02 @ 4.7h | 0.91 |  | dip_bounce: 29.2% below 24h high 0.000296289 XRP, age 727.0d |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-27T00:00 | $10.00 | 0.99 | 0.99 @ 20.9h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 28.7% below 24h high 0.000249005 XRP, age 671.0d |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-27T00:00 | $10.00 | 1.02 | 1.02 @ 18.9h | 0.95 |  | dip_bounce: 16.7% below 24h high 8.70965e-06 XRP, age 694.0d |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-10-27T00:00 | $10.00 | 0.97 | 0.99 @ 2.0h | 0.95 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 41% | dip_bounce: 16.7% below 24h high 1.98416e-07 XRP, age 255.0d |

## How high do they run? (tracking only — no rule uses this)

129 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 33 | 26% |
| ≥ +20% | 6 | 5% |
| ≥ +30% | 5 | 4% |
| ≥ +50% | 3 | 2% |
| ≥ +100% | 0 | 0% |

Median peak **x1.02** · median hours to peak **2.7h** · best x1.75 · median low x0.96 · ≤ −10% at some point: 36 of 129

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [INU](https://xrpl.to/token/r38ghAFYDauA1V7ADEnQ5RCVbcpWvN568Z-INU) | FAIL_SAFETY | pool too small (xrpl.to TVL 254 XRP) | 127 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,086 XRP) | 543 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,170 XRP) | 585 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 71% (excl. AMM) | 2136 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | 24h volume 165 XRP too low | 19737 |
| [CFH](https://xrpl.to/token/rDTHkzTq3Acxu6QrSLVfHrR3KadFknMkfS-CFH) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,611 XRP) | 1306 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,198 XRP) | 599 |
| [G.O.A.T](https://xrpl.to/token/rEfm8SFkKqiD6cx7ieeTBAcALkhH2sKpNz-472E4F2E412E5400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 306 XRP) | 153 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3872 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6590 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 11967 |
| [0FF](https://xrpl.to/token/rGVYRZVjDG8YwVF69dPbB4vv6qrr66hono-0FF) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,201 XRP) | 601 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,610 XRP < 2,000 | 1610 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 406 XRP) | 203 |
| [321BG](https://xrpl.to/token/rJeCmBFjiz1TBD32wSeLEGKXofYxekiwjZ-3332314247000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 183 XRP) | 91 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 79% (excl. AMM) | 10571 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 2633 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42850 |
| [XRPICASSO](https://xrpl.to/token/rKRp2BqRmHgkY6Akyr2wh5UehuTyPmv1iG-58525049434153534F0000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 519 XRP) | 260 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2610 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,108 XRP) | 554 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,954 XRP) | 977 |
| [ROCK](https://xrpl.to/token/rM2LZ53PobDBpEWZJp9cCAZhViRyy1TbyL-524F434B00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 73% (excl. AMM) | 3294 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 10356 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9337 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4108 |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6132 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3431 |
| [EAPE](https://xrpl.to/token/rPUQrzNnAurx4CckQ59NH2ECbYvRq229sD-4541504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 777 XRP) | 389 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 768 XRP) | 384 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 330 XRP too low | 16189 |
| [PHASER](https://xrpl.to/token/rQLfUoZNafhTTJCoCt64isgCcmXdL5a5cp-5048415345520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,782 XRP) | 1391 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7281 |
| [PIPES](https://xrpl.to/token/rUe1BVJmxscgDnCEsanRQa4RzxXy39sQKN-5049504553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 481 XRP) | 240 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228512 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 405 XRP too low | 308657 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,707 XRP) | 1353 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 77117 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending | 6957 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 66% (excl. AMM) | 2838 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
