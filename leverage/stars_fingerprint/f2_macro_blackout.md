# F2 macro blackout test (PAPER). F2 squeeze LONG 10x, TP +3% / stop -1.5%, $100 per trade, one at a time, after fees/slippage/funding/liquidation.
Blackout = skip new entries from 12h before a scheduled FOMC decision or CPI release (variant: until 2h after). Events: 2024-10-10 12:30 UTC CPI, 2024-11-07 19:00 UTC FOMC, 2024-11-13 13:30 UTC CPI, 2024-12-11 13:30 UTC CPI, 2024-12-18 19:00 UTC FOMC, 2025-01-15 13:30 UTC CPI, 2025-01-29 19:00 UTC FOMC, 2025-02-12 13:30 UTC CPI, 2025-03-12 12:30 UTC CPI, 2025-03-19 18:00 UTC FOMC, 2026-07-29 18:00 UTC FOMC, 2026-08-12 12:30 UTC CPI, 2026-09-11 12:30 UTC CPI, 2026-09-16 18:00 UTC FOMC, 2026-10-14 12:30 UTC CPI

| Period | Variant | Trades | Win rate | P/L after fees | Worst drawdown | Liquidations |
|---|---|---|---|---|---|---|
| Oct-Dec 2024 | Baseline F2 | 133 | 47% | $+686 | -$146 | 0 |
| Oct-Dec 2024 | Blackout 12h before | 126 | 48% | $+664 | -$176 | 0 |
| Oct-Dec 2024 | Blackout 12h before + 2h after | 125 | 47% | $+635 | -$176 | 0 |
| Jan-Mar 2025 | Baseline F2 | 99 | 36% | $+16 | -$246 | 0 |
| Jan-Mar 2025 | Blackout 12h before | 94 | 36% | $+6 | -$246 | 0 |
| Jan-Mar 2025 | Blackout 12h before + 2h after | 91 | 36% | $+10 | -$246 | 0 |
| Last 60 days (Aug 27-Oct 25 2026) | Baseline F2 | 10 | 50% | $+63 | -$33 | 0 |
| Last 60 days (Aug 27-Oct 25 2026) | Blackout 12h before | 10 | 50% | $+63 | -$33 | 0 |
| Last 60 days (Aug 27-Oct 25 2026) | Blackout 12h before + 2h after | 10 | 50% | $+63 | -$33 | 0 |

## What the blackout removed
- Oct-Dec 2024, Blackout 12h before: removed 7 baseline trades (net $+22; 3 won / 4 lost); 0 different trades taken instead (net $+0). Removed: 2024-11-13 02:00 UTC STOP $-16, 2024-11-13 03:00 UTC STOP $-16, 2024-11-13 04:00 UTC STOP $-16, 2024-11-13 05:00 UTC STOP $-16, 2024-11-13 06:00 UTC TAKE $+29, 2024-11-13 09:00 UTC TAKE $+29, 2024-12-11 02:00 UTC TAKE $+29
- Oct-Dec 2024, Blackout 12h before + 2h after: removed 8 baseline trades (net $+51; 4 won / 4 lost); 0 different trades taken instead (net $+0). Removed: 2024-11-13 02:00 UTC STOP $-16, 2024-11-13 03:00 UTC STOP $-16, 2024-11-13 04:00 UTC STOP $-16, 2024-11-13 05:00 UTC STOP $-16, 2024-11-13 06:00 UTC TAKE $+29, 2024-11-13 09:00 UTC TAKE $+29, 2024-11-13 14:00 UTC TAKE $+29, 2024-12-11 02:00 UTC TAKE $+29
- Jan-Mar 2025, Blackout 12h before: removed 5 baseline trades (net $+9; 2 won / 3 lost); 0 different trades taken instead (net $+0). Removed: 2025-01-15 02:00 UTC TAKE $+29, 2025-01-15 08:00 UTC STOP $-16, 2025-01-15 10:00 UTC STOP $-16, 2025-01-15 12:00 UTC TAKE $+29, 2025-03-19 15:00 UTC STOP $-16
- Jan-Mar 2025, Blackout 12h before + 2h after: removed 8 baseline trades (net $+5; 3 won / 5 lost); 0 different trades taken instead (net $+0). Removed: 2025-01-15 02:00 UTC TAKE $+29, 2025-01-15 08:00 UTC STOP $-16, 2025-01-15 10:00 UTC STOP $-16, 2025-01-15 12:00 UTC TAKE $+29, 2025-01-15 14:00 UTC TAKE $+29, 2025-03-19 15:00 UTC STOP $-16, 2025-03-19 18:00 UTC STOP $-16, 2025-03-19 19:00 UTC STOP $-16
- Last 60 days (Aug 27-Oct 25 2026), Blackout 12h before: removed 0 baseline trades (net $+0; 0 won / 0 lost); 0 different trades taken instead (net $+0). Removed: none
- Last 60 days (Aug 27-Oct 25 2026), Blackout 12h before + 2h after: removed 0 baseline trades (net $+0; 0 won / 0 lost); 0 different trades taken instead (net $+0). Removed: none

## Verdict
The blackout does not help F2 in this data. It removed 7-8 trades per rally period, and those trades were net *winners* (+$22/+$51 Oct-Dec 2024, +$9/+$5 Jan-Mar 2025), so P/L fell slightly and the Oct-Dec drawdown got worse (-$146 to -$176). In the last 60 days, no F2 entry fell in a blackout window, so nothing changed. The sample is tiny (12-16 removed trades in total, clustered on 2-4 event days), so this does not prove event risk is harmless. It only shows that a 12h pre-event skip would not have paid for itself on F2. Note that the 10x long opened 2026-10-28 ~12:00 UTC (6h before FOMC) is outside the test window.
