# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-19T19:24:06+00:00** (UTC) · XRP/USD 0.9680 (bitstamp) · last discovery 2026-11-19T19:24:06+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$61.13** | **-38.87** | $2.54 | 6 / $58.59 | $-37.27 | $-1.41 | 23 / 49 (32%) | 78 (72) | -14.61 | -1.40 | 63.16 | -14.88 | $7.65 (0.29992) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$73.69** | **-26.31** | $2.02 | 7 / $71.67 | $-27.74 | $+1.67 | 24 / 60 (29%) | 91 (84) | -4.63 | +1.52 | 76.13 | -1.91 | $9.25 (0.39332) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$78.86** | **-21.14** | $78.86 | 0 / $0.00 | $-20.45 | $+0.00 | 56 / 214 (21%) | 270 (270) | -14.88 | +0.00 | 81.47 | +3.44 | $30.41 (1.11921) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$63.82** | **-36.18** | $4.86 | 6 / $58.96 | $-34.45 | $-1.04 | 74 / 161 (31%) | 241 (235) | -12.25 | -1.30 | 65.93 | -12.17 | $26.58 (1.15297) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 91.03 | +12.92 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$94.85** | **-5.15** | $64.28 | 3 / $30.57 | $-4.95 | $+0.57 | 79 / 106 (43%) | 188 (185) | +1.50 | +0.72 | 97.98 | +19.88 | $25.09 (1.25937) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$75.53** | **-24.47** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T19:04 | $10.00 | 1.00 | 1.00 @ 0.3h | 1.00 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 1.02 | 1.02 @ 8.8h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T18:18 | $10.00 | 1.02 | 1.05 @ 2.6h | 0.91 |  |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-17T12:01 | $10.00 | 0.85 | 1.00 @ 7.6h | 0.84 | top-10 holders own 42% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.97 | 0.99 @ 1.1h | 0.97 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 1.01 | 1.01 @ 55.6h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 1.00 | 1.00 @ 8.8h | 1.00 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.05 | 1.05 @ 16.9h | 0.99 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.02 | 1.02 @ 16.9h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T15:50 | $10.00 | 1.01 | 1.04 @ 5.1h | 0.91 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.97 | 0.99 @ 1.1h | 0.97 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 1.09 | 1.09 @ 55.3h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 1.01 | 1.01 @ 55.6h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-19T19:04 | $10.00 | 1.00 | 1.00 @ 0.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.34% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-19T02:22 | $10.00 | 0.96 | 1.00 @ 0.1h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-19T02:12 | $10.00 | 1.00 | 1.00 @ 17.2h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.00% <= 2.0% |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | 2026-11-19T02:12 | $10.00 | 0.99 | 0.99 @ 17.2h | 0.99 | top-10 holders own 47% | slow_scalp: new/top-15 trending, round trip 0.25% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-18T20:57 | $10.00 | 0.97 | 0.99 @ 0.1h | 0.97 | only 24% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.12% <= 2.0% |
| [WBC](https://xrpl.to/token/rnFdeZggmwKLXGaHvTL4aTwfEsPPXV5FHa-WBC) | 2026-11-18T20:57 | $10.00 | 0.96 | 0.98 @ 0.4h | 0.96 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 1.07 | 1.07 @ 9.0h | 0.96 | top-10 holders own 44% | dip_bounce: 38.3% below 24h high 6.66378e-05 XRP, age 5.4d |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-18T20:57 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 |  | dip_bounce: 24.5% below 24h high 0.000490698 XRP, age 527.3d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-18T20:57 | $10.00 | 1.03 | 1.04 @ 0.5h | 0.99 | top-10 holders own 31% | dip_bounce: 16.5% below 24h high 2.07402e-05 XRP, age 764.9d |

## How high do they run? (tracking only — no rule uses this)

759 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 109 | 14% |
| ≥ +20% | 34 | 4% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.6h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 128 of 759

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9306 |
| [122](https://xrpl.to/token/r3DRvEEWW3dSM3aQnFkNPW44xJDNB7NU9P-122) | FAIL_SAFETY | pool too small (xrpl.to TVL 27 XRP) | 14 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3810 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62437 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 33604 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 523 XRP) | 261 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30629 |
| [XGM](https://xrpl.to/token/r9y81Gs4ywWV93sC4jhGpCc7cZWrK6YAr2-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 143 XRP) | 72 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,070 XRP) | 1535 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 475 XRP) | 237 |
| [RAMP](https://xrpl.to/token/rBsaniKL1PeSLCfah8aSBscbKFPr19AGf9-52414D5000000000000000000000000000000000) | FAIL_SAFETY | pool 1,955 XRP < 2,000 | 1955 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 160 XRP too low | 61867 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | 24h volume 285 XRP too low | 18430 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,018 XRP) | 509 |
| [PERCY](https://xrpl.to/token/rE2HYC1jehXeE9x5ze7NLnSFmGRLAEwt3-5045524359000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 293 XRP too low | 2566 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4277 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 229 XRP too low | 7229 |
| [DALE](https://xrpl.to/token/rGeujAELaCqCkM9jktG2MkeQNzNEDtd62z-44414C4500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,998 XRP) | 999 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 827 XRP) | 413 |
| [EGG](https://xrpl.to/token/rJ8J3n4cwCmXE3NnuUuSGP1HYABsrNadMj-EGG) | FAIL_SAFETY | pool too small (xrpl.to TVL 2 XRP) | 1 |
| [GODFATHER](https://xrpl.to/token/rJDy51gMWfvWyQN6gQRLnTFUHM4WKwPZXQ-474F444641544845520000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 38 XRP) | 19 |
| [PVE](https://xrpl.to/token/rJs1u9sS3372vBQEWp3LW34FyePvjmePCn-PVE) | FAIL_SAFETY | pool too small (xrpl.to TVL 32 XRP) | 16 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 159408 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,850 XRP) | 1425 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool 1,940 XRP < 2,000 | 1940 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,223 XRP) | 612 |
| [VOX](https://xrpl.to/token/rM22BKFMSx7qDi8bp7Ke4nGg9apo1GfJXD-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 17 XRP) | 8 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,028 XRP) | 1014 |
| [XGM](https://xrpl.to/token/rNKfDB5djjH8iwGLApBWJCR1eW9khxU2qy-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,226 XRP) | 613 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 397 XRP too low | 3240 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2293 |
| [MLRD](https://xrpl.to/token/rPytUzcUxVbzv439EShC7hPWFND8NCbEMU-4D4C524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 827 XRP) | 414 |
| [FZV](https://xrpl.to/token/rUkSXmFrYDkSJnjBSb79VdLfbNjjYwLCLp-FZV) | FAIL_SAFETY | pool too small (xrpl.to TVL 76 XRP) | 38 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 221929 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81152 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 74216 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool 1,706 XRP < 2,000 | 1706 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2591 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11272 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 135 XRP too low | 13930 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
