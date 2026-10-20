"""Buy-only weekly dip ladder for XRP/RLUSD (PAPER ONLY: no keys, no orders).
Every `refresh_days` the ladder is reset: unfilled orders are cancelled and ALL unspent RLUSD is
split evenly across limit buys at -2/-4/-6/-8/-10% (configurable) below the current price.
It never sells XRP. Reserve XRP (1 base + 0.2 trust line + 0.2 per open offer) is bought up front
from the budget and counted as XRP held (it is locked, not lost)."""

def new_state(price, cfg, now_unix):
    steps = cfg["steps_pct"]
    reserve_xrp = cfg.get("base_reserve_xrp", 1.0) + cfg.get("trustline_reserve_xrp", 0.2) + cfg.get("owner_reserve_xrp", 0.2) * len(steps)
    entry = 1 + cfg.get("entry_cost_pct", 0.05) / 100
    reserve_usd = reserve_xrp * price * entry
    st = {"budget_usd": cfg["budget_usd"], "start_price": price, "reserve_xrp": reserve_xrp, "reserve_cost_usd": reserve_usd,
          "xrp": 0.0, "cash_usd": cfg["budget_usd"] - reserve_usd, "orders": [], "ref": None,
          "next_refresh_unix": now_unix, "refreshes": 0, "buys": 0, "sells": 0, "fees_xrp": 0.0}
    return st

def maybe_refresh(st, cfg, now_unix, price):
    if now_unix < st["next_refresh_unix"]:
        return False
    free = st["cash_usd"] + sum(o["usd"] for o in st["orders"])
    steps = cfg["steps_pct"]
    st["orders"] = [{"price": round(price * (1 - s / 100), 6), "usd": free / len(steps), "step_pct": s} for s in steps] if free > 0.01 else []
    st["cash_usd"] = 0.0 if st["orders"] else free
    st["ref"] = price; st["refreshes"] += 1
    st["next_refresh_unix"] = now_unix + cfg.get("refresh_days", 7) * 86400
    return True

def process(st, path, cfg, ts=None):
    trig = cfg.get("trigger_pct", 0.05) / 100; fee = cfg.get("tx_fee_xrp", 0.00001)
    ev = []
    for p in path:
        keep = []
        for o in st["orders"]:
            if p <= o["price"] * (1 - trig):
                q = o["usd"] / o["price"]
                st["xrp"] += q - fee; st["fees_xrp"] += fee; st["buys"] += 1
                ev.append({"ts": ts, "side": "BUY", "price": o["price"], "xrp": round(q, 6), "rlusd": round(o["usd"], 4),
                           "fee_xrp": fee, "mkt": round(p, 6), "step_pct": o["step_pct"]})
            else:
                keep.append(o)
        st["orders"] = keep
    return ev

def total_xrp(st):
    return st["xrp"] + st["reserve_xrp"]

def unspent_usd(st):
    return st["cash_usd"] + sum(o["usd"] for o in st["orders"])
