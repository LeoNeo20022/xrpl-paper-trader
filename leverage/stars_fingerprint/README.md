# Stars Aligned fingerprint study (PAPER research only)

No keys, no orders, no wallets. The question: Stars Aligned (10x, 4-of-4 vote) has not triggered yet. Looking back, when *would* a 10x trade have
worked, and what showed up on the charts beforehand?

**Method.** Every closed 1h candle is treated as a possible entry, both LONG and SHORT. That is 1,439 hours in the last 60 days (Aug 27 to Oct 25, 2026) and
4,166 hours in the Oct 2024–Mar 2025 rally. Each trade runs in the same ta.py engine and with the same Stars settings as `../backtest_stars.py`: XRPUSDT 10x isolated,
take profit +3% and stop −1.5% price move, Binance-style taker/maker fees, slippage, 8-hourly funding and liquidation. A **winner** hit +3% before −1.5% (7-day cap).
The pre-entry signs are read with no look-ahead: the 4h EMA200, 1h/4h trend, RSI, EMA20 slope, 24h breakout, 24h move, volume vs the weekly median, ATR,
funding, open interest change, long/short ratio percentile, the committee's crowding flag, Fear & Greed (Theo's saved file), hour of day, CPI/PPI/FOMC from
`events_calendar.csv`, and each voter's proxy call including the Stars stand-ins.

Data: the last 60 days use Binance perp 5-min candles, real funding and Binance metrics for OI and long/short. The rally uses the saved Bitstamp 5-min file with real Binance funding
(note: backtest_stars.py assumes a flat 0.01%) and Binance metrics. Votes are checked hourly here, but every 15 minutes in backtest_stars.py.

Run: `python3 leverage/stars_fingerprint/fingerprint.py` (about 30 s once the data is cached in /tmp).

| File | What |
|---|---|
| sign_table.md | Each sign, per side and period: hours, wins, losses, win rate, lift, and the share of all winners and all losers that showed it |
| rules.md / rules.json | Strict out-of-sample test. The best 1–2-sign rules are picked on one period, then checked unchanged on the other |
| fingerprints.md | 3 proposed fingerprints and the current Stars rule, split into Rally A (Oct–Dec 2024), Rally B (Jan–Mar 2025) and the last 60 days |
| top_moves.csv | The biggest winning moves per side per period, one row per UTC day, for Riley's news check (copied to /home/box/shared/strategy-lab/stars_top_moves.csv) |
| candidates_*.csv | Every candidate hour: features, plus the outcome for both sides |

**Key caveats.** Neighbouring hours overlap heavily: one big move counts as many "winning hours", so the trade counts in fingerprints.md and rules.md are the honest ones.
The samples are small: 10–20 trades per rule per period. Most rules picked on one period failed on the other. 10x leaves no room for error: one −1.5% stop costs about 17% of the margin,
and a gap of about 9.5% would wipe the margin out (no liquidations occurred in this data). A stake of $100 per trade can lose more than $100 in a streak; see the worst-drawdown figures.

## Follow-up tests (2026-10-27): Pip's pop fade, Theo's guarded long, the starsg variant
All of these are in fingerprints.md, which also counts the signal hours that won and lost.
- **Pop fade SHORT** (24h up 3%+, RSI 65+, funding above 0, F&G 55+): it lost money in every period.
  - Oct–Dec 2024: 27% wins, −$542.
  - Jan–Mar 2025: 28% wins, −$137.
  - Last 60 days: 35% wins, −$10.
  - In most of its signal hours, price kept rising before the short could make +3%.
- **Theo's guarded LONG** (OI up 5%+ AND funding −0.01..+0.03% or crowded shorts) versus F1 without the guard:
  - It made less in Oct–Dec 2024: +$450 vs +$677.
  - It lost a little less in Jan–Mar 2025: −$94 vs −$126.
  - It was identical in the last 60 days.
  - Its worst drawdown was the same or smaller.
- **starsg** (Stars plus Theo's guarded and Pip's pop-fade stand-ins) fired 2 times in 3 periods. It is paper only, for comparison with Stars.
Live paper lines: `leverage/stars_extra.py` (see the main README).

## Regime switch (2026-10-27): `switch.py` -> switch.md
Rule: UP means the 4h close is above a rising 4h EMA200 (rising = higher than 24h ago; a variant uses 72h). In UP, take only F2 longs; otherwise take only F3 shorts.
Gate: it had to beat both F2 alone and F3 alone in at least 2 of 3 periods, with drawdown no worse.
Result: **FAIL** for both versions.
- The 24h version was close to F2 in Oct–Dec 2024 and lost in Jan–Mar 2025.
- The 72h version made money in all 3 periods, but never beat the better standalone line.
No live line was added. Pop fade was retired on Oct 26 (no new entries; record kept).
