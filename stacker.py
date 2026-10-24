"""XRP stacker: sell-high / buy-back-lower ladder whose only goal is MORE XRP (PAPER ONLY: no keys, no orders).

How it works
- Starts 100% in XRP (the same XRP count as 'keep $100 in XRP'). 1 + 0.2 + 0.2*levels XRP is ledger reserve (locked) and never sold.
- Costs: fee_pct_per_fill (default 0.25% = AMM 0.205% + ~0.045% slippage) on every fill, plus the XRPL network fee on every
  OfferCreate / OfferCancel / TrustSet.
- From a reference price `ref`, `levels` sell slices sit at ref*(1+s)^1 .. ref*(1+s)^N (s = spacing_pct).
  Each slice is `slice_pct`% of the sellable stack at the time the ladder is (re)built.
- When price reaches a slice's sell price S, that slice of XRP is sold for RLUSD (fee charged).
- The RLUSD is only PARKED: a buy-back is placed at B = S/(1+s) using ALL of that RLUSD.
  One completed round trip: q XRP -> q*S*(1-f) RLUSD -> q*(1+s)*(1-f)^2 XRP, i.e. ~+2.5% more XRP on that slice
  at s=3%, f=0.25%. No RLUSD profit is ever banked.
- After a buy-back the slice re-arms its sell at S again with its (bigger) XRP quantity.
- Trail down: when every slice holds XRP (nothing parked) and price is >= 1 spacing below ref, the ladder is rebuilt
  at the current price (slices re-sized to the current stack, so gains compound). This keeps it cycling in down-trends.
- Time fallback: a slice parked in RLUSD for more than `max_park_days` is bought back at market (taker fee), which
  can LOCK IN FEWER XRP. Then, once nothing is parked, the ladder is rebuilt at the current price.
  Risk: in a sustained rally this strategy ends with fewer XRP than simply holding.
"""

def new_state(price, cfg):
    entry = 1 + cfg.get("entry_cost_pct", 0.05) / 100
    xrp = cfg["budget_usd"] / (price * entry)
    st = {"budget_usd": cfg["budget_usd"], "start_price": price, "start_xrp": xrp, "xrp": xrp, "parked_usd": 0.0,
          "reserve_xrp": cfg.get("base_reserve_xrp", 1.0) + cfg.get("trustline_reserve_xrp", 0.2) + cfg.get("owner_reserve_xrp", 0.2) * cfg["levels"],
          "ref": price, "levels": [], "buys": 0, "sells": 0, "round_trips": 0, "forced_rebuys": 0,
          "xrp_gained_trips": 0.0, "xrp_lost_forced": 0.0, "fees_xrp": 0.0, "reanchors": 0, "bar": 0,
          "fees_usd": cfg["budget_usd"] - xrp * price, "net_fees_xrp": 0.0}   # fees_usd starts with the 0.05% taker cost of the initial buy
    netfee(st, cfg, 1)   # TrustSet for RLUSD
    build(st, cfg, price)
    return st

def netfee(st, cfg, n):
    f = n * cfg.get("tx_fee_xrp", 0.00002); st["xrp"] -= f; st["net_fees_xrp"] += f; st["fees_xrp"] += f

def build(st, cfg, price):
    """(Re)build the sell ladder: OfferCancel for each resting sell + OfferCreate for each new one (network fee each)."""
    netfee(st, cfg, sum(L["state"] == "sell" for L in st["levels"]) + cfg["levels"])
    s = cfg["spacing_pct"] / 100
    sellable = max(0.0, st["xrp"] - st["reserve_xrp"])
    q = sellable * cfg["slice_pct"] / 100
    st["ref"] = price
    st["levels"] = [{"i": i + 1, "sell": round(price * (1 + s) ** (i + 1), 6), "buy": round(price * (1 + s) ** i, 6),
                     "qty": q, "state": "sell"} for i in range(cfg["levels"])]

def total_xrp(st): return st["xrp"]
def parked_usd(st): return st["parked_usd"]

def process(st, path, cfg, ts=None, ts_unix=None):
    s = cfg["spacing_pct"] / 100
    f = (cfg.get("fee_pct_per_fill", 0.25) + cfg.get("extra_cost_pct_per_fill", 0.0)) / 100
    trig = cfg.get("trigger_pct", 0.05) / 100
    tx = cfg.get("tx_fee_xrp", 0.00001)
    max_park = cfg.get("max_park_days", 7) * 86400
    ev = []; st["bar"] += 1
    for p in path:
        for L in st["levels"]:
            if L["state"] == "sell" and p >= L["sell"] * (1 + trig) and st["xrp"] - L["qty"] >= st["reserve_xrp"]:
                gross = L["qty"] * L["sell"]; net = gross * (1 - f)
                st["xrp"] -= L["qty"] + tx; st["parked_usd"] += net; st["fees_xrp"] += tx; st["sells"] += 1
                st["fees_usd"] += gross * f; st["net_fees_xrp"] += tx
                L.update(state="buy", usd=net, sold_qty=L["qty"], bar=st["bar"], parked_since=ts_unix)
                ev.append({"ts": ts, "side": "SELL", "price": L["sell"], "xrp": round(L["qty"], 6), "rlusd": round(gross, 4),
                           "fee_xrp": tx, "mkt": round(p, 6), "step_pct": round(L["i"] * cfg["spacing_pct"], 2)})
            elif L["state"] == "buy" and L["bar"] < st["bar"] and p <= L["buy"] * (1 - trig):
                q = L["usd"] * (1 - f) / L["buy"]
                gain = q - L["sold_qty"] - 2 * tx
                st["xrp"] += q - tx; st["parked_usd"] -= L["usd"]; st["fees_xrp"] += tx
                st["fees_usd"] += L["usd"] * f; st["net_fees_xrp"] += tx
                st["buys"] += 1; st["round_trips"] += 1; st["xrp_gained_trips"] += gain
                ev.append({"ts": ts, "side": "BUY", "price": L["buy"], "xrp": round(q, 6), "rlusd": round(L["usd"], 4),
                           "fee_xrp": tx, "xrp_kept": round(gain, 6), "mkt": round(p, 6), "step_pct": round(L["i"] * cfg["spacing_pct"], 2)})
                L.update(state="sell", qty=q); [L.pop(k, None) for k in ("usd", "sold_qty", "bar", "parked_since")]
        if ts_unix is not None:   # time fallback: buy back at market (taker) after max_park_days
            for L in st["levels"]:
                if L["state"] == "buy" and L.get("parked_since") is not None and ts_unix - L["parked_since"] > max_park:
                    px = p * (1 + f); q = L["usd"] / px; loss = q - L["sold_qty"] - 2 * tx
                    st["xrp"] += q - tx; st["parked_usd"] -= L["usd"]; st["fees_xrp"] += tx
                    st["fees_usd"] += L["usd"] * f / (1 + f); st["net_fees_xrp"] += tx + cfg.get("tx_fee_xrp", 0.00002); st["xrp"] -= cfg.get("tx_fee_xrp", 0.00002)  # + OfferCancel of the resting buy-back
                    st["buys"] += 1; st["forced_rebuys"] += 1; st["xrp_lost_forced"] += loss
                    ev.append({"ts": ts, "side": "BUY", "price": round(px, 6), "xrp": round(q, 6), "rlusd": round(L["usd"], 4),
                               "fee_xrp": tx, "xrp_kept": round(loss, 6), "mkt": round(p, 6), "step_pct": "timeout"})
                    L.update(state="sell", qty=q); [L.pop(k, None) for k in ("usd", "sold_qty", "bar", "parked_since")]
                    st["_rebuild"] = True
        if all(L["state"] == "sell" for L in st["levels"]):
            if p <= st["ref"] * (1 - s) or st.get("_rebuild"):
                st.pop("_rebuild", None); st["reanchors"] += 1; build(st, cfg, p)
    return ev
