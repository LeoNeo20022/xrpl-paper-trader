# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-09T00:46:03+00:00** (UTC) · XRP/USD 1.1208 (bitstamp) · last discovery 2026-11-09T00:46:03+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$79.34** | **-20.66** | $2.79 | 8 / $76.55 | $-17.03 | $-3.45 | 19 / 31 (38%) | 58 (50) | -6.90 | -0.63 | 70.78 | -7.25 | $5.94 (0.27808) | 1.6 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$90.81** | **-9.19** | $7.78 | 9 / $83.03 | $-2.00 | $-6.97 | 21 / 36 (37%) | 66 (57) | +5.54 | -3.12 | 81.02 | +2.99 | $6.90 (0.33794) | 1.8 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$90.33** | **-9.67** | $40.54 | 5 / $49.79 | $-8.88 | $-0.21 | 34 / 126 (21%) | 165 (160) | -4.70 | -0.59 | 80.59 | +2.56 | $18.44 (0.90626) | 1.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$81.67** | **-18.33** | $3.55 | 8 / $78.12 | $-15.94 | $-1.88 | 56 / 100 (36%) | 164 (156) | -6.10 | -0.70 | 72.87 | -5.24 | $18.02 (0.82334) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 78.61 | +0.50 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$107.82** | **+7.82** | $79.63 | 3 / $28.18 | $+10.30 | $-1.82 | 68 / 72 (49%) | 143 (140) | +9.72 | -0.69 | 96.19 | +18.09 | $19.37 (1.05134) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$87.46** | **-12.54** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T18:05 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.98 |  |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-08T13:54 | $10.00 | 0.93 | 0.99 @ 0.7h | 0.90 | top-10 holders own 34% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-08T11:55 | $10.00 | 0.99 | 0.99 @ 12.8h | 0.97 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.03 | 1.05 @ 6.6h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.98 | 1.00 @ 0.9h | 0.98 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.02 | 1.07 @ 7.6h | 0.99 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T17:19 | $10.00 | 1.01 | 1.03 @ 21.6h | 0.98 | only 21% of LP burned (liquidity can be pulled) |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T05:47 | $10.00 | 0.98 | 0.98 @ 5.2h | 0.97 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |

### plus5 — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T15:40 | $10.00 | 0.99 | 1.00 @ 1.6h | 0.99 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.03 | 1.05 @ 6.6h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.98 | 1.00 @ 0.9h | 0.98 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.02 | 1.07 @ 7.6h | 0.99 | top-10 holders own 31% |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-07T14:58 | $10.00 | 0.93 | 1.02 @ 25.6h | 0.92 | top-10 holders own 38% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T02:55 | $10.00 | 0.97 | 0.99 @ 36.0h | 0.95 | only 21% of LP burned (liquidity can be pulled) |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-07T02:55 | $10.00 | 0.84 | 1.07 @ 18.9h | 0.80 | top-10 holders own 46% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T00:12 | $10.00 | 0.99 | 0.99 @ 10.7h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-11-06T22:54 | $10.00 | 0.88 | 0.98 @ 0.4h | 0.88 | top-10 holders own 46% |

### scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-09T00:10 | $10.00 | 0.96 | 0.98 @ 0.1h | 0.96 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 30% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-09T00:00 | $10.00 | 1.00 | 1.00 @ 0.8h | 1.00 |  |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 34% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-09T00:00 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-09T00:46 | $10.00 | 1.00 | – | – | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.90% <= 2.0% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.80% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.99 | 0.99 @ 0.8h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.19% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-08T12:46 | $10.00 | 1.00 | 1.01 @ 6.5h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T09:38 | $10.00 | 0.99 | 1.00 @ 2.9h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.38% <= 2.0% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-08T03:13 | $10.00 | 0.98 | 0.99 @ 12.0h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 1.66% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-08T01:04 | $10.00 | 0.99 | 1.01 @ 18.3h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-08T14:54 | $10.00 | 0.99 | 1.00 @ 0.4h | 0.97 | top-10 holders own 31% | dip_bounce: 16.2% below 24h high 6.26523e-07 XRP, age 107.9d |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-08T13:34 | $10.00 | 0.99 | 1.07 @ 0.1h | 0.95 | top-10 holders own 34% | dip_bounce: 29.2% below 24h high 2.05164e-05 XRP, age 735.6d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T03:13 | $10.00 | 0.95 | 0.99 @ 16.1h | 0.92 | top-10 holders own 31% | dip_bounce: 15.2% below 24h high 3.878e-05 XRP, age 754.1d |

## How high do they run? (tracking only — no rule uses this)

500 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 88 | 18% |
| ≥ +20% | 30 | 6% |
| ≥ +30% | 19 | 4% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 99 of 500

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4167 |
| [EULER](https://xrpl.to/token/r3uXxU883rgcMbVureoafeCx1VX4WbeQfk-45554C4552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 16 XRP) | 8 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 70842 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29271 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 715 XRP) | 358 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,172 XRP) | 586 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool 1,632 XRP < 2,000 | 1632 |
| [SCHWATOSHI](https://xrpl.to/token/rB1xGmTgqF8WSRbyaRD3AR4PkyTC1eyErL-5343485741544F53484900000000000000000000) | FAIL_SAFETY | pool 1,951 XRP < 2,000 | 1951 |
| [GHOST](https://xrpl.to/token/rB8FVTvTjLie6tC2kFabczgt6QedWY45k5-47484F5354000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 67 XRP) | 34 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,799 XRP) | 1400 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,459 XRP) | 1229 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 267 XRP too low | 61525 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19211 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 235367 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,784 XRP) | 1392 |
| [OWL](https://xrpl.to/token/rH8oHtbNDueptu9Djoee8J97sTP9hecBww-OWL) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,724 XRP) | 1362 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 311 XRP too low | 15968 |
| [MOUSE](https://xrpl.to/token/rJevHGVUzAUPSGxiECgqcNVNVjRkTBWD7T-4D4F555345000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6828 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 11012 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,006 XRP) | 503 |
| [HAZZY](https://xrpl.to/token/rKLt8jGHt7oM4cv94FvxQpGywYbf1FMoon-48415A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 229 XRP) | 115 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5390 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156587 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,908 XRP) | 1454 |
| [CREATE](https://xrpl.to/token/rMqZY49eXVxU9rgrHVix7jkLeZcEeni9nU-4352454154450000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,988 XRP) | 994 |
| [LAZZY](https://xrpl.to/token/rMs5orCnoGiPU69ueCbWCry28UKDEBhGC5-4C415A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 612 XRP) | 306 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 4628 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,444 XRP) | 1222 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 267 XRP) | 133 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 185 XRP) | 93 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 40979 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2682509 |
| [TEST](https://xrpl.to/token/rU55fFMW8kpTM5k2yWWz1oEnHjHm2CBPsE-5445535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 75 XRP) | 38 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6142 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5616 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 225773 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81840 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 77859 |
| [SIMON](https://xrpl.to/token/raF19Hb2JpxixGYbsjXYyfshWoQjKLcY3f-53494D4F4E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 381 XRP) | 190 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2557 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
