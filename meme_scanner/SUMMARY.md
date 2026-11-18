# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-18T12:53:56+00:00** (UTC) · XRP/USD 0.9824 (bitstamp) · last discovery 2026-11-18T12:53:56+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$61.20** | **-38.80** | $2.72 | 6 / $58.48 | $-37.09 | $-1.52 | 22 / 48 (31%) | 76 (70) | -14.02 | -2.80 | 62.30 | -15.73 | $7.44 (0.29976) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$73.29** | **-26.71** | $2.46 | 7 / $70.84 | $-27.30 | $+0.84 | 23 / 58 (28%) | 88 (81) | -4.22 | -0.38 | 74.61 | -3.43 | $8.84 (0.39308) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$77.15** | **-22.85** | $77.15 | 0 / $0.00 | $-22.17 | $+0.00 | 50 / 210 (19%) | 260 (260) | -15.40 | +0.00 | 78.53 | +0.50 | $29.50 (1.11841) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$64.07** | **-35.93** | $3.79 | 6 / $60.28 | $-35.52 | $+0.28 | 71 / 157 (31%) | 234 (228) | -14.64 | +0.24 | 65.22 | -12.88 | $25.90 (1.15241) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 89.69 | +11.59 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$97.28** | **-2.72** | $65.86 | 3 / $31.42 | $-3.36 | $+1.42 | 78 / 103 (43%) | 184 (181) | +2.78 | +1.28 | 99.03 | +20.92 | $24.53 (1.25905) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$76.66** | **-23.34** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T18:18 | $10.00 | 0.92 | 1.05 @ 2.6h | 0.91 |  |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-17T12:01 | $10.00 | 0.89 | 1.00 @ 7.6h | 0.84 | top-10 holders own 42% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.98 | 0.99 @ 1.1h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 0.99 | 0.99 @ 24.6h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-16T17:49 | $10.00 | 0.95 | 0.99 @ 1.8h | 0.87 | only 24% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-16T06:58 | $10.00 | 0.99 | 1.05 @ 15.5h | 0.97 |  |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T15:50 | $10.00 | 0.92 | 1.04 @ 5.1h | 0.91 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.98 | 0.99 @ 1.1h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.99 | 1.01 @ 5.3h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 0.99 | 0.99 @ 24.6h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-16T03:03 | $10.00 | 0.91 | 0.98 @ 2.2h | 0.87 | top-10 holders own 43% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-16T00:28 | $10.00 | 1.02 | 1.07 @ 22.2h | 0.97 |  |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-15T23:03 | $10.00 | 1.16 | 1.30 @ 49.6h | 0.98 | top-10 holders own 40% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-18T10:15 | $10.00 | 0.99 | 0.99 @ 2.6h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-18T02:26 | $10.00 | 1.01 | 1.01 @ 10.5h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-18T01:19 | $10.00 | 1.01 | 1.02 @ 5.5h | 0.99 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [SWITCH](https://xrpl.to/token/rJ8jyXpdAZhfxMamtLadk8LYFxd1ff6iKQ-5357495443480000000000000000000000000000) | 2026-11-18T00:35 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 | only 25% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.38% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-17T23:20 | $10.00 | 1.03 | 1.04 @ 4.5h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T15:30 | $10.00 | 1.00 | 1.02 @ 1.6h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-18T01:19 | $10.00 | 1.04 | 1.04 @ 11.5h | 0.99 | top-10 holders own 42% | dip_bounce: 20.3% below 24h high 8.08849e-07 XRP, age 758.1d |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T23:20 | $10.00 | 1.01 | 1.01 @ 10.4h | 0.99 |  | dip_bounce: 17.3% below 24h high 3.88668e-06 XRP, age 758.0d |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-17T13:44 | $10.00 | 1.08 | 1.08 @ 9.6h | 0.98 | only 24% of LP burned (liquidity can be pulled) | dip_bounce: 15.1% below 24h high 4.19682e-07 XRP, age 660.0d |

## How high do they run? (tracking only — no rule uses this)

737 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 107 | 15% |
| ≥ +20% | 34 | 5% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.6h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 127 of 737

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8275 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 105 XRP too low | 3894 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62744 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 33453 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 168 XRP) | 84 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 2227 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 472 XRP too low | 20032 |
| [XGM](https://xrpl.to/token/r9y81Gs4ywWV93sC4jhGpCc7cZWrK6YAr2-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 278 XRP) | 139 |
| [PteroX](https://xrpl.to/token/rB3wmmWaYnLUjSLFTYRrXbhrsKdhimac9B-507465726F580000000000000000000000000000) | FAIL_SAFETY | pool 1,649 XRP < 2,000 | 1649 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 446 XRP) | 223 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 321 XRP too low | 18652 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,088 XRP) | 544 |
| [LKH](https://xrpl.to/token/rE2BANxWnyeyGgqyidRSQ9A54t2XVJS55v-4C4B480000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 69 XRP) | 34 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 425 XRP too low | 7054 |
| [B2X](https://xrpl.to/token/rGGq6KDhhi8wkjBPG3QohwWGMhssu8fGtt-B2X) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,856 XRP) | 928 |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | SKIP_ENTRY | 24h volume 465 XRP too low | 31848 |
| [EXPOSED](https://xrpl.to/token/rHfKWt7g9DvWL2av6om7jorF2sic3oQWFo-4558504F53454400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 245 XRP) | 123 |
| [GODFATHER](https://xrpl.to/token/rJDy51gMWfvWyQN6gQRLnTFUHM4WKwPZXQ-474F444641544845520000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 34 XRP) | 17 |
| [PVE](https://xrpl.to/token/rJs1u9sS3372vBQEWp3LW34FyePvjmePCn-PVE) | FAIL_SAFETY | pool too small (xrpl.to TVL 43 XRP) | 21 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 161819 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending | 2301 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 393 XRP) | 196 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,533 XRP) | 767 |
| [VOX](https://xrpl.to/token/rM22BKFMSx7qDi8bp7Ke4nGg9apo1GfJXD-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 15 XRP) | 7 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 10302 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,367 XRP) | 1184 |
| [XGM](https://xrpl.to/token/rNKfDB5djjH8iwGLApBWJCR1eW9khxU2qy-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,135 XRP) | 568 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3399 |
| [Retire](https://xrpl.to/token/rPFDe5C4qv4JTyTVsGDMWTYJtUsTW337XN-5265746972650000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 379 XRP) | 190 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43264 |
| [MLRD](https://xrpl.to/token/rPytUzcUxVbzv439EShC7hPWFND8NCbEMU-4D4C524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 576 XRP) | 288 |
| [SIB](https://xrpl.to/token/rPz9bsto7F4adfUfE5iDQAgW2DWo74YZsw-SIB) | FAIL_SAFETY | pool too small (xrpl.to TVL 658 XRP) | 329 |
| [XVR](https://xrpl.to/token/rRCA6gnPkvpKmWwfcYxHQ845gFQ5ThYQe-XVR) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,917 XRP) | 958 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2680762 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5640 |
| [AGENTS](https://xrpl.to/token/rUfDg9MXCKRUZvQm47e8UhpUGHouwchUpo-4147454E54530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 206 XRP) | 103 |
| [FZV](https://xrpl.to/token/rUkSXmFrYDkSJnjBSb79VdLfbNjjYwLCLp-FZV) | FAIL_SAFETY | pool too small (xrpl.to TVL 92 XRP) | 46 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 223796 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81344 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 75919 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
