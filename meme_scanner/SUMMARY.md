# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-21T23:29:59+00:00** (UTC) · XRP/USD 0.9308 (bitstamp) · last discovery 2026-11-21T23:29:59+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$58.38** | **-41.62** | $8.88 | 5 / $49.50 | $-40.94 | $-0.50 | 23 / 53 (30%) | 81 (76) | -15.93 | -0.41 | 62.71 | -15.32 | $7.88 (0.30020) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$69.66** | **-30.34** | $0.09 | 7 / $69.57 | $-29.67 | $-0.43 | 24 / 64 (27%) | 95 (88) | -3.96 | -0.59 | 74.84 | -3.19 | $9.56 (0.39364) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$78.41** | **-21.59** | $78.41 | 0 / $0.00 | $-20.90 | $+0.00 | 67 / 223 (23%) | 290 (290) | -18.02 | +0.00 | 84.24 | +6.21 | $32.53 (1.12081) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$58.46** | **-41.54** | $7.66 | 5 / $50.80 | $-41.65 | $+0.80 | 75 / 173 (30%) | 253 (248) | -16.34 | -0.12 | 62.81 | -15.30 | $27.71 (1.15397) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 94.66 | +16.55 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$85.15** | **-14.85** | $75.00 | 1 / $10.15 | $-14.22 | $+0.15 | 80 / 110 (42%) | 191 (190) | -7.02 | +0.16 | 91.47 | +13.37 | $25.62 (1.25969) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$72.64** | **-27.36** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T23:05 | $10.00 | 1.00 | 1.00 @ 24.4h | 0.99 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.98 | 0.99 @ 0.6h | 0.93 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T19:04 | $10.00 | 0.99 | 1.01 @ 13.7h | 0.97 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.98 | 1.02 @ 8.8h | 0.98 | only 28% of LP burned (liquidity can be pulled) |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T17:15 | $10.00 | 1.00 | 1.00 @ 30.2h | 0.99 |  |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.98 | 0.99 @ 19.2h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.96 | 1.00 @ 10.7h | 0.95 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.99 | 1.01 @ 22.5h | 0.98 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 1.02 | 1.08 @ 30.9h | 0.99 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T02:12 | $10.00 | 0.98 | 1.02 @ 16.9h | 0.97 | only 28% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | 2026-11-21T18:24 | $10.00 | 1.02 | 1.02 @ 5.1h | 0.94 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.21% <= 2.0% |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | 2026-11-21T18:24 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 44% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-21T11:54 | $10.00 | 0.99 | 1.00 @ 0.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-21T11:54 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-20T23:30 | $10.00 | 1.01 | 1.01 @ 24.0h | 0.98 | only 37% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-21T18:24 | $10.00 | 1.02 | 1.02 @ 5.1h | 0.99 | top-10 holders own 45% | dip_bounce: 22.3% below 24h high 5.41755e-05 XRP, age 28.6d |

## How high do they run? (tracking only — no rule uses this)

792 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 109 | 14% |
| ≥ +20% | 34 | 4% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 132 of 792

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [WARD](https://xrpl.to/token/r1GmYwqEFNiAEdLCpjvKSxjEgbLhYcGWQ-5741524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,350 XRP) | 1175 |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9209 |
| [RPR](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-RPR) | FAIL_SAFETY | issuer not blackholed (can still mint) | 4526 |
| [JEZUS](https://xrpl.to/token/r4AgGS5mrckhY4bSTJwCWgpWKsEZGeWm1J-4A455A5553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,332 XRP) | 1166 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 368 XRP too low | 7515 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 62976 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32232 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30576 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 301 XRP too low | 19720 |
| [HBAR](https://xrpl.to/token/rBWPqhs7YZdUN2CJcZPQTv4qAvqts3nkBw-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,140 XRP) | 1070 |
| [Jester](https://xrpl.to/token/rBx9hAq9AQpJZyHqpTyTiw9jjsR3W866bC-4A65737465720000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,038 XRP) | 519 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,094 XRP) | 1047 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6964 |
| [$BUBBLES](https://xrpl.to/token/rGUKfQ2Sm35KFSZ6BuKsjHxgyKSYgV7pzs-24425542424C4553000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,954 XRP) | 977 |
| [DALE](https://xrpl.to/token/rGeujAELaCqCkM9jktG2MkeQNzNEDtd62z-44414C4500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,608 XRP) | 804 |
| [EGG](https://xrpl.to/token/rJ8J3n4cwCmXE3NnuUuSGP1HYABsrNadMj-EGG) | FAIL_SAFETY | pool too small (xrpl.to TVL 3 XRP) | 1 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 11283 |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6759 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 364 XRP too low | 43930 |
| [dfgsdf](https://xrpl.to/token/rKH61s7vXBk9gMCvTtXNjGi7H5jJYkHMHY-6466677364660000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 127 XRP) | 63 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5006 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 159953 |
| [Exrploit](https://xrpl.to/token/rLSD1svPhf5V5ryhhqGZac6iEcNmUSHH1M-457872706C6F6974000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 165 XRP) | 83 |
| [LFQP](https://xrpl.to/token/rLnh3vjwgjjr6CNBq7ddsdcnCddxhsGLXN-4C46515000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 270 XRP) | 135 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3343 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 778 XRP) | 389 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,656 XRP < 2,000 | 1656 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 4846 |
| [VOX](https://xrpl.to/token/rUiHyCL7UuFfn4gRSFFfRyVZgzRtLVQyQc-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 913 XRP) | 456 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 225518 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 258 XRP too low | 310411 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 85580 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 163 XRP too low | 10711 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2568 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51232 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 42427 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 202 XRP too low | 13650 |
| [589](https://xrpl.to/token/rfb7KpF5Ad5cQzQLJCQX7aUkFeVpkNUVen-589) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,153 XRP) | 1577 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending; 24h volume 112 XRP too low | 26494 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 131465 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
