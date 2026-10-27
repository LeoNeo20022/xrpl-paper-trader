"""PAPER-ONLY 'Stars Aligned' curiosity line: XRP at 10x, long or short, ONLY when all 4 team voters agree (4 of 4).
No keys, no orders, no wallets. Offshore-rules paper only (Binance-style XRPUSDT perp, isolated margin); Kraken US's XRP perp
(17% maintenance margin) cannot do 10x.

- Votes: the same effective calls as the team committee (a teammate's own row in votes.csv if valid, else its automated proxy,
  committee.proxy_votes). Opens only on 4/4 LONG or 4/4 SHORT, if flat. Every other line keeps the 3-of-4 rule.
- Exits: take profit +3% price move (~ +30% on margin), stop -1.5% price move (user-approved 2026-10-27, maker 0.02%, needs a 0.05% trade-through), stop -1% price
  move (stop-market, taker 0.05% + 0.05% slippage; a gap fills at the open). One position at a time.
- Costs, 8-hourly funding (both directions) and liquidation (margin + P/L <= 0.5% maintenance of notional, whole margin lost)
  are the ta.py engine used by every leverage line.
- No news/event blackout (removed 2026-10-27 so the line is free to short a sell-the-news dump).
- Stars-only stand-ins (used ONLY for this line's 4/4 check; the 3-of-4 committee and its proxies are unchanged; real votes override):
  Casey's proxy votes SHORT instead of IDLE when the last closed 4h candle is below the 4h EMA200 AND crowding flags crowded longs.
  Pip's proxy votes LONG instead of IDLE when the last closed 4h candle is above the 4h EMA200, crowding is clear (not crowded
  either way) AND funding is calm (known and between -0.01% and +0.03% per 8h, i.e. inside both crowding funding thresholds).
- Paper sizes $50, $100, $500: com_xrp_10x_stars_50 / _100 / _500."""
import csv, os
from datetime import datetime, timezone
import ta, committee

NEWS_DEFAULT = "/home/box/shared/strategy-lab/xrp-news-events.csv"
LEV, TP_PCT, STOP_PCT, BLACKOUT_H = 10, 3.0, 1.5, 3   # TP +3% / stop -1.5% (user-approved 2026-10-27); BLACKOUT_H kept only for reference, blackout removed
BUDGETS = (50, 100, 500)


def name(b): return f"com_xrp_10x_stars_{b}"

def cfg(common, budget, tp=None, stop=None):
    return dict(common, leverage=LEV, mmr_pct=common["mmr_pct"]["XRPUSDT"] if isinstance(common["mmr_pct"], dict) else common["mmr_pct"],
                budget_usd=budget, quick_tp_pct=tp or TP_PCT, quick_stop_pct=stop or STOP_PCT, quick_tp_min_lev=0)

def breakeven(common, tp=None, stop=None):
    """Fees-only break-even win rate: one TP win vs one stop loss at 10x on $100 (no funding, no gaps). Returns (win, loss, rate)."""
    c = cfg(common, 100, tp, stop); r = []
    for exit_px in (1.0 + (tp or TP_PCT) / 100 + 0.01, 1.0 - (stop or STOP_PCT) / 100 - 0.01):
        a = ta.new_state(c); ta.step(a, c, 0, [1.0, 1.0], signal(0, 1.0, "LONG", "be", stop), "x"); r += [e["trade_net_usd"] for e in ta.step(a, c, 300, [1.0, exit_px], {}, "y")]
    return r[0], r[1], -r[1] / (r[0] - r[1])

def _ts(s):
    d = datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
    return int((d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp())

def load_news(path=NEWS_DEFAULT):
    """Times of 'high' items in Riley's log. Importance column: first of importance / impact / size that exists."""
    try:
        out = []
        with open(path, newline="") as f:
            rd = csv.DictReader(f)
            col = next((c for c in ("importance", "impact", "size") if c in (rd.fieldnames or [])), None)
            if col is None: print("stars: news log has no importance column, news check skipped"); return []
            for r in rd:
                try:
                    if (r.get(col) or "").strip().lower() == "high": out.append(_ts(r["timestamp_utc"]))
                except Exception: pass
        return out
    except Exception as e:
        print("stars: news log unavailable, news check skipped:", repr(e)); return []

def blackout_times(news_path=NEWS_DEFAULT, use_news=True):
    return sorted(set(committee.EVENTS) | (set(load_news(news_path)) if use_news else set()))

def in_blackout(t, times):
    return any(abs(t - e) < BLACKOUT_H * 3600 for e in times)

def unanimous(calls):
    """calls: {voter: call dict or None}. Returns LONG/SHORT when all 4 agree, else None."""
    cv = [c["call"] if c else "IDLE" for c in calls.values()]
    return cv[0] if len(cv) == 4 and cv[0] in ("LONG", "SHORT") and all(x == cv[0] for x in cv) else None

def signal(t, price, side, why, stop=None):
    """Signal dict for ta.step; atr chosen so stop_atr x atr = STOP_PCT of price (quick stop then gives -1% from the fill)."""
    return {t: {"signal": side, "atr": price * (stop or STOP_PCT) / 100 / 1.5, "trend": "", "why": why}}

def standins(calls, cr, ema200_4h, common):
    """Stars-only stand-ins on top of the normal effective calls. Only touches PROXY IDLE calls of Casey and Pip."""
    out = dict(calls); f = (cr or {}).get("funding_pct"); crowded = (cr or {}).get("crowded")
    c = out.get("casey")
    if c and c.get("proxy") and c["call"] == "IDLE" and ema200_4h == "below" and crowded == "longs":
        out["casey"] = dict(c, call="SHORT", confidence=None, note="stars stand-in: 4h below EMA200 + crowded longs", standin=True)
    p = out.get("pip")
    calm = f is not None and common["crowd_funding_short_pct"] < f < common["crowd_funding_long_pct"]
    if p and p.get("proxy") and p["call"] == "IDLE" and ema200_4h == "above" and not crowded and calm:
        out["pip"] = dict(p, call="LONG", confidence=None, note=f"stars stand-in: 4h above EMA200, crowding clear, funding calm {f}%", standin=True)
    return out
