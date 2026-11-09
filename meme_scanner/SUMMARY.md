# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-09T21:14:52+00:00** (UTC) · XRP/USD 1.0900 (bitstamp) · last discovery 2026-11-09T21:14:52+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$75.02** | **-24.98** | $2.79 | 8 / $72.23 | $-17.03 | $-7.77 | 19 / 31 (38%) | 58 (50) | -6.90 | -2.65 | 68.83 | -9.20 | $5.94 (0.27808) | 1.6 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$85.79** | **-14.21** | $7.78 | 9 / $78.01 | $-2.00 | $-11.99 | 21 / 36 (37%) | 66 (57) | +5.54 | -5.63 | 78.71 | +0.68 | $6.89 (0.33794) | 1.8 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$88.05** | **-11.95** | $88.05 | 0 / $0.00 | $-11.35 | $+0.00 | 37 / 133 (22%) | 170 (170) | -6.96 | +0.00 | 80.78 | +2.75 | $19.21 (0.95792) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$80.13** | **-19.87** | $1.63 | 8 / $78.50 | $-17.83 | $-1.50 | 57 / 105 (35%) | 170 (162) | -5.97 | -0.45 | 73.52 | -4.59 | $18.69 (0.86488) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 80.84 | +2.73 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$106.45** | **+6.45** | $97.24 | 1 / $9.20 | $+7.92 | $-0.80 | 70 / 75 (48%) | 146 (145) | +9.02 | -0.60 | 97.66 | +19.55 | $19.89 (1.07211) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$85.05** | **-14.95** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005020 XRP/tx = max(0.00002, live open-ledger fee 0.00502), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T18:05 | $10.00 | 0.95 | 0.99 @ 0.2h | 0.93 |  |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-08T13:54 | $10.00 | 0.87 | 0.99 @ 0.7h | 0.87 | top-10 holders own 34% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-08T11:55 | $10.00 | 0.95 | 1.02 @ 17.0h | 0.93 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.01 | 1.05 @ 6.6h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.96 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.91 | 1.07 @ 7.6h | 0.84 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T17:19 | $10.00 | 1.05 | 1.08 @ 50.1h | 0.98 | only 21% of LP burned (liquidity can be pulled) |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T05:47 | $10.00 | 0.99 | 0.99 @ 58.1h | 0.97 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |

### plus5 — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T15:40 | $10.00 | 0.96 | 1.00 @ 1.6h | 0.93 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 1.01 | 1.05 @ 6.6h | 0.99 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.96 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.91 | 1.07 @ 7.6h | 0.84 | top-10 holders own 31% |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-07T14:58 | $10.00 | 0.92 | 1.02 @ 25.6h | 0.91 | top-10 holders own 38% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-07T02:55 | $10.00 | 1.01 | 1.04 @ 64.5h | 0.95 | only 21% of LP burned (liquidity can be pulled) |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-07T02:55 | $10.00 | 0.79 | 1.07 @ 18.9h | 0.79 | top-10 holders own 46% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-07T00:12 | $10.00 | 1.00 | 1.00 @ 63.7h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-11-06T22:54 | $10.00 | 0.78 | 0.98 @ 0.4h | 0.78 | top-10 holders own 46% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-09T18:06 | $10.00 | 0.95 | 0.98 @ 0.1h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-11-09T13:52 | $10.00 | 0.99 | 0.99 @ 1.2h | 0.99 | only 48% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.43% <= 2.0% |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-09T09:52 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | top-10 holders own 40% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-09T03:36 | $10.00 | 1.02 | 1.03 @ 1.1h | 0.98 | top-10 holders own 43% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-09T03:16 | $10.00 | 1.02 | 1.02 @ 17.6h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-09T00:46 | $10.00 | 0.99 | 1.00 @ 16.9h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 0.97 | 0.99 @ 0.2h | 0.95 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.90% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-09T00:00 | $10.00 | 1.03 | 1.06 @ 19.5h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.19% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-09T04:46 | $10.00 | 0.93 | 1.06 @ 11.4h | 0.93 | top-10 holders own 47% | dip_bounce: 16.5% below 24h high 8.66137e-05 XRP, age 16.0d |

## How high do they run? (tracking only — no rule uses this)

514 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 18% |
| ≥ +20% | 30 | 6% |
| ≥ +30% | 19 | 4% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 103 of 514

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8658 |
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4146 |
| [EULER](https://xrpl.to/token/r3uXxU883rgcMbVureoafeCx1VX4WbeQfk-45554C4552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 6 XRP) | 3 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 70110 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 886 XRP) | 443 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19852 |
| [GHOST](https://xrpl.to/token/rB8FVTvTjLie6tC2kFabczgt6QedWY45k5-47484F5354000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 67 XRP) | 34 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 9063 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 224 XRP too low | 62551 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2674 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 188402 |
| [IOV](https://xrpl.to/token/rEQRwzSJQru4tVSywEWN4cKRK9sPfFo6t3-IOV) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,834 XRP) | 917 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6450 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,140 XRP) | 1570 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12586 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 397 XRP too low | 42799 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 910 XRP) | 455 |
| [HAZZY](https://xrpl.to/token/rKLt8jGHt7oM4cv94FvxQpGywYbf1FMoon-48415A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 179 XRP) | 90 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5429 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,356 XRP) | 678 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157811 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,765 XRP) | 1382 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9259 |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 402 XRP too low | 4297 |
| [EUROP](https://xrpl.to/token/rMkEuRii9w9uBMQDnWV5AA43gvYZR9JxVK-4555524F50000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Stablecoin; not a meme (stablecoin/major/KYC issuer); pool too small (xrpl.to TVL 586 XRP) | 293 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 4287 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 268 XRP) | 134 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 198 XRP) | 99 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,183 XRP) | 591 |
| [TEST](https://xrpl.to/token/rU55fFMW8kpTM5k2yWWz1oEnHjHm2CBPsE-5445535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 75 XRP) | 38 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5980 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5940 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 224615 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 82109 |
| [SIMON](https://xrpl.to/token/raF19Hb2JpxixGYbsjXYyfshWoQjKLcY3f-53494D4F4E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 244 XRP) | 122 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending | 11265 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2568 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13560 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 11065 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 48759 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
