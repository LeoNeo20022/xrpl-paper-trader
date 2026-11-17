# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-17T20:37:15+00:00** (UTC) · XRP/USD 0.9695 (bitstamp) · last discovery 2026-11-17T20:37:15+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$62.67** | **-37.33** | $2.72 | 6 / $59.95 | $-37.09 | $-0.05 | 22 / 48 (31%) | 76 (70) | -14.02 | -0.49 | 64.64 | -13.39 | $7.44 (0.29976) | 1.2 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$74.93** | **-25.07** | $2.46 | 7 / $72.48 | $-27.30 | $+2.48 | 23 / 58 (28%) | 88 (81) | -4.22 | +2.27 | 77.29 | -0.74 | $8.84 (0.39308) | 1.4 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$78.71** | **-21.29** | $78.71 | 0 / $0.00 | $-20.60 | $+0.00 | 49 / 201 (20%) | 250 (250) | -14.16 | +0.00 | 81.19 | +3.16 | $28.30 (1.11761) | 0.0 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$66.83** | **-33.17** | $6.33 | 6 / $60.49 | $-32.98 | $+0.49 | 70 / 153 (31%) | 229 (223) | -10.82 | -0.01 | 68.93 | -9.18 | $25.35 (1.15201) | 1.2 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 90.88 | +12.78 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$93.80** | **-6.20** | $83.14 | 1 / $10.66 | $-6.08 | $+0.66 | 77 / 103 (43%) | 181 (180) | +0.22 | +0.70 | 96.76 | +18.65 | $24.31 (1.25889) | 0.2 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$75.65** | **-24.35** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T18:18 | $10.00 | 1.05 | 1.05 @ 2.1h | 0.99 |  |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-17T12:01 | $10.00 | 1.00 | 1.00 @ 7.6h | 0.99 | top-10 holders own 42% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.98 | 0.99 @ 1.1h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 0.99 | 0.99 @ 8.8h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-16T17:49 | $10.00 | 0.94 | 0.99 @ 1.8h | 0.87 | only 24% of LP burned (liquidity can be pulled) |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-16T06:58 | $10.00 | 0.99 | 1.05 @ 15.5h | 0.97 |  |

### plus5 — open positions (7)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T15:50 | $10.00 | 1.04 | 1.04 @ 4.6h | 0.98 |  |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.98 | 0.99 @ 1.1h | 0.98 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T11:46 | $10.00 | 0.99 | 1.01 @ 5.3h | 0.97 | only 23% of LP burned (liquidity can be pulled) |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-17T11:46 | $10.00 | 0.99 | 0.99 @ 8.8h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | 2026-11-16T03:03 | $10.00 | 0.91 | 0.98 @ 2.2h | 0.87 | top-10 holders own 43% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-16T00:28 | $10.00 | 1.01 | 1.07 @ 22.2h | 0.97 |  |
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-15T23:03 | $10.00 | 1.30 | 1.30 @ 45.6h | 0.98 | top-10 holders own 40% |

### scalp — open positions (0)

None.

### slow_scalp — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PIGEONS](https://xrpl.to/token/rfQVVT7X5FynwK87EczgP2T8RQXmQcQSf-504947454F4E5300000000000000000000000000) | 2026-11-17T17:53 | $10.00 | 0.98 | 0.98 @ 2.7h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [SIGMA](https://xrpl.to/token/rfKYWZ84fm9eVEdoTcsQCo1WdqMPyaUF5z-5349474D41000000000000000000000000000000) | 2026-11-17T15:30 | $10.00 | 1.04 | 1.04 @ 5.0h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 0.51% <= 2.0% |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-17T15:30 | $10.00 | 1.00 | 1.02 @ 1.6h | 0.99 | only 23% of LP burned (liquidity can be pulled) | slow_scalp: new/top-15 trending, round trip 0.92% <= 2.0% |
| [XDC](https://xrpl.to/token/rL2mB7aK22Fdzvx7Hp277cJcvPNC2V3QeF-XDC) | 2026-11-17T11:26 | $10.00 | 1.00 | 1.00 @ 9.2h | 1.00 | top-10 holders own 42% | slow_scalp: new/top-15 trending, round trip 0.11% <= 2.0% |
| [HONEY](https://xrpl.to/token/rNa4hZ4kfPwEdN5gSbbNr33aSpyF5ZjzDm-484F4E4559000000000000000000000000000000) | 2026-11-17T02:21 | $10.00 | 0.98 | 0.98 @ 18.1h | 0.98 |  | slow_scalp: new/top-15 trending, round trip 1.99% <= 2.0% |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | 2026-11-17T00:32 | $10.00 | 0.99 | 1.00 @ 4.5h | 0.99 | only 15% of LP burned (liquidity can be pulled); top-10 holders own 49% | slow_scalp: new/top-15 trending, round trip 1.40% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (1)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-17T13:44 | $10.00 | 1.07 | 1.07 @ 6.7h | 0.98 | only 24% of LP burned (liquidity can be pulled) | dip_bounce: 15.1% below 24h high 4.19682e-07 XRP, age 660.0d |

## How high do they run? (tracking only — no rule uses this)

719 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 106 | 15% |
| ≥ +20% | 33 | 5% |
| ≥ +30% | 20 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **2.6h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 124 of 719

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63420 |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 33496 |
| [ZONK](https://xrpl.to/token/r68mfG1vqS4dNGowzsUq7iLJZC6W65BEJ-5A4F4E4B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 148 XRP) | 74 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 30605 |
| [TOTO](https://xrpl.to/token/r9sH6YEVRyg8uYaKfyk1EfH36Lfq7a8PUD-544F544F00000000000000000000000000000000) | SKIP_ENTRY | 24h volume 467 XRP too low | 20034 |
| [BITx](https://xrpl.to/token/rBitcoiNXev8VoVxV7pwoQx1sSfonVP9i3-4249547800000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 436 XRP) | 218 |
| [CULT](https://xrpl.to/token/rCULtAKrKbQjk1Tpmg5hkw4dpcf9S9KCs-43554C5400000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 291 XRP too low | 61921 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 434 XRP too low | 18595 |
| [SPREZ](https://xrpl.to/token/rDdEARmBVLVQZBNp3RLt3NCbyvpUGKqHEx-535052455A000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,442 XRP) | 721 |
| [LKH](https://xrpl.to/token/rE2BANxWnyeyGgqyidRSQ9A54t2XVJS55v-4C4B480000000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 68 XRP) | 34 |
| [$ALEX](https://xrpl.to/token/rEwd8T3xMrhJwybaEPCMYY9NeDnxdmpiYw-24414C4558000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,168 XRP) | 1584 |
| [TIME](https://xrpl.to/token/rExSpmk2PAqxKRTT3mhjCrCpqVasBra5v8-54494D4500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7048 |
| [1CELL](https://xrpl.to/token/rGCtayZogyWdKj8GAUgGSURd2ThfcyBQhP-3143454C4C000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 3,161 XRP) | 1581 |
| [B2X](https://xrpl.to/token/rGGq6KDhhi8wkjBPG3QohwWGMhssu8fGtt-B2X) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,854 XRP) | 927 |
| [scrap](https://xrpl.to/token/rGHtYnnigyuaHehWGfAdoEhkoirkGNdZzo-7363726170000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 456 XRP too low | 13479 |
| [WHALE](https://xrpl.to/token/rH2AarcXtxzEbf6DprZz2PYGQJjANcnkYy-5748414C45000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 823 XRP) | 411 |
| [SQWIDZ](https://xrpl.to/token/rH8XeTmXoF9cKVk1GnvsA8ZTEKGbpQTP7h-53515749445A0000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 618 XRP) | 309 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 16406 |
| [EXPOSED](https://xrpl.to/token/rHfKWt7g9DvWL2av6om7jorF2sic3oQWFo-4558504F53454400000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 251 XRP) | 125 |
| [SWITCH](https://xrpl.to/token/rJ8jyXpdAZhfxMamtLadk8LYFxd1ff6iKQ-5357495443480000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 7191 |
| [PVE](https://xrpl.to/token/rJs1u9sS3372vBQEWp3LW34FyePvjmePCn-PVE) | FAIL_SAFETY | pool too small (xrpl.to TVL 34 XRP) | 17 |
| [FAMILY](https://xrpl.to/token/rJttfuZqs91hXGS5hvB42reVQvL3CgtgXi-46414D494C590000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 99 XRP too low | 3813 |
| [PROFIT](https://xrpl.to/token/rJwLNwaBUh9a7ajk9FeeLAuA791wVe3oyg-50524F4649540000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 278 XRP too low | 43535 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 162633 |
| [$BURST](https://xrpl.to/token/rLeGXSzGpGDxBnEPzCbYiUofRTcnHMnGif-2442555253540000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 88% (excl. AMM) | 2641 |
| [VOX](https://xrpl.to/token/rM22BKFMSx7qDi8bp7Ke4nGg9apo1GfJXD-VOX) | FAIL_SAFETY | pool too small (xrpl.to TVL 15 XRP) | 8 |
| [Xmen](https://xrpl.to/token/rMFL2KuFPMuiujdbVGbMzNNjj5QKyd6dZf-586D656E00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 9719 |
| [XEDGR](https://xrpl.to/token/rMvjj98VXmcrZgzkWxbWgC3JYtyaHcAsMY-5845444752000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,361 XRP) | 1181 |
| [XGM](https://xrpl.to/token/rNKfDB5djjH8iwGLApBWJCR1eW9khxU2qy-XGM) | FAIL_SAFETY | pool too small (xrpl.to TVL 929 XRP) | 464 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3124 |
| [PLR](https://xrpl.to/token/rNSYhWLhuHvmURwWbJPBKZMSPsyG5Qek17-PLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 2,874 XRP) | 1437 |
| [Retire](https://xrpl.to/token/rPFDe5C4qv4JTyTVsGDMWTYJtUsTW337XN-5265746972650000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 473 XRP) | 237 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,836 XRP < 2,000 | 1836 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 227 XRP too low | 13840 |
| [MLRD](https://xrpl.to/token/rPytUzcUxVbzv439EShC7hPWFND8NCbEMU-4D4C524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 616 XRP) | 308 |
| [XVR](https://xrpl.to/token/rRCA6gnPkvpKmWwfcYxHQ845gFQ5ThYQe-XVR) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,184 XRP) | 592 |
| [XYZ](https://xrpl.to/token/rU5nUwkBUPx3MFPQSHmMnr9S9yg4g8cKLc-XYZ) | SKIP_ENTRY | not new and not top trending | 5284 |
| [AGENTS](https://xrpl.to/token/rUfDg9MXCKRUZvQm47e8UhpUGHouwchUpo-4147454E54530000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 208 XRP) | 104 |
| [FZV](https://xrpl.to/token/rUkSXmFrYDkSJnjBSb79VdLfbNjjYwLCLp-FZV) | FAIL_SAFETY | pool too small (xrpl.to TVL 95 XRP) | 48 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 223284 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
