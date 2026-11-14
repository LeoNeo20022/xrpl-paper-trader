# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-14T02:25:14+00:00** (UTC) · XRP/USD 0.9924 (bitstamp) · last discovery 2026-11-14T02:25:14+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$63.99** | **-36.01** | $7.88 | 6 / $56.11 | $-31.95 | $-3.89 | 19 / 41 (32%) | 66 (60) | -13.62 | -0.90 | 64.47 | -13.56 | $6.47 (0.27880) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$74.42** | **-25.58** | $8.92 | 7 / $65.51 | $-20.86 | $-4.49 | 22 / 48 (31%) | 77 (70) | -3.30 | -0.79 | 74.99 | -3.04 | $7.82 (0.34906) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$81.29** | **-18.71** | $61.85 | 2 / $19.44 | $-17.48 | $-0.56 | 40 / 178 (18%) | 220 (218) | -10.95 | -0.29 | 81.91 | +3.88 | $24.98 (1.08399) | 0.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$70.20** | **-29.80** | $2.84 | 7 / $67.36 | $-26.53 | $-2.64 | 63 / 134 (32%) | 204 (197) | -7.99 | -1.21 | 70.74 | -7.36 | $22.39 (1.03139) | 1.4 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 88.78 | +10.68 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$95.40** | **-4.60** | $76.77 | 2 / $18.63 | $-2.49 | $-1.37 | 73 / 93 (44%) | 168 (166) | +2.99 | -1.08 | 96.13 | +18.02 | $22.52 (1.18736) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$77.44** | **-22.56** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005024 XRP/tx = max(0.00002, live open-ledger fee 0.005024), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-13T17:29 | $10.00 | 0.97 | 0.99 @ 3.1h | 0.95 | top-10 holders own 31% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-13T05:52 | $10.00 | 1.00 | 1.02 @ 7.3h | 0.99 | only 29% of LP burned (liquidity can be pulled) |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-11T18:13 | $10.00 | 0.98 | 1.01 @ 10.4h | 0.96 | top-10 holders own 40% |
| [BERT](https://xrpl.to/token/rpwAnF1mMZRszxdinETFHwzGQiPgsv3jHR-4245525400000000000000000000000000000000) | 2026-11-11T11:57 | $10.00 | 0.97 | 1.00 @ 4.5h | 0.97 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 60.2h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.99 | 1.01 @ 21.2h | 0.96 |  |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-13T02:59 | $10.00 | 0.97 | 0.99 @ 6.3h | 0.97 | only 36% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-13T00:18 | $10.00 | 1.00 | 1.01 @ 15.6h | 0.99 | only 22% of LP burned (liquidity can be pulled) |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-12T23:00 | $10.00 | 1.00 | 1.02 @ 14.2h | 0.99 | only 29% of LP burned (liquidity can be pulled) |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-11-11T15:45 | $10.00 | 1.02 | 1.03 @ 12.1h | 0.98 | top-10 holders own 30% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-11T11:42 | $10.00 | 1.00 | 1.00 @ 60.2h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.99 | 1.01 @ 21.2h | 0.96 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-11T11:42 | $10.00 | 0.93 | 1.01 @ 11.3h | 0.93 | top-10 holders own 43% |

### scalp — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-14T02:05 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | top-10 holders own 45% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-14T01:50 | $10.00 | 0.98 | 0.99 @ 0.4h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |

### slow_scalp — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-14T01:50 | $10.00 | 0.98 | 0.99 @ 0.4h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.40% <= 2.0% |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | 2026-11-14T01:50 | $10.00 | 0.98 | 0.98 @ 0.4h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 32% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SPLASH](https://xrpl.to/token/rwfGtVZKpPX6vb51xE5RGTgXkQ4W9wSUrz-53504C4153480000000000000000000000000000) | 2026-11-14T00:47 | $10.00 | 0.97 | 0.98 @ 0.1h | 0.97 | top-10 holders own 48% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-14T00:18 | $10.00 | 0.98 | 0.99 @ 0.1h | 0.98 | only 22% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.02% <= 2.0% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-13T16:39 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-13T10:03 | $10.00 | 0.98 | 1.00 @ 2.8h | 0.97 | only 29% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-13T05:47 | $10.00 | 1.00 | 1.00 @ 17.4h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.01% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-14T01:55 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 31% | dip_bounce: 22.6% below 24h high 2.40722e-05 XRP, age 760.1d |
| [Jokka](https://xrpl.to/token/rKMwfvWZekbcQMFWVbRm3GidhC2tbJVmv2-4A6F6B6B61000000000000000000000000000000) | 2026-11-13T15:39 | $10.00 | 0.90 | 0.99 @ 0.2h | 0.90 | top-10 holders own 37% | dip_bounce: 33.5% below 24h high 0.000163484 XRP, age 489.9d |

## How high do they run? (tracking only — no rule uses this)

632 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 94 | 15% |
| ≥ +20% | 31 | 5% |
| ≥ +30% | 19 | 3% |
| ≥ +50% | 10 | 2% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.7h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 111 of 632

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 57% (excl. AMM) | 3318 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 370 XRP too low | 4442 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63731 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 412 XRP too low | 28576 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29381 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 335 XRP too low | 20125 |
| [BLACKOUT](https://xrpl.to/token/rBBJjs9N54719B12jgqidAK22Z8eiiX9LM-424C41434B4F5554000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 311 XRP) | 155 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 371 XRP) | 185 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 297 XRP too low | 62195 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2364 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 200009 |
| [Chubs](https://xrpl.to/token/rDaU7GkANXeZpC9evgjE6nAc8qi6wttGEX-4368756273000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,829 XRP) | 914 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,122 XRP) | 561 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 5634 |
| [RIZL](https://xrpl.to/token/rGGTx2B14imh3fCu1HAWQbiZTA6Uit2GbH-52495A4C00000000000000000000000000000000) | FAIL_SAFETY | pool 1,609 XRP < 2,000 | 1609 |
| [EXPOSED](https://xrpl.to/token/rHfKWt7g9DvWL2av6om7jorF2sic3oQWFo-4558504F53454400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 464 XRP) | 232 |
| [ZERPS](https://xrpl.to/token/rJztCAZEQvKcMSQTpKUZRJJjA11aUTk9Aw-5A45525053000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 788 XRP) | 394 |
| [Jokka](https://xrpl.to/token/rKMwfvWZekbcQMFWVbRm3GidhC2tbJVmv2-4A6F6B6B61000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2643 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 163490 |
| [BLKSWN](https://xrpl.to/token/rKxvi3eDot8aBACcGjpVyPv7cpYF4AiETJ-424C4B53574E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 30 XRP) | 15 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2345 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,082 XRP) | 1041 |
| [Rope](https://xrpl.to/token/rM35EybdZXP1hW5fRMjRhE3ubhgwCkHy1N-526F706500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 92 XRP) | 46 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 51% (excl. AMM) | 9944 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3762 |
| [XRPATH](https://xrpl.to/token/rPJkdEVCQimfyWmAy6KSpw1vXRYM4HGxTY-5852504154480000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,729 XRP) | 1364 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,059 XRP) | 1029 |
| [🌊JeetTide](https://xrpl.to/token/rPeZtayaDWY7oygidnkSPK99bdLPFbYYAW-F09F8C8A4A656574546964650000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 343 XRP) | 171 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending | 14032 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 929 XRP) | 465 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 4807 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 223051 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 81757 |
| [Degen](https://xrpl.to/token/raD9kyvKgG9zN16XWMbx79VnMZFH1Lz7Xv-446567656E000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,856 XRP) | 928 |
| [Pickle](https://xrpl.to/token/raFnkrmagzEoK3yABLyZBbGR4tQQNYzoFh-5069636B6C650000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 68 XRP) | 34 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 188 XRP too low | 11252 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 10929 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 49396 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 46061 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 25829 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
