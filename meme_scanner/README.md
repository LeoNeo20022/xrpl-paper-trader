# XRPL meme scanner (PAPER ONLY)

Log-only test of XRPL meme tokens (First Ledger style). It **never** touches a wallet, holds no keys, and signs or submits nothing.
It scans about every 5 minutes on GitHub Actions (`.github/workflows/meme-scanner.yml`: GitHub fires the cron irregularly, so each run loops 8 scans 300 s apart and commits after each; a new trigger waits for the running loop) and is completely separate from the XRP/RLUSD grid paper trader in the repo root.
Every logged trade is labelled `PAPER-NOT-ON-LEDGER`.

## What each run does
0. **Every run (~5 min):** price every open paper position from its XRPL AMM pool and apply exits (ledger only, free, ~5 s).
1. **Discover** — every run if the optional `XRPLTO_API_KEY` repo secret is set (free xrpl.to key, sent only as the `X-Api-Key` header, never logged; if xrpl.to rejects it, the run falls back to anonymous access with the 15-min throttle for an hour); without a key, only if ≥ 15 min since the last discovery (timestamp in `state/meta.json`) — tokens from [xrpl.to](https://xrpl.to): the newest 50 tokens (kept if under 72h old) and the top 40 by trending score; **with the API key also** the top 100 by 24h XRP volume (`dip_bounce` universe) and the top 50 by 1-hour price change (`breakout` universe). Extra-list tokens only get ledger safety checks if they already show a breakout or dip signal in xrpl.to's numbers. `/v1/tokens` costs 1 credit per call, `/v1/ohlc` 5 credits. Anonymous: only the 2 original lists, ≤ 192 calls/day, ~5,800/month (limit 333/day, 10k/month). With the free key at ~5-min runs (≤ 288/day): 4 list calls + 0–6 OHLC calls (usually 0–2) per discovery ≈ 1,150–4,000 credits/day typical, ≤ ~9,800/day worst case (≈ 35K–120K/month typical, ≤ ~300K worst case; free tier: 33K requests/day, 1M credits/month). Credits used by the last discovery are shown in `SUMMARY.md`. If xrpl.to is down, it falls back to scanning the most recent ≤60 XRPL ledgers per run for new `AMMCreate` XRP pools.
2. **Safety checks** from the public XRP Ledger (`account_info`, `amm_info`, `account_lines` via xrplcluster.com, s1/s2.ripple.com):
   - Hard fail: clawback enabled, RequireAuth, global freeze, AMM asset frozen, transfer fee > 1%, issuer not blackholed (master key disabled + no/blackhole regular key + no signer list), no XRP AMM pool, pool < 2,000 XRP, top-10 holders > 50% of supply (excluding the AMM pool), xrpl.to "Scam"/"Stablecoin" tags, stablecoins/majors.
   - Warnings only: top-10 > 30%, less than 50% of LP tokens burned (liquidity could be pulled), freezable issuer.
   - Holder concentration is computed from ledger trust lines when there are ≤ ~3,200 holders, otherwise xrpl.to's top-10 figure is used.
3. **Entry rule (hold, plus5, scalp — unchanged)**: passes all hard checks, is *new* (< 72h) or *top-15 trending*, 24h volume ≥ 500 XRP, and simulated round-trip cost ≤ 6%. Buys only happen on discovery runs.
   **Bankrolls:** `hold`, `plus5` and `scalp` each have their own independent $100 paper bankroll (cash tracked in USD at each fill). On every discovery, each strategy buys $10 of each passing token (new tokens first, then by trending score) while it has ≥ $10 cash, max 10 new buys per strategy per UTC day, one open position per token per strategy, and **no rebuy of a token within 24h of fully exiting it** (avoids chasing the same pump/dump). Exit proceeds go back to that strategy's cash. The first 10 shared v1 buys (Oct 24, 11:16 UTC) were copied into all three bankrolls with their original fills ($100 fully deployed each); the original file is kept as `state/positions_v1_migrated.json`.
3b. **Entry rules for the 3 strategies added Oct 24** (each: own $100 bankroll, $10 per buy, max 10 buys/UTC day, one position per token, no rebuy within 24h of exiting, same hard safety fails, round-trip cost limit as listed). Each decision is logged to `logs/signals.csv`:
   - `slow_scalp`: the same tokens the original strategies would buy (new or top-15 trending, 24h volume ≥ 500 XRP), but only if the simulated $10 round trip costs **≤ 2%**.
   - `breakout`: xrpl.to says the token is up ≥ 10% in the last hour (prefilter, from the 1h-change list or any other discovered token), 24h volume ≥ 500 XRP, round trip ≤ 6%. Then it is confirmed with 26 five-minute candles from xrpl.to `/v1/ohlc` (max 6 calls per run, biggest movers first): the **live ledger pool price is ≥ 10% above the close of the candle that ended ~60 min ago**, and **volume is rising = XRP volume in the last 60 min is above both the 60 min before that and the 24h hourly average (24h volume ÷ 24)**.
   - `dip_bounce`: established tokens only — **older than 3 days** (xrpl.to creation date), pool ≥ 2,000 XRP, 24h volume ≥ 500 XRP, round trip ≤ 6% — whose **live ledger pool price is ≥ 15% below xrpl.to's 24h high**. Universe: the top 100 tokens by 24h XRP volume plus anything in the new/trending lists. Deepest dips are bought first.
4. **Fills** are simulated against the token's XRP AMM pool with constant-product math: pool trading fee (charged on input), price impact for that size, issuer transfer fee (applied on both legs, conservative), and the 0.000012 XRP network fee. The order book (CLOB) is ignored, so real fills could be slightly better. The 0.2 XRP trust line reserve is not a cost (refundable) and is not counted.
5. **Exit strategies**, one per bankroll (triggers use the *net* sell value vs XRP paid, except the breakout trailing stop):
   - `hold`: sell half at +100%, stop −50%, close the rest at 72h
   - `plus5`: sell all at +50% (~+$5), stop −50%, 72h max
   - `scalp`: +20% take profit, −10% stop, 60 min max
   - `slow_scalp`: +8% take profit, −6% stop, 6h max
   - `breakout`: trailing stop — sell everything when the pool price falls 8% below the highest price seen since entry (checked every ~5 min; at entry the high is the entry price, so it also acts as an 8% stop); 24h max
   - `dip_bounce`: +10% take profit, −10% stop, 24h max
   If the pool disappears (rug), the position is closed at 0.
   **Caveat:** prices are only checked every ~5 minutes (GitHub can delay runs), so exits happen at the price seen at that poll, not the exact trigger level. Fast pumps/dumps will overshoot.

## Files
- `config.json` — all thresholds.
- `logs/candidates.csv` — every token seen with safety results (a row on first sight and whenever its verdict changes).
- `logs/paper_buys.csv` — simulated buys per strategy with fill price, slippage and fees.
- `logs/exits.csv` — simulated exits per strategy with gross and net P&L in XRP and USD.
- `logs/signals.csv` — entry decisions (eligible / skip + numbers) for slow_scalp, breakout and dip_bounce; a row when a token's decision changes.
- `SUMMARY.md` — per-strategy cash, open value, equity vs $100 (USD first, XRP second), realized/unrealized net P&L, wins/losses, trades, a "keep $100 in XRP" baseline, rejected tokens.
- `state/strategies.json` — the six bankrolls (cash, open and closed positions); `state/seen.json` — tokens seen; `state/meta.json` — run info.

Run locally: `python3 meme_scanner/scanner.py` (Python 3.9+, stdlib only).

Token data by <a href="https://xrpl.to">xrpl.to</a>.

## Fees (as if signed in Xaman), since 2026-10-24
- Every simulated transaction pays the XRPL network fee: max(0.00002 XRP, live open-ledger fee), capped at 0.01 XRP. Each buy = TrustSet (add line) + swap; each exit = swap; a full exit also removes the line (TrustSet). TrustSet fees are charged going forward from Oct 24 ~14:30 UTC; earlier swaps paid 0.000012 XRP.
- AMM pool fee, price impact (slippage) and issuer transfer fees were already inside every simulated fill.
- Trust line owner reserve (0.2 XRP per open line) is locked by the ledger, not spent; it is shown separately.
- NOT included: Xaman's own service fee. Xaman charges 0.8% of value on token swaps, AMM deposits/withdrawals and DEX market trades (TrustSet and offer cancels are free): https://help.xaman.app/app/getting-started-with-xaman/understanding-the-xaman-service-fee
