#!/usr/bin/env python3
"""One-off (2026-10-24): rebuild the grid paper history from Bitstamp 5-min candles after two bad XRPL book reads
(mid $0.646 on 2026-10-20 08:54 UTC, $0.679 on 2026-10-22 21:22 UTC) caused phantom fills.
Each historical tick is replayed in order: candles closed by that tick, then that tick's XRPL mid ONLY if it passes the
sanity guard (0 < spread < 2%) and is within 1% of the latest Bitstamp close. amm_lp is untouched. PAPER ONLY."""
import csv, json, os, shutil, time
from datetime import datetime
import paper_runner as R

import sys
TAG = sys.argv[1] if len(sys.argv) > 1 else "archive_phantom_2026-10-24"   # 2nd use: archive_resize_2026-10-24 ($100 per strategy)
REPLAYED = list(R.CFG["strategies"].keys())          # dip_ladder, scalp_2pct, scalp_2pct_rlusd
SA, LA = os.path.join(R.SDIR, TAG), os.path.join(R.LDIR, TAG)

def main():
    os.makedirs(SA, exist_ok=True); os.makedirs(LA, exist_ok=True)
    ms = R.load(R.MARKET_STATE); shutil.copy2(R.MARKET_STATE, SA)
    old_sum = list(csv.DictReader(open(os.path.join(R.LDIR, "summary.csv"))))
    old_tax = list(csv.DictReader(open(R.TAX)))
    for f in ("summary.csv", "tax_export.csv"): shutil.copy2(os.path.join(R.LDIR, f), LA)
    for n in REPLAYED:
        sp = os.path.join(R.SDIR, f"{n}.json")
        if os.path.exists(sp): shutil.move(sp, SA)
        for k in ("fills", "ticks"):
            lp = os.path.join(R.LDIR, f"{n}_{k}.csv")
            if os.path.exists(lp): shutil.move(lp, LA)
    # tax export: keep only lines that are not replayed (amm_lp); replay re-adds the rest
    with open(R.TAX, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=R.TAX_FIELDS); w.writeheader()
        w.writerows(r for r in old_tax if r["Strategy"] not in REPLAYED)
    os.remove(os.path.join(R.LDIR, "summary.csv"))

    taker = 1 + R.CFG.get("taker_cost_pct", 0.05) / 100
    start = datetime.fromisoformat(ms["started"]).timestamp()
    ticks = [(datetime.fromisoformat(r["ts"]).timestamp(), r) for r in old_sum]
    last_tick = ticks[-1][0]
    hist = R.candles_between(int(start) // 300 * 300 - 300, int(last_tick), time.time())
    hist = [c for c in hist if c[0] + 300 <= last_tick]
    states = {}
    for n, sc in R.CFG["strategies"].items():
        states[n] = R.init_strategy(n, sc, ms["start_mid"], start, ms["started"])
    ci, last_c, used, skipped, out_rows = 0, None, 0, [], []
    for T, old in ticks:
        batch = []
        while ci < len(hist) and hist[ci][0] + 300 <= T:
            batch.append(hist[ci]); ci += 1
        if batch: last_c = batch[-1]
        ref = last_c[1][-1] if last_c else None
        mid, spread = float(old["xrpl_mid"]), float(old["spread_pct"])
        ok = R.book_mid_ok(mid, spread, ref)
        if ok: used += 1
        else: skipped.append((old["ts"], mid, spread, ref))
        val_mid = mid if ok or ref is None else ref
        rows = []
        for n, sc in R.CFG["strategies"].items():
            ev, x, usd, fills, sells, extra = R.run_strategy(n, sc, states[n], batch, {"mid": mid if ok else None, "ref": val_mid}, T, old["ts"])
            row = R.tick_row(n, sc, states[n], ev, x, usd, fills, sells, extra, old["ts"], val_mid, taker)
            R.append(os.path.join(R.LDIR, f"{n}_ticks.csv"), row, list(row.keys())); rows.append(row)
        srow = R.build_srow(old["ts"], val_mid, spread, len(batch), rows, ms)
        for k, v in old.items():                               # carry the untouched amm_lp columns
            if k.startswith("amm_lp_") and v != "": srow[k] = v
        if old.get("amm_lp_value_usd"): srow["amm_lp_vs_xrp_usd"] = round(float(old["amm_lp_value_usd"]) - float(srow["baseline_xrp_value_usd"]), 4)
        out_rows.append(srow)
    fields = list(dict.fromkeys(k for r in out_rows[::-1] for k in r))
    with open(os.path.join(R.LDIR, "summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out_rows)
    for n in REPLAYED: states[n]["replayed"] = "2026-10-24"; R.save(os.path.join(R.SDIR, f"{n}.json"), states[n])
    if last_c: ms["last_candle_ts"] = last_c[0]; ms["last_close"] = last_c[1][-1]
    ms["replayed"] = {"on": "2026-10-24", "ticks": len(ticks), "candles": ci, "book_mids_used": used, "book_mids_rejected": len(skipped)}
    R.save(R.MARKET_STATE, ms)
    print(json.dumps(ms["replayed"]), "rejected:", skipped)
    print({n: (out_rows[-1][f"{n}_value_usd"], out_rows[-1][f"{n}_fills"]) for n in REPLAYED})

if __name__ == "__main__":
    main()
