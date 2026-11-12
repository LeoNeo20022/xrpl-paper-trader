# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-12T13:09:56+00:00** (UTC) · XRP/USD 1.0253 (bitstamp) · last discovery 2026-11-12T13:09:56+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$66.36** | **-33.64** | $9.25 | 6 / $57.11 | $-30.57 | $-2.89 | 19 / 39 (33%) | 64 (58) | -13.28 | -0.73 | 64.72 | -13.31 | $6.40 (0.27864) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$76.87** | **-23.13** | $2.11 | 8 / $74.76 | $-17.67 | $-5.24 | 22 / 44 (33%) | 74 (66) | -2.62 | -1.24 | 74.97 | -3.06 | $7.52 (0.34878) | 1.6 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$84.51** | **-15.49** | $84.51 | 0 / $0.00 | $-14.82 | $+0.00 | 39 / 161 (20%) | 200 (200) | -9.67 | +0.00 | 82.43 | +4.39 | $22.53 (1.07243) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$73.75** | **-26.25** | $6.14 | 7 / $67.60 | $-23.24 | $-2.40 | 62 / 122 (34%) | 191 (184) | -7.42 | -0.56 | 71.93 | -6.18 | $20.67 (1.01035) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 85.93 | +7.83 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$100.21** | **+0.21** | $61.51 | 4 / $38.70 | $+2.23 | $-1.30 | 71 / 86 (45%) | 161 (157) | +6.32 | -0.20 | 97.73 | +19.63 | $21.37 (1.14366) | 0.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$80.01** | **-19.99** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005284 XRP/tx = max(0.00002, live open-ledger fee 0.005284), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-11T18:13 | $10.00 | 0.98 | 1.01 @ 10.4h | 0.96 | top-10 holders own 40% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T11:57 | $10.00 | 0.97 | 1.00 @ 4.5h | 0.97 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 25.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.01 | 1.01 @ 21.2h | 1.00 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T17:27 | $10.00 | 0.97 | 1.01 @ 24.9h | 0.96 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-10T05:48 | $10.00 | 1.00 | 1.03 @ 33.9h | 0.97 |  |

### plus5 — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T15:45 | $10.00 | 1.03 | 1.03 @ 12.1h | 0.98 | top-10 holders own 30% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 0.99 | 0.99 @ 25.3h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 1.01 | 1.01 @ 21.2h | 1.00 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.97 | 1.01 @ 11.3h | 0.94 | top-10 holders own 43% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-10T02:57 | $10.00 | 0.96 | 1.00 @ 11.7h | 0.95 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-10T02:57 | $10.00 | 0.89 | 0.98 @ 1.5h | 0.85 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-10T00:13 | $10.00 | 1.03 | 1.09 @ 46.0h | 0.92 | top-10 holders own 31% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-09T22:59 | $10.00 | 0.98 | 1.01 @ 40.7h | 0.96 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-12T09:59 | $10.00 | 0.98 | 0.98 @ 3.0h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 1.84% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-12T07:22 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-12T01:21 | $10.00 | 1.00 | 1.00 @ 2.2h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-12T01:21 | $10.00 | 0.99 | 0.99 @ 3.7h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.40% <= 2.0% |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-12T00:18 | $10.00 | 0.97 | 1.00 @ 4.3h | 0.97 | top-10 holders own 40% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-12T00:18 | $10.00 | 0.97 | 0.98 @ 5.0h | 0.97 | top-10 holders own 43% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T16:28 | $10.00 | 1.04 | 1.04 @ 11.3h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.69% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-12T01:51 | $10.00 | 1.00 | 1.00 @ 11.1h | 0.99 | top-10 holders own 31% | dip_bounce: 18.0% below 24h high 2.28449e-05 XRP, age 758.1d |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-12T01:31 | $10.00 | 0.96 | 0.98 @ 0.2h | 0.93 | only 37% of LP burned (liquidity can be pulled) | dip_bounce: 16.0% below 24h high 0.0044 XRP, age 629.4d |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-11T20:02 | $10.00 | 0.99 | 1.02 @ 8.6h | 0.98 | top-10 holders own 40% | dip_bounce: 15.1% below 24h high 0.00039634 XRP, age 520.3d |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T14:06 | $10.00 | 1.02 | 1.03 @ 13.7h | 0.97 | top-10 holders own 30% | dip_bounce: 16.6% below 24h high 0.000252203 XRP, age 742.6d |

## How high do they run? (tracking only — no rule uses this)

588 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 91 | 15% |
| ≥ +20% | 30 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.0h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 107 of 588

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9844 |
| [AmericaFirst](https://xrpl.to/token/r4GD2HMVKJWhfzvgHcUL6frneuUACAzqwo-416D657269636146697273740000000000000000) | SKIP_ENTRY | not new and not top trending | 7121 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 65433 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 27668 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29996 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,880 XRP) | 1440 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 312 XRP) | 156 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62389 |
| [OIL](https://xrpl.to/token/rD9Z2mjnDNaGa4PFhQaEJxvpnLP8MAZzSa-OIL) | FAIL_SAFETY | pool too small (xrpl.to TVL 384 XRP) | 192 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | 24h volume 320 XRP too low | 18718 |
| [Chubs](https://xrpl.to/token/rDaU7GkANXeZpC9evgjE6nAc8qi6wttGEX-4368756273000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,641 XRP) | 821 |
| [1CELL](https://xrpl.to/token/rGCtayZogyWdKj8GAUgGSURd2ThfcyBQhP-3143454C4C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,499 XRP) | 1249 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 238294 |
| [Chubbs](https://xrpl.to/token/rGHjYv2YiRbY3Zr8L6b1R6WvGw5N5B7c8o-4368756262730000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 328 XRP) | 164 |
| [CAST](https://xrpl.to/token/rGLndPDgEPyaGfgZhyxkQy6Qo22zz3pfDH-4341535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 431 XRP) | 216 |
| [Charity](https://xrpl.to/token/rGfX5v4zHeu6SpepPzoHwwFPWUbKVGLCBS-4368617269747900000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,695 XRP) | 847 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,767 XRP < 2,000 | 1767 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 339 XRP) | 170 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43463 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 160859 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,360 XRP) | 1180 |
| [Rope](https://xrpl.to/token/rM35EybdZXP1hW5fRMjRhE3ubhgwCkHy1N-526F706500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 136 XRP) | 68 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 53% (excl. AMM) | 3575 |
| [XRPATH](https://xrpl.to/token/rPJkdEVCQimfyWmAy6KSpw1vXRYM4HGxTY-5852504154480000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,599 XRP) | 1300 |
| [XRPLIL](https://xrpl.to/token/rPLMPHiThKUsx5sXKMFfq2Nw4moba2VTew-5852504C494C0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 306 XRP) | 153 |
| [RUDE](https://xrpl.to/token/rPqAK1XJpz52goduf7rudnBvg9NJLtgYF-5255444500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 220 XRP) | 110 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5616 |
| [HIYO](https://xrpl.to/token/rU5wZyCbZ2WhT51SLDV12vUHtcsqJn9631-4849594F00000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5487 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 224625 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 308255 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 82005 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 77013 |
| [gei](https://xrpl.to/token/raadqNCqPHhqpb5HEMBjbfFa21YYu9GWfW-gei) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 2599 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 13863 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 50038 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 45182 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26207 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 94150 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 85548 |
| [FATZY](https://xrpl.to/token/rhXjaKtS96Z4EqYv2zjUYfHt3JWQteMQdf-4641545A59000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 127 XRP) | 63 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
