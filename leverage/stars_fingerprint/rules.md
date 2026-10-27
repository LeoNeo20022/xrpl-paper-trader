# Fingerprint rules (fit on one period, tested unchanged on the other). Break-even 36%


## Fit on rally, test on last60d, LONG

- **LONG when 4h close below EMA200 + event in last 24h**
  - fit (rally): 14 trades, 57% wins, $+135, worst drawdown -$58
  - test (last60d): 8 trades, 38% wins, $+5, worst drawdown -$59
- **LONG when 4h far below EMA200 (<-10%) + L/S ratio bottom 20% of week**
  - fit (rally): 18 trades, 50% wins, $+115, worst drawdown -$54
  - test (last60d): 0 trades, 0% wins, $+0, worst drawdown -$0
- **LONG when crowded shorts + event in next 24h**
  - fit (rally): 15 trades, 53% wins, $+119, worst drawdown -$61
  - test (last60d): 0 trades, 0% wins, $+0, worst drawdown -$0

## Fit on rally, test on last60d, SHORT

- **SHORT when funding negative + 2+ voters say LONG**
  - fit (rally): 22 trades, 50% wins, $+140, worst drawdown -$78
  - test (last60d): 7 trades, 43% wins, $+22, worst drawdown -$33
- **SHORT when 1h trend down + F&G extreme greed >75**
  - fit (rally): 11 trades, 36% wins, $+2, worst drawdown -$91
  - test (last60d): 0 trades, 0% wins, $+0, worst drawdown -$0
- **SHORT when hour 04-08 UTC (9pm-1am PT) + Casey votes LONG**
  - fit (rally): 28 trades, 43% wins, $+91, worst drawdown -$134
  - test (last60d): 2 trades, 0% wins, $-33, worst drawdown -$33

## Fit on last60d, test on rally, LONG

- **LONG when funding calm (0 to 0.01%) + OI -5% in 24h**
  - fit (last60d): 12 trades, 58% wins, $+122, worst drawdown -$42
  - test (rally): 140 trades, 31% wins, $-295, worst drawdown -$467
- **LONG when OI +5% in 24h**
  - fit (last60d): 13 trades, 46% wins, $+59, worst drawdown -$49
  - test (rally): 230 trades, 41% wins, $+551, worst drawdown -$324
- **LONG when 4h close below EMA200 + L/S ratio bottom 20% of week**
  - fit (last60d): 9 trades, 33% wins, $-11, worst drawdown -$66
  - test (rally): 44 trades, 45% wins, $+189, worst drawdown -$87

## Fit on last60d, test on rally, SHORT

- **SHORT when F&G greed 55-75 + event in next 24h**
  - fit (last60d): 9 trades, 78% wins, $+171, worst drawdown -$44
  - test (rally): 25 trades, 20% wins, $-182, worst drawdown -$229
- **SHORT when 1h trend up (EMA50>EMA200) + 4h trend down**
  - fit (last60d): 9 trades, 44% wins, $+35, worst drawdown -$43
  - test (rally): 15 trades, 20% wins, $-109, worst drawdown -$138
- **SHORT when hour 20-24 UTC (1-5pm PT) + 2+ voters say LONG**
  - fit (last60d): 14 trades, 64% wins, $+182, worst drawdown -$51
  - test (rally): 80 trades, 31% wins, $-169, worst drawdown -$368
