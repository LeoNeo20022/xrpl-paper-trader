# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-11T06:04:36+00:00** (UTC) · XRP/USD 1.0608 (bitstamp) · last discovery 2026-11-11T06:04:36+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$68.45** | **-31.55** | $0.85 | 8 / $67.61 | $-18.97 | $-12.39 | 19 / 33 (37%) | 60 (52) | -7.31 | -6.59 | 64.53 | -13.50 | $6.04 (0.27824) | 1.6 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$78.43** | **-21.57** | $8.21 | 8 / $70.22 | $-11.57 | $-9.78 | 21 / 41 (34%) | 70 (62) | -0.14 | -4.67 | 73.94 | -4.10 | $7.23 (0.34846) | 1.6 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$85.68** | **-14.32** | $85.68 | 0 / $0.00 | $-13.69 | $+0.00 | 39 / 151 (21%) | 190 (190) | -8.79 | +0.00 | 80.76 | +2.73 | $21.44 (1.01089) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$76.55** | **-23.45** | $7.00 | 7 / $69.56 | $-22.42 | $-0.44 | 58 / 117 (33%) | 182 (175) | -7.43 | -0.16 | 72.16 | -5.94 | $19.71 (0.94605) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 83.06 | +4.95 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$103.10** | **+3.10** | $63.62 | 4 / $39.48 | $+4.33 | $-0.52 | 70 / 82 (46%) | 156 (152) | +7.80 | -0.18 | 97.19 | +19.09 | $20.69 (1.12298) | 0.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$82.78** | **-17.22** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T17:27 | $10.00 | 1.00 | 1.00 @ 12.5h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T05:48 | $10.00 | 1.02 | 1.02 @ 24.1h | 0.97 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T18:05 | $10.00 | 1.07 | 1.08 @ 45.1h | 0.93 |  |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-08T13:54 | $10.00 | 0.68 | 0.99 @ 0.7h | 0.58 | top-10 holders own 34% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-08T11:55 | $10.00 | 0.91 | 1.02 @ 17.0h | 0.91 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.98 | 1.05 @ 6.6h | 0.92 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.95 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.61 | 1.07 @ 7.6h | 0.51 | top-10 holders own 31% |

### plus5 — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T02:57 | $10.00 | 0.99 | 1.00 @ 11.7h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-10T02:57 | $10.00 | 0.91 | 0.98 @ 1.5h | 0.91 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T00:13 | $10.00 | 0.94 | 1.09 @ 2.5h | 0.92 | top-10 holders own 31% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-09T22:59 | $10.00 | 1.00 | 1.01 @ 2.1h | 0.96 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T15:40 | $10.00 | 1.08 | 1.09 @ 47.5h | 0.93 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.98 | 1.05 @ 6.6h | 0.92 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.95 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.61 | 1.07 @ 7.6h | 0.51 | top-10 holders own 31% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-11T03:44 | $10.00 | 0.99 | 0.99 @ 2.3h | 0.99 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.68% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-11T01:13 | $10.00 | 0.99 | 0.99 @ 2.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T00:52 | $10.00 | 1.00 | 1.00 @ 1.9h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 1.03 | 1.03 @ 3.9h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 1.00 | 1.00 @ 5.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | 2026-11-10T09:55 | $10.00 | 1.00 | 1.01 @ 2.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-10T06:51 | $10.00 | 0.97 | 0.99 @ 0.8h | 0.96 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.33% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | 2026-11-10T19:26 | $10.00 | 0.98 | 0.98 @ 10.6h | 0.97 |  | dip_bounce: 31.4% below 24h high 3.86046e-08 XRP, age 550.8d |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-10T14:16 | $10.00 | 0.98 | 1.03 @ 9.0h | 0.98 | top-10 holders own 34% | dip_bounce: 24.8% below 24h high 1.41183e-05 XRP, age 737.6d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-11-10T13:40 | $10.00 | 1.03 | 1.03 @ 16.4h | 0.99 |  | dip_bounce: 18.1% below 24h high 1.76548e-06 XRP, age 694.6d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-11-10T09:30 | $10.00 | 0.99 | 0.99 @ 0.4h | 0.99 |  | dip_bounce: 19.5% below 24h high 7.61673e-06 XRP, age 752.4d |

## How high do they run? (tracking only — no rule uses this)

559 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 16% |
| ≥ +20% | 30 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 104 of 559

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8513 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3262 |
| [EULER](https://xrpl.to/token/r3uXxU883rgcMbVureoafeCx1VX4WbeQfk-45554C4552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 5 XRP) | 3 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 67078 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 27982 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,727 XRP) | 1363 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2180 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 221 XRP) | 111 |
| [CSC](https://xrpl.to/token/rCSCManTZ8ME9EoLrSHHYKW8PPwWMgkwr-CSC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 19898 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 171 XRP too low | 62280 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2198 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5954 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 240553 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,647 XRP < 2,000 | 1647 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12221 |
| [CAST](https://xrpl.to/token/rGLndPDgEPyaGfgZhyxkQy6Qo22zz3pfDH-4341535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 503 XRP) | 252 |
| [CHROOPS](https://xrpl.to/token/rH4Gxnxpik3Qv5PC5ppB1NZg1jrc2YhqeW-4348524F4F505300000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 556 XRP) | 278 |
| [LHT](https://xrpl.to/token/rHashLabsu2H6hXDSunL8AcVDmTyE17Z35-LHT) | FAIL_SAFETY | top-10 holders own 70% (excl. AMM) | 31121 |
| [CHICKEN](https://xrpl.to/token/rHiyGzWBVv9D6PgQhw3LZBV8Ef91pV4ux4-434849434B454E00000000000000000000000000) | FAIL_SAFETY | pool 1,666 XRP < 2,000 | 1666 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 388 XRP too low | 42535 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 908 XRP) | 454 |
| [HAZZY](https://xrpl.to/token/rKLt8jGHt7oM4cv94FvxQpGywYbf1FMoon-48415A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 167 XRP) | 84 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5338 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,317 XRP) | 659 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158754 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending; 24h volume 383 XRP too low | 2456 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 101 XRP too low | 9011 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 4053 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,885 XRP) | 1442 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 234 XRP) | 117 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 332 XRP) | 166 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 39976 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 105 XRP too low | 13823 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,095 XRP) | 548 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6371 |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 264 XRP too low | 17180 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 224964 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81474 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 78142 |
| [SIMON](https://xrpl.to/token/raF19Hb2JpxixGYbsjXYyfshWoQjKLcY3f-53494D4F4E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 185 XRP) | 92 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
