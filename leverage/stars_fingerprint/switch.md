# Regime switch (PAPER): UP (4h close above a rising 4h EMA200) -> F2 longs only, else F3 shorts only. 10x, TP +3% / stop -1.5%, $100 per trade, after fees/funding.

Oct-Dec 2024 has no EMA200 slope until about Nov 7 (the 4h EMA200 needs ~37 days of warm-up), so hours before that are skipped by the switch.

| Line | Oct-Dec 2024 | Jan-Mar 2025 | Last 60 days |
|---|---|---|---|
| Switch, EMA200 rising vs 24h ago | 134 trades, 47% wins, $+669, worst drawdown -$146; regime flips 4; trades within 48h of a flip: 0 (0 won), $+0 | 61 trades, 33% wins, $-91, worst drawdown -$290; regime flips 20; trades within 48h of a flip: 24 (7 won), $-75 | 9 trades, 44% wins, $+34, worst drawdown -$33; regime flips 3; trades within 48h of a flip: 2 (1 won), $+12 |
| Switch, EMA200 rising vs 72h ago | 136 trades, 46% wins, $+591, worst drawdown -$146; regime flips 7; trades within 48h of a flip: 2 (2 won), $+58 | 55 trades, 44% wins, $+190, worst drawdown -$142; regime flips 8; trades within 48h of a flip: 4 (3 won), $+71 | 8 trades, 38% wins, $+5, worst drawdown -$39; regime flips 3; trades within 48h of a flip: 1 (0 won), $-17 |
| F2 alone (longs) | 133 trades, 47% wins, $+686, worst drawdown -$146 | 99 trades, 36% wins, $+16, worst drawdown -$246 | 10 trades, 50% wins, $+63, worst drawdown -$33 |
| F3 alone (shorts) | 82 trades, 24% wins, $-432, worst drawdown -$476 | 46 trades, 46% wins, $+204, worst drawdown -$89 | 19 trades, 53% wins, $+145, worst drawdown -$72 |

Gate ema200_4h_rising24: beats both standalone in 0 of 3 periods; drawdown never worse than the worse standalone: False -> FAIL

Gate ema200_4h_rising72: beats both standalone in 0 of 3 periods; drawdown never worse than the worse standalone: True -> FAIL
