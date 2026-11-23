# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-23T15:10:23+00:00** (UTC) · XRP/USD 0.9914 (bitstamp) · last discovery 2026-11-23T15:10:23+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$55.31** | **-44.69** | $2.31 | 5 / $52.99 | $-47.50 | $+2.99 | 23 / 56 (29%) | 84 (79) | -21.94 | -1.16 | 55.79 | -22.25 | $8.11 (0.30044) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$66.44** | **-33.56** | $2.97 | 6 / $63.47 | $-36.78 | $+3.47 | 24 / 68 (26%) | 98 (92) | -10.21 | -1.78 | 67.02 | -11.02 | $9.78 (0.41392) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$72.99** | **-27.01** | $53.08 | 2 / $19.90 | $-26.19 | $-0.10 | 73 / 235 (24%) | 310 (308) | -25.73 | -0.10 | 73.62 | -4.41 | $34.30 (1.20233) | 0.4 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$54.97** | **-45.03** | $3.70 | 5 / $51.27 | $-45.61 | $+1.27 | 80 / 178 (31%) | 263 (258) | -22.88 | -0.73 | 55.45 | -22.66 | $28.69 (1.17477) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 88.87 | +10.77 | $2.26 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$89.66** | **-10.34** | $58.81 | 3 / $30.86 | $-10.41 | $+0.86 | 84 / 110 (43%) | 197 (194) | -3.82 | -0.46 | 90.44 | +12.34 | $26.18 (1.28009) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$77.36** | **-22.64** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-23T04:59 | $10.00 | 0.98 | 0.98 @ 10.2h | 0.98 |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T19:09 | $10.00 | 0.95 | 1.00 @ 0.1h | 0.95 | top-10 holders own 31% |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T23:05 | $10.00 | 0.97 | 1.00 @ 36.6h | 0.97 |  |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.98 | 1.01 @ 49.4h | 0.93 | only 22% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 0.96 | 1.00 @ 0.2h | 0.96 | top-10 holders own 31% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-22T11:44 | $10.00 | 0.97 | 1.00 @ 6.9h | 0.95 | only 22% of LP burned (liquidity can be pulled) |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | 2026-11-20T17:15 | $10.00 | 1.01 | 1.02 @ 19.2h | 1.00 |  |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | 2026-11-20T17:15 | $10.00 | 0.97 | 1.00 @ 43.0h | 0.97 |  |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.99 | 1.00 @ 50.0h | 0.98 | only 49% of LP burned (liquidity can be pulled); top-10 holders own 32% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-20T17:15 | $10.00 | 0.94 | 1.00 @ 10.7h | 0.93 |  |

### scalp — open positions (2)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 1.00 | – | – |  |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 1.00 | – | – | top-10 holders own 31% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 1.00 | – | – | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.05% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 1.00 | – | – |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-23T04:29 | $10.00 | 1.00 | 1.00 @ 10.7h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.53% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-22T23:48 | $10.00 | 0.99 | 1.00 @ 4.9h | 0.99 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-22T18:39 | $10.00 | 0.95 | 1.00 @ 0.6h | 0.95 | top-10 holders own 31% | slow_scalp: new/top-15 trending, round trip 0.09% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-23T15:10 | $10.00 | 1.00 | – | – | top-10 holders own 31% | dip_bounce: 29.1% below 24h high 2.69848e-05 XRP, age 769.6d |
| [OLX](https://xrpl.to/token/rswiX7wDL25Go4wGdLJK1ssSMpUsRGosJR-OLX) | 2026-11-23T04:29 | $10.00 | 0.96 | 0.99 @ 0.2h | 0.96 |  | dip_bounce: 15.4% below 24h high 0.000571808 XRP, age 612.1d |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | 2026-11-22T23:48 | $10.00 | 1.01 | 1.01 @ 15.4h | 0.99 | top-10 holders own 50% | dip_bounce: 21.9% below 24h high 0.0309492 XRP, age 712.0d |

## How high do they run? (tracking only — no rule uses this)

827 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 111 | 13% |
| ≥ +20% | 35 | 4% |
| ≥ +30% | 20 | 2% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.8h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 137 of 827

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [bwif](https://xrpl.to/token/r33jHP8k9eFY9Vf1SLU2XKfoQ8A3SkXPEh-6277696600000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 311 XRP too low | 7859 |
| [RKITTY](https://xrpl.to/token/r4Qn3ShtyP2vyqp6TGGsASyRp824XEP7t2-524B495454590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 901 XRP) | 450 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 61829 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 32388 |
| [XRPX](https://xrpl.to/token/r4tPgvSFTJYMxqLZsz9R6i2mykXUAZ6298-5852505800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 806 XRP) | 403 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 985 XRP) | 493 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 410 XRP too low | 30223 |
| [BEAR](https://xrpl.to/token/rBEARGUAsyu7tUw53rufQzFdWmJHpJEqFW-4245415200000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 100271 |
| [BEARCO](https://xrpl.to/token/rBEArcotnrcp42HoZofMZx4Mf9E8ADZxSm-42454152434F0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,471 XRP) | 1236 |
| [Jester](https://xrpl.to/token/rBx9hAq9AQpJZyHqpTyTiw9jjsR3W866bC-4A65737465720000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,043 XRP) | 521 |
| [CSC](https://xrpl.to/token/rCSCManTZ8ME9EoLrSHHYKW8PPwWMgkwr-CSC) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 22698 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | 24h volume 464 XRP too low | 61122 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 2350 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18596 |
| [X589](https://xrpl.to/token/rEmMBNqUEq1uUmN6e8G6XoQHXBwFvZS75Q-5835383900000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 910 XRP) | 455 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6749 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 12614 |
| [GiB](https://xrpl.to/token/rJ5PL1DYXyDuUPNzpSRq52Wz56jFZb8RuP-GiB) | SKIP_ENTRY | not new and not top trending | 2599 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 43974 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 158011 |
| [PUNX](https://xrpl.to/token/rLJQQctWoqmUuTon7VFfN2g4chQKbUn9YN-50554E5800000000000000000000000000000000) | FAIL_SAFETY | pool 1,778 XRP < 2,000 | 1778 |
| [Exrploit](https://xrpl.to/token/rLSD1svPhf5V5ryhhqGZac6iEcNmUSHH1M-457872706C6F6974000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 106 XRP) | 53 |
| [LFQP](https://xrpl.to/token/rLnh3vjwgjjr6CNBq7ddsdcnCddxhsGLXN-4C46515000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 199 XRP) | 99 |
| [XRPLOL](https://xrpl.to/token/rMDfsTapNvFSo7irSe6gYpPmYj3EjqbcqF-5852504C4F4C0000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 393 XRP too low | 10509 |
| [XDX](https://xrpl.to/token/rMJAXYsbNzhwp7FfYnAsYP5ty3R9XnurPo-XDX) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 3031 |
| [RippleBay](https://xrpl.to/token/rNmsGPj3PTX4USe5RBnJzdBApX3PgrmRsG-526970706C654261790000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,086 XRP) | 1043 |
| [XRPE](https://xrpl.to/token/rNxGzJYhRWLkYH3NcxJ2kjHFr31a5yvJzn-5852504500000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 855 XRP) | 427 |
| [HOHO](https://xrpl.to/token/rP8kFHLYYC6716moBnbJEi2mGEFW93LduD-484F484F00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 237 XRP) | 118 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,628 XRP < 2,000 | 1628 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 223 XRP too low | 42507 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 93 XRP too low | 13633 |
| [CRYPTO](https://xrpl.to/token/rRbiKwcueo6MchUpMFDce9XpDwHhRLPFo-43525950544F0000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 100% (excl. AMM) | 2679763 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 917 XRP) | 458 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 227182 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 84927 |
| [ATM](https://xrpl.to/token/raDZ4t8WPXkmDfJWMLBcNZmmSHmBC523NZ-ATM) | SKIP_ENTRY | not new and not top trending | 74568 |
| [COLD](https://xrpl.to/token/raPik8UUR185WkELJ1x661VpTFGutvCatf-434F4C4400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,006 XRP) | 1003 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 11208 |
| [SGB](https://xrpl.to/token/rctArjqVvTHihekzDeecKo6mkTYTUSBNc-SGB) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 10959 |
| [FLR](https://xrpl.to/token/rcxJwVnftZzXqyH9YheB8TgeiZUhNo1Eu-FLR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 52197 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
