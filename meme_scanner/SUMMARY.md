# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-01T06:05:20+00:00** (UTC) · XRP/USD 1.2534 (bitstamp) · last discovery 2026-11-01T06:05:20+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$100.15** | **+0.15** | $0.71 | 10 / $99.45 | $+0.82 | $-0.55 | 11 / 10 (52%) | 31 (21) | +3.21 | -0.99 | 79.91 | +1.88 | $3.07 (0.18480) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$116.79** | **+16.79** | $5.23 | 11 / $111.56 | $+15.37 | $+1.56 | 13 / 15 (46%) | 39 (28) | +14.43 | +0.70 | 93.18 | +15.15 | $4.35 (0.22538) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$94.17** | **-5.83** | $94.17 | 0 / $0.00 | $-5.58 | $+0.00 | 23 / 67 (26%) | 90 (90) | -3.34 | +0.00 | 75.13 | -2.90 | $9.97 (0.39673) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$95.25** | **-4.75** | $5.46 | 9 / $89.80 | $-4.30 | $-0.20 | 32 / 48 (40%) | 89 (80) | -2.67 | -0.40 | 76.00 | -2.11 | $9.35 (0.38393) | 1.8 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.30 | -7.81 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$115.66** | **+15.66** | $105.92 | 1 / $9.74 | $+16.26 | $-0.26 | 38 / 35 (52%) | 74 (73) | +12.51 | -0.21 | 92.28 | +14.17 | $9.35 (0.53052) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.80** | **-2.20** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T17:54 | $10.00 | 0.91 | 0.99 @ 0.1h | 0.83 | top-10 holders own 30% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-10-30T15:45 | $10.00 | 0.81 | 0.99 @ 0.4h | 0.69 | top-10 holders own 34% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 1.00 | 1.01 @ 33.0h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 38.3h | 0.98 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.12 @ 32.8h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.96 | 1.00 @ 7.0h | 0.96 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.08 | 1.12 @ 20.5h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 35.9h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.10 @ 17.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T02:39 | $10.00 | 0.99 | 1.00 @ 0.5h | 0.99 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T02:39 | $10.00 | 1.18 | 1.25 @ 0.5h | 0.99 | top-10 holders own 49% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T22:51 | $10.00 | 0.97 | 0.98 @ 0.2h | 0.96 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 1.00 | 1.01 @ 33.0h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.00 @ 4.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.99 | 1.00 @ 38.3h | 0.98 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.12 @ 32.8h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.96 | 1.00 @ 7.0h | 0.96 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.08 | 1.12 @ 20.5h | 1.00 |  |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.78 | 0.99 @ 6.2h | 0.76 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.10 @ 17.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (9)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T04:10 | $10.00 | 0.98 | 0.98 @ 0.3h | 0.98 | only 34% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-01T00:17 | $10.00 | 0.99 | 0.99 @ 0.4h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-01T00:07 | $10.00 | 0.99 | 0.99 @ 1.9h | 0.98 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-01T00:07 | $10.00 | 0.98 | 1.00 @ 2.9h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | 2026-11-01T00:07 | $10.00 | 1.04 | 1.04 @ 2.5h | 0.99 | top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 0.33% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 0.99 | 0.99 @ 1.4h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.75% <= 2.0% |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 1.01 | 1.02 @ 1.4h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 1.00 | 1.00 @ 6.0h | 0.99 | top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 0.14% <= 2.0% |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 0.98 | 0.99 @ 0.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.57% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | 2026-10-31T22:25 | $10.00 | 0.97 | 0.98 @ 3.0h | 0.97 | top-10 holders own 47% | dip_bounce: 24.7% below 24h high 6.27e-06 XRP, age 59.0d |

## How high do they run? (tracking only — no rule uses this)

262 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 60 | 23% |
| ≥ +20% | 21 | 8% |
| ≥ +30% | 13 | 5% |
| ≥ +50% | 8 | 3% |
| ≥ +100% | 1 | 0% |

Median peak **x1.01** · median hours to peak **3.1h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 58 of 262

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 8727 |
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9322 |
| [SOCKS](https://xrpl.to/token/r3D3XjfF9xSoSsRKHMrZ6RTV6SJvucMoon-534F434B53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 335 XRP) | 167 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 334 XRP too low | 6309 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4744 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 389 XRP) | 194 |
| [CODIUS](https://xrpl.to/token/r4zXT1VJ97qmCEDkDBhbRgLDB53cyxkTm3-434F444955530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 889 XRP) | 444 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32439 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool 1,646 XRP < 2,000 | 1646 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,775 XRP) | 1388 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool 1,864 XRP < 2,000 | 1864 |
| [UGA](https://xrpl.to/token/rBFJGmWj6YaabVCxfsjiCM8pfYXs8xFdeC-UGA) | SKIP_ENTRY | not new and not top trending | 7912 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 360 XRP too low | 62394 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,954 XRP) | 1477 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 262 XRP) | 131 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4793 |
| [OURO](https://xrpl.to/token/rHwkshB9XXd5Do3V3uqZeJv91mazdVTbEX-4F55524F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 716 XRP) | 358 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 339 XRP) | 169 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 78% (excl. AMM) | 11299 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 41446 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158289 |
| [$BURST](https://xrpl.to/token/rLeGXSzGpGDxBnEPzCbYiUofRTcnHMnGif-2442555253540000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 89% (excl. AMM) | 2536 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 220 XRP) | 110 |
| [CAPYS](https://xrpl.to/token/rMCnAekjKq3ikbvgUGcGi1J5dDdt2yCkzi-4341505953000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 974 XRP) | 487 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 5882 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 6553 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 82038 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 79173 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18935 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 62% (excl. AMM) | 46160 |
| [REN](https://xrpl.to/token/rfJaHW5KanrqDbpC8emVV9bUcemFk1EHVe-REN) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,789 XRP) | 895 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 14661 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 25333 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 81855 |
| [SPC](https://xrpl.to/token/rhnvCzgjfeK6Qabq7iTYcJc2h23483nriX-SPC) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7190 |
| [WARP](https://xrpl.to/token/rhuQ5tKUHG77J5ovRN4GVSwZJT5SDTZZCD-5741525000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,304 XRP) | 1152 |
| [LIFTY](https://xrpl.to/token/rnEacpNjFMwDVLvjQaBi7qyaj3VqkjbpuP-4C49465459000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 235 XRP) | 117 |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10352 |
| [SPY](https://xrpl.to/token/rnmJEi7hzEL34R7x48e732qvSnmF5wsLtQ-SPY) | FAIL_SAFETY | top-10 holders own 79% (excl. AMM) | 9750 |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2636 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
