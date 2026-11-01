# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-01T23:02:53+00:00** (UTC) · XRP/USD 1.2459 (bitstamp) · last discovery 2026-11-01T23:02:53+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$109.76** | **+9.76** | $0.87 | 11 / $108.89 | $+5.99 | $+3.89 | 11 / 10 (52%) | 32 (21) | +7.33 | +3.07 | 88.10 | +10.06 | $3.26 (0.18486) | 2.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$109.33** | **+9.33** | $0.08 | 11 / $109.24 | $+10.23 | $-0.76 | 13 / 16 (45%) | 40 (29) | +10.29 | -0.59 | 87.75 | +9.72 | $4.45 (0.22546) | 2.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$94.17** | **-5.83** | $94.17 | 0 / $0.00 | $-5.58 | $+0.00 | 23 / 67 (26%) | 90 (90) | -3.34 | +0.00 | 75.58 | -2.45 | $9.97 (0.39673) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$95.01** | **-4.99** | $34.94 | 6 / $60.08 | $-4.82 | $+0.08 | 33 / 51 (39%) | 90 (84) | -3.04 | +0.19 | 76.26 | -1.84 | $9.64 (0.38413) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 70.72 | -7.38 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$114.36** | **+14.36** | $74.88 | 4 / $39.48 | $+15.25 | $-0.52 | 39 / 38 (51%) | 81 (77) | +11.71 | -0.33 | 91.79 | +13.69 | $10.21 (0.57108) | 0.8 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$97.22** | **-2.78** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.005020 XRP/tx = max(0.00002, live open-ledger fee 0.00502), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.97 | 0.98 @ 1.0h | 0.97 | only 34% of LP burned (liquidity can be pulled) |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-10-30T17:54 | $10.00 | 0.78 | 0.99 @ 0.1h | 0.69 | top-10 holders own 30% |
| [YAGA](https://xrpl.to/token/rpYYe5GQWX7hEPkyMGuDnaCvYM74BxtBLL-5941474100000000000000000000000000000000) | 2026-10-30T15:45 | $5.00 | 2.49 | 2.88 @ 52.9h | 0.69 | top-10 holders own 34% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.98 | 1.01 @ 33.0h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.01 @ 55.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.95 | 1.00 @ 38.3h | 0.94 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.84 | 1.12 @ 32.8h | 0.83 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.97 | 1.00 @ 7.0h | 0.95 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.09 | 1.12 @ 20.5h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-10-30T11:19 | $10.00 | 1.00 | 1.00 @ 35.9h | 0.99 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.10 @ 17.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### plus5 — open positions (11)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T14:51 | $10.00 | 0.97 | 0.98 @ 3.2h | 0.97 | only 34% of LP burned (liquidity can be pulled) |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T02:39 | $10.00 | 1.05 | 1.06 @ 13.1h | 0.99 |  |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T02:39 | $10.00 | 1.09 | 1.25 @ 0.5h | 0.99 | top-10 holders own 49% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-10-31T22:51 | $10.00 | 0.93 | 1.00 @ 10.5h | 0.88 |  |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-10-30T13:43 | $10.00 | 0.98 | 1.01 @ 33.0h | 0.97 | only 28% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-10-30T13:28 | $10.00 | 1.00 | 1.01 @ 55.9h | 1.00 |  |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-10-30T11:45 | $10.00 | 0.95 | 1.00 @ 38.3h | 0.94 |  |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.84 | 1.12 @ 32.8h | 0.83 | top-10 holders own 43% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 0.97 | 1.00 @ 7.0h | 0.95 |  |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.09 | 1.12 @ 20.5h | 1.00 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-10-30T11:19 | $10.00 | 1.06 | 1.10 @ 17.3h | 0.99 | only 23% of LP burned (liquidity can be pulled) |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BCHAMP](https://xrpl.to/token/rhYhn7s6z4HAfuJm7ehuSE7wxepRoUPwpi-424348414D500000000000000000000000000000) | 2026-11-01T04:10 | $10.00 | 0.97 | 0.99 @ 7.2h | 0.97 | only 34% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-01T00:17 | $10.00 | 0.98 | 0.99 @ 0.4h | 0.98 | only 13% of LP burned (liquidity can be pulled); top-10 holders own 36% | slow_scalp: new/top-15 trending, round trip 0.99% <= 2.0% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-01T00:07 | $10.00 | 0.96 | 0.99 @ 1.9h | 0.96 | only 28% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.78% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-01T00:07 | $10.00 | 0.99 | 1.00 @ 2.9h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [Tabby](https://xrpl.to/token/rsU4M9r6MZ6nhZZvFSiK8uWfq4hfz8188t-5461626279000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 1.07 | 1.08 @ 15.7h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.13% <= 2.0% |
| [PEPE](https://xrpl.to/token/rJEApMjV7KVVopB8NB1WXQpQYVu84vRGTa-5045504500000000000000000000000000000000) | 2026-11-01T00:02 | $10.00 | 1.04 | 1.05 @ 14.5h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.57% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | 2026-11-01T20:49 | $10.00 | 0.97 | 0.98 @ 1.2h | 0.95 |  | dip_bounce: 16.4% below 24h high 0.000196076 XRP, age 372.0d |
| [WALRUS](https://xrpl.to/token/rHYYwa8esP5eJCiWnSVY7STTHVH1iQVKqR-57414C5255530000000000000000000000000000) | 2026-11-01T17:04 | $10.00 | 0.98 | 0.99 @ 0.1h | 0.98 | top-10 holders own 35% | dip_bounce: 29.9% below 24h high 0.000459695 XRP, age 428.8d |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | 2026-11-01T09:33 | $10.00 | 0.95 | 1.03 @ 6.2h | 0.90 | top-10 holders own 49% | dip_bounce: 17.5% below 24h high 0.000103908 XRP, age 8.2d |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | 2026-11-01T07:48 | $10.00 | 1.05 | 1.10 @ 6.7h | 1.00 | top-10 holders own 34% | dip_bounce: 28.2% below 24h high 0.0043742 XRP, age 727.3d |

## How high do they run? (tracking only — no rule uses this)

272 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 63 | 23% |
| ≥ +20% | 23 | 8% |
| ≥ +30% | 14 | 5% |
| ≥ +50% | 9 | 3% |
| ≥ +100% | 2 | 1% |

Median peak **x1.01** · median hours to peak **3.3h** · best x3.18 · median low x0.97 · ≤ −10% at some point: 64 of 272

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [SOCKS](https://xrpl.to/token/r3D3XjfF9xSoSsRKHMrZ6RTV6SJvucMoon-534F434B53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 293 XRP) | 146 |
| [ASC](https://xrpl.to/token/r3qWgpz2ry3BhcRJ8JE6rxM8esrfhuKp4R-ASC) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,919 XRP) | 959 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending | 4741 |
| [STIMPY](https://xrpl.to/token/r4MczP3UQ4i7qbXx5r4cq9N36w4pyaPpqL-5354494D50590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2753 |
| [CROSS](https://xrpl.to/token/r4pQePYga7dJbrkfvo5b6njyWFHBn5TsSb-43524F5353000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 360 XRP) | 180 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 982 XRP) | 491 |
| [CODIUS](https://xrpl.to/token/r4zXT1VJ97qmCEDkDBhbRgLDB53cyxkTm3-434F444955530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 899 XRP) | 450 |
| [BOROS](https://xrpl.to/token/r9cXzxVoKRTPFXASnkdVWkvRDwSuT1zCuF-424F524F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,020 XRP) | 1510 |
| [CHAOS](https://xrpl.to/token/r9x2gBJncTSo8kK3kf7qE5qYoJCfSQoEkq-4348414F53000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,589 XRP) | 794 |
| [FUZZYPEPE](https://xrpl.to/token/rB8mxgyWN3wFSQHRs5aB6Psgvk1yGWW5Fi-46555A5A59504550450000000000000000000000) | FAIL_SAFETY | pool 1,826 XRP < 2,000 | 1826 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 62328 |
| [FUZZYB](https://xrpl.to/token/rCiqVyZRZsdEAcoitSeE5Hqd6dxmkX5Kp-46555A5A59420000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,009 XRP) | 1504 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2447 |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 188744 |
| [UBER](https://xrpl.to/token/rDoNUnQhJXtwqKRKVDZZ115RAMDSgDqKvi-5542455200000000000000000000000000000000) | FAIL_SAFETY | pool 1,683 XRP < 2,000 | 1683 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 210 XRP) | 105 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7621 |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 241126 |
| [B3B](https://xrpl.to/token/rH5g41CxkBi7wtYEgnkFGoRrsPU4TVyuiG-B3B) | FAIL_SAFETY | pool 1,676 XRP < 2,000 | 1676 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 15884 |
| [WALRUS](https://xrpl.to/token/rHYYwa8esP5eJCiWnSVY7STTHVH1iQVKqR-57414C5255530000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2791 |
| [GRINDR](https://xrpl.to/token/rHxGL8fhAn5VjjKrzPEUBCsXs5eEsnGre1-4752494E44520000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 424 XRP) | 212 |
| [SWITCH](https://xrpl.to/token/rJ8jyXpdAZhfxMamtLadk8LYFxd1ff6iKQ-5357495443480000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6923 |
| [LOST](https://xrpl.to/token/rJLvsT5DmzhEa48u3F1coB7bKCgmkGiBQr-4C4F535400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 165 XRP) | 82 |
| [REAL](https://xrpl.to/token/rKVyXn1AhqMTvNA9hS6XkFjQNn2VE8Nz88-5245414C00000000000000000000000000000000) | FAIL_SAFETY | excluded tag: Scam | 5810 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158019 |
| [WOFL](https://xrpl.to/token/rLbGxnf4F9pm3EGg1Uo4eJnYDvA7ariTTG-574F464C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 530 XRP) | 265 |
| [$BURST](https://xrpl.to/token/rLeGXSzGpGDxBnEPzCbYiUofRTcnHMnGif-2442555253540000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 88% (excl. AMM) | 2685 |
| [MOON](https://xrpl.to/token/rLrSng5xXN4vb3MprdRjEwGi78D17Lv8di-4D4F4F4E00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 282 XRP) | 141 |
| [$JSWRZ](https://xrpl.to/token/rLrrDKPRjnvQMJFjk7YxEew2AvpAAfejGM-244A5357525A0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2080 |
| [BXE](https://xrpl.to/token/rM1J2Mc2eCSFpCz5QXxhDG2KWkGQWgy87r-BXE) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,046 XRP) | 1023 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7729 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 5114 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,640 XRP) | 1320 |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7115 |
| [AOL](https://xrpl.to/token/rNdvnjS37QtXjTaS2bjGwswyMfbDzmmzmU-AOL) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,011 XRP) | 505 |
| [CABAL](https://xrpl.to/token/rPYSbL1c4uMbpzdL8echLw7guh8o8kZsPJ-434142414C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 863 XRP) | 432 |
| [ELEVNFIVE](https://xrpl.to/token/rU4gxrLrgZAEEPQuTQ3KhaT1hD8DGXKyTi-454C45564E464956450000000000000000000000) | FAIL_SAFETY | pool 1,673 XRP < 2,000 | 1673 |
| [BTCL](https://xrpl.to/token/rUgeZXZvcXX9UstkspHr1gHJKj89PqogtU-4254434C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,987 XRP) | 1493 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending | 310269 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
