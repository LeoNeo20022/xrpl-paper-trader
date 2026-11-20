# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-20T08:42:32+00:00** (UTC) · XRP/USD 0.9635 (bitstamp) · last discovery 2026-11-20T08:42:32+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$61.05** | **-38.95** | $2.54 | 6 / $58.51 | $-37.27 | $-1.49 | 23 / 49 (32%) | 78 (72) | -14.61 | -1.19 | 63.37 | -14.67 | $7.65 (0.29992) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$73.42** | **-26.58** | $2.02 | 7 / $71.40 | $-27.74 | $+1.40 | 24 / 60 (29%) | 91 (84) | -4.63 | +1.58 | 76.20 | -1.83 | $9.24 (0.39332) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$78.62** | **-21.38** | $78.62 | 0 / $0.00 | $-20.70 | $+0.00 | 58 / 219 (21%) | 277 (277) | -15.10 | +0.00 | 81.60 | +3.56 | $31.22 (1.11977) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$64.03** | **-35.97** | $3.97 | 6 / $60.06 | $-35.35 | $+0.06 | 75 / 165 (31%) | 246 (240) | -13.28 | +0.24 | 66.46 | -11.65 | $27.07 (1.15337) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 91.45 | +13.34 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$88.67** | **-11.33** | $79.13 | 1 / $9.54 | $-10.09 | $-0.46 | 80 / 108 (43%) | 189 (188) | -3.61 | -0.46 | 92.03 | +13.93 | $25.32 (1.25953) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$75.18** | **-24.82** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T19:04 | $10.00 | 1.01 | 1.01 @ 13.6h | 1.00 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 1.00 | 1.02 @ 8.8h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T18:18 | $10.00 | 1.02 | 1.05 @ 2.6h | 0.91 |  |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-17T12:01 | $10.00 | 0.87 | 1.00 @ 7.6h | 0.84 | top-10 holders own 42% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.95 | 0.99 @ 1.1h | 0.95 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 1.03 | 1.03 @ 68.8h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 1.01 | 1.01 @ 22.4h | 1.00 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.08 | 1.08 @ 30.5h | 0.99 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.01 | 1.02 @ 16.9h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T15:50 | $10.00 | 1.01 | 1.04 @ 5.1h | 0.91 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.95 | 0.99 @ 1.1h | 0.95 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 1.06 | 1.09 @ 55.3h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 1.03 | 1.03 @ 68.8h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-20T01:14 | $10.00 | 1.00 | 1.00 @ 7.3h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T01:14 | $10.00 | 0.98 | 0.98 @ 7.3h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 1.66% <= 2.0% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-19T19:04 | $10.00 | 1.06 | 1.06 @ 13.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.34% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-20T01:14 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.95 | top-10 holders own 45% | dip_bounce: 16.0% below 24h high 5.98338e-05 XRP, age 26.9d |

## How high do they run? (tracking only — no rule uses this)

770 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 109 | 14% |
| ≥ +20% | 34 | 4% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 129 of 770

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [WARD](https://xrpl.to/token/r1GmYwqEFNiAEdLCpjvKSxjEgbLhYcGWQ-5741524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,352 XRP) | 1176 |
| [INU](https://xrpl.to/token/r38ghAFYDauA1V7ADEnQ5RCVbcpWvN568Z-INU) | FAIL_SAFETY | pool too small (xrpl.to TVL 217 XRP) | 109 |
| [122](https://xrpl.to/token/r3DRvEEWW3dSM3aQnFkNPW44xJDNB7NU9P-122) | FAIL_SAFETY | pool too small (xrpl.to TVL 28 XRP) | 14 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 61261 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 33516 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 335 XRP) | 168 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,276 XRP) | 638 |
| [BRETT](https://xrpl.to/token/r9aQij7Hj4XnPVKDcK5zhPGDrAMmi4mqVp-4252455454000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 444 XRP) | 222 |
| [XGM](https://xrpl.to/token/r9y81Gs4ywWV93sC4jhGpCc7cZWrK6YAr2-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 144 XRP) | 72 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,625 XRP) | 1312 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 463 XRP) | 232 |
| [Jester](https://xrpl.to/token/rBx9hAq9AQpJZyHqpTyTiw9jjsR3W866bC-4A65737465720000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,305 XRP) | 1153 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 175 XRP too low | 61839 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 96 XRP too low | 18398 |
| [CLOCK](https://xrpl.to/token/rEUme77m2NNsFtUJ9MRrp2c1xorsikAEyR-434C4F434B000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 97 XRP) | 49 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6981 |
| [DALE](https://xrpl.to/token/rGeujAELaCqCkM9jktG2MkeQNzNEDtd62z-44414C4500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,772 XRP) | 886 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,255 XRP) | 1128 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 753 XRP) | 376 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 219 XRP too low | 16549 |
| [EGG](https://xrpl.to/token/rJ8J3n4cwCmXE3NnuUuSGP1HYABsrNadMj-EGG) | FAIL_SAFETY | pool too small (xrpl.to TVL 2 XRP) | 1 |
| [GODFATHER](https://xrpl.to/token/rJDy51gMWfvWyQN6gQRLnTFUHM4WKwPZXQ-474F444641544845520000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 39 XRP) | 20 |
| [PVE](https://xrpl.to/token/rJs1u9sS3372vBQEWp3LW34FyePvjmePCn-PVE) | FAIL_SAFETY | pool too small (xrpl.to TVL 32 XRP) | 16 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43751 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 159275 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,971 XRP) | 1486 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 305 XRP too low | 10353 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,987 XRP) | 994 |
| [MarioCoin](https://xrpl.to/token/rNp8bzT7FQX3TVB8da1jUDKzFgGYKwqKkU-4D6172696F436F696E0000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 145 XRP) | 73 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,688 XRP < 2,000 | 1688 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42708 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 233 XRP too low | 13778 |
| [MLRD](https://xrpl.to/token/rPytUzcUxVbzv439EShC7hPWFND8NCbEMU-4D4C524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 465 XRP) | 233 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5129 |
| [FZV](https://xrpl.to/token/rUkSXmFrYDkSJnjBSb79VdLfbNjjYwLCLp-FZV) | FAIL_SAFETY | pool too small (xrpl.to TVL 76 XRP) | 38 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 221987 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 83275 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 228 XRP too low | 10868 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 45129 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 200 XRP too low | 13548 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
