# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-22T03:42:46+00:00** (UTC) · XRP/USD 0.9156 (bitstamp) · last discovery 2026-11-22T03:42:46+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$57.83** | **-42.17** | $8.88 | 5 / $48.95 | $-40.94 | $-1.05 | 23 / 53 (30%) | 81 (76) | -15.93 | -0.13 | 63.15 | -14.88 | $7.88 (0.30020) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$68.36** | **-31.64** | $9.10 | 6 / $59.26 | $-30.66 | $-0.74 | 24 / 66 (27%) | 96 (90) | -4.05 | -0.70 | 74.66 | -3.38 | $9.70 (0.39376) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$77.65** | **-22.35** | $67.71 | 1 / $9.94 | $-21.60 | $-0.06 | 67 / 227 (23%) | 295 (294) | -18.25 | -0.05 | 84.80 | +6.77 | $32.84 (1.12117) | 0.2 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$55.98** | **-44.02** | $7.19 | 5 / $48.80 | $-42.13 | $-1.20 | 76 / 174 (30%) | 255 (250) | -17.10 | -1.15 | 61.14 | -16.96 | $28.00 (1.15413) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 96.23 | +18.12 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$84.90** | **-15.10** | $65.00 | 2 / $19.90 | $-14.22 | $-0.10 | 80 / 110 (42%) | 192 (190) | -7.02 | +0.08 | 92.72 | +14.62 | $25.66 (1.25973) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$71.45** | **-28.55** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T23:05 | $10.00 | 1.00 | 1.00 @ 24.4h | 0.99 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.99 | 0.99 @ 34.2h | 0.93 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T19:04 | $10.00 | 0.99 | 1.01 @ 13.7h | 0.97 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.99 | 1.02 @ 8.8h | 0.98 | only 28% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | 2026-11-22T03:22 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 33% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T17:15 | $10.00 | 1.00 | 1.00 @ 30.2h | 0.99 |  |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.99 | 0.99 @ 34.1h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.95 | 1.00 @ 10.7h | 0.95 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-19T10:16 | $10.00 | 0.99 | 1.01 @ 22.5h | 0.98 |  |

### scalp — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T03:22 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | top-10 holders own 31% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-22T00:04 | $10.00 | 0.98 | 0.98 @ 3.6h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-21T23:35 | $10.00 | 0.95 | 0.99 @ 0.5h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | 2026-11-21T18:24 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 44% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-21T11:54 | $10.00 | 0.99 | 1.00 @ 0.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-21T11:54 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XLM](https://xrpl.to/token/r44CR5cYKVyzuJpFUtF2ZRDizVZpvtkc4C-XLM) | 2026-11-22T03:37 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 50% | dip_bounce: 22.0% below 24h high 5.08336e-07 XRP, age 723.2d |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-21T18:24 | $10.00 | 1.02 | 1.02 @ 9.3h | 0.99 | top-10 holders own 45% | dip_bounce: 22.3% below 24h high 5.41755e-05 XRP, age 28.6d |

## How high do they run? (tracking only — no rule uses this)

800 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 109 | 14% |
| ≥ +20% | 34 | 4% |
| ≥ +30% | 20 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 132 of 800

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [WARD](https://xrpl.to/token/r1GmYwqEFNiAEdLCpjvKSxjEgbLhYcGWQ-5741524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,350 XRP) | 1175 |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 446 XRP too low | 9209 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3707 |
| [RPR](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-RPR) | FAIL_SAFETY | issuer not blackholed (can still mint) | 4626 |
| [XLM](https://xrpl.to/token/r44CR5cYKVyzuJpFUtF2ZRDizVZpvtkc4C-XLM) | SKIP_ENTRY | not new and not top trending | 2516 |
| [JEZUS](https://xrpl.to/token/r4AgGS5mrckhY4bSTJwCWgpWKsEZGeWm1J-4A455A5553000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,652 XRP) | 1326 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 64049 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 439 XRP) | 220 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30527 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 297 XRP too low | 19721 |
| [Jester](https://xrpl.to/token/rBx9hAq9AQpJZyHqpTyTiw9jjsR3W866bC-4A65737465720000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,012 XRP) | 506 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 283 XRP too low | 61566 |
| [Oof](https://xrpl.to/token/rEYAtBL8BbyHETFkpWSPZmEBZGGgn2YShZ-Oof) | FAIL_SAFETY | pool too small (xrpl.to TVL 871 XRP) | 436 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7015 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 11267 |
| [PUPPET](https://xrpl.to/token/rJfQFeHTZcnRsY4Ba5sJVKUhLs48E9apBn-5055505045540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6759 |
| [dfgsdf](https://xrpl.to/token/rKH61s7vXBk9gMCvTtXNjGi7H5jJYkHMHY-6466677364660000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 127 XRP) | 63 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 160103 |
| [Exrploit](https://xrpl.to/token/rLSD1svPhf5V5ryhhqGZac6iEcNmUSHH1M-457872706C6F6974000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 138 XRP) | 69 |
| [LFQP](https://xrpl.to/token/rLnh3vjwgjjr6CNBq7ddsdcnCddxhsGLXN-4C46515000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 270 XRP) | 135 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10539 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3493 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 721 XRP) | 361 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,653 XRP < 2,000 | 1653 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5455 |
| [Pebble](https://xrpl.to/token/rUNZsXtpU5NaDePcyYJmjRZjoFdGNRLaQn-506562626C650000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 393 XRP too low | 3438 |
| [VOX](https://xrpl.to/token/rUiHyCL7UuFfn4gRSFFfRyVZgzRtLVQyQc-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 932 XRP) | 466 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227167 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 308 XRP too low | 310464 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 85658 |
| [MWZ](https://xrpl.to/token/rf6xCFKUGmDiGw8bKRjCh7fXUCneedAhqR-MWZ) | FAIL_SAFETY | pool too small (xrpl.to TVL 533 XRP) | 266 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 43302 |
| [589](https://xrpl.to/token/rfb7KpF5Ad5cQzQLJCQX7aUkFeVpkNUVen-589) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,153 XRP) | 1577 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending; 24h volume 118 XRP too low | 26487 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 131465 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 82329 |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 122497 |
| [DONNIE](https://xrpl.to/token/rhhaVvZF69sQBgiDuM2avL2pbrryT5cGTF-444F4E4E49450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 352 XRP too low | 20161 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 5595 |
| [WARP](https://xrpl.to/token/rhuQ5tKUHG77J5ovRN4GVSwZJT5SDTZZCD-5741525000000000000000000000000000000000) | FAIL_SAFETY | pool 1,710 XRP < 2,000 | 1710 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
