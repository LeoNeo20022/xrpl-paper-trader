# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-26T06:16:38+00:00** (UTC) · XRP/USD 0.9521 (bitstamp) · last discovery 2026-11-26T06:16:38+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$56.15** | **-43.85** | $6.47 | 5 / $49.68 | $-43.34 | $-0.32 | 27 / 57 (32%) | 89 (84) | -19.38 | -0.57 | 58.98 | -19.06 | $8.59 (0.30084) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$64.00** | **-36.00** | $6.09 | 6 / $57.91 | $-33.66 | $-2.09 | 28 / 70 (29%) | 104 (98) | -9.07 | -2.95 | 67.22 | -10.81 | $10.43 (0.41440) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$72.51** | **-27.49** | $42.90 | 3 / $29.61 | $-26.38 | $-0.39 | 81 / 249 (25%) | 333 (330) | -24.88 | -0.22 | 76.16 | -1.87 | $36.59 (1.20413) | 0.6 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$55.55** | **-44.45** | $4.18 | 5 / $51.37 | $-45.13 | $+1.37 | 87 / 183 (32%) | 275 (270) | -20.72 | -0.20 | 58.35 | -19.76 | $29.73 (1.17573) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 92.55 | +14.44 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$90.74** | **-9.26** | $70.75 | 2 / $19.99 | $-8.45 | $-0.01 | 89 / 115 (44%) | 206 (204) | -0.97 | -0.13 | 95.31 | +17.20 | $27.23 (1.30081) | 0.4 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$74.29** | **-25.71** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 22% of LP burned (liquidity can be pulled) |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 51.6h | 0.98 |  |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 0.98 @ 26.9h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 37.4h | 0.98 | only 27% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 0.99 | 0.99 @ 14.8h | 0.97 | top-10 holders own 35% |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.97 | 0.98 @ 26.9h | 0.97 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 42% |
| [DROP](https://xrpl.to/token/rszenFJoDdiGjyezQc8pME9KWDQH43Tswh-44524F5000000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 1.00 | 1.00 @ 37.4h | 0.98 | only 27% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.85 | 0.98 @ 0.2h | 0.85 |  |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-24T02:10 | $10.00 | 0.92 | 0.99 @ 0.1h | 0.89 |  |

### scalp — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-26T06:06 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 22% of LP burned (liquidity can be pulled) |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.99 | 0.99 @ 0.5h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 1.09% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 1.00 | 1.00 @ 0.6h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 1.00 | 1.00 @ 6.5h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-25T15:31 | $10.00 | 0.99 | 0.99 @ 14.8h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |
| [JELLY](https://xrpl.to/token/rKHsxmaqf2SfcyU9LRi3VyjpAtyg6ZrQMp-4A454C4C59000000000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 1.00 | 1.00 @ 14.8h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 1.00 | 1.00 @ 0.5h | 1.00 | top-10 holders own 32% | dip_bounce: 15.8% below 24h high 7.27828e-07 XRP, age 125.5d |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-25T23:46 | $10.00 | 0.99 | 0.99 @ 6.0h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | dip_bounce: 63.5% below 24h high 0.000578934 XRP, age 766.0d |

## How high do they run? (tracking only — no rule uses this)

871 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 119 | 14% |
| ≥ +20% | 38 | 4% |
| ≥ +30% | 22 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.0h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 140 of 871

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 7734 |
| [XRPNOMICS](https://xrpl.to/token/r38o5rKYgTUg5Dgu2pDsC1xkroMbpivGJj-5852504E4F4D4943530000000000000000000000) | FAIL_SAFETY | top-10 holders own 56% (excl. AMM) | 3599 |
| [CoinMP](https://xrpl.to/token/r3VGG8wwkMfD1Lfn3D3dzEdvUcsupwLGtz-436F696E4D500000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 113 XRP) | 57 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 67% (excl. AMM) | 4733 |
| [SHROOMIES](https://xrpl.to/token/r4M4TzSypz2gRdS86hTM7oFcSs6yRmEPKZ-5348524F4F4D4945530000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 499 XRP too low | 3659 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 61533 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32735 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 19659 |
| [FSX](https://xrpl.to/token/rBSYoYEc4A3Wyxf2gDtN2j5sJay35zdyX4-FSX) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,073 XRP) | 537 |
| [HBAR](https://xrpl.to/token/rBWPqhs7YZdUN2CJcZPQTv4qAvqts3nkBw-4842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,851 XRP) | 1425 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 429 XRP too low | 62031 |
| [Jbkvkjv](https://xrpl.to/token/rE5Tr2kJs1HkkZcfxhKJupyyYButcsGr86-4A626B766B6A7600000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 251 XRP) | 125 |
| [BFOOT](https://xrpl.to/token/rEjQsRE5gJDng9bnkV2WUYPtgtkD28fWMd-42464F4F54000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 473 XRP too low | 4696 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 855 XRP) | 427 |
| [XLR](https://xrpl.to/token/rG6hnGh7PS2zBQ6sXccoCVR4sTSVoqrErF-XLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 38 XRP) | 19 |
| [XRPuffin](https://xrpl.to/token/rGAxsQvcFuydfwSYEAkovZobp5R2fHZSyH-585250756666696E000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,676 XRP) | 838 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 358 XRP too low | 12886 |
| [TLS](https://xrpl.to/token/rKDWNsSZzXh5wBbDmTWwQT2oaGeTdW29jt-TLS) | FAIL_SAFETY | pool too small (xrpl.to TVL 481 XRP) | 241 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 157927 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,019 XRP) | 1509 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 187 XRP too low | 10512 |
| [CHIMPS](https://xrpl.to/token/rMdQw9azZu94CedtczEpNwXMjB1jCrZMia-4348494D50530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 713 XRP) | 357 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 54% (excl. AMM) | 3724 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 873 XRP) | 437 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,129 XRP) | 565 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 228917 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 88690 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 74700 |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | SKIP_ENTRY | not new and not top trending; 24h volume 168 XRP too low | 10698 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,687 XRP) | 1343 |
| [CORE](https://xrpl.to/token/rcoreNywaoz2ZCQ8Lg2EbSLnGuRBmun6D-434F524500000000000000000000000000000000) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 10876 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 51736 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 40616 |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 14258 |
| [NOMAD](https://xrpl.to/token/rfj6nPXU3j9YHA4Tvub9JeaYFrBvomJhSU-4E4F4D4144000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 43 XRP) | 22 |
| [SOIL](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-534F494C00000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 20441 |
| [WETH](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-5745544800000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 130313 |
| [mXRP](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-6D58525000000000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint) | 61170 |
| [SHX](https://xrpl.to/token/rfmS3zqrQrka8wVyhXifEeyTwe8AMz2Yhw-SHX) | FAIL_SAFETY | issuer not blackholed (can still mint) | 81898 |
| [Phantom](https://xrpl.to/token/rfwDHEbmc28ocKY7KxMa6XgddnUnpYWytg-5068616E746F6D00000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 99 XRP) | 50 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
