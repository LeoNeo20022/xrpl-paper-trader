# XRPL meme scanner (PAPER ONLY)

Log-only test of XRPL meme tokens (First Ledger style). It **never** touches a wallet, holds no keys, and signs or submits nothing.
It runs every 5 minutes on GitHub Actions (`.github/workflows/meme-scanner.yml`) and is completely separate from the XRP/RLUSD grid paper trader in the repo root.
Every logged trade is labelled `PAPER-NOT-ON-LEDGER`.

## What each run does
0. **Every run (~5 min):** price every open paper position from its XRPL AMM pool and apply exits (ledger only, free, ~5 s).
1. **Discover** (only if ≥ 15 min since the last discovery, tracked as a timestamp in `state/meta.json`) tokens from [xrpl.to](https://xrpl.to): the newest 50 tokens (kept if under 72h old) and the top 40 by trending score. 2 calls per discovery → at most 192 calls/day, ~5,800/month, inside the free anonymous limit (333/day, 10k/month). If xrpl.to is down, it falls back to scanning the last ~120 XRPL ledgers for new `AMMCreate` XRP pools.
2. **Safety checks** from the public XRP Ledger (`account_info`, `amm_info`, `account_lines` via xrplcluster.com, s1/s2.ripple.com):
   - Hard fail: clawback enabled, RequireAuth, global freeze, AMM asset frozen, transfer fee > 1%, issuer not blackholed (master key disabled + no/blackhole regular key + no signer list), no XRP AMM pool, pool < 2,000 XRP, top-10 holders > 50% of supply (excluding the AMM pool), xrpl.to "Scam"/"Stablecoin" tags, stablecoins/majors.
   - Warnings only: top-10 > 30%, less than 50% of LP tokens burned (liquidity could be pulled), freezable issuer.
   - Holder concentration is computed from ledger trust lines when there are ≤ ~3,200 holders, otherwise xrpl.to's top-10 figure is used.
3. **Entry rule**: passes all hard checks, is *new* (< 72h) or *top-15 trending*, 24h volume ≥ 500 XRP, and simulated round-trip cost ≤ 6%. Buys only happen on discovery runs.
   **Bankrolls:** `hold`, `plus5` and `scalp` each have their own independent $100 paper bankroll (cash tracked in USD at each fill). On every discovery, each strategy buys $10 of each passing token (new tokens first, then by trending score) while it has ≥ $10 cash, max 10 new buys per strategy per UTC day, one open position per token per strategy, and **no rebuy of a token within 24h of fully exiting it** (avoids chasing the same pump/dump). Exit proceeds go back to that strategy's cash. The first 10 shared v1 buys (Oct 24, 11:16 UTC) were copied into all three bankrolls with their original fills ($100 fully deployed each); the original file is kept as `state/positions_v1_migrated.json`.
4. **Fills** are simulated against the token's XRP AMM pool with constant-product math: pool trading fee (charged on input), price impact for that size, issuer transfer fee (applied on both legs, conservative), and the 0.000012 XRP network fee. The order book (CLOB) is ignored, so real fills could be slightly better. The 0.2 XRP trust line reserve is not a cost (refundable) and is not counted.
5. **Three exit strategies**, one per bankroll (triggers use the *net* sell value vs XRP paid):
   - `hold`: sell half at +100%, stop −50%, close the rest at 72h
   - `plus5`: sell all at +50% (~+$5), stop −50%, 72h max
   - `scalp`: +20% take profit, −10% stop, 60 min max
   If the pool disappears (rug), the position is closed at 0.
   **Caveat:** prices are only checked every ~5 minutes (GitHub can delay runs), so exits happen at the price seen at that poll, not the exact trigger level. Fast pumps/dumps will overshoot.

## Files
- `config.json` — all thresholds.
- `logs/candidates.csv` — every token seen with safety results (a row on first sight and whenever its verdict changes).
- `logs/paper_buys.csv` — simulated buys per strategy with fill price, slippage and fees.
- `logs/exits.csv` — simulated exits per strategy with gross and net P&L in XRP and USD.
- `SUMMARY.md` — per-strategy cash, open value, equity vs $100 (USD and XRP), realized/unrealized net P&L, win rate, trades, rejected tokens.
- `state/strategies.json` — the three bankrolls (cash, open and closed positions); `state/seen.json` — tokens seen; `state/meta.json` — run info.

Run locally: `python3 meme_scanner/scanner.py` (Python 3.9+, stdlib only).

Token data by <a href="https://xrpl.to">xrpl.to</a>.
