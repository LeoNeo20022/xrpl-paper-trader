# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-12T00:33:08+00:00** (UTC) · XRP/USD 1.0525 (bitstamp) · last discovery 2026-11-12T00:33:08+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$68.13** | **-31.87** | $9.25 | 6 / $58.88 | $-30.57 | $-1.12 | 19 / 39 (33%) | 64 (58) | -13.28 | -0.48 | 64.73 | -13.30 | $6.40 (0.27864) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$78.66** | **-21.34** | $2.11 | 8 / $76.55 | $-17.67 | $-3.45 | 22 / 44 (33%) | 74 (66) | -2.62 | -1.42 | 74.74 | -3.30 | $7.53 (0.34878) | 1.6 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$85.12** | **-14.88** | $15.64 | 7 / $69.48 | $-13.69 | $-0.52 | 39 / 151 (21%) | 197 (190) | -8.79 | -0.49 | 80.88 | +2.84 | $21.85 (1.07191) | 1.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$76.00** | **-24.00** | $5.35 | 7 / $70.65 | $-24.05 | $+0.65 | 59 / 121 (33%) | 187 (180) | -8.40 | +0.84 | 72.21 | -5.89 | $20.27 (0.97536) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 83.71 | +5.61 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$103.57** | **+3.57** | $73.25 | 3 / $30.33 | $+3.96 | $+0.33 | 71 / 85 (46%) | 159 (156) | +7.89 | +0.44 | 98.41 | +20.30 | $21.17 (1.13350) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$82.13** | **-17.87** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-11T18:13 | $10.00 | 1.01 | 1.01 @ 6.3h | 0.96 | top-10 holders own 40% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T11:57 | $10.00 | 0.98 | 1.00 @ 4.5h | 0.97 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 3.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 12.8h | 1.00 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T17:27 | $10.00 | 0.97 | 1.01 @ 24.9h | 0.96 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T05:48 | $10.00 | 1.00 | 1.03 @ 33.9h | 0.97 |  |

### plus5 — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T15:45 | $10.00 | 1.00 | 1.00 @ 6.4h | 0.98 | top-10 holders own 30% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 3.5h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 12.8h | 1.00 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.97 | 1.01 @ 11.3h | 0.94 | top-10 holders own 43% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T02:57 | $10.00 | 0.95 | 1.00 @ 11.7h | 0.95 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-10T02:57 | $10.00 | 0.88 | 0.98 @ 1.5h | 0.85 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T00:13 | $10.00 | 1.06 | 1.09 @ 46.0h | 0.92 | top-10 holders own 31% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-09T22:59 | $10.00 | 0.99 | 1.01 @ 40.7h | 0.96 |  |

### scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-12T00:23 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 1.00 | 1.00 @ 0.5h | 0.98 | top-10 holders own 40% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 1.00 | 1.00 @ 0.5h | 1.00 |  |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 30% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 29% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | top-10 holders own 31% |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-11-12T00:03 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-12T00:18 | $10.00 | 1.00 | 1.00 @ 0.2h | 0.98 | top-10 holders own 40% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-12T00:18 | $10.00 | 0.98 | 0.98 @ 0.2h | 0.98 | top-10 holders own 43% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T16:28 | $10.00 | 1.01 | 1.02 @ 5.8h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-11T09:58 | $10.00 | 1.06 | 1.06 @ 14.6h | 0.99 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.07% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-11T06:55 | $10.00 | 1.03 | 1.04 @ 7.9h | 0.99 | only 29% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-11T01:13 | $10.00 | 1.00 | 1.01 @ 19.3h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T00:52 | $10.00 | 1.01 | 1.01 @ 14.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-11T20:02 | $10.00 | 1.02 | 1.02 @ 4.5h | 0.98 | top-10 holders own 40% | dip_bounce: 15.1% below 24h high 0.00039634 XRP, age 520.3d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T14:06 | $10.00 | 0.99 | 1.01 @ 0.6h | 0.97 | top-10 holders own 30% | dip_bounce: 16.6% below 24h high 0.000252203 XRP, age 742.6d |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-11T12:35 | $10.00 | 1.03 | 1.03 @ 9.3h | 0.98 | top-10 holders own 47% | dip_bounce: 16.7% below 24h high 8.29751e-05 XRP, age 18.4d |

## How high do they run? (tracking only — no rule uses this)

580 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 16% |
| ≥ +20% | 30 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 106 of 580

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9884 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3274 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 65396 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 27551 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30015 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 2206 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 277 XRP) | 139 |
| [OIL](https://xrpl.to/token/rD9Z2mjnDNaGa4PFhQaEJxvpnLP8MAZzSa-OIL) | FAIL_SAFETY | pool too small (xrpl.to TVL 393 XRP) | 197 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2086 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 201948 |
| [QKITTY](https://xrpl.to/token/rDH4j77czJ2tcehLGukV76HKzPqw9PHJhA-514B495454590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 59 XRP) | 30 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18738 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6167 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,671 XRP < 2,000 | 1671 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12259 |
| [CAST](https://xrpl.to/token/rGLndPDgEPyaGfgZhyxkQy6Qo22zz3pfDH-4341535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 397 XRP) | 199 |
| [4761](https://xrpl.to/token/rGSvs6kDEmxsuH5upTcmqGzKZZ7Sisg19Y-3437363100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 65 XRP) | 33 |
| [CHROOPS](https://xrpl.to/token/rH4Gxnxpik3Qv5PC5ppB1NZg1jrc2YhqeW-4348524F4F505300000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 134 XRP) | 67 |
| [LIFE](https://xrpl.to/token/rHJyHHptZoej8JNjrcSFPfku78zR7ct8nq-4C49464500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 58 XRP) | 29 |
| [Vetcoin](https://xrpl.to/token/rHrtvZj2LYFJDDNNccwQxVrR1xCgFFCN1v-566574636F696E00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 64 XRP) | 32 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43103 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 935 XRP) | 468 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,244 XRP) | 622 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 160985 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,597 XRP) | 1298 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 3693 |
| [XRPATH](https://xrpl.to/token/rPJkdEVCQimfyWmAy6KSpw1vXRYM4HGxTY-5852504154480000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,701 XRP) | 1351 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 446 XRP) | 223 |
| [RUDE](https://xrpl.to/token/rPqAK1XJpz52goduf7rudnBvg9NJLtgYF-5255444500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 220 XRP) | 110 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 308246 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81542 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 76697 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending | 11256 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2599 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 50038 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26123 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 94149 |
| [mXRP](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-6D58525000000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 61105 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 85511 |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 559667 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
