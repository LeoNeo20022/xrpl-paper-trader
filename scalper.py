"""XRP-accumulating scalp ladder for XRP/RLUSD (PAPER ONLY: no keys, no orders).

How it works
- A ladder of N buy levels sits below an anchor price, `spacing_pct` apart. Each level spends a
  fixed RLUSD chunk when price dips to it.
- After a level buys q XRP for cost C at price b, a take-profit sell is placed at t = b*(1+tp_pct).
  It sells only enough XRP to return C to the trading balance plus the savings share of the profit:
      sell_qty = C*(1 + save_share*tp) / t        kept_xrp = q - sell_qty  (> 0)
  So every round trip: trading RLUSD is restored, savings += save_share*C*tp, XRP stack grows by
  roughly (1-save_share)*C*tp / t.
- When the level's sell fills, the level re-arms its buy.
- Trailing anchor: if price rises > spacing above the anchor and the top level is idle, the idle
  levels are moved up under the new price (so it keeps scalping in up-trends instead of idling).
- Re-center rule (`recenter_mode`):
    "off"   : static ladder (default).
    "trail" : idle levels jump up as soon as price is > 1 spacing above the anchor.
    "range" : idle levels move up only after price has been RANGE-BOUND: over the last
              `range_days` days, (highest high - lowest low) / lowest low <= `range_pct`%,
              AND price is > 1 spacing above the anchor (ladder has fallen behind),
              AND at least `recenter_cooldown_h` hours since the last re-center.
              New anchor = current price. Levels holding XRP keep their sell targets.
  Re-centering only ever moves idle buy levels up; nothing is sold to do it.
- Optional `core_pct` of the budget is bought as XRP up front and never sold.
- Reserves (1 XRP base + 0.2 trust line + 0.2 per open offer) are bought up front and counted
  as XRP (they are locked, not lost).
"""

def new_state(price, cfg):
    n = cfg["levels"]
    reserve_xrp = cfg.get("base_reserve_xrp", 1.0) + cfg.get("trustline_reserve_xrp", 0.2) + cfg.get("owner_reserve_xrp", 0.2) * n
    entry = 1 + cfg.get("entry_cost_pct", 0.05) / 100          # taker cost to buy reserve/core XRP up front
    budget = cfg["budget_usd"]
    reserve_usd = reserve_xrp * price * entry
    core_usd = (budget - reserve_usd) * cfg.get("core_pct", 0) / 100
    core_xrp = core_usd / (price * entry)
    trading = budget - reserve_usd - core_usd
    st = {"budget_usd": budget, "start_price": price, "anchor": price, "reserve_xrp": reserve_xrp,
          "core_xrp": core_xrp, "scalp_xrp": 0.0, "kept_xrp": 0.0, "trading_usd": trading,
          "savings_usd": 0.0, "chunk_usd": trading / n, "fees_usd": 0.0, "buys": 0, "sells": 0,
          "round_trips": 0, "reanchors": 0, "bar": 0, "levels": []}
    place_ladder(st, cfg)
    return st

def place_ladder(st, cfg):
    s = cfg["spacing_pct"] / 100
    held = [L for L in st["levels"] if L["state"] == "sell"]
    st["levels"] = held + [{"buy": round(st["anchor"] * (1 - s) ** (i + 1), 6), "state": "buy"}
                           for i in range(cfg["levels"] - len(held))]

def total_xrp(st):
    return st["reserve_xrp"] + st["core_xrp"] + st["scalp_xrp"]

def equity(st, price):
    return st["trading_usd"] + st["savings_usd"] + total_xrp(st) * price

def process(st, path, cfg, ts=None):
    """Walk a price path (one bar). Buys need price <= level*(1-trigger); sells >= target*(1+trigger).
    A level bought in this bar cannot sell until a later bar (no same-candle round trips)."""
    tp = cfg.get("tp_pct", cfg["spacing_pct"]) / 100
    trig = cfg.get("trigger_pct", 0.05) / 100
    fee_pct = cfg.get("extra_cost_pct_per_fill", 0.0) / 100
    txfee_xrp = cfg.get("tx_fee_xrp", 0.00001)
    k = cfg.get("save_share", 0.5)
    ev = []
    st["bar"] += 1
    for p in path:
        for L in st["levels"]:
            if L["state"] == "buy" and p <= L["buy"] * (1 - trig) and st["trading_usd"] >= st["chunk_usd"] * 0.999:
                C = min(st["chunk_usd"], st["trading_usd"])
                fee = C * fee_pct
                q = (C - fee) / L["buy"]
                st["trading_usd"] -= C; st["scalp_xrp"] += q - txfee_xrp
                st["fees_usd"] += fee + txfee_xrp * p; st["buys"] += 1
                t = L["buy"] * (1 + tp)
                sell_qty = C * (1 + k * tp) / (t * (1 - fee_pct))
                L.update(state="sell", cost=C, qty=q, target=round(t, 6), sell_qty=sell_qty, bar=st["bar"])
                ev.append({"ts": ts, "side": "BUY", "price": L["buy"], "xrp": round(q, 6), "rlusd": round(C, 4), "fee_xrp": txfee_xrp, "mkt": round(p, 6)})
            elif L["state"] == "sell" and L["bar"] < st["bar"] and p >= L["target"] * (1 + trig):
                gross = L["sell_qty"] * L["target"]; fee = gross * fee_pct
                net = gross - fee
                save = net - L["cost"]
                st["trading_usd"] += L["cost"]; st["savings_usd"] += save
                st["scalp_xrp"] -= L["sell_qty"] + txfee_xrp
                kept = L["qty"] - L["sell_qty"]; st["kept_xrp"] += kept
                st["fees_usd"] += fee + txfee_xrp * p; st["sells"] += 1; st["round_trips"] += 1
                ev.append({"ts": ts, "side": "SELL", "price": L["target"], "xrp": round(L["sell_qty"], 6),
                           "rlusd": round(gross, 4), "to_savings": round(save, 5), "xrp_kept": round(kept, 6), "fee_xrp": txfee_xrp, "mkt": round(p, 6)})
                L.clear(); L.update(buy=round(ev[-1]["price"] / (1 + tp), 6), state="buy")
        # trailing anchor
        s = cfg["spacing_pct"] / 100
        if recenter_mode(cfg) == "trail" and p > st["anchor"] * (1 + s):
            top = max(st["levels"], key=lambda L: L.get("buy", 0) if L["state"] == "buy" else -1)
            if top["state"] == "buy":
                st["anchor"] = p; st["reanchors"] += 1; place_ladder(st, cfg)
    return ev


def recenter_mode(cfg):
    m = cfg.get("recenter_mode")
    if m is None:                      # backward compat with the old boolean
        m = "trail" if cfg.get("trail", False) else "off"
    return m

def observe(st, cfg, ts_unix, hi, lo, price):
    """Feed one bar's high/low (any bar size) and apply the 'range' re-center rule.
    Keeps hourly buckets in st['range_hist'] so the state stays small for the paper runner."""
    if recenter_mode(cfg) != "range":
        return False
    days = cfg.get("range_days", 3)
    hour = int(ts_unix) // 3600 * 3600
    h = st.setdefault("range_hist", [])
    if h and h[-1][0] == hour:
        h[-1][1] = max(h[-1][1], hi); h[-1][2] = min(h[-1][2], lo)
    else:
        h.append([hour, hi, lo])
    cutoff = hour - days * 86400
    while h and h[0][0] <= cutoff:
        h.pop(0)
    if len(h) < days * 24 - 1:          # need (almost) the full window of history
        return False
    hh = max(x[1] for x in h); ll = min(x[2] for x in h)
    s = cfg["spacing_pct"] / 100
    last = st.get("last_recenter_unix", -1e18)
    if ((hh - ll) / ll * 100 <= cfg.get("range_pct", 12) and price > st["anchor"] * (1 + s)
            and ts_unix - last >= cfg.get("recenter_cooldown_h", 24) * 3600):
        st["anchor"] = price; st["reanchors"] += 1; st["last_recenter_unix"] = ts_unix
        place_ladder(st, cfg)
        return True
    return False

def topup(st, usd):
    """Add new RLUSD to the trading balance and grow every level's chunk evenly."""
    st["trading_usd"] += usd
    st["chunk_usd"] += usd / max(1, len(st["levels"]))
    st["budget_usd"] += usd
