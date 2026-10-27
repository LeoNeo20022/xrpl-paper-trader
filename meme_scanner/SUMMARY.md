# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-27T15:51:01+00:00** (UTC) · XRP/USD 1.3188 (bitstamp) · last discovery 2026-10-27T15:51:01+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$101.93** | **+1.93** | $12.57 | 9 / $89.36 | $+2.68 | $-0.64 | 6 / 4 (60%) | 19 (10) | +0.88 | -1.16 | 77.30 | -0.74 | $1.58 (0.16378) | 1.8 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$104.22** | **+4.22** | $4.12 | 11 / $100.10 | $+14.22 | $-9.90 | 7 / 4 (64%) | 22 (11) | +9.81 | -8.54 | 79.03 | +0.99 | $1.98 (0.16394) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$95.63** | **-4.37** | $95.63 | 0 / $0.00 | $-4.25 | $+0.00 | 10 / 30 (25%) | 40 (40) | -3.35 | +0.00 | 72.52 | -5.52 | $4.06 (0.19139) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$100.84** | **+0.84** | $60.94 | 4 / $39.90 | $+1.04 | $-0.10 | 15 / 21 (42%) | 40 (36) | +0.23 | -0.43 | 76.47 | -1.64 | $4.02 (0.15442) | 0.8 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.30** | **-11.70** | $68.00 | 2 / $20.30 | $-11.97 | $+0.30 | 3 / 16 (16%) | 21 (19) | -9.63 | -0.04 | 66.95 | -11.15 | $2.12 (0.05302) | 0.4 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$104.69** | **+4.69** | $34.90 | 7 / $69.79 | $+5.10 | $-0.21 | 16 / 14 (53%) | 37 (30) | +3.06 | -0.76 | 79.39 | +1.28 | $4.02 (0.30378) | 1.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$102.91** | **+2.91** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-10-27T15:40 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 35% of LP burned (liquidity can be pulled) |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.98 @ 1.3h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.15 | 1.16 @ 3.8h | 0.98 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.92 | 0.99 @ 0.1h | 0.91 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.99 | 1.00 @ 2.3h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.97 | 0.98 @ 0.9h | 0.97 | top-10 holders own 47% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 0.90 | 1.15 @ 1.1h | 0.89 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 4.3h | 0.98 | top-10 holders own 35% |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.98 @ 1.3h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.98 | 1.00 @ 0.1h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.15 | 1.16 @ 3.8h | 0.98 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-10-27T11:16 | $10.00 | 0.92 | 0.99 @ 0.1h | 0.91 | only 39% of LP burned (liquidity can be pulled); top-10 holders own 30% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.99 | 1.00 @ 2.3h | 0.97 |  |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.97 | 0.98 @ 0.9h | 0.97 | top-10 holders own 47% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.76 | 0.99 @ 0.1h | 0.74 | top-10 holders own 30% |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-10-27T11:16 | $10.00 | 0.90 | 1.15 @ 1.1h | 0.89 | top-10 holders own 48% |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-10-27T11:16 | $10.00 | 0.98 | 0.98 @ 4.3h | 0.98 | top-10 holders own 35% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.54 | 0.98 @ 0.1h | 0.51 | top-10 holders own 43% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-25T22:24 | $10.00 | 0.72 | 1.01 @ 0.9h | 0.71 | only 29% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-27T03:35 | $10.00 | 1.02 | 1.06 @ 9.4h | 1.00 | top-10 holders own 37% | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-27T02:39 | $10.00 | 0.97 | 0.99 @ 0.8h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-27T00:10 | $10.00 | 0.99 | 1.00 @ 9.9h | 0.98 | top-10 holders own 47% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [NFG](https://xrpl.to/token/rNFGBqAKm2xFMsrTDHHJv5Hxq3gfYYWxH1-NFG) | 2026-10-27T00:10 | $10.00 | 0.96 | 0.98 @ 13.4h | 0.96 | only 27% of LP burned (liquidity can be pulled); top-10 holders own 39% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | 2026-10-26T19:17 | $10.00 | 1.01 | 1.01 @ 17.7h | 0.93 | only 44% of LP burned (liquidity can be pulled); top-10 holders own 44% | breakout: +14.8% in 1h, vol last hour 581 vs prior 6 / 24h avg 149 XRP |
| [Dood](https://xrpl.to/token/rn5Y9N8APtrc7PVqXdMjkG9qvfw7FWi4kC-446F6F6400000000000000000000000000000000) | 2026-10-26T17:58 | $10.00 | 0.99 | 0.99 @ 19.6h | 0.99 | top-10 holders own 37% | breakout: +16.4% in 1h, vol last hour 600 vs prior 0 / 24h avg 26 XRP |

### dip_bounce — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-10-27T00:35 | $10.00 | 1.03 | 1.03 @ 14.2h | 1.00 |  | dip_bounce: 15.9% below 24h high 1.41367e-10 XRP, age 693.0d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-27T00:00 | $10.00 | 0.94 | 1.02 @ 4.7h | 0.91 |  | dip_bounce: 29.2% below 24h high 0.000296289 XRP, age 727.0d |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-27T00:00 | $10.00 | 0.99 | 0.99 @ 15.8h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 28.7% below 24h high 0.000249005 XRP, age 671.0d |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-27T00:00 | $10.00 | 1.00 | 1.00 @ 15.8h | 0.95 |  | dip_bounce: 16.7% below 24h high 8.70965e-06 XRP, age 694.0d |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | 2026-10-27T00:00 | $10.00 | 0.96 | 0.99 @ 2.0h | 0.95 | only 32% of LP burned (liquidity can be pulled); top-10 holders own 41% | dip_bounce: 16.7% below 24h high 1.98416e-07 XRP, age 255.0d |
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-26T20:34 | $10.00 | 1.00 | 1.00 @ 2.6h | 0.99 | top-10 holders own 30% | dip_bounce: 15.5% below 24h high 5.58147e-09 XRP, age 664.9d |
| [FADE](https://xrpl.to/token/r4Peot5JGx6KPRX147oZ2TbRSocLdzBHvy-4641444500000000000000000000000000000000) | 2026-10-26T15:55 | $10.00 | 0.99 | 0.99 @ 3.9h | 0.98 |  | dip_bounce: 22.7% below 24h high 1.07077 XRP, age 734.7d |

## How high do they run? (tracking only — no rule uses this)

128 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 32 | 25% |
| ≥ +20% | 6 | 5% |
| ≥ +30% | 5 | 4% |
| ≥ +50% | 3 | 2% |
| ≥ +100% | 0 | 0% |

Median peak **x1.02** · median hours to peak **2.4h** · best x1.75 · median low x0.96 · ≤ −10% at some point: 33 of 128

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [INU](https://xrpl.to/token/r38ghAFYDauA1V7ADEnQ5RCVbcpWvN568Z-INU) | FAIL_SAFETY | pool too small (xrpl.to TVL 248 XRP) | 124 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 6438 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,144 XRP) | 572 |
| [POOL](https://xrpl.to/token/r9D5RhucFjzBmdXcwc68VRbG2EYr4zqJmF-504F4F4C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,625 XRP) | 1313 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,036 XRP) | 518 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 71% (excl. AMM) | 2078 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 7674 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62750 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 192691 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | 24h volume 262 XRP too low | 19734 |
| [CRAP](https://xrpl.to/token/rDpyFiCNn7m5Y4zqzP5W1bUUGG4SEffnom-4352415000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,827 XRP) | 1414 |
| [PERCY](https://xrpl.to/token/rE2HYC1jehXeE9x5ze7NLnSFmGRLAEwt3-5045524359000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2057 |
| [G.O.A.T](https://xrpl.to/token/rEfm8SFkKqiD6cx7ieeTBAcALkhH2sKpNz-472E4F2E412E5400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 354 XRP) | 177 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 413 XRP) | 206 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6254 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 11967 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 11705 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,856 XRP < 2,000 | 1856 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 452 XRP) | 226 |
| [321BG](https://xrpl.to/token/rJeCmBFjiz1TBD32wSeLEGKXofYxekiwjZ-3332314247000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 186 XRP) | 93 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 2612 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42449 |
| [XRPICASSO](https://xrpl.to/token/rKRp2BqRmHgkY6Akyr2wh5UehuTyPmv1iG-58525049434153534F0000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 555 XRP) | 277 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 154390 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2610 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,114 XRP) | 557 |
| [ROCK](https://xrpl.to/token/rM2LZ53PobDBpEWZJp9cCAZhViRyy1TbyL-524F434B00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 74% (excl. AMM) | 3227 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9247 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,682 XRP) | 841 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3430 |
| [EAPE](https://xrpl.to/token/rPUQrzNnAurx4CckQ59NH2ECbYvRq229sD-4541504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 659 XRP) | 330 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 782 XRP) | 391 |
| [SIB](https://xrpl.to/token/rPz9bsto7F4adfUfE5iDQAgW2DWo74YZsw-SIB) | FAIL_SAFETY | pool too small (xrpl.to TVL 764 XRP) | 382 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7258 |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | SKIP_ENTRY | not new and not top trending | 2163 |
| [PIPES](https://xrpl.to/token/rUe1BVJmxscgDnCEsanRQa4RzxXy39sQKN-5049504553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 514 XRP) | 257 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227972 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 410 XRP too low | 308656 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,763 XRP) | 1382 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 78153 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
