# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-11T00:52:29+00:00** (UTC) · XRP/USD 1.0509 (bitstamp) · last discovery 2026-11-11T00:52:29+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$68.54** | **-31.46** | $0.85 | 8 / $67.69 | $-18.97 | $-12.31 | 19 / 33 (37%) | 60 (52) | -7.31 | -5.91 | 65.22 | -12.81 | $6.04 (0.27824) | 1.6 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$78.67** | **-21.33** | $8.21 | 8 / $70.46 | $-11.57 | $-9.54 | 21 / 41 (34%) | 70 (62) | -0.14 | -3.82 | 74.86 | -3.17 | $7.23 (0.34846) | 1.6 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$86.45** | **-13.55** | $37.18 | 5 / $49.27 | $-12.19 | $-0.73 | 38 / 142 (21%) | 185 (180) | -7.67 | -0.51 | 82.26 | +4.23 | $20.39 (1.00015) | 1.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$75.20** | **-24.80** | $8.07 | 7 / $67.13 | $-21.35 | $-2.87 | 58 / 115 (34%) | 180 (173) | -7.14 | -1.13 | 71.55 | -6.55 | $19.58 (0.94589) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 83.84 | +5.74 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$101.98** | **+1.98** | $15.89 | 9 / $86.09 | $+6.58 | $-3.91 | 70 / 77 (48%) | 156 (147) | +8.17 | -1.11 | 97.04 | +18.93 | $20.56 (1.10259) | 1.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$82.01** | **-17.99** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T17:27 | $10.00 | 1.00 | 1.00 @ 7.4h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T05:48 | $10.00 | 0.97 | 1.01 @ 7.6h | 0.97 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T18:05 | $10.00 | 1.04 | 1.08 @ 45.1h | 0.93 |  |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-08T13:54 | $10.00 | 0.68 | 0.99 @ 0.7h | 0.58 | top-10 holders own 34% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-08T11:55 | $10.00 | 0.97 | 1.02 @ 17.0h | 0.93 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.95 | 1.05 @ 6.6h | 0.92 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.95 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.74 | 1.07 @ 7.6h | 0.74 | top-10 holders own 31% |

### plus5 — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T02:57 | $10.00 | 0.99 | 1.00 @ 11.7h | 0.98 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-10T02:57 | $10.00 | 0.97 | 0.98 @ 1.5h | 0.95 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T00:13 | $10.00 | 0.95 | 1.09 @ 2.5h | 0.92 | top-10 holders own 31% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-09T22:59 | $10.00 | 0.96 | 1.01 @ 2.1h | 0.96 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-08T15:40 | $10.00 | 1.04 | 1.09 @ 47.5h | 0.93 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.95 | 1.05 @ 6.6h | 0.92 | only 28% of LP burned (liquidity can be pulled) |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-08T11:39 | $10.00 | 0.96 | 1.00 @ 0.9h | 0.95 |  |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-08T11:39 | $10.00 | 0.74 | 1.07 @ 7.6h | 0.74 | top-10 holders own 31% |

### scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-11-11T00:52 | $10.00 | 1.00 | – | – | top-10 holders own 46% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-11T00:06 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-11T00:01 | $10.00 | 1.00 | 1.00 @ 0.3h | 1.00 |  |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | 2026-11-11T00:01 | $10.00 | 0.99 | 0.99 @ 0.8h | 0.99 |  |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T00:01 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 |  |

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T00:52 | $10.00 | 1.00 | – | – | only 12% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T00:16 | $10.00 | 0.99 | 0.99 @ 0.0h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | 2026-11-10T09:55 | $10.00 | 1.00 | 1.01 @ 2.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-10T06:51 | $10.00 | 0.97 | 0.99 @ 0.8h | 0.96 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.33% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T03:41 | $10.00 | 0.97 | 0.99 @ 0.2h | 0.94 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.55% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T01:09 | $10.00 | 0.96 | 1.00 @ 13.6h | 0.96 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | 2026-11-10T19:26 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.97 |  | dip_bounce: 31.4% below 24h high 3.86046e-08 XRP, age 550.8d |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-11-10T14:16 | $10.00 | 0.98 | 1.03 @ 9.0h | 0.98 | top-10 holders own 34% | dip_bounce: 24.8% below 24h high 1.41183e-05 XRP, age 737.6d |
| [PBM](https://xrpl.to/token/rURxaGdf9PpkYeU6ZXe7PuENVuBKk2iAV4-PBM) | 2026-11-10T13:40 | $10.00 | 1.02 | 1.02 @ 8.3h | 0.99 |  | dip_bounce: 18.1% below 24h high 1.76548e-06 XRP, age 694.6d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-11-10T09:30 | $10.00 | 0.99 | 0.99 @ 0.4h | 0.99 |  | dip_bounce: 19.5% below 24h high 7.61673e-06 XRP, age 752.4d |
| [PONGO](https://xrpl.to/token/rwCq6TENSo3Hh9LKipXnLaxaeXBXKubqki-504F4E474F000000000000000000000000000000) | 2026-11-10T05:18 | $10.00 | 1.00 | 1.00 @ 11.4h | 1.00 |  | dip_bounce: 15.8% below 24h high 6.16991e-10 XRP, age 707.2d |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T03:36 | $10.00 | 0.97 | 0.99 @ 0.3h | 0.94 | top-10 holders own 31% | dip_bounce: 23.4% below 24h high 5.97379e-07 XRP, age 109.4d |
| [BOX](https://xrpl.to/token/rhLJ2ma5pScsxVhL5EQr71w3FgASVLwP84-BOX) | 2026-11-10T02:14 | $10.00 | 0.99 | 1.00 @ 0.1h | 0.99 | top-10 holders own 37% | dip_bounce: 23.2% below 24h high 0.00191853 XRP, age 686.1d |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-10T02:09 | $10.00 | 1.00 | 1.00 @ 0.2h | 0.93 |  | dip_bounce: 15.6% below 24h high 0.000111455 XRP, age 754.1d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-10T01:44 | $10.00 | 0.95 | 0.99 @ 0.1h | 0.94 | top-10 holders own 31% | dip_bounce: 25.7% below 24h high 3.20624e-05 XRP, age 756.1d |

## How high do they run? (tracking only — no rule uses this)

551 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 17% |
| ≥ +20% | 30 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.6h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 104 of 551

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 8512 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3076 |
| [BRICKY](https://xrpl.to/token/r3YS7og21UrYRCdhXmU6rzDcMWoDo4f7hm-425249434B590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4007 |
| [EULER](https://xrpl.to/token/r3uXxU883rgcMbVureoafeCx1VX4WbeQfk-45554C4552000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 5 XRP) | 3 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 67166 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,816 XRP) | 1408 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 236 XRP too low | 19963 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,431 XRP) | 1216 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 251 XRP) | 126 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 148 XRP too low | 62383 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6678 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 235511 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,673 XRP < 2,000 | 1673 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12061 |
| [CAST](https://xrpl.to/token/rGLndPDgEPyaGfgZhyxkQy6Qo22zz3pfDH-4341535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 408 XRP) | 204 |
| [GoCa](https://xrpl.to/token/rGzizAp3BepbEzxth8Jr8GSXB8R7P2mnkJ-476F436100000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,402 XRP) | 701 |
| [CHROOPS](https://xrpl.to/token/rH4Gxnxpik3Qv5PC5ppB1NZg1jrc2YhqeW-4348524F4F505300000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 288 XRP) | 144 |
| [CHICKEN](https://xrpl.to/token/rHiyGzWBVv9D6PgQhw3LZBV8Ef91pV4ux4-434849434B454E00000000000000000000000000) | FAIL_SAFETY | pool 1,656 XRP < 2,000 | 1656 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 42314 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 821 XRP) | 411 |
| [HAZZY](https://xrpl.to/token/rKLt8jGHt7oM4cv94FvxQpGywYbf1FMoon-48415A5A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 167 XRP) | 84 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5202 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158668 |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | SKIP_ENTRY | not new and not top trending; 24h volume 378 XRP too low | 2460 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,459 XRP) | 1229 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 8944 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 4057 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 239 XRP) | 120 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 248 XRP) | 124 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 41248 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 108 XRP too low | 13824 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,093 XRP) | 546 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6326 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 224543 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 80558 |
| [SIMON](https://xrpl.to/token/raF19Hb2JpxixGYbsjXYyfshWoQjKLcY3f-53494D4F4E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 184 XRP) | 92 |
| [AiCat](https://xrpl.to/token/raPPs1h8iJYmfWu1vzVuMsEaJXeKpZWYmK-4169436174000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 77 XRP) | 39 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13899 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 45016 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13861 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
