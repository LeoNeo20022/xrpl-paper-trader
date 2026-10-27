# Pump fade (PAPER): 10x SHORT after a +15% pump, TP +3% / stop -1.5%, 24h limit, 12h cooldown, $100/trade, after fees, slippage and real funding

| Variant | Oct-Dec 2024 | Jan-Mar 2025 | Last 60 days |
|---|---|---|---|
| A: +15% vs 72h low | 43 trades, 35% wins, $-22, DD -$217, 0 liq; signal hours 531, further +3% first 221 (42%) | 38 trades, 24% wins, $-127, DD -$233, 0 liq; signal hours 439, further +3% first 136 (31%) | 3 trades, 67% wins, $+42, DD -$16, 0 liq; signal hours 19, further +3% first 3 (16%) |
| B: +15% vs close 72h ago | 31 trades, 26% wins, $-144, DD -$198, 0 liq; signal hours 363, further +3% first 163 (45%) | 16 trades, 50% wins, $+102, DD -$45, 0 liq; signal hours 149, further +3% first 39 (26%) | 1 trades, 0% wins, $-16, DD -$16, 0 liq; signal hours 9, further +3% first 1 (11%) |
| A + longs crowded (Theo) | 18 trades, 33% wins, $-22, DD -$109, 0 liq; signal hours 130, further +3% first 50 (38%) | 4 trades, 25% wins, $-20, DD -$61, 0 liq; signal hours 13, further +3% first 3 (23%) | 0 trades, 0% wins, $+0, DD -$0, 0 liq; signal hours 0, further +3% first 0 (0%) |
| ref: retired pop fade | -$542 | -$137 | -$10 |
| ref: F3 | -$432 | +$204 | +$145 |

## News overlap (variant A trades; 17 bullish news moves in Riley's file)

- Within 12h after a bullish headline move: 10 trades, 1 won, $-119
  - 2024-11-12 09:00 UTC: STOP, $-16.4
  - 2024-11-14 02:00 UTC: STOP, $-16.3
  - 2024-11-14 23:00 UTC: TAKE, $+29.2
  - 2024-11-16 01:00 UTC: STOP, $-16.4
  - 2024-11-22 00:00 UTC: STOP, $-16.4
  - 2024-12-01 20:00 UTC: STOP, $-16.4
  - 2024-12-04 13:00 UTC: STOP, $-16.4
  - 2025-02-03 17:00 UTC: STOP, $-16.4
  - 2025-03-02 20:00 UTC: STOP, $-16.4
  - 2025-03-03 10:00 UTC: STOP, $-16.4
- All other A trades: 74 trades, 25 won, $+11

Caveat: biased subset. Riley's list only holds the 48 biggest moves, so bullish headlines never followed by a big move are missing; this cannot test 'short after bullish news' in general.

Gate (variant A): positive in 1 of 3 periods, >= 8 trades in every period: False -> FAIL
Notes: 'prior 72h low' excludes the signal bar. Timeouts are marked at the 24h close (engine equity). No live paper line added.
