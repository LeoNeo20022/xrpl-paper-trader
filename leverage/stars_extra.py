"""PAPER-ONLY extra 10x XRP lines next to Stars Aligned (user-approved 2026-10-27, paper only). No keys, no orders, no wallets.
Same model as stars.py: XRPUSDT 10x isolated, TP +3% / stop -1.5% price move, ta.py fees/slippage/funding/liquidation, $50/$100/$500.
Backtests: stars_fingerprint/ (fingerprints.md). Lines (each one position at a time, signals logged to stars_extra_log.csv):
- f2       LONG  'squeeze': crowded shorts, OR open interest +5% in 24h with the last 4h close above the 4h EMA200. Checked on hour closes.
- f3       SHORT 'failed pullback': Casey's effective call is LONG (his uptrend-pullback trigger) but funding < +0.03%/8h. Hour closes.
- popfade  SHORT Pip's 'pop fade': XRP +3% or more in 24h, 1h RSI >= 65, funding > 0, Fear & Greed >= 55; allowed above the 4h EMA200.
           RETIRED Oct 26 2026 (lost in all 3 backtest periods, 27-35% wins vs 36% break-even): no new entries or signal logs; its record is kept.
           Pop fade still feeds Pip's stand-in inside starsg.
- starsg   Stars variant (4 of 4, every 15-min round like Stars): Stars stand-ins (stars.standins), plus
           Theo's guarded stand-in: LONG when OI +5% in 24h AND (funding -0.01..+0.03%/8h OR crowded shorts); his normal SHORT calls are kept;
           otherwise IDLE (his unguarded trend LONG becomes IDLE);
           Pip's stand-in: SHORT on his existing rule (below the 4h EMA200 + crowded longs stalling) OR on pop fade.
           Real votes always override stand-ins. The original Stars line (com_xrp_10x_stars_*) is unchanged for comparison."""
import committee, stars

LINES = {"f2": "squeeze LONG (crowded shorts, or OI +5% above the 4h EMA200)",
         "f3": "failed-pullback SHORT (Casey long trigger, funding < 0.03%)",
         "popfade": "Pip pop-fade SHORT (FLAGGED WEAK in backtests)",
         "starsg": "Stars 4/4 with Theo guarded + Pip pop-fade stand-ins"}
HOURLY = {"f2", "f3", "popfade"}
RETIRED = {"popfade": "retired Oct 26: lost in all 3 periods"}   # no new entries, no signal logging; record kept

def name(line, b): return f"com_xrp_10x_{line}_{b}"

def feats(ctx, t, cr, trend):
    k = ctx.hour_idx(t)
    return {"p24": trend.get("p24"), "rsi1h": ctx.rsi[k] if k is not None else None, "funding_pct": (cr or {}).get("funding_pct"),
            "fng": (cr or {}).get("fng"), "oi24": (cr or {}).get("oi_24h_pct"), "crowded": (cr or {}).get("crowded"), "e4": trend.get("ema200_4h")}

def popfade(f):
    return (f["p24"] is not None and f["p24"] >= 3 and f["rsi1h"] is not None and f["rsi1h"] >= 65
            and f["funding_pct"] is not None and f["funding_pct"] > 0 and f["fng"] is not None and f["fng"] >= 55)

def theo_guard(f):
    fp = f["funding_pct"]
    return f["oi24"] is not None and f["oi24"] >= 5 and ((fp is not None and -0.01 <= fp <= 0.03) or f["crowded"] == "shorts")

def guarded_calls(scalls, f):
    out = dict(scalls); th = out.get("theo")
    if th and th.get("proxy"):
        if theo_guard(f): out["theo"] = dict(th, call="LONG", confidence=None, note="starsg Theo guard: OI +5% + funding calm / crowded shorts", standin=True)
        elif th["call"] != "SHORT": out["theo"] = dict(th, call="IDLE", confidence=None, note="starsg Theo guard: no guarded LONG", standin=th["call"] == "LONG")
    p = out.get("pip")
    if p and p.get("proxy") and popfade(f) and p["call"] != "SHORT":
        out["pip"] = dict(p, call="SHORT", confidence=None, note=f"starsg Pip pop fade: 24h {f['p24']:+.1f}%, RSI {f['rsi1h']:.0f}, funding {f['funding_pct']}%, F&G {f['fng']}", standin=True)
    return out

def signals(t, calls, scalls, f):
    """{line: (side, calls_used or None, why)} for this round."""
    out = {}
    if t % 3600 == 0:
        if f["crowded"] == "shorts" or (f["oi24"] is not None and f["oi24"] >= 5 and f["e4"] == "above"):
            out["f2"] = ("LONG", None, f"crowded {f['crowded']}, OI 24h {f['oi24']}%, 4h vs EMA200 {f['e4']}")
        c = calls.get("casey")
        if c and c["call"] == "LONG" and f["funding_pct"] is not None and f["funding_pct"] < 0.03:
            out["f3"] = ("SHORT", None, f"Casey LONG ({'proxy' if c.get('proxy') else 'real'}), funding {f['funding_pct']}%")
        if popfade(f) and "popfade" not in RETIRED:
            out["popfade"] = ("SHORT", None, f"24h {f['p24']:+.1f}%, RSI {f['rsi1h']:.0f}, funding {f['funding_pct']}%, F&G {f['fng']}")
    g = guarded_calls(scalls, f); side = stars.unanimous(g)
    if side: out["starsg"] = (side, g, "4/4 " + "/".join(g[v]["call"] for v in ("casey", "pip", "theo", "remy")))
    return out
