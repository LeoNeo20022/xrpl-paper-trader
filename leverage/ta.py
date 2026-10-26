"""PAPER-ONLY trend-pullback strategy, long AND short, on a simulated Binance XRPUSDT perpetual (isolated margin).
No keys, no orders: arithmetic on public prices only. Parameters are textbook defaults chosen before any testing.

Chart reading (on CLOSED 1-hour candles):
- Trend: UP when EMA50 > EMA200 and close > EMA200; DOWN when EMA50 < EMA200 and close < EMA200; otherwise unclear -> stay flat.
- Long in an UP trend on a pullback: RSI(14) was under 40 on the previous hour and is now rising, OR MACD(12,26,9) crosses above its signal.
- Short in a DOWN trend on a bounce: RSI(14) was over 60 and is now falling, OR MACD crosses below its signal.
- Exits: stop-loss 1.5 x ATR(14), take-profit 3 x ATR(14) from the entry price. One position at a time; no other exits.
Execution model:
- Entry = market order at the next 5-min candle's open after the signal hour closes: taker 0.05% + 0.05% slippage.
- Whole paper balance is the isolated margin; notional = margin x leverage.
- Take-profit = resting limit (maker 0.02%), fills only if price trades 0.05% through it.
- Stop-loss = stop-market (taker 0.05% + 0.05% slippage); if a candle OPENS past the stop (gap) it fills at that open.
- Funding every 8h (00/08/16 UTC) on the notional: positive rate -> longs pay, shorts receive; negative -> the reverse. Booked to the isolated margin.
- Liquidation (whole margin lost) when margin + unrealised P/L <= 0.5% of notional, checked on each 5-min candle's extremes.
  With these stops a liquidation needs a gap through both the stop and the liquidation price."""

def ema(xs, n):
    k = 2 / (n + 1); out = []; e = None
    for x in xs:
        e = x if e is None else e + k * (x - e); out.append(e)
    return out

def wilder(xs, n):
    out = []; a = None
    for i, x in enumerate(xs):
        if i < n - 1: out.append(None); continue
        a = sum(xs[:n]) / n if a is None else (a * (n - 1) + x) / n
        out.append(a)
    return out

def indicators(bars, c):
    """bars: [(open_ts, o, h, l, cl)] closed 1h candles. Returns per-bar dicts keyed by CLOSE time (open_ts + 3600)."""
    cl = [b[4] for b in bars]
    ef, es = ema(cl, c["ema_fast"]), ema(cl, c["ema_slow"])
    ch = [0.0] + [cl[i] - cl[i - 1] for i in range(1, len(cl))]
    ag, al = wilder([max(x, 0) for x in ch], c["rsi_len"]), wilder([max(-x, 0) for x in ch], c["rsi_len"])
    rsi = [None if g is None else (100.0 if l == 0 else 100 - 100 / (1 + g / l)) for g, l in zip(ag, al)]
    f, s, sg = c["macd"]; m = [a - b for a, b in zip(ema(cl, f), ema(cl, s))]; sig = ema(m, sg)
    tr = [bars[0][2] - bars[0][3]] + [max(bars[i][2] - bars[i][3], abs(bars[i][2] - cl[i - 1]), abs(bars[i][3] - cl[i - 1])) for i in range(1, len(bars))]
    atr = wilder(tr, c["atr_len"])
    out = {}
    for i in range(1, len(bars)):
        if i < c["ema_slow"] or rsi[i - 1] is None or atr[i] is None: continue
        up = ef[i] > es[i] and cl[i] > es[i]; dn = ef[i] < es[i] and cl[i] < es[i]
        bull = m[i - 1] <= sig[i - 1] and m[i] > sig[i]; bear = m[i - 1] >= sig[i - 1] and m[i] < sig[i]
        rsi_up = rsi[i - 1] < c["rsi_long_below"] and rsi[i] > rsi[i - 1]
        rsi_dn = rsi[i - 1] > c["rsi_short_above"] and rsi[i] < rsi[i - 1]
        sigl = "LONG" if up and (rsi_up or bull) else "SHORT" if dn and (rsi_dn or bear) else None
        out[bars[i][0] + 3600] = {"signal": sigl, "trend": "up" if up else "down" if dn else "unclear", "atr": atr[i],
                                  "rsi": round(rsi[i], 2), "close": cl[i], "why": ("RSI" if (rsi_up or rsi_dn) else "MACD") if sigl else None}
    return out

def bars_1h(candles5):
    """Aggregate closed 5-min candles [(t, path)] into complete 1h bars [(open_ts, o, h, l, c)]."""
    g = {}
    for t, p in candles5: g.setdefault(t // 3600 * 3600, []).append((t, p))
    out = []
    for h in sorted(g):
        cs = sorted(g[h])
        if len(cs) < 12: continue
        out.append((h, cs[0][1][0], max(max(p) for _, p in cs), min(min(p) for _, p in cs), cs[-1][1][-1]))
    return out

def new_state(cfg):
    return {"cash": float(cfg["budget_usd"]), "pos": None, "trades": 0, "wins": 0, "longs": 0, "shorts": 0, "liquidations": 0,
            "liq_lost_usd": 0.0, "fees_usd": 0.0, "funding_usd": 0.0, "peak_equity": float(cfg["budget_usd"]), "max_dd_pct": 0.0,
            "realised_usd": 0.0, "last_signal_ts": None, "last_funding_ts": None}

def liq_price(pos, cfg):
    q, E, M, m = pos["qty"], pos["entry"], pos["margin"], cfg["mmr_pct"] / 100
    return (q * E - M) / (q * (1 - m)) if pos["side"] == "LONG" else (q * E + M) / (q * (1 + m))

def upnl(pos, p):
    return pos["qty"] * ((p - pos["entry"]) if pos["side"] == "LONG" else (pos["entry"] - p))

def equity(st, p, cfg):
    if not st["pos"]: return st["cash"]
    pos = st["pos"]; cost = pos["qty"] * p * (cfg["taker_pct"] + cfg["slippage_pct"]) / 100
    return st["cash"] + pos["margin"] + upnl(pos, p) - cost

def open_pos(st, cfg, side, px, atr, ts, why):
    slip = cfg["slippage_pct"] / 100
    fill = px * (1 + slip) if side == "LONG" else px * (1 - slip)
    lev = cfg["leverage"]; M0 = st["cash"]
    notional = M0 * lev / (1 + lev * cfg["taker_pct"] / 100)        # leave room for the entry fee
    fee = notional * cfg["taker_pct"] / 100; q = notional / fill; M = M0 - fee
    d = 1 if side == "LONG" else -1
    st["pos"] = {"side": side, "entry": fill, "qty": q, "margin": M, "stop": fill - d * cfg["stop_atr"] * atr,
                 "target": fill + d * cfg["target_atr"] * atr, "opened": ts, "fees": fee, "funding": 0.0, "start_cash": M0}
    st["cash"] = 0.0; st["fees_usd"] += fee
    st["longs" if side == "LONG" else "shorts"] += 1
    return {"ts": ts, "event": f"OPEN_{side}", "price": round(fill, 5), "qty_xrp": round(q, 3), "notional_usd": round(notional, 4),
            "margin_usd": round(M, 4), "fee_usd": round(fee, 5), "stop": round(st["pos"]["stop"], 5), "target": round(st["pos"]["target"], 5),
            "liq_price": round(liq_price(st["pos"], cfg), 5), "why": why}

def close_pos(st, cfg, px, kind, ts):
    pos = st["pos"]; fee_pct = cfg["maker_pct"] if kind == "TAKE_PROFIT" else cfg["taker_pct"]
    slip = 0 if kind == "TAKE_PROFIT" else cfg["slippage_pct"] / 100
    fill = px * (1 - slip) if pos["side"] == "LONG" else px * (1 + slip)
    fee = pos["qty"] * fill * fee_pct / 100; pnl = upnl(pos, fill)
    st["cash"] = pos["margin"] + pnl - fee; st["fees_usd"] += fee
    net = st["cash"] - pos["start_cash"]
    st["trades"] += 1; st["wins"] += net > 0; st["realised_usd"] += net; st["pos"] = None
    return {"ts": ts, "event": f"{kind}_{pos['side']}", "price": round(fill, 5), "qty_xrp": round(pos["qty"], 3), "fee_usd": round(fee, 5),
            "trade_net_usd": round(net, 4), "funding_usd": round(pos["funding"], 5)}

def liquidate(st, cfg, p, ts):
    pos = st["pos"]; lost = pos["margin"]
    st["liquidations"] += 1; st["liq_lost_usd"] += lost; st["trades"] += 1; st["realised_usd"] -= pos["start_cash"]
    st["cash"] = 0.0; st["pos"] = None
    return {"ts": ts, "event": f"LIQUIDATION_{pos['side']}", "price": round(liq_price(pos, cfg), 5), "mkt": round(p, 5),
            "qty_xrp": round(pos["qty"], 3), "margin_lost_usd": round(lost, 4)}

def funding(st, t, rate, px, ts):
    st["last_funding_ts"] = t
    pos = st["pos"]
    if not pos: return None
    pay = pos["qty"] * px * rate * (1 if pos["side"] == "LONG" else -1)   # negative pay = received
    pos["margin"] -= pay; pos["funding"] += pay; st["funding_usd"] += pay
    return {"ts": ts, "event": "FUNDING", "price": round(px, 5), "rate": rate, "funding_usd": round(pay, 6)}

def step(st, cfg, t, path, ind, ts):
    """One closed 5-min candle opening at t. A signal from the 1h bar that closed at t is acted on at this candle's open."""
    ev = []
    sig = ind.get(t)
    if sig and t != st.get("last_signal_ts"):
        st["last_signal_ts"] = t
        if sig["signal"] and not st["pos"] and st["cash"] > 1.0:
            lev = sig.get("leverage", cfg["leverage"])            # 'mix' sizing passes a per-trade leverage; other lines use cfg
            if lev != cfg["leverage"]: st["mix_high_trades"] = st.get("mix_high_trades", 0) + 1
            why = f"{sig['why']} in {sig['trend']}trend, ATR {sig['atr']:.4f}" if sig.get("trend") else f"{sig['why']}, stop dist {sig['atr'] * cfg['stop_atr']:.5g}"
            ev.append(dict(open_pos(st, dict(cfg, leverage=lev), sig["signal"], path[0], sig["atr"], ts, why), leverage=lev))
    trig = cfg["trigger_pct"] / 100
    for i, p in enumerate(path):
        pos = st["pos"]
        if not pos: break
        L = pos["side"] == "LONG"; lq = liq_price(pos, cfg)
        if i == 0 and (p <= lq if L else p >= lq): ev.append(liquidate(st, cfg, p, ts)); break      # gapped through stop AND liq
        if (p <= pos["stop"]) if L else (p >= pos["stop"]):
            ev.append(close_pos(st, cfg, p if i == 0 else pos["stop"], "STOP_LOSS", ts)); break
        if i > 0 and ((p >= pos["target"] * (1 + trig)) if L else (p <= pos["target"] * (1 - trig))):
            ev.append(close_pos(st, cfg, pos["target"], "TAKE_PROFIT", ts)); break
    eqs = [equity(st, x, cfg) for x in path]
    st["peak_equity"] = max(st["peak_equity"], max(eqs)); worst = min(eqs)
    st["max_dd_pct"] = max(st["max_dd_pct"], (1 - worst / st["peak_equity"]) * 100) if st["peak_equity"] > 0 else 100
    return ev
