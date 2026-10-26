"""PAPER backtest: the committee 'get on base' 5x (TP +1.5%, stop = tighter of 1% or 1.5x ATR) and the committee 2x line at a
$500 budget, re-run with REAL US contract sizes and REAL US fee schedules instead of fractional Binance-style sizing.
- Whole contracts only: contracts = floor(budget x leverage / (entry price x contract size)); 0 contracts -> the entry is skipped.
  XRP: Coinbase nano XRP Perp Style (XPP) = 500 XRP; Kraken Derivatives US PXRPUH (Bitnomial) = 500 XRP.
  BTC: Coinbase nano Bitcoin Perp (BIP) = 0.01 BTC; Kraken PBTCUC = 0.01 BTC.
- Fees per contract per side (open and close), on top of the existing 0.05% slippage on market fills (entries, stops):
  * binance_frac : the original model (fractional size, 0.05% taker / 0.02% maker) for reference.
  * coinbase     : 0.02% of notional + $0.15 per contract (Coinbase's lowest advertised US rate 'as low as 0.02%' with the
                   $0.15/contract exchange+clearing+NFA minimum; additive structure as in Coinbase's published CFSE schedule).
  * coinbase_hi  : 0.05% of notional + $0.15 per contract (the 0.05% stated in Coinbase's Advanced Trade futures API guide).
  * kraken       : $0.0113 per contract flat (Kraken Derivatives US all-in: $0.0003 commission + $0.001 exchange/clearing + $0.01 NFA).
  * coinbase_m  : coinbase fees, contracts also capped by overnight margin: $370 per XPP contract at ~$1.30 (~57% of notional,
                   third-party broker table lpfutures.com/margins; CFM's own figure unverified), applied as 57% of notional at all prices.
                   With $500 this allows 1 XRP contract at today's price (intraday margin $230 would allow 2).
- Funding: Binance's real 8h rates used as a proxy (Coinbase funds hourly, Kraken settles daily; real venue history not used).
- Not modelled: US overnight vs intraday margin (5x may need intraday margin; holding through the daily close may need more
  margin), Coinbase's 0.10% liquidation fee (no liquidations occurred), venue-specific spreads/depth.
Same data, rules and windows as backtest_sizes.py / backtest_committee.py. Usage: python3 backtest_contracts.py -> backtest_contracts_output.txt"""
import os, sys
sys.argv = sys.argv[:1]
from backtest_committee import *   # noqa: F401,F403
import ta

B = 500
CSIZE = {"XRPUSDT": 500.0, "BTCUSDT": 0.01}
FEES = {"binance_frac": None,
        "coinbase": dict(pct=0.02, per=0.15), "coinbase_hi": dict(pct=0.05, per=0.15), "kraken": dict(pct=0.0, per=0.0113),
        "coinbase_m": dict(pct=0.02, per=0.15, margin_pct=57.0)}
LABEL = {"binance_frac": "Original model (fractional, Binance 0.05%/0.02%)", "coinbase": "Whole contracts, Coinbase 0.02% + $0.15/contract",
         "coinbase_hi": "Whole contracts, Coinbase 0.05% + $0.15/contract", "kraken": "Whole contracts, Kraken $0.0113/contract",
         "coinbase_m": "Coinbase 0.02% + $0.15, capped by overnight margin (~57% of notional/contract)"}
QUICK = {"quick_tp_pct": 1.5, "quick_stop_pct": 1.0, "quick_tp_min_lev": 0}
LINES = [("Committee+Theo 5x get-on-base TP +1.5%", VARIANTS[1], QUICK), ("Committee+Theo 2x", VARIANTS[0], None)]
_orig = (ta.open_pos, ta.close_pos, ta.equity)
MODEL = {"fee": None, "csize": None}

def fee(n, notional):
    f = MODEL["fee"]; return notional * f["pct"] / 100 + n * f["per"]

def open_pos(st, cfg, side, px, atr, ts, why):
    if MODEL["fee"] is None: return _orig[0](st, cfg, side, px, atr, ts, why)
    slip = cfg["slippage_pct"] / 100; fill = px * (1 + slip) if side == "LONG" else px * (1 - slip)
    lev = min(cfg["leverage"], MODEL["fee"].get("lev_cap", 99)); M0 = st["cash"]; cs = MODEL["csize"]
    n = int(M0 * lev // (fill * cs))
    if MODEL["fee"].get("margin_pct"): n = min(n, int(M0 // (fill * cs * MODEL["fee"]["margin_pct"] / 100)))
    while n > 0 and fee(n, n * cs * fill) >= M0: n -= 1
    if n <= 0:
        st["skipped"] = st.get("skipped", 0) + 1
        return {"ts": ts, "event": "SKIP_TOO_SMALL", "price": fill}
    q = n * cs; notional = q * fill; f = fee(n, notional); M = M0 - f; d = 1 if side == "LONG" else -1
    st["pos"] = {"side": side, "entry": fill, "qty": q, "n": n, "margin": M, "stop": fill - d * cfg["stop_atr"] * atr,
                 "target": fill + d * cfg["target_atr"] * atr, "opened": ts, "fees": f, "funding": 0.0, "start_cash": M0}
    if cfg.get("quick_tp_pct") and lev >= cfg.get("quick_tp_min_lev", 0):
        sd = min(cfg["stop_atr"] * atr, fill * cfg.get("quick_stop_pct", 1.0) / 100)
        st["pos"].update(target=fill * (1 + d * cfg["quick_tp_pct"] / 100), stop=fill - d * sd, quick_tp=True)
    st["cash"] = 0.0; st["fees_usd"] += f; st["longs" if side == "LONG" else "shorts"] += 1
    st["contracts"] = st.get("contracts", []) + [n]; st["eff_lev"] = st.get("eff_lev", []) + [notional / M0]
    return {"ts": ts, "event": f"OPEN_{side}", "price": fill, "qty_xrp": q, "notional_usd": notional, "margin_usd": M, "fee_usd": f,
            "stop": st["pos"]["stop"], "target": st["pos"]["target"], "liq_price": ta.liq_price(st["pos"], cfg), "why": why}

def close_pos(st, cfg, px, kind, ts):
    if MODEL["fee"] is None: return _orig[1](st, cfg, px, kind, ts)
    pos = st["pos"]; slip = 0 if kind == "TAKE_PROFIT" else cfg["slippage_pct"] / 100
    fill = px * (1 - slip) if pos["side"] == "LONG" else px * (1 + slip)
    f = fee(pos["n"], pos["qty"] * fill); pnl = ta.upnl(pos, fill)
    st["cash"] = pos["margin"] + pnl - f; st["fees_usd"] += f; net = st["cash"] - pos["start_cash"]
    st["trades"] += 1; st["wins"] += net > 0; st["realised_usd"] += net; st["pos"] = None
    k = "win_usd" if net > 0 else "loss_usd"; st[k] = st.get(k, 0.0) + net
    return {"ts": ts, "event": f"{kind}_{pos['side']}", "price": fill, "fee_usd": f, "trade_net_usd": net, "funding_usd": pos["funding"]}

def close_sided(st, cfg, px, kind, ts):
    side = st["pos"]["side"]; e = close_inner(st, cfg, px, kind, ts)
    d = st.setdefault("by_side", {}).setdefault(side, [0, 0, 0.0]); d[0] += 1; d[1] += e["trade_net_usd"] > 0; d[2] += e["trade_net_usd"]
    return e
close_inner = close_pos

def sides(st):
    out = []
    for s in ("LONG", "SHORT"):
        n, w, pl = st.get("by_side", {}).get(s, [0, 0, 0.0])
        out.append(f"{n}, {w / n * 100:.0f}%, {pl:+.2f}" if n else "0")
    return out

def equity(st, p, cfg):
    if MODEL["fee"] is None: return _orig[2](st, p, cfg)
    if not st["pos"]: return st["cash"]
    pos = st["pos"]; return st["cash"] + pos["margin"] + ta.upnl(pos, p) - fee(pos["n"], pos["qty"] * p) - pos["qty"] * p * cfg["slippage_pct"] / 100

ta.open_pos, ta.close_pos, ta.equity = open_pos, close_sided, equity

def main():
    L = [f"PAPER backtest, run {iso(time.time())} UTC. $500 budget. " + __doc__.split("Usage:")[0].strip(), ""]
    totals = {}
    for coin, sym in CC["coins"].items():
        rec, fund, old, ofund = load(sym)
        ctx_r, ind_r, _ = prep(rec, fund, sym); ctx_o, ind_o, _ = prep(old, ofund, sym)
        end = rec[-1][0] + 300
        s0 = min(t for t in ctx_o[(True, True)].t5 if ctx_o[(True, True)].ready(t)) // 86400 * 86400 + 86400
        wins = [(f"Last {w} days", [c for c in rec if c[0] >= end - w * 86400], ctx_r, fund) for w in (14, 30, 60)]
        wins.append(("Oct 2024 - Mar 2025", [c for c in old if c[0] >= s0], ctx_o, ofund))
        for label, sub, ctxs, fm in wins:
            h = (hold(sub) - 100) * B / 100; days = len(sub) / 288
            L += [f"## {sym} - {label} ({sub[0][1][0]:.4g} -> {sub[-1][1][-1]:.4g}, {days:.0f} days)", "",
                  "| Line | Fee/size model | P/L after fees+funding | Per day | Worst drawdown | Trades | Win rate | Fees | Funding | Contracts per trade (eff. leverage) | Entries skipped (too small) | Longs: closed, win rate, P/L | Shorts: closed, win rate, P/L | vs hold |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
            for name, var, ex in LINES:
                for fk, fv in FEES.items():
                    MODEL["fee"] = fv; MODEL["csize"] = CSIZE[sym]
                    v, st = run_com(sub, ctxs, fm, var, sym, budget=B, extra=ex)
                    MODEL["fee"] = None
                    pl = v - B; n = st["trades"]; cn = st.get("contracts", []); el = st.get("eff_lev", [])
                    ctr = f"{min(cn)}-{max(cn)} ({min(el):.1f}x-{max(el):.1f}x)" if cn else ("fractional" if fv is None else "—")
                    totals.setdefault((sym, name, fk), []).append(pl); totals.setdefault((sym, "hold", ""), [])
                    L.append(f"| {name} | {LABEL[fk]} | **{pl:+.2f}** | {pl / days:+.2f} | -{st.get('max_dd_usd', 0):.2f} ({st['max_dd_pct']:.0f}%) | {n} | "
                             f"{(st['wins'] / n * 100 if n else 0):.0f}% | ${st['fees_usd']:.2f} | ${st['funding_usd']:+.2f} | {ctr} | {st.get('skipped', 0)} | {' | '.join(sides(st))} | {pl - h:+.2f} |")
            totals[(sym, "hold", "")].append(h)
            L += [f"| Just hold $500 of {coin.upper()} | — | **{h:+.2f}** | {h / days:+.2f} | | | | | | | | | | |", ""]
            print("\n".join(L[-15:]), flush=True)
    L += ["## Totals over the 4 windows per coin (14d + 30d + 60d + Oct 2024-Mar 2025; the windows overlap) and the 8-window total (XRP + BTC)", "",
          "| Line | Fee/size model | XRP 4-window total | BTC 4-window total | 8-window total |", "|---|---|---|---|---|"]
    for name, _, _ in LINES:
        for fk in FEES:
            x = sum(totals[("XRPUSDT", name, fk)]); b = sum(totals[("BTCUSDT", name, fk)])
            L.append(f"| {name} | {LABEL[fk]} | {x:+.2f} | {b:+.2f} | {x + b:+.2f} |")
    x = sum(totals[("XRPUSDT", "hold", "")]); b = sum(totals[("BTCUSDT", "hold", "")])
    L.append(f"| Just hold $500 | — | {x:+.2f} | {b:+.2f} | {x + b:+.2f} |")
    open(os.path.join(HERE, "backtest_contracts_output.txt"), "w").write("\n".join(L) + "\n")
    print("\n".join(L[-12:]))

if __name__ == "__main__":
    main()
