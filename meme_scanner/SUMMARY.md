# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-10-30T11:39:50+00:00** (UTC) · XRP/USD 1.2479 (bitstamp) · last discovery 2026-10-30T11:39:50+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$103.08** | **+3.08** | $4.58 | 10 / $98.49 | $-0.31 | $+3.49 | 9 / 7 (56%) | 26 (16) | +0.37 | +4.54 | 82.60 | +4.57 | $2.51 (0.16432) | 2.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$117.58** | **+17.58** | $0.61 | 12 / $116.96 | $+20.75 | $-3.04 | 12 / 9 (57%) | 33 (21) | +16.08 | +0.09 | 94.22 | +16.19 | $3.68 (0.20478) | 2.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$95.98** | **-4.02** | $95.98 | 0 / $0.00 | $-3.81 | $+0.00 | 17 / 53 (24%) | 70 (70) | -1.74 | +0.00 | 76.92 | -1.12 | $7.85 (0.31504) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$98.81** | **-1.19** | $18.32 | 8 / $80.49 | $-1.48 | $+0.49 | 22 / 40 (35%) | 70 (62) | +0.61 | -0.54 | 79.18 | +1.07 | $7.51 (0.30209) | 1.6 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.61 | -7.50 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$119.55** | **+19.55** | $68.84 | 5 / $50.71 | $+19.14 | $+0.71 | 33 / 26 (56%) | 64 (59) | +15.36 | -0.10 | 95.80 | +17.70 | $7.74 (0.45841) | 1.0 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.38** | **-2.62** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (10)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T11:19 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | 2026-10-27T17:51 | $5.00 | 2.19 | 3.18 @ 44.3h | 0.73 | top-10 holders own 47% |
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-10-27T15:40 | $10.00 | 0.85 | 0.98 @ 0.1h | 0.85 | only 35% of LP burned (liquidity can be pulled) |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 50.3h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.94 | 1.00 @ 0.1h | 0.94 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.26 | 1.31 @ 14.9h | 0.96 |  |

### plus5 — open positions (12)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.98 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 0.1h | 1.00 |  |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 1.05 | 1.16 @ 15.3h | 0.98 | only 19% of LP burned (liquidity can be pulled) |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-10-29T02:36 | $10.00 | 0.92 | 0.99 @ 3.6h | 0.88 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-28T22:49 | $10.00 | 0.94 | 0.99 @ 9.9h | 0.92 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-10-28T22:27 | $10.00 | 0.97 | 1.03 @ 21.1h | 0.96 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 31% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-10-27T13:42 | $10.00 | 0.98 | 0.99 @ 50.3h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-10-27T13:03 | $10.00 | 0.94 | 1.00 @ 0.1h | 0.94 |  |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-27T11:40 | $10.00 | 1.26 | 1.31 @ 14.9h | 0.96 |  |

### scalp — open positions (0)

None.

### slow_scalp — open positions (8)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-30T01:25 | $10.00 | 0.99 | 1.00 @ 0.2h | 0.99 | top-10 holders own 30% | slow_scalp: new/top-15 trending, round trip 0.14% <= 2.0% |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | 2026-10-30T00:53 | $10.00 | 0.99 | 0.99 @ 10.8h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.75% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T00:12 | $10.00 | 0.99 | 0.99 @ 0.3h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T00:07 | $10.00 | 1.04 | 1.04 @ 10.2h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.12% <= 2.0% |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-30T00:07 | $10.00 | 0.99 | 1.00 @ 9.7h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.12% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.97 | 1.00 @ 0.2h | 0.95 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.97 | 0.99 @ 5.6h | 0.97 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 1.00 | 1.02 @ 6.3h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.08% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T03:52 | $10.00 | 1.06 | 1.06 @ 7.4h | 0.98 | top-10 holders own 30% | dip_bounce: 15.7% below 24h high 7.0907e-07 XRP, age 98.5d |
| [BRITTO](https://xrpl.to/token/rfxwXDzenkYoXSEbNA4cZjaT9FY3eeL47e-42524954544F0000000000000000000000000000) | 2026-10-30T01:59 | $10.00 | 0.99 | 1.00 @ 1.7h | 0.98 |  | dip_bounce: 39.1% below 24h high 1.19011e-05 XRP, age 741.1d |
| [CODED](https://xrpl.to/token/rnNErmg9xVmcxxNZUwivbJSH6i9GUwYPFj-434F444544000000000000000000000000000000) | 2026-10-30T01:05 | $10.00 | 0.95 | 1.00 @ 1.3h | 0.92 | top-10 holders own 42% | dip_bounce: 22.8% below 24h high 0.000138199 XRP, age 722.0d |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | 2026-10-30T00:02 | $10.00 | 1.01 | 1.01 @ 8.2h | 0.99 | only 43% of LP burned (liquidity can be pulled); top-10 holders own 42% | dip_bounce: 18.1% below 24h high 0.000199108 XRP, age 674.0d |
| [LIHUA](https://xrpl.to/token/rnhtvpHsAgigmVemgtzt7pujj4gv6LVL2a-4C49485541000000000000000000000000000000) | 2026-10-30T00:02 | $10.00 | 0.99 | 1.00 @ 3.1h | 0.99 | top-10 holders own 30% | dip_bounce: 17.3% below 24h high 7.59124e-09 XRP, age 668.0d |

## How high do they run? (tracking only — no rule uses this)

215 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 54 | 25% |
| ≥ +20% | 20 | 9% |
| ≥ +30% | 13 | 6% |
| ≥ +50% | 8 | 4% |
| ≥ +100% | 1 | 0% |

Median peak **x1.01** · median hours to peak **2.7h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 46 of 215

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 9482 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4488 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 701 XRP) | 350 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30931 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,117 XRP) | 559 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,944 XRP) | 1472 |
| [LOX](https://xrpl.to/token/r9kzhatDuUyAxAYbbsZAbs8nLr3t7sa6Wk-LOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,084 XRP) | 1542 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | top-10 holders own 69% (excl. AMM) | 2147 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62596 |
| [XRB](https://xrpl.to/token/rD9ixf7RRUKuKVFTsZa3fZGAN6HtNziPKa-XRB) | FAIL_SAFETY | pool too small (xrpl.to TVL 663 XRP) | 332 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 106 XRP too low | 19769 |
| [$FLR](https://xrpl.to/token/rDnNiyQ71fWy9NPciRFarpuhvV6hQVAzJM-24464C5200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,943 XRP) | 1472 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool 1,681 XRP < 2,000 | 1681 |
| [XOX](https://xrpl.to/token/rGJbFqiLdh23e9WigQ5sxTfFqTENveLX21-XOX) | SKIP_ENTRY | not new and not top trending | 11296 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,949 XRP < 2,000 | 1949 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 362 XRP) | 181 |
| [MILK](https://xrpl.to/token/rHjMMxnM84UGwVgABSmt3esFGxtDYK8RaZ-4D494C4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 411 XRP) | 205 |
| [OURO](https://xrpl.to/token/rHwkshB9XXd5Do3V3uqZeJv91mazdVTbEX-4F55524F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 413 XRP) | 207 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 465 XRP) | 232 |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7447 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 10871 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43061 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 6061 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156240 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,118 XRP) | 559 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9488 |
| [JUST1](https://xrpl.to/token/rNA9GrVUYJz7XPudUVdEkMSJ15XCWhBh81-4A55535431000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,133 XRP) | 567 |
| [Chosen](https://xrpl.to/token/rNFcv6vYT7mUmpjknwK9wd5edqkhJkg8KN-43686F73656E0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,061 XRP) | 1531 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 5277 |
| [NXS](https://xrpl.to/token/rNexusA23ZQdtejTCeHZZaiKoJRsrnXboq-NXS) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,889 XRP) | 945 |
| [CABAL](https://xrpl.to/token/rPYSbL1c4uMbpzdL8echLw7guh8o8kZsPJ-434142414C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 657 XRP) | 328 |
| [TRUMPY](https://xrpl.to/token/rPaqoKAo2ezcbKbxzu1XhAnBZ9WpowUmSW-5452554D50590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,670 XRP) | 835 |
| [LEDG](https://xrpl.to/token/rPvKPe13jyCyVWyzGhA8obji4E57JUM3qK-4C45444700000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,141 XRP) | 571 |
| [XRT](https://xrpl.to/token/rPvuCxw1m8u2SWTqtRN6ZEcb1xPbU4cPFR-XRT) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,561 XRP) | 1280 |
| [FRIZZY](https://xrpl.to/token/rQHU5KQJytJW8Yv1JdGmdhLPNRG7T6LztR-4652495A5A590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 158 XRP) | 79 |
| [SHACKLED](https://xrpl.to/token/rUFcWC9THJaXvEsc8kqf7orUzxfCxYRXjY-534841434B4C4544000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 740 XRP) | 370 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 230163 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 309762 |
| [SWAN](https://xrpl.to/token/ra8imJzWCDGdpruLZJWkzPMnZtxjJUdevM-5357414E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,022 XRP) | 1011 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 78593 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
