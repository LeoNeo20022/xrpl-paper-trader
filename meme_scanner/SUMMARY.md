# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-11T14:21:44+00:00** (UTC) · XRP/USD 1.0556 (bitstamp) · last discovery 2026-11-11T14:21:44+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$68.88** | **-31.12** | $9.26 | 6 / $59.62 | $-30.56 | $-0.38 | 19 / 38 (33%) | 63 (57) | -14.00 | +0.78 | 65.25 | -12.78 | $6.27 (0.27856) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$79.35** | **-20.65** | $2.02 | 8 / $77.33 | $-17.76 | $-2.67 | 21 / 44 (32%) | 73 (65) | -3.39 | -0.21 | 75.17 | -2.86 | $7.46 (0.34870) | 1.6 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$85.68** | **-14.32** | $85.68 | 0 / $0.00 | $-13.69 | $+0.00 | 39 / 151 (21%) | 190 (190) | -8.79 | +0.00 | 81.16 | +3.13 | $21.44 (1.01089) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$76.91** | **-23.09** | $6.02 | 7 / $70.88 | $-23.38 | $+0.88 | 58 / 119 (33%) | 184 (177) | -7.70 | +0.77 | 72.85 | -5.25 | $19.91 (0.97512) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 83.47 | +5.36 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$103.05** | **+3.05** | $73.33 | 3 / $29.72 | $+4.04 | $-0.28 | 71 / 84 (46%) | 158 (155) | +7.90 | -0.16 | 97.62 | +19.52 | $20.93 (1.12318) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$82.37** | **-17.63** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T11:57 | $10.00 | 1.00 | 1.00 @ 2.4h | 0.99 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 2.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 2.7h | 1.00 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T17:27 | $10.00 | 1.00 | 1.00 @ 20.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T05:48 | $10.00 | 1.02 | 1.02 @ 30.9h | 0.97 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T18:05 | $10.00 | 1.08 | 1.08 @ 45.1h | 0.93 |  |

### plus5 — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 2.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 2.7h | 1.00 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.98 | 1.00 @ 2.2h | 0.98 | top-10 holders own 43% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T02:57 | $10.00 | 0.99 | 1.00 @ 11.7h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-10T02:57 | $10.00 | 0.92 | 0.98 @ 1.5h | 0.91 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T00:13 | $10.00 | 1.01 | 1.09 @ 2.5h | 0.92 | top-10 holders own 31% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-09T22:59 | $10.00 | 1.00 | 1.01 @ 2.1h | 0.96 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T15:40 | $10.00 | 1.09 | 1.09 @ 47.5h | 0.93 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-11T09:58 | $10.00 | 1.02 | 1.02 @ 4.4h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.07% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-11T06:55 | $10.00 | 1.02 | 1.02 @ 7.1h | 0.99 | only 29% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-11T03:44 | $10.00 | 0.99 | 0.99 @ 10.2h | 0.99 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.68% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-11T01:13 | $10.00 | 1.00 | 1.00 @ 10.9h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T00:52 | $10.00 | 1.01 | 1.01 @ 13.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 1.04 | 1.04 @ 14.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 1.01 | 1.01 @ 14.1h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T14:06 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 30% | dip_bounce: 16.6% below 24h high 0.000252203 XRP, age 742.6d |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-11T12:35 | $10.00 | 0.99 | 0.99 @ 1.4h | 0.99 | top-10 holders own 47% | dip_bounce: 16.7% below 24h high 8.29751e-05 XRP, age 18.4d |
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | 2026-11-10T19:26 | $10.00 | 1.00 | 1.00 @ 18.9h | 0.97 |  | dip_bounce: 31.4% below 24h high 3.86046e-08 XRP, age 550.8d |

## How high do they run? (tracking only — no rule uses this)

567 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 16% |
| ≥ +20% | 30 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 104 of 567

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8410 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3261 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 65073 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 28085 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 922 XRP) | 461 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2188 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 240 XRP) | 120 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 137 XRP too low | 62280 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 200383 |
| [QKITTY](https://xrpl.to/token/rDH4j77czJ2tcehLGukV76HKzPqw9PHJhA-514B495454590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 59 XRP) | 29 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18506 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6107 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 240483 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,613 XRP < 2,000 | 1613 |
| [CAST](https://xrpl.to/token/rGLndPDgEPyaGfgZhyxkQy6Qo22zz3pfDH-4341535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 483 XRP) | 242 |
| [4761](https://xrpl.to/token/rGSvs6kDEmxsuH5upTcmqGzKZZ7Sisg19Y-3437363100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 65 XRP) | 33 |
| [CHROOPS](https://xrpl.to/token/rH4Gxnxpik3Qv5PC5ppB1NZg1jrc2YhqeW-4348524F4F505300000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 184 XRP) | 92 |
| [LIFE](https://xrpl.to/token/rHJyHHptZoej8JNjrcSFPfku78zR7ct8nq-4C49464500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 58 XRP) | 29 |
| [Vetcoin](https://xrpl.to/token/rHrtvZj2LYFJDDNNccwQxVrR1xCgFFCN1v-566574636F696E00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 64 XRP) | 32 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 947 XRP) | 473 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,296 XRP) | 648 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 161001 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 3691 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 238 XRP) | 119 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 553 XRP) | 276 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 40669 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,099 XRP) | 549 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6036 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 82917 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 78179 |
| [SIMON](https://xrpl.to/token/raF19Hb2JpxixGYbsjXYyfshWoQjKLcY3f-53494D4F4E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 177 XRP) | 89 |
| [AiCat](https://xrpl.to/token/raPPs1h8iJYmfWu1vzVuMsEaJXeKpZWYmK-4169436174000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 70 XRP) | 35 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13695 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 45038 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26310 |
| [mXRP](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-6D58525000000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 61105 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 85904 |
| [FATZY](https://xrpl.to/token/rhXjaKtS96Z4EqYv2zjUYfHt3JWQteMQdf-4641545A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 133 XRP) | 67 |
| [DONNIE](https://xrpl.to/token/rhhaVvZF69sQBgiDuM2avL2pbrryT5cGTF-444F4E4E49450000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19288 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 6377 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
