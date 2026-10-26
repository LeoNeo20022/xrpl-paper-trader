"""PAPER-ONLY leveraged XRP grid, modelled on Binance USDⓈ-M XRPUSDT perpetual futures (isolated margin, one-way mode).
No keys, no logins, no orders: it only does arithmetic on public prices.

Strategy (a leveraged mirror of scalp_2pct, profit banked in USDT like scalp_2pct_rlusd):
- 10 buy levels 2% apart below the start price, each worth $10 of MARGIN ($100 budget / 10).
  A level that fills opens notional = margin x leverage (2x -> $20 of XRP, 5x -> $50 of XRP) as a maker limit order.
- Each filled level gets a reduce-only limit sell 2% above its buy price (maker). On fill, the margin comes back and the
  profit is banked in USDT (never recompounded). Then the level re-arms its buy. The ladder never moves (static).
- All filled levels form ONE long position (Binance one-way mode): average entry, one pool of isolated margin.
- Costs: maker 0.02% per fill (Binance VIP0), funding every 8h (00/08/16 UTC) on the open notional, deducted from the
  isolated margin, and fills only if the price trades 0.05% through the limit (queue/slippage proxy).
- LIQUIDATION: after every price point (incl. each 5-min candle's low) the position is liquidated if
  margin + unrealised PnL <= notional x maintenance-margin rate (XRPUSDT tier 1: 0.50%). The whole isolated margin is
  lost (Binance keeps any remainder as the clearance fee / insurance fund). All held levels re-arm as buys; the grid
  carries on only with the cash left.
- Value shown = what you'd have if you closed everything now at market: cash + margin + uPnL - taker 0.05% - 0.05% slippage.
Last-price candle lows are used, which is harsher than Binance's mark price (mark price smooths wicks)."""

def new_state(price, cfg):
    s = cfg["spacing_pct"] / 100
    n = cfg["levels"]
    st = {"budget_usd": cfg["budget_usd"], "start_price": price, "anchor": price, "cash": float(cfg["budget_usd"]),
          "margin": 0.0, "qty": 0.0, "entry": 0.0, "chunk": cfg["budget_usd"] / n, "realised_usd": 0.0,
          "fees_trade_usd": 0.0, "funding_usd": 0.0, "liq_lost_usd": 0.0, "liquidations": 0, "buys": 0, "sells": 0,
          "bar": 0, "last_funding_ts": None, "peak_equity": float(cfg["budget_usd"]), "max_dd_pct": 0.0,
          "levels": [{"buy": round(price * (1 - s) ** (i + 1), 4), "state": "buy"} for i in range(n)]}
    return st

def liq_price(st, cfg):
    """Long, isolated, tier-1 (no maintenance amount): liquidate when margin + q(P - E) = q*P*mmr."""
    if st["qty"] <= 0: return 0.0
    q, E, M, m = st["qty"], st["entry"], st["margin"], cfg["mmr_pct"] / 100
    return max(0.0, (q * E - M) / (q * (1 - m)))

def equity(st, price, cfg):
    """Close-everything-now value: taker fee + slippage on the open notional."""
    close_cost = st["qty"] * price * (cfg["taker_pct"] + cfg["slippage_pct"]) / 100
    return st["cash"] + st["margin"] + st["qty"] * (price - st["entry"]) - close_cost

def _liquidate(st, cfg, p, ts):
    lost = st["margin"]
    ev = {"ts": ts, "side": "LIQUIDATION", "price": round(liq_price(st, cfg), 5), "mkt_low": round(p, 5), "qty_xrp": round(st["qty"], 4),
          "entry": round(st["entry"], 5), "notional_usd": round(st["qty"] * st["entry"], 4), "margin_lost_usd": round(lost, 4),
          "levels_lost": sum(L["state"] == "sell" for L in st["levels"])}
    st["liq_lost_usd"] += lost; st["liquidations"] += 1
    st["margin"] = st["qty"] = st["entry"] = 0.0
    for L in st["levels"]:
        if L["state"] == "sell":
            b = L["buy"]; L.clear(); L.update(buy=b, state="buy")
    return ev

def funding(st, cfg, t_fund, rate, price, ts, assumed=False):
    """One 8-hourly funding settlement. Positive rate: longs pay. Paid from the isolated margin."""
    st["last_funding_ts"] = t_fund
    if st["qty"] <= 0: return None
    pay = st["qty"] * price * rate
    st["margin"] -= pay; st["funding_usd"] += pay
    return {"ts": ts, "side": "FUNDING", "price": round(price, 5), "qty_xrp": round(st["qty"], 4), "rate": rate,
            "funding_usd": round(pay, 6), "assumed_rate": assumed}

def process(st, path, cfg, ts=None):
    """Walk one candle's price path (o, h/l, l/h, c). Fills need the price to trade `trigger_pct` through the limit.
    A level bought in this candle cannot take profit until a later candle. Liquidation checked after every point."""
    lev = cfg["leverage"]; tp = cfg["tp_pct"] / 100; trig = cfg["trigger_pct"] / 100; mk = cfg["maker_pct"] / 100
    ev = []; st["bar"] += 1
    for p in path:
        for L in st["levels"]:
            if L["state"] == "buy" and p <= L["buy"] * (1 - trig) and st["cash"] >= st["chunk"] * 1.001:
                m = st["chunk"]; b = L["buy"]; n = m * lev; q = n / b; fee = n * mk
                st["cash"] -= m + fee; st["fees_trade_usd"] += fee
                st["entry"] = (st["entry"] * st["qty"] + b * q) / (st["qty"] + q); st["qty"] += q; st["margin"] += m
                st["buys"] += 1
                L.update(state="sell", qty=q, target=round(b * (1 + tp), 4), bar=st["bar"])
                ev.append({"ts": ts, "side": "OPEN_LONG", "price": b, "qty_xrp": round(q, 4), "notional_usd": round(n, 4),
                           "margin_usd": round(m, 4), "fee_usd": round(fee, 5), "mkt": round(p, 5)})
            elif L["state"] == "sell" and L["bar"] < st["bar"] and p >= L["target"] * (1 + trig) and st["qty"] > 0:
                q = min(L["qty"], st["qty"]); t = L["target"]
                rel = st["margin"] * q / st["qty"]                    # isolated margin released pro rata
                pnl = (t - st["entry"]) * q; fee = q * t * mk
                st["cash"] += rel + pnl - fee; st["margin"] -= rel; st["qty"] -= q
                if st["qty"] < 1e-9: st["qty"] = 0.0; st["entry"] = 0.0
                st["fees_trade_usd"] += fee; st["sells"] += 1
                st["realised_usd"] = st.get("realised_usd", 0.0) + pnl - fee
                ev.append({"ts": ts, "side": "CLOSE_LONG", "price": t, "qty_xrp": round(q, 4), "notional_usd": round(q * t, 4),
                           "realised_pnl_usd": round(pnl, 5), "fee_usd": round(fee, 5), "mkt": round(p, 5)})
                b = L["buy"]; L.clear(); L.update(buy=b, state="buy")
        if st["qty"] > 0 and (st["margin"] + st["qty"] * (p - st["entry"]) <= st["qty"] * p * cfg["mmr_pct"] / 100):
            ev.append(_liquidate(st, cfg, p, ts))
    st["peak_equity"] = max(st["peak_equity"], equity(st, max(path), cfg))
    worst = min(equity(st, min(path), cfg), equity(st, path[-1], cfg))   # intra-candle low counts for drawdown
    st["max_dd_pct"] = max(st["max_dd_pct"], (1 - worst / st["peak_equity"]) * 100)
    return ev
