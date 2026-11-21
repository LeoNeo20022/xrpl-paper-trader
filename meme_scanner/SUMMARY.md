# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-21T04:21:15+00:00** (UTC) · XRP/USD 0.8752 (bitstamp) · last discovery 2026-11-21T04:21:15+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$55.11** | **-44.89** | $8.88 | 5 / $46.24 | $-40.94 | $-3.76 | 23 / 53 (30%) | 81 (76) | -15.93 | -0.76 | 62.97 | -15.06 | $7.88 (0.30020) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$65.52** | **-34.48** | $0.09 | 7 / $65.43 | $-29.67 | $-4.57 | 24 / 64 (27%) | 95 (88) | -3.96 | -0.57 | 74.87 | -3.16 | $9.55 (0.39364) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$78.35** | **-21.65** | $58.58 | 2 / $19.77 | $-20.73 | $-0.23 | 60 / 220 (21%) | 282 (280) | -15.55 | -0.22 | 89.52 | +11.49 | $31.37 (1.12009) | 0.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$57.15** | **-42.85** | $11.71 | 5 / $45.43 | $-37.60 | $-4.57 | 75 / 168 (31%) | 248 (243) | -13.41 | -1.26 | 65.29 | -12.81 | $27.26 (1.15357) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 100.67 | +22.57 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$85.00** | **-15.00** | $85.00 | 0 / $0.00 | $-14.22 | $+0.00 | 80 / 110 (42%) | 190 (190) | -7.02 | +0.00 | 97.12 | +19.02 | $25.51 (1.25965) | 0.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$68.29** | **-31.71** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T23:05 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.01 @ 10.7h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.93 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T19:04 | $10.00 | 0.97 | 1.01 @ 13.7h | 0.97 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.99 | 1.02 @ 8.8h | 0.98 | only 28% of LP burned (liquidity can be pulled) |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.01 @ 10.7h | 1.00 |  |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T17:15 | $10.00 | 1.00 | 1.00 @ 6.1h | 0.99 |  |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.99 | 0.99 @ 10.9h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.97 | 1.00 @ 10.7h | 0.97 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.98 | 1.01 @ 22.5h | 0.98 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.01 | 1.08 @ 30.9h | 0.99 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 0.99 | 1.02 @ 16.9h | 0.97 | only 28% of LP burned (liquidity can be pulled) |

### scalp — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-21T03:56 | $10.00 | 0.99 | 0.99 @ 0.4h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-21T03:56 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-20T23:30 | $10.00 | 0.99 | 0.99 @ 4.8h | 0.98 | only 37% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.97 | 1.00 @ 10.7h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 0.97 | 1.00 @ 0.6h | 0.97 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 0.97 | 1.00 @ 9.3h | 0.94 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-20T08:32 | $10.00 | 0.98 | 0.99 @ 9.1h | 0.97 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (0)

None.

## How high do they run? (tracking only — no rule uses this)

781 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 109 | 14% |
| ≥ +20% | 34 | 4% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 131 of 781

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [WARD](https://xrpl.to/token/r1GmYwqEFNiAEdLCpjvKSxjEgbLhYcGWQ-5741524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,346 XRP) | 1173 |
| [INU](https://xrpl.to/token/r38ghAFYDauA1V7ADEnQ5RCVbcpWvN568Z-INU) | FAIL_SAFETY | pool too small (xrpl.to TVL 217 XRP) | 109 |
| [122](https://xrpl.to/token/r3DRvEEWW3dSM3aQnFkNPW44xJDNB7NU9P-122) | FAIL_SAFETY | pool too small (xrpl.to TVL 28 XRP) | 14 |
| [JEZUS](https://xrpl.to/token/r4AgGS5mrckhY4bSTJwCWgpWKsEZGeWm1J-4A455A5553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,307 XRP) | 1153 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 364 XRP too low | 7545 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62064 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32256 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30685 |
| [BRETT](https://xrpl.to/token/r9aQij7Hj4XnPVKDcK5zhPGDrAMmi4mqVp-4252455454000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 452 XRP) | 226 |
| [XGM](https://xrpl.to/token/r9y81Gs4ywWV93sC4jhGpCc7cZWrK6YAr2-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 127 XRP) | 63 |
| [Jester](https://xrpl.to/token/rBx9hAq9AQpJZyHqpTyTiw9jjsR3W866bC-4A65737465720000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,227 XRP) | 1114 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | 24h volume 258 XRP too low | 61802 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 194998 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | 24h volume 249 XRP too low | 18318 |
| [CFH](https://xrpl.to/token/rDTHkzTq3Acxu6QrSLVfHrR3KadFknMkfS-CFH) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,398 XRP) | 699 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 992 XRP) | 496 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,094 XRP) | 1047 |
| [CLOCK](https://xrpl.to/token/rEUme77m2NNsFtUJ9MRrp2c1xorsikAEyR-434C4F434B000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 93 XRP) | 46 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 220926 |
| [LIONS](https://xrpl.to/token/rGHtf1GTfXEXSPxmZfnQrUMGUpajYqAuzS-4C494F4E53000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3741 |
| [$BUBBLES](https://xrpl.to/token/rGUKfQ2Sm35KFSZ6BuKsjHxgyKSYgV7pzs-24425542424C4553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,954 XRP) | 977 |
| [DALE](https://xrpl.to/token/rGeujAELaCqCkM9jktG2MkeQNzNEDtd62z-44414C4500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,648 XRP) | 824 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 210 XRP too low | 16556 |
| [EGG](https://xrpl.to/token/rJ8J3n4cwCmXE3NnuUuSGP1HYABsrNadMj-EGG) | FAIL_SAFETY | pool too small (xrpl.to TVL 3 XRP) | 2 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 10071 |
| [dfgsdf](https://xrpl.to/token/rKH61s7vXBk9gMCvTtXNjGi7H5jJYkHMHY-6466677364660000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 131 XRP) | 66 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 160160 |
| [JoelKatz](https://xrpl.to/token/rKzxgXw99kiVcT9QWN4EPPDn8QxktxBT79-4A6F656C4B61747A000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,050 XRP) | 525 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending; 24h volume 241 XRP too low | 2301 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,406 XRP) | 1203 |
| [LFQP](https://xrpl.to/token/rLnh3vjwgjjr6CNBq7ddsdcnCddxhsGLXN-4C46515000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 348 XRP) | 174 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10824 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3367 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 734 XRP) | 367 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,831 XRP < 2,000 | 1831 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42731 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 214 XRP too low | 13768 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2680251 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 4918 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 222078 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
