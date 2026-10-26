#!/usr/bin/env python3
"""PAPER-ONLY live lines for the candidate live setup: $1,000 on Kraken Derivatives US XRP perpetual (PXRPUH, Bitnomial),
running the rule-based committee 'get on base' quick line (TP +1.5% underlying, stop = tighter of 1% or 1.5x ATR), same
committee signals/rules as com_xrp_5x_quick, at leverage caps 2x and 3x:  com_xrp_kraken_1k_2x, com_xrp_kraken_1k_3x.
No keys, no logins, no orders, no wallet: public keyless prices only (same data path as committee_runner.py).
Execution model (differs from the Binance-style ta.py defaults, patched in this process only):
- Whole contracts only: 1 PXRPUH = 500 XRP; contracts = floor(cash x leverage cap / (entry price x 500)); 0 -> entry skipped.
- Fees: Kraken all-in $0.0113 per contract per side (support.kraken.com/articles/us-futures-fees) + the existing 0.05% slippage
  on market fills (entries, stops); take-profit = resting limit, no slippage.
- Funding: the existing stand-in (Binance/OKX 8-hourly rates; Kraken's real PXRPUH funding history not used).
- Liquidation: when account equity <= 17% of position notional (Bitnomial clearinghouse maintenance margin for XRPUH,
  bitnomial.com/clearinghouse); the position is closed at that price with slippage + fees and a $10 Kraken liquidation fee
  (support.kraken.com/articles/margin-on-us-futures). Kraken's initial margin for PXRPUH is unverified.
Writes leverage/state/<line>.json, leverage/logs/<line>_events.csv / _ticks.csv and a marked section in
leverage/SUMMARY_LEVERAGE.md and SUMMARY.md."""
import json, os, time
from datetime import datetime, timezone
import ta, committee, levdata
from committee_runner import history, append, load, save, EV, CC, SDIR, LDIR, HERE, ROOT, QUICK, FNG

SYM, COIN = "XRPUSDT", "xrp"
CS = 500.0; PER = 0.0113; MMR = 17.0; LIQ_FEE = 10.0; BUDGET = 1000.0; TARGET_DAY = 4.0
LINES = [("com_xrp_kraken_1k_2x", 2), ("com_xrp_kraken_1k_3x", 3)]
BEGIN, END = "<!-- KRAKEN-1K-BEGIN -->", "<!-- KRAKEN-1K-END -->"

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")

def open_pos(st, cfg, side, px, atr, ts, why):
    slip = cfg["slippage_pct"] / 100; fill = px * (1 + slip) if side == "LONG" else px * (1 - slip)
    lev = cfg["leverage"]; M0 = st["cash"]; n = int(M0 * lev // (fill * CS))
    if n <= 0:
        st["skipped"] = st.get("skipped", 0) + 1
        return {"ts": ts, "event": "SKIP_TOO_SMALL", "price": round(fill, 5), "why": f"{why}; cash {M0:.2f} < 1 contract"}
    q = n * CS; notional = q * fill; fee = n * PER; d = 1 if side == "LONG" else -1
    st["pos"] = {"side": side, "entry": fill, "qty": q, "n": n, "margin": M0 - fee, "stop": fill - d * cfg["stop_atr"] * atr,
                 "target": fill + d * cfg["target_atr"] * atr, "opened": ts, "fees": fee, "funding": 0.0, "start_cash": M0}
    sd = min(cfg["stop_atr"] * atr, fill * cfg["quick_stop_pct"] / 100)
    st["pos"].update(target=fill * (1 + d * cfg["quick_tp_pct"] / 100), stop=fill - d * sd, quick_tp=True)
    st["cash"] = 0.0; st["fees_usd"] += fee; st["longs" if side == "LONG" else "shorts"] += 1
    return {"ts": ts, "event": f"OPEN_{side}", "price": round(fill, 5), "qty_xrp": q, "notional_usd": round(notional, 4),
            "margin_usd": round(M0 - fee, 4), "fee_usd": round(fee, 5), "stop": round(st["pos"]["stop"], 5), "target": round(st["pos"]["target"], 5),
            "liq_price": round(ta.liq_price(st["pos"], cfg), 5), "why": f"{why}; {n} contract(s), {notional / M0:.2f}x"}

def _book(st, side, net):
    st["trades"] += 1; st["wins"] += net > 0; st["realised_usd"] += net
    k = "win_usd" if net > 0 else "loss_usd"; st[k] = st.get(k, 0.0) + net
    s = st.setdefault("by_side", {}).setdefault(side, [0, 0, 0.0]); s[0] += 1; s[1] += net > 0; s[2] += net

def close_pos(st, cfg, px, kind, ts):
    pos = st["pos"]; slip = 0 if kind == "TAKE_PROFIT" else cfg["slippage_pct"] / 100
    fill = px * (1 - slip) if pos["side"] == "LONG" else px * (1 + slip)
    fee = pos["n"] * PER; st["cash"] = pos["margin"] + ta.upnl(pos, fill) - fee; st["fees_usd"] += fee
    net = st["cash"] - pos["start_cash"]; st["pos"] = None; _book(st, pos["side"], net)
    return {"ts": ts, "event": f"{kind}_{pos['side']}", "price": round(fill, 5), "qty_xrp": pos["qty"], "fee_usd": round(fee, 5),
            "trade_net_usd": round(net, 4), "funding_usd": round(pos["funding"], 5)}

def liquidate(st, cfg, p, ts):
    pos = st["pos"]; lq = ta.liq_price(pos, cfg); px = p if (p < lq if pos["side"] == "LONG" else p > lq) else lq   # gap -> worse of the two
    slip = cfg["slippage_pct"] / 100; fill = px * (1 - slip) if pos["side"] == "LONG" else px * (1 + slip)
    fee = pos["n"] * PER + LIQ_FEE; st["cash"] = max(0.0, pos["margin"] + ta.upnl(pos, fill) - fee); st["fees_usd"] += fee
    net = st["cash"] - pos["start_cash"]; st["liquidations"] += 1; st["liq_lost_usd"] += -net; st["pos"] = None; _book(st, pos["side"], net)
    return {"ts": ts, "event": f"LIQUIDATION_{pos['side']}", "price": round(fill, 5), "mkt": round(p, 5), "qty_xrp": pos["qty"],
            "fee_usd": round(fee, 4), "trade_net_usd": round(net, 4), "margin_lost_usd": round(-net, 4)}

def equity(st, p, cfg):
    if not st["pos"]: return st["cash"]
    pos = st["pos"]; return st["cash"] + pos["margin"] + ta.upnl(pos, p) - pos["n"] * PER - pos["qty"] * p * cfg["slippage_pct"] / 100

ta.open_pos, ta.close_pos, ta.liquidate, ta.equity = open_pos, close_pos, liquidate, equity   # this process only

def main():
    now = time.time(); ts = iso(now); rows = []
    src, bars, c5 = history(SYM, now)
    fund, fsrc = levdata.funding_since(now - 5 * 86400, SYM); crowd, csrc = levdata.crowd_live(SYM)
    ctx = committee.Context(c5, bars, fund, dict(CC["common"], mmr_pct=MMR), crowd, FNG[0])
    for name, lev in LINES:
        cfg = dict(CC["common"], leverage=lev, mmr_pct=MMR, budget_usd=BUDGET, **QUICK, quick_tp_min_lev=0)
        sp = os.path.join(SDIR, f"{name}.json"); st = load(sp)
        if st is None:
            st = committee.new_state(cfg)
            st.update(started=iso(c5[-1][0] + 300), start_price=c5[-1][1][-1], last_candle_ts=c5[-1][0], venue="Kraken Derivatives US PXRPUH (paper)")
            print(f"{name} started at {st['start_price']}")
        evs = []
        for t, path in [(t, p) for t, p in c5 if t > st["last_candle_ts"]]:
            evs += committee.step(st, cfg, ctx, t, path, iso(t), fund.get(t, levdata.FUNDING_ASSUMED))
            st["last_candle_ts"] = t
        for e in evs:
            append(os.path.join(LDIR, f"{name}_events.csv"), dict(e, label="PAPER-NOT-REAL"), EV)
            print(("*** PAPER LIQUIDATION " if e["event"].startswith("LIQ") else "") + f"[{name}]", e)
        price = c5[-1][1][-1]; st["last_run"] = ts; save(sp, st)
        val = equity(st, price, cfg); p = st["pos"]
        days = max((now - datetime.fromisoformat(st["started"]).timestamp()) / 86400, 1e-9)
        bs = st.get("by_side", {}); hold = BUDGET / (st["start_price"] * 1.0005) * price
        row = {"ts": ts, "line": name, "leverage_cap": lev, "started": st["started"], "price": round(price, 6), "source": src, "funding_source": fsrc,
               "value_usd": round(val, 4), "pl_usd": round(val - BUDGET, 4), "days": round(days, 3), "pl_per_day": round((val - BUDGET) / days, 4),
               "max_drawdown_usd": round(st.get("max_dd_usd", 0), 4), "max_drawdown_pct": round(st["max_dd_pct"], 2),
               "trades": st["trades"], "wins": st["wins"], "long_closed": bs.get("LONG", [0])[0], "long_wins": bs.get("LONG", [0, 0])[1],
               "long_pl": round(bs.get("LONG", [0, 0, 0.0])[2], 4), "short_closed": bs.get("SHORT", [0])[0], "short_wins": bs.get("SHORT", [0, 0])[1],
               "short_pl": round(bs.get("SHORT", [0, 0, 0.0])[2], 4), "position": p["side"] if p else "FLAT", "contracts": p["n"] if p else 0,
               "entry": round(p["entry"], 6) if p else "", "stop": round(p["stop"], 6) if p else "", "target": round(p["target"], 6) if p else "",
               "liq_price": round(ta.liq_price(p, cfg), 6) if p else "", "fees_usd": round(st["fees_usd"], 4), "funding_usd": round(st["funding_usd"], 4),
               "liquidations": st["liquidations"], "skipped": st.get("skipped", 0), "hold_value_usd": round(hold, 4), "decisions": json.dumps(st["decisions"])}
        append(os.path.join(LDIR, f"{name}_ticks.csv"), row, list(row.keys())); rows.append(row)
    write_md(rows); print(json.dumps(rows, indent=1))

def write_md(rows):
    side = lambda n, w, pl: f"{n} ({w / n * 100:.0f}% wins) {pl:+.2f}" if n else "0"
    L = [BEGIN, "## Candidate live setup (PAPER-NOT-REAL): $1,000 on Kraken US XRP perpetual PXRPUH, committee 'get on base' line, 2x and 3x caps", "",
         f"Same committee signals/rules as `com_xrp_5x_quick` (take profit +1.5% underlying, stop the tighter of 1% or 1.5x ATR), whole 500-XRP contracts only, "
         f"Kraken fees $0.0113/contract/side + 0.05% slippage on market fills, funding stand-in (`{rows[0]['funding_source']}`), liquidation at 17% maintenance "
         f"margin + $10 fee. Last update {rows[0]['ts']} at ${rows[0]['price']:.4f}. Target: $4/day after fees.", "",
         "| Line | Started | **P/L after fees + funding** | **$/day vs $4 target** | Worst drawdown | Trades (win rate) | Longs: closed (wins) P/L | Shorts: closed (wins) P/L | Contracts held now | Fees / funding | Liquidations | vs hold $1,000 XRP |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        held = f"{r['contracts']} {r['position']} @ {r['entry']} (stop {r['stop']}, TP {r['target']}, liq {r['liq_price']})" if r["contracts"] else "0 (FLAT)"
        wr = f"{r['wins'] / r['trades'] * 100:.0f}%" if r["trades"] else "—"
        L.append(f"| `{r['line']}` ({r['leverage_cap']}x cap) | {r['started']} | **{r['pl_usd']:+.2f}** | **{r['pl_per_day']:+.2f}** ({r['pl_per_day'] - TARGET_DAY:+.2f} vs $4) | "
                 f"-{r['max_drawdown_usd']:.2f} ({r['max_drawdown_pct']:.1f}%) | {r['trades']} ({wr}) | {side(r['long_closed'], r['long_wins'], r['long_pl'])} | "
                 f"{side(r['short_closed'], r['short_wins'], r['short_pl'])} | {held} | ${r['fees_usd']:.2f} / ${r['funding_usd']:+.2f} | {r['liquidations']} | {r['value_usd'] - r['hold_value_usd']:+.2f} |")
    L += ["", "- $/day is P/L since start divided by days running; tiny in the first days. Backtest: `leverage/backtest_contracts_1k_output.txt`. "
          "Kraken's PXRPUH initial margin is unverified (3x assumed safer than 5x).", END]
    md = "\n".join(L) + "\n"
    for p in (os.path.join(HERE, "SUMMARY_LEVERAGE.md"), os.path.join(ROOT, "SUMMARY.md")):
        s = open(p).read() if os.path.exists(p) else ""
        if BEGIN in s and END in s: s = s[:s.index(BEGIN)] + md.rstrip("\n") + s[s.index(END) + len(END):]
        else: s = s.rstrip("\n") + "\n\n" + md
        open(p, "w").write(s)

if __name__ == "__main__":
    main()
