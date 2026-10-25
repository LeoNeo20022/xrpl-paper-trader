# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-25T12:51:31+00:00** (UTC) · XRP/USD 1.2954 (bitstamp) · last discovery 2026-10-25T12:51:31+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$105.95** | **+5.95** | $0.00 | 10 / $105.95 | $+0.00 | $+5.95 | – | 10 (0) | +0.00 | +3.76 | 81.79 | +3.76 | $0.27 (0.00012) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$105.95** | **+5.95** | $0.00 | 10 / $105.95 | $+0.00 | $+5.95 | – | 10 (0) | +0.00 | +3.76 | 81.79 | +3.76 | $0.27 (0.00012) | 2.0 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$98.42** | **-1.58** | $98.42 | 0 / $0.00 | $-1.57 | $+0.00 | 6 / 14 (30%) | 20 (20) | -1.56 | +0.00 | 75.98 | -2.05 | $1.61 (0.01129) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$100.69** | **+0.69** | $90.75 | 1 / $9.94 | $+0.80 | $-0.06 | 8 / 11 (42%) | 20 (19) | +0.36 | -0.05 | 77.73 | -0.37 | $1.70 (0.08129) | 0.2 |
| breakout | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$96.50** | **-3.50** | $55.72 | 4 / $40.78 | $-4.26 | $+0.78 | 1 / 4 (20%) | 9 (5) | -3.34 | +0.44 | 74.49 | -3.61 | $0.67 (0.03169) | 0.8 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$105.02** | **+5.02** | $2.18 | 10 / $102.84 | $+2.19 | $+2.84 | 2 / 0 (100%) | 12 (2) | +1.57 | +1.48 | 81.07 | +2.97 | $0.70 (0.01388) | 2.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$101.08** | **+1.08** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings |
|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.17 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.09 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.08 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.03 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.02 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.10 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.05 |  |

### plus5 — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings |
|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.17 | top-10 holders own 31% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-24T11:16 | $10.00 | 1.00 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-24T11:16 | $10.00 | 1.09 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.08 | only 23% of LP burned (liquidity can be pulled) |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.03 | top-10 holders own 42% |
| [$FLIPPY](https://xrpl.to/token/rsENFmELvj92orrCKTkDTug53MzwsB7zBd-24464C4950505900000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | top-10 holders own 37% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.02 |  |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.10 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 50% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-24T11:16 | $10.00 | 1.05 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-10-25T09:11 | $10.00 | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |

### breakout — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | 2026-10-25T06:51 | $10.00 | 0.98 | top-10 holders own 36% | breakout: +14.2% in 1h, vol last hour 742 vs prior 5 / 24h avg 37 XRP |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-24T23:25 | $10.00 | 1.00 | top-10 holders own 44% | breakout: +10.6% in 1h, vol last hour 1664 vs prior 292 / 24h avg 490 XRP |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-10-24T19:56 | $10.00 | 1.09 |  | breakout: +10.8% in 1h, vol last hour 1186 vs prior 2 / 24h avg 140 XRP |
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | 2026-10-24T18:54 | $10.00 | 0.99 |  | breakout: +13.7% in 1h, vol last hour 1274 vs prior 336 / 24h avg 172 XRP |

### dip_bounce — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Warnings | Why bought |
|---|---|---|---|---|---|
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-25T00:01 | $10.00 | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 27.6% below 24h high 0.000238291 XRP, age 669.0d |
| [W&B](https://xrpl.to/token/raCwgDN3QmiBrDQCdsYSnZECh1qtbTqp8N-W&B) | 2026-10-25T00:01 | $10.00 | 1.00 |  | dip_bounce: 26.1% below 24h high 1.16775e-05 XRP, age 728.0d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 0.91 |  | dip_bounce: 32.3% below 24h high 5.5575e-06 XRP, age 735.6d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.03 | top-10 holders own 42% | dip_bounce: 27.2% below 24h high 0.000211242 XRP, age 716.6d |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | 2026-10-24T13:37 | $10.00 | 1.10 | only 48% of LP burned (liquidity can be pulled) | dip_bounce: 22.5% below 24h high 0.0133504 XRP, age 725.6d |
| [NOX](https://xrpl.to/token/rBbu9c7zyuiDH4bq7uJhdLhzsRdEkSrYFX-NOX) | 2026-10-24T13:37 | $10.00 | 1.07 |  | dip_bounce: 21.8% below 24h high 0.0341682 XRP, age 691.6d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.02 | top-10 holders own 31% | dip_bounce: 19.5% below 24h high 2.83763e-05 XRP, age 739.6d |
| [RIPPLE](https://xrpl.to/token/rMgrYs2XYgbGaLZ19HbUXfi9rpsaFQYwgc-524950504C450000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.03 |  | dip_bounce: 18.7% below 24h high 0.000211392 XRP, age 733.6d |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-24T13:37 | $10.00 | 1.03 |  | dip_bounce: 17.2% below 24h high 5.8921e-07 XRP, age 502.2d |
| [BOX](https://xrpl.to/token/rhLJ2ma5pScsxVhL5EQr71w3FgASVLwP84-BOX) | 2026-10-24T13:37 | $10.00 | 1.02 | top-10 holders own 35% | dip_bounce: 16.2% below 24h high 0.00153201 XRP, age 669.6d |

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9722 |
| [BTC](https://xrpl.to/token/r39mx8HT42TVUsF25AffcaLdMPehdactJf-BTC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 1631 |
| [XCORE](https://xrpl.to/token/r3dVizzUAS3U29WKaaSALqkieytA2LCoRe-58434F5245000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,885 XRP) | 1442 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 27142 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,201 XRP) | 600 |
| [TRIPPR](https://xrpl.to/token/r9QYoVFNFZV1rZtFZEypPPpka2iEVDgqY1-5452495050520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,715 XRP) | 857 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18482 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 8497 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 3392 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 11474 |
| [AFFBAL](https://xrpl.to/token/rGu3gexApNkWR3ST7LW1mc1rZACXcxwcfi-41464642414C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,775 XRP) | 887 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,269 XRP) | 634 |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7566 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6918 |
| [321BG](https://xrpl.to/token/rJeCmBFjiz1TBD32wSeLEGKXofYxekiwjZ-3332314247000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 312 XRP) | 156 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 154963 |
| [BUZZY](https://xrpl.to/token/rLFDsYQcd7uerRnmYy3sRVTZ6P2uTjfrak-42555A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 220 XRP) | 110 |
| [KOTL](https://xrpl.to/token/rLFucYbEhZ7sLae1QMmvBCAs14eDttZWWS-4B4F544C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,097 XRP) | 1049 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,276 XRP) | 1138 |
| [ROCK](https://xrpl.to/token/rM2LZ53PobDBpEWZJp9cCAZhViRyy1TbyL-524F434B00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 336 XRP too low | 3869 |
| [ZELLE](https://xrpl.to/token/rM8Qdyff1EPUvrPb71ZXMMRsHzAkbyS2zH-5A454C4C45000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 883 XRP) | 442 |
| [XDNA](https://xrpl.to/token/rMKUCQ5G3YJHVJ7pEDncew2WCJpJUGuWC6-58444E4100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 434 XRP) | 217 |
| [WBLV](https://xrpl.to/token/rMhk9GPrsoWWAgWB4ai9QrELm8G1rMDySM-57424C5600000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,099 XRP) | 1550 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 4451 |
| [LUTHER](https://xrpl.to/token/rPBWcjbyqcrGxpUe4awobqMmB2WaeUhuFb-4C55544845520000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4453 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,175 XRP) | 587 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | FAIL_SAFETY | pool 1,966 XRP < 2,000 | 1966 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7072 |
| [BTCL](https://xrpl.to/token/rUgeZXZvcXX9UstkspHr1gHJKj89PqogtU-4254434C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,688 XRP < 2,000 | 1688 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 233790 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 82007 |
| [W&B](https://xrpl.to/token/raCwgDN3QmiBrDQCdsYSnZECh1qtbTqp8N-W&B) | SKIP_ENTRY | not new and not top trending | 4025 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18713 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 46558 |
| [TEMPLAR](https://xrpl.to/token/rfGrJ5R5GB1SR48LRBJrD5vkvhXVgUxX4G-54454D504C415200000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 391 XRP) | 196 |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10592 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 90793 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 83016 |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 773614 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7212 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
