"""PAPER-ONLY: show every XRPL line at $100 (as run) and scaled to $500, side by side, in SUMMARY.md.
The $100 lines are not touched. $500 = the $100 result x5, minus extra price impact for 5x larger orders, sized from the
LIVE XRP/RLUSD AMM pool depth (public amm_info, no keys): a market order of q dollars against a constant-product pool with
R dollars on the far side moves the price by about q/R, so its cost is about q^2/R. Extra at $500 = sum over fills of
(5q)^2/R - 5*q^2/R = 20*q^2/R. Grid limit orders fill at their price, but depth still matters for them, so all fills are
charged (conservative). Worst drawdown = biggest peak-to-trough drop of the line's value in its tick log (x5 at $500).
The leveraged perp grid (lev_2x/lev_5x) is modelled on Binance XRPUSDT, where $2,500 of notional is far inside top-of-book: no
extra slippage. Writes a block between SIZES markers in SUMMARY.md."""
import csv, json, os, urllib.request
ROOT = os.path.dirname(os.path.abspath(__file__))
BEGIN, END = "<!-- SIZES:BEGIN -->", "<!-- SIZES:END -->"
CFG = json.load(open(os.path.join(ROOT, "config.json")))
LINES = [("dip_ladder", "logs"), ("scalp_2pct", "logs"), ("scalp_2pct_rlusd", "logs"), ("xrp_stacker", "logs"), ("xrp_stacker_6pct", "logs"),
         ("amm_lp", "logs"), ("lev_2x", "leverage/logs"), ("lev_5x", "leverage/logs")]

def pool_depth():
    body = json.dumps({"method": "amm_info", "params": [{"amm_account": CFG["amm_lp"]["amm_account"], "ledger_index": "validated"}]}).encode()
    for node in ("https://xrplcluster.com", "https://s1.ripple.com:51234", "https://s2.ripple.com:51234"):
        try:
            r = json.loads(urllib.request.urlopen(urllib.request.Request(node, body, {"Content-Type": "application/json"}), timeout=20).read())["result"]["amm"]
            xrp = int(r["amount"]) / 1e6 if isinstance(r["amount"], str) else float(r["amount"]["value"])
            usd = float(r["amount2"]["value"]) if isinstance(r["amount2"], dict) else int(r["amount2"]) / 1e6
            return xrp, usd, node
        except Exception as e: print("amm_info", node, str(e)[:80])
    return None, None, None

def rows(path):
    try: return list(csv.DictReader(open(path)))
    except FileNotFoundError: return []

def main():
    pxrp, pusd, node = pool_depth()
    R = pusd if pusd else None
    L = [BEGIN, "## Every XRPL line at $100 vs $500 (PAPER; $100 is what actually ran, $500 is scaled)", "",
         f"$500 = the $100 result x5 minus extra price impact for 5x larger orders, using live XRP/RLUSD AMM depth "
         + (f"(pool {pxrp:,.0f} XRP / {pusd:,.0f} RLUSD from {node})" if R else "(pool depth unavailable this run: no extra charged)")
         + ". Worst drawdown = biggest drop from a high point in the line's history. Profit is after fees.", "",
         "| Line | **$100: profit** | $100: worst drawdown | **$500: profit** | $500: worst drawdown | Extra cost at $500 (depth) |", "|---|---|---|---|---|---|"]
    for name, d in LINES:
        t = rows(os.path.join(ROOT, d, f"{name}_ticks.csv"))
        if not t: continue
        v = [float(r["value_usd"]) for r in t if r.get("value_usd")]
        start = float(t[0].get("budget_usd") or 100)
        peak, dd = v[0], 0.0
        for x in v: peak = max(peak, x); dd = max(dd, peak - x)
        prof = v[-1] - start
        fills = rows(os.path.join(ROOT, d, f"{name}_fills.csv"))
        q = [float(f["rlusd"]) for f in fills if f.get("rlusd")]
        if name == "amm_lp": q = []        # two-sided deposit at the pool ratio: no price impact
        extra = sum(20 * x * x / R for x in q) if R and not name.startswith("lev_") else 0.0
        L.append(f"| `{name}` | **{prof:+.2f}** | -{dd:.2f} | **{prof * 5 - extra:+.2f}** | -{dd * 5:.2f} | ${extra:.4f} ({len(q)} fills) |")
    L += ["", "Leverage TA and committee lines run real $50/$100/$500 twins; see their sections below.", END]
    md = "\n".join(L) + "\n"
    p = os.path.join(ROOT, "SUMMARY.md"); s = open(p).read()
    if BEGIN in s: s = s[:s.index(BEGIN)].rstrip("\n") + "\n" + (s[s.index(END) + len(END):].lstrip("\n") if END in s else "")
    open(p, "w").write(s.rstrip("\n") + "\n\n" + md); print(md)

if __name__ == "__main__":
    main()
