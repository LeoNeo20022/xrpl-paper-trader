# Fingerprint rules: PAPER, 10x, TP +3% / stop -1.5%, $100 per trade (no compounding), one trade at a time, after fees/slippage/funding. Break-even win rate 36%.
Signs were picked because they beat break-even in BOTH the rally and the last 60 days (so this is NOT a clean out-of-sample test; the clean one is rules.md).

| Rule | Rally A Oct-Dec 2024 | Rally B Jan-Mar 2025 | Last 60 days |
|---|---|---|---|
| F1 positioning surge LONG: OI +5% in 24h | 139 trades, 47% wins, $+677, worst drawdown -$178 | 91 trades, 33% wins, $-126, worst drawdown -$324 | 13 trades, 46% wins, $+59, worst drawdown -$49 |
| F2 squeeze LONG: crowded shorts, or OI +5% with 4h above EMA200 | 133 trades, 47% wins, $+686, worst drawdown -$146 | 99 trades, 36% wins, $+16, worst drawdown -$246 | 10 trades, 50% wins, $+63, worst drawdown -$33 |
| F3 failed-pullback SHORT: Casey's long trigger fires but funding is not hot (<0.03%) | 82 trades, 24% wins, $-432, worst drawdown -$476 | 46 trades, 46% wins, $+204, worst drawdown -$89 | 19 trades, 53% wins, $+145, worst drawdown -$72 |
| ref: current Stars rule (4/4 incl. stand-ins) LONG | 5 trades, 60% wins, $+54, worst drawdown -$22 | 3 trades, 33% wins, $-4, worst drawdown -$36 | 0 trades, 0% wins, $+0, worst drawdown -$0 |
| ref: current Stars rule (4/4 incl. stand-ins) SHORT | 0 trades, 0% wins, $+0, worst drawdown -$0 | 0 trades, 0% wins, $+0, worst drawdown -$0 | 0 trades, 0% wins, $+0, worst drawdown -$0 |
| ref: any hour, LONG | 492 trades, 37% wins, $+292, worst drawdown -$734 | 457 trades, 31% wins, $-1121, worst drawdown -$1385 | 131 trades, 28% wins, $-468, worst drawdown -$499 |
| ref: any hour, SHORT | 510 trades, 28% wins, $-1751, worst drawdown -$2035 | 454 trades, 31% wins, $-937, worst drawdown -$1116 | 120 trades, 35% wins, $-52, worst drawdown -$326 |
