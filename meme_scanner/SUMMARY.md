# XRPL meme scanner — PAPER ONLY (PAPER-NOT-ON-LEDGER)

Log-only experiment: no wallet, no keys, no orders. Every number below is simulated from public data.
Data by <a href="https://xrpl.to">xrpl.to</a> (token discovery); safety checks and prices from the public XRP Ledger.

Last run: **2026-11-28T09:41:10+00:00** (UTC) · XRP/USD 0.9398 (bitstamp) · last discovery 2026-11-28T09:41:10+00:00 (UTC, every run, API key) · xrpl.to credits used by last discovery: 4

## Bankrolls — scoreboard is USD/RLUSD (each strategy has its own $100, $10 per trade)

| Strategy | Rule | Started (UTC) | **Equity USD** | **vs $100** | Cash | Open (n / value) | Realized USD | Unrealized USD | Wins / losses (win rate) | Trades (closed) | Realized XRP | Unrealized XRP | Equity XRP | vs start XRP | Fees paid USD (network XRP) | Reserve locked XRP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hold | ½ at +100%, stop −50%, 72h | 2026-10-24 11:16 | **$56.11** | **-43.89** | $6.22 | 5 / $49.89 | $-43.60 | $-0.11 | 27 / 60 (31%) | 92 (87) | -20.67 | +1.37 | 59.70 | -18.33 | $8.84 (0.30108) | 1.0 |
| plus5 | all at +50%, stop −50%, 72h | 2026-10-24 11:16 | **$62.95** | **-37.05** | $4.24 | 6 / $58.71 | $-35.50 | $-1.29 | 28 / 74 (27%) | 108 (102) | -12.33 | +0.06 | 66.98 | -11.05 | $10.81 (0.41472) | 1.2 |
| scalp | +20% / −10% / 60 min | 2026-10-24 11:16 | **$72.99** | **-27.01** | $33.46 | 4 / $39.53 | $-25.81 | $-0.47 | 87 / 261 (25%) | 352 (348) | -23.73 | -0.48 | 77.67 | -0.37 | $38.17 (1.20561) | 0.8 |
| slow_scalp | new/top-15 trending, round trip ≤2%; +8% / −6% / 24h (was 6h until Oct 25) | 2026-10-24 13:37 | **$54.70** | **-45.30** | $4.92 | 5 / $49.78 | $-44.38 | $-0.22 | 93 / 187 (33%) | 285 (280) | -21.37 | +0.24 | 58.20 | -19.90 | $30.50 (1.17653) | 1.0 |
| breakout — **paused Oct 26 (low win rate)** | up ≥10% in 1h + rising volume; trailing stop 8% below high / 24h | 2026-10-24 13:37 | **$88.11** | **-11.89** | $88.11 | 0 / $0.00 | $-11.85 | $+0.00 | 5 / 16 (24%) | 21 (21) | -9.81 | +0.00 | 93.75 | +15.65 | $2.25 (0.06334) | 0.0 |
| dip_bounce | >3 days old, ≥15% below 24h high; +10% / −10% / 24h | 2026-10-24 13:37 | **$91.02** | **-8.98** | $61.67 | 3 / $29.35 | $-7.54 | $-0.65 | 91 / 119 (43%) | 213 (210) | +1.13 | -0.46 | 96.84 | +18.74 | $27.73 (1.30133) | 0.6 |
| *baseline: keep $100 in XRP* | buy XRP at $1.2815, hold | 2026-10-24 11:16 | **$73.34** | **-26.66** | – | – | – | – | – | – | – | – | 78.03 | +0.00 | – | – |

**All P/L above is after fees.** Fees paid = AMM pool fee + price impact (slippage) + issuer transfer fee + XRPL network fee, as if each tx were a plain transaction signed in Xaman (network fee now 0.000020 XRP/tx = max(0.00002, live open-ledger fee 1e-05), cap 0.01). Each buy = TrustSet + swap; each exit = swap; a full exit also removes the trust line (TrustSet). TrustSet fees are charged from Oct 24 ~14:30 UTC on; earlier network fees were 0.000012 XRP per swap. Reserve locked = 0.2 XRP per open trust line: held by the ledger and returned when the line is removed, so it is not a cost. Not included: Xaman's own 0.8% service fee on swaps/DEX trades (see README).

Cash is kept in USD at each fill. Values are net of AMM pool fee, price impact, issuer transfer fee and network fee (open positions valued at what selling right now would return). Equity XRP = equity USD ÷ current XRP/USD; start XRP = $100 at the start price. Each strategy is an independent hypothetical: their buys of the same token are each simulated against the same pool. Exits fire at the price seen at each ~5-min poll, so real fills could be better or worse than the trigger level. The 3 newer strategies started later than hold/plus5/scalp (see Started), so compare them per day, not just by total.

### hold — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.01 @ 10.4h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 25.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.19 | 1.19 @ 25.4h | 0.91 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-25T23:46 | $10.00 | 0.98 | 1.01 @ 33.1h | 0.97 | only 22% of LP burned (liquidity can be pulled) |

### plus5 — open positions (6)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [FUZZY](https://xrpl.to/token/rhCAT4hRdi2Y9puNdkpMzxrdKa5wkppR62-46555A5A59000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 0.96 | 0.99 @ 0.4h | 0.96 | only 22% of LP burned (liquidity can be pulled) |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.01 @ 10.4h | 1.00 |  |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T08:18 | $10.00 | 1.00 | 1.00 @ 25.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [DeepTide](https://xrpl.to/token/rnHDzEH4xyW6u4LbXqDoX1uk36v5ovhbFi-4465657054696465000000000000000000000000) | 2026-11-27T08:18 | $10.00 | 1.19 | 1.19 @ 25.4h | 0.91 | top-10 holders own 31% |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | 2026-11-26T05:46 | $10.00 | 0.96 | 0.99 @ 0.6h | 0.96 | only 23% of LP burned (liquidity can be pulled) |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | 2026-11-25T15:31 | $10.00 | 0.90 | 1.00 @ 51.4h | 0.90 | top-10 holders own 35% |

### scalp — open positions (4)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings |
|---|---|---|---|---|---|---|
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-28T09:26 | $10.00 | 0.99 | 0.99 @ 0.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% |
| [SEAL](https://xrpl.to/token/r4pXXQzJ8soYSX4QKeeW4BzRQS1PCtVYLJ-5345414C00000000000000000000000000000000) | 2026-11-28T09:26 | $10.00 | 0.98 | 0.98 @ 0.1h | 0.98 |  |
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-28T09:26 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  |
| [404](https://xrpl.to/token/raHJ4Jz9PYk356wWaDMYw79B17iWtfsSMi-404) | 2026-11-28T09:26 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | only 38% of LP burned (liquidity can be pulled); top-10 holders own 31% |

### slow_scalp — open positions (5)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [PHNIX](https://xrpl.to/token/rDFXbW2ZZCG5WgPtqwNiA2xZokLMm9ivmN-50484E4958000000000000000000000000000000) | 2026-11-28T09:26 | $10.00 | 1.00 | 1.00 @ 0.2h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.44% <= 2.0% |
| [ARMY](https://xrpl.to/token/rGG3wQ4kUzd7Jnmk1n5NWPZjjut62kCBfC-41524D5900000000000000000000000000000000) | 2026-11-28T01:32 | $10.00 | 1.00 | 1.00 @ 0.4h | 1.00 |  | slow_scalp: new/top-15 trending, round trip 0.00% <= 2.0% |
| [XMEME](https://xrpl.to/token/r4UPddYeGeZgDhSGPkooURsQtmGda4oYQW-584D454D45000000000000000000000000000000) | 2026-11-28T01:32 | $10.00 | 0.98 | 0.98 @ 7.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 1.88% <= 2.0% |
| [PLX](https://xrpl.to/token/rGLEgQdktoN4Be5thhk6seg1HifGPBxY5Q-PLX) | 2026-11-27T18:18 | $10.00 | 0.99 | 0.99 @ 15.1h | 0.99 | only 12% of LP burned (liquidity can be pulled); top-10 holders own 35% | slow_scalp: new/top-15 trending, round trip 1.03% <= 2.0% |
| [BURN](https://xrpl.to/token/rwgNTwrsZKPe7xYCy4emjFAYpgnuioHSkd-4255524E00000000000000000000000000000000) | 2026-11-27T18:18 | $10.00 | 1.05 | 1.05 @ 15.1h | 1.00 | top-10 holders own 34% | slow_scalp: new/top-15 trending, round trip 0.10% <= 2.0% |

### breakout (paused Oct 26 (low win rate), exits only) — open positions (0)

None.

### dip_bounce — open positions (3)

| Token | Bought (UTC) | Cost | Now (net, x) | Peak (x, h after buy) | Low (x) | Warnings | Why bought |
|---|---|---|---|---|---|---|---|
| [BMT](https://xrpl.to/token/rE8dJChTgdF4GD84z8Ah5NoNbVvMTqRMLk-BMT) | 2026-11-28T09:26 | $10.00 | 0.99 | 0.99 @ 0.2h | 0.99 | top-10 holders own 31% | dip_bounce: 15.9% below 24h high 0.000121198 XRP, age 670.8d |
| [XMEME](https://xrpl.to/token/r4UPddYeGeZgDhSGPkooURsQtmGda4oYQW-584D454D45000000000000000000000000000000) | 2026-11-28T01:32 | $10.00 | 0.98 | 0.98 @ 7.9h | 0.98 | only 0% of LP burned (liquidity can be pulled); top-10 holders own 34% | dip_bounce: 16.4% below 24h high 3.66089e-06 XRP, age 1297.4d |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | 2026-11-27T18:18 | $10.00 | 0.99 | 1.10 @ 7.8h | 0.91 | top-10 holders own 31% | dip_bounce: 24.7% below 24h high 1.85909e-05 XRP, age 773.8d |

## How high do they run? (tracking only — no rule uses this)

903 unique buys (same token + buy time counted once across strategies, using whichever strategy watched it longest/highest). Multiples are **net** (what selling the whole $10 buy would return, after pool fee, slippage, transfer and network fee), seen at the ~5-min polls; buys made before Oct 25 were backfilled from xrpl.to 5-min candles (approximate).

| Reached at any point | Buys | Share |
|---|---|---|
| ≥ +10% | 121 | 13% |
| ≥ +20% | 39 | 4% |
| ≥ +30% | 23 | 3% |
| ≥ +50% | 10 | 1% |
| ≥ +100% | 2 | 0% |

Median peak **x1.00** · median hours to peak **3.2h** · best x3.18 · median low x0.98 · ≤ −10% at some point: 142 of 903

## Recently rejected (latest verdict per token)

| Token | Verdict | Reasons | Pool XRP |
|---|---|---|---|
| [Laugh](https://xrpl.to/token/r32nbPw6cyt3KdxinB4ua6WSLRrrF4SXAC-4C61756768000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 333 XRP too low | 9812 |
| [BG123HEART](https://xrpl.to/token/r3LXwcvxiENopYX9UuFcKxmRJ1Q6YZAczx-4247313233484541525400000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 259 XRP) | 130 |
| [CoinMP](https://xrpl.to/token/r3VGG8wwkMfD1Lfn3D3dzEdvUcsupwLGtz-436F696E4D500000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 74 XRP) | 37 |
| [MAHARISHI](https://xrpl.to/token/r43GYf7zhmTQ6xkwdWgTYzFRuxyHapoJEm-4D41484152495348490000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 176 XRP) | 88 |
| [XRP1000](https://xrpl.to/token/r44m3YiRMjeHDfytEUQPVqDpr8f2zsQ2U1-5852503130303000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 59% (excl. AMM) | 2641 |
| [XNODE](https://xrpl.to/token/r4CSnJij8KscghxxY4nybuBXiexdQgxn31-584E4F4445000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 21 XRP) | 11 |
| [YELLOW](https://xrpl.to/token/r4ZosXJjnRikUaRyTTAjTx84Si6NJhaazf-59454C4C4F570000000000000000000000000000) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 63876 |
| [RPLS](https://xrpl.to/token/r93hE5FNShDdUqazHzNvwsCxL9mSqwyiru-52504C5300000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 6590 |
| [Teddy](https://xrpl.to/token/r9Qk4VGodriw2xKLG9sRbTXWgknkz9TkDd-5465646479000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 29301 |
| [XRPayNet](https://xrpl.to/token/r9rRLst96Ue4YTDQkWWkX1ePB6p6Ye4FkA-58525061794E6574000000000000000000000000) | FAIL_SAFETY | top-10 holders own 52% (excl. AMM) | 2372 |
| [TNA](https://xrpl.to/token/rB54t5GDvpGc6frv2D6CpUueVJDBE6qfp3-TNA) | FAIL_SAFETY | pool too small (xrpl.to TVL 146 XRP) | 73 |
| [BG123OLIVE](https://xrpl.to/token/rBWguRQdj4m7gCr1GJJgJ9Xa5pK5jK8U2M-42473132334F4C49564500000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 230 XRP) | 115 |
| [XBAR](https://xrpl.to/token/rBbpmcuvmokBb7yFR6ZE8fNHbBLskyR8Ar-5842415200000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 1,798 XRP) | 899 |
| [BIRD](https://xrpl.to/token/rBirdPrE3GjXV7eW3PKANNHDizkbKztSp6-4249524400000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 364 XRP) | 182 |
| [$max](https://xrpl.to/token/rDAgpQSwp41PCrG7LyqxtAxbvssFM7rH6d-246D617800000000000000000000000000000000) | FAIL_SAFETY | pool 1,967 XRP < 2,000 | 1967 |
| [Horizon](https://xrpl.to/token/rDKJWtrPqKiMBzK9FTVvebMVec7FJtJLx6-486F72697A6F6E00000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 18772 |
| [DARK](https://xrpl.to/token/rDarkDFbpZAmMB8mKbbEbzHfpt8xkzjVwP-4441524B00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 147 XRP) | 74 |
| [BMT](https://xrpl.to/token/rE8dJChTgdF4GD84z8Ah5NoNbVvMTqRMLk-BMT) | SKIP_ENTRY | not new and not top trending | 6091 |
| [XLR](https://xrpl.to/token/rG6hnGh7PS2zBQ6sXccoCVR4sTSVoqrErF-XLR) | FAIL_SAFETY | pool too small (xrpl.to TVL 15 XRP) | 8 |
| [GRIM](https://xrpl.to/token/rHLRdLwXiBZSD53ZQz8ogGJz25LzNCCjSz-4752494D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 440 XRP too low | 15204 |
| [Xoge](https://xrpl.to/token/rJMtvf5B3GbuFMrqybh5wYVXEH4QE8VyU1-586F676500000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 351 XRP too low | 4732 |
| [OAR](https://xrpl.to/token/rJf7VZxBt6g2rBTan6uve89U8PRzSUy8bS-4F41520000000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 77% (excl. AMM) | 9500 |
| [GALAXY](https://xrpl.to/token/rKfmJxRNm5XptQ9AGVw2vJNTHw7UZyo2xm-47414C4158590000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 909 XRP) | 455 |
| [XLM](https://xrpl.to/token/rKiCet8SdvWxPXnAgYarFUXMh1zCPz432Y-XLM) | FAIL_SAFETY | issuer not blackholed (can still mint/freeze) | 156196 |
| [BAPES](https://xrpl.to/token/rLUR2xrdeP77xUKW3S93jaA8k5h4JAwkix-4241504553000000000000000000000000000000) | FAIL_SAFETY | pool 1,951 XRP < 2,000 | 1951 |
| [LIGHT](https://xrpl.to/token/rLighYhWbYwJ9AMX7YevAqwVqUDtFUHQEu-4C49474854000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 201 XRP) | 100 |
| [XRdoge](https://xrpl.to/token/rLqUC2eCPohYvJCEBJ77eCCqVL2uEiczjA-5852646F67650000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 10020 |
| [HOOTS](https://xrpl.to/token/rNPWp2RX2GHVbFbG77k76Ak8nhKwrHu17b-484F4F5453000000000000000000000000000000) | FAIL_SAFETY | top-10 holders own 55% (excl. AMM) | 3839 |
| [SWARM](https://xrpl.to/token/rPeUGJhb6DrrTSRA8WPnae8fv4x3P6G7HS-535741524D000000000000000000000000000000) | FAIL_SAFETY | pool 1,711 XRP < 2,000 | 1711 |
| [FARM](https://xrpl.to/token/rPrAEfVATUNDTJm9CUa8tYeD7oJrVdEGhU-4641524D00000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 261 XRP too low | 41927 |
| [Schmeckles](https://xrpl.to/token/rPxw83ZP6thv7KmG5DpAW4cDW55DZRZ9wu-5363686D65636B6C657300000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 112 XRP too low | 13693 |
| [STX](https://xrpl.to/token/rSTAYKxF2K77ZLZ8GoAwTqPGaphAqMyXV-STX) | FAIL_SAFETY | pool too small (xrpl.to TVL 847 XRP) | 423 |
| [SCHWEPE](https://xrpl.to/token/rUQXurByxmKni4aLpuWMYMxxV5GWT1Azw2-5343485745504500000000000000000000000000) | SKIP_ENTRY | not new and not top trending; 24h volume 310 XRP too low | 15371 |
| [XPM](https://xrpl.to/token/rXPMxBeefHGxx2K7g5qmmWq3gFsgawkoa-XPM) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 229700 |
| [MAG](https://xrpl.to/token/rXmagwMmnFtVet3uL26Q2iwk287SRvVMJ-MAG) | SKIP_ENTRY | not new and not top trending; 24h volume 390 XRP too low | 309452 |
| [EVR](https://xrpl.to/token/ra9g3LAJm9xJu8Awe7oWzR6VXFB1mpFtSe-EVR) | FAIL_SAFETY | not a meme (stablecoin/major/KYC issuer) | 93834 |
| [SHEL](https://xrpl.to/token/rapiKsAKqcRKUVnP61Uugcvqf3gfFPMdze-5348454C00000000000000000000000000000000) | FAIL_SAFETY | pool too small (xrpl.to TVL 355 XRP) | 177 |
| [NORTH](https://xrpl.to/token/razRVbPbtNtFt5TTa63XE122uRzoYooEpJ-4E4F525448000000000000000000000000000000) | SKIP_ENTRY | not new and not top trending | 11393 |
| [SLT](https://xrpl.to/token/rfGCeDUdtbzKbXfgvrpG745qdC1hcZBz8S-SLT) | FAIL_SAFETY | top-10 holders own 61% (excl. AMM) | 41188 |
| [589](https://xrpl.to/token/rfcasq9uRbvwcmLFvc4ti3j8Qt1CYCGgHz-589) | SKIP_ENTRY | not new and not top trending | 26137 |

Logs: `logs/candidates.csv`, `logs/signals.csv` (entry decisions of the 3 newer strategies), `logs/paper_buys.csv`, `logs/exits.csv`. Thresholds: `config.json`. Method: `README.md`.
