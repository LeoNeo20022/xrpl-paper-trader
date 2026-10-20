"""Shared grid logic for XRP/RLUSD paper trading (simulation only, no wallet, no orders)."""
import math

def make_levels(lo, hi, spacing_pct):
    """Geometric levels from lo to hi, spacing_pct apart."""
    r = 1 + spacing_pct / 100
    n = int(math.floor(math.log(hi / lo) / math.log(r))) + 1
    return [round(lo * r ** i, 6) for i in range(n)]

def init_state(levels, price, budget_usd, entry_cost_pct=0.05, owner_reserve_xrp=0.2,
               base_reserve_xrp=1.0, trustline_reserve_xrp=0.2):
    """Classic grid: one 'slot' between each pair of adjacent levels.
    Slots fully below price start as BUY orders (hold USD); slots above start as SELL (hold XRP).
    Reserve XRP (base + trust line + 0.2 per open offer) is set aside first, bought at entry."""
    n_slots = len(levels) - 1
    reserve_xrp = base_reserve_xrp + trustline_reserve_xrp + owner_reserve_xrp * n_slots
    reserve_usd = reserve_xrp * price * (1 + entry_cost_pct / 100)
    tradable = budget_usd - reserve_usd
    per_slot = tradable / n_slots
    slots, usd, xrp, cost = [], 0.0, 0.0, 0.0
    for i in range(n_slots):
        buy, sell = levels[i], levels[i + 1]
        if sell <= price or (buy < price < sell and price - buy > sell - price):
            # price above this slot -> wait to buy at `buy`
            slots.append({"buy": buy, "sell": sell, "side": "buy", "qty": per_slot / buy})
            usd += per_slot
        else:
            # price below/at slot -> hold XRP, wait to sell at `sell`
            q = per_slot / price / (1 + entry_cost_pct / 100)
            cost += per_slot - q * price
            slots.append({"buy": buy, "sell": sell, "side": "sell", "qty": q})
            xrp += q
    return {"slots": slots, "usd": usd, "xrp": xrp, "reserve_xrp": reserve_xrp,
            "entry_cost_usd": cost + reserve_usd - reserve_xrp * price,
            "realized_usd": 0.0, "fees_usd": 0.0, "fills": 0, "round_trips": 0,
            "budget_usd": budget_usd, "start_price": price}

def step(state, price_path, fee_pct=0.0, tx_fee_xrp=0.00001, trigger_pct=0.0, ts=None):
    """Walk a sequence of prices; fill a buy when price <= buy*(1-trigger), a sell when
    price >= sell*(1+trigger). Each fill flips the slot. Returns list of fill events."""
    events = []
    for p in price_path:
        for s in state["slots"]:
            if s["side"] == "buy" and p <= s["buy"] * (1 - trigger_pct / 100):
                cost = s["qty"] * s["buy"]
                fee = cost * fee_pct / 100 + tx_fee_xrp * p
                state["usd"] -= cost + fee; state["xrp"] += s["qty"]
                state["fees_usd"] += fee; state["fills"] += 1
                s["side"] = "sell"; s["cost_basis"] = cost + fee
                events.append({"ts": ts, "side": "BUY", "price": s["buy"], "qty": round(s["qty"], 6),
                               "usd": round(cost, 4), "fee_usd": round(fee, 6), "mkt": round(p, 6)})
            elif s["side"] == "sell" and p >= s["sell"] * (1 + trigger_pct / 100):
                proceeds = s["qty"] * s["sell"]
                fee = proceeds * fee_pct / 100 + tx_fee_xrp * p
                state["usd"] += proceeds - fee; state["xrp"] -= s["qty"]
                state["fees_usd"] += fee; state["fills"] += 1
                if "cost_basis" in s:
                    state["realized_usd"] += proceeds - fee - s.pop("cost_basis")
                    state["round_trips"] += 1
                # re-size so the next buy uses the same USD (keeps it simple: same qty)
                s["side"] = "buy"
                events.append({"ts": ts, "side": "SELL", "price": s["sell"], "qty": round(s["qty"], 6),
                               "usd": round(proceeds, 4), "fee_usd": round(fee, 6), "mkt": round(p, 6)})
    return events

def equity(state, price):
    return state["usd"] + (state["xrp"] + state["reserve_xrp"]) * price
