"""PAPER-ONLY 'committee' strategy: four rule-based voters decide LONG / SHORT / IDLE every 15 minutes on a simulated
Binance perp (XRPUSDT or BTCUSDT), isolated margin. Execution, fees, funding (both directions), slippage and liquidation
reuse ta.py, so results compare 1:1 with leverage_ta. No keys, no orders. Parameters in committee_config.json, fixed up front.

Voters (each returns a vote and a short reason; context = last CLOSED 1h bar + closed 5-min candles):
1. Long scout  : swing uptrend (1h EMA20 > EMA50 and close > EMA50) AND a pullback (5-min RSI14 dipped < 35 in the last 3
                 candles and is now rising) or a reversal (1h MACD histogram < 0 and rising 2 hours in a row). Else IDLE.
2. Short scout : swing downtrend (EMA20 < EMA50 and close < EMA50) AND a bounce (5-min RSI14 > 65 in the last 3 candles and
                 now falling), a breakdown (5-min close below the lowest 1h low of the prior 24 hours), or MACD histogram > 0
                 and falling 2 hours in a row. Else IDLE.
3. Idle guard  : IDLE if choppy (1h ADX14 < 20), wide ATR (1h ATR% > 1.5x its 7-day median), a volatility spike (last 5-min
                 range > 3x 5-min ATR14), funding extreme (|last funding| >= 0.05% per 8h) or within 2h after a stop-out or
                 liquidation. With no red flag it sides with the big trend (EMA50 vs EMA200).
4. Chart reader: 1h fractal swing points (2 bars each side). First RSI divergence at a fresh swing (price lower low + RSI higher
                 low = LONG; higher high + lower RSI high = SHORT), then structure (higher highs + higher lows above EMA50 = LONG;
                 lower highs + lower lows below EMA50 = SHORT), then support/resistance (within 0.5 ATR of the last swing low in a
                 big uptrend = LONG; of the last swing high in a big downtrend = SHORT). Else IDLE.
Decision: >= 3 of 4 agree on LONG or SHORT -> open (if flat). Exactly 2 LONG vs 2 SHORT -> TIE: stay flat, log to ties.csv
and track shadow 'if long' / 'if short' trades (same stops/targets, closed at market after 48h). Anything else -> stay out.
Exits: stop 1.5x 1h ATR14, target 3x ATR14, one position at a time (same as leverage_ta).
Crowding (added 2026-10-26): crowded longs = >= 2 of {funding >= +0.03%/8h, OI (coins) +5% in 24h, long/short account ratio in
the top 20% of its last 7 days}; crowded shorts mirror (funding <= -0.01%, OI +5%, ratio in the bottom 20%). Then the idle guard
refuses to side with the crowd (IDLE, or the opposite big trend), and the opposite scout gets a contrarian trigger that does not
need its swing trend (5-min RSI turning from an extreme, or price across the 1h EMA20). Fear & Greed is a 4th crowding signal
(> 75 greed counts for crowded longs, < 25 fear for crowded shorts) and in extreme greed the long scout needs two triggers (mirror
for the short scout in extreme fear); it is a tilt, never a signal on its own.
Theo's rules R1-R6 (unverified, each toggleable in committee_config.json, fired rules logged per vote): see _theo_note there.
Confidence (for 'mix' sizing): scouts 0.8 with two triggers, 0.6 with one, 0.5 contrarian-only; guard 0.8 if ADX >= 30 else 0.6;
chart reader 0.8 divergence, 0.7 structure, 0.6 support/resistance. Mix = 2x, or 5x when all 4 agree or the agreeing voters average
>= 0.75 confidence with the 1h and 4h trends aligned."""
import bisect, csv, os
from datetime import datetime
import ta

def load_events(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "events_calendar.csv")):
    """Editable CPI/PPI/FOMC calendar (UTC) for Theo's rule 4 news blackout."""
    try: return sorted(int(datetime.fromisoformat(r["datetime_utc"].replace("Z", "+00:00")).timestamp()) for r in csv.DictReader(open(path)))
    except Exception as e: print("events calendar unavailable:", e); return []
EVENTS = load_events()

def wilder(xs, n): return ta.wilder(xs, n)

def rsi_series(cl, n):
    ch = [0.0] + [cl[i] - cl[i - 1] for i in range(1, len(cl))]
    ag, al = wilder([max(x, 0) for x in ch], n), wilder([max(-x, 0) for x in ch], n)
    return [None if g is None else (100.0 if l == 0 else 100 - 100 / (1 + g / l)) for g, l in zip(ag, al)]

def adx_series(bars, n):
    pdm, ndm, tr = [0.0], [0.0], [bars[0][2] - bars[0][3]]
    for i in range(1, len(bars)):
        up, dn = bars[i][2] - bars[i - 1][2], bars[i - 1][3] - bars[i][3]
        pdm.append(up if up > dn and up > 0 else 0.0); ndm.append(dn if dn > up and dn > 0 else 0.0)
        tr.append(max(bars[i][2] - bars[i][3], abs(bars[i][2] - bars[i - 1][4]), abs(bars[i][3] - bars[i - 1][4])))
    a, p, m = wilder(tr, n), wilder(pdm, n), wilder(ndm, n)
    dx = [None if x is None or x == 0 else 100 * abs(pp - mm) / (pp + mm) if (pp + mm) > 0 else 0.0 for x, pp, mm in zip(a, p, m)]
    first = next((i for i, d in enumerate(dx) if d is not None), None)
    out = [None] * len(bars)
    if first is None: return out
    vals = [d for d in dx[first:]]
    sm = wilder(vals, n)
    for i, v in enumerate(sm): out[first + i] = v
    return out

class Context:
    """Precomputed indicators for one coin. c5: [(t, path)] 5-min, bars: [(open_ts, o, h, l, c)] closed 1h, fund: {ts: rate}."""
    def __init__(self, c5, bars, fund, c, crowd=None, fng=None):
        self.c, self.c5, self.bars = c, c5, bars
        self.fng = fng or {}; self.fng_t = sorted(self.fng)
        self.crowd = crowd or {}; self.crowd_t = sorted(self.crowd)
        g = {}
        for b in bars: g.setdefault(b[0] // 14400 * 14400, []).append(b)
        self.b4t = [h for h in sorted(g) if len(g[h]) == 4]; c4 = [g[h][-1][4] for h in self.b4t]
        self.e4_20, self.e4_50, self.e4_200, self.c4 = ta.ema(c4, 20), ta.ema(c4, 50), ta.ema(c4, 200), c4
        self.t5 = [t for t, _ in c5]; cl5 = [p[-1] for _, p in c5]
        self.cl5 = cl5; self.rsi5 = rsi_series(cl5, c["rsi_len"])
        tr5 = [max(p) - min(p) if i == 0 else max(max(p) - min(p), abs(max(p) - cl5[i - 1]), abs(min(p) - cl5[i - 1])) for i, (_, p) in enumerate(c5)]
        self.rng5 = [max(p) - min(p) for _, p in c5]; self.atr5 = wilder(tr5, c["atr_len"])
        self.bt = [b[0] for b in bars]; cl = [b[4] for b in bars]; self.cl = cl
        self.e20, self.e50, self.e200 = ta.ema(cl, c["ema_short"]), ta.ema(cl, c["ema_fast"]), ta.ema(cl, c["ema_slow"])
        self.rsi = rsi_series(cl, c["rsi_len"])
        f, s, g = c["macd"]; m = [a - b for a, b in zip(ta.ema(cl, f), ta.ema(cl, s))]; sig = ta.ema(m, g)
        self.hist = [a - b for a, b in zip(m, sig)]
        tr = [bars[0][2] - bars[0][3]] + [max(bars[i][2] - bars[i][3], abs(bars[i][2] - cl[i - 1]), abs(bars[i][3] - cl[i - 1])) for i in range(1, len(bars))]
        self.atr = wilder(tr, c["atr_len"]); self.adx = adx_series(bars, c["adx_len"])
        W = c["guard_atr_median_hours"]; self.atr_med = [None] * len(bars)
        for i in range(W, len(bars)):
            w = sorted(self.atr[j] / cl[j] for j in range(i - W, i) if self.atr[j] is not None)
            if len(w) > W // 2: self.atr_med[i] = w[len(w) // 2]
        k = c["chart_swing_bars"]; self.sh, self.sl = [], []   # (index, price, rsi)
        for i in range(k, len(bars) - k):
            if all(bars[i][2] > bars[j][2] for j in range(i - k, i + k + 1) if j != i): self.sh.append((i, bars[i][2], self.rsi[i]))
            if all(bars[i][3] < bars[j][3] for j in range(i - k, i + k + 1) if j != i): self.sl.append((i, bars[i][3], self.rsi[i]))
        self.ft = sorted(fund); self.fund = fund

    def trend4h(self, t):
        i = bisect.bisect_right(self.b4t, t - 14400) - 1
        if i < 50: return None
        return "up" if self.e4_20[i] > self.e4_50[i] else "down"

    def ema200_4h(self, t):
        """'above' / 'below' for the last closed 4h bar vs the 4h EMA200 (None until 200 4h bars exist)."""
        i = bisect.bisect_right(self.b4t, t - 14400) - 1
        if i < 200: return None
        return "above" if self.c4[i] > self.e4_200[i] else "below"

    def crowding(self, t, fr):
        """Crowding read with a 1h lag (no look-ahead). Returns dict of metrics + 'longs'/'shorts'/None."""
        c = self.c; h = t // 3600 * 3600 - 3600
        out = {"funding_pct": round(fr * 100, 4) if fr is not None else None, "oi_24h_pct": None, "ls_ratio": None, "ls_pctile": None, "fng": None, "crowded": None}
        fi = bisect.bisect_right(self.fng_t, t - 3600) - 1
        if fi >= 0 and t - self.fng_t[fi] <= 3 * 86400: out["fng"] = self.fng[self.fng_t[fi]]
        if not c.get("crowding", True): return out
        i = bisect.bisect_right(self.crowd_t, h) - 1
        if i >= 0 and h - self.crowd_t[i] <= 3 * 3600:
            now = self.crowd[self.crowd_t[i]]
            past = self.crowd.get(self.crowd_t[i] - c["crowd_oi_hours"] * 3600)
            if now.get("oi") and past and past.get("oi"): out["oi_24h_pct"] = round((now["oi"] / past["oi"] - 1) * 100, 2)
            if now.get("ls"):
                out["ls_ratio"] = round(now["ls"], 3)
                lo = bisect.bisect_left(self.crowd_t, self.crowd_t[i] - c["crowd_ls_window_h"] * 3600)
                hist = [self.crowd[x]["ls"] for x in self.crowd_t[lo:i] if self.crowd[x].get("ls")]
                if len(hist) >= c["crowd_ls_window_h"] // 2: out["ls_pctile"] = round(sum(x < now["ls"] for x in hist) / len(hist) * 100)
        oi_up = out["oi_24h_pct"] is not None and out["oi_24h_pct"] >= c["crowd_oi_rise_pct"]
        greed = out["fng"] is not None and out["fng"] > c["fng_greed_above"]; fear = out["fng"] is not None and out["fng"] < c["fng_fear_below"]
        lg = greed + (fr is not None and fr * 100 >= c["crowd_funding_long_pct"]) + oi_up + (out["ls_pctile"] is not None and out["ls_pctile"] >= c["crowd_ls_pctile_high"])
        sh = fear + (fr is not None and fr * 100 <= c["crowd_funding_short_pct"]) + oi_up + (out["ls_pctile"] is not None and out["ls_pctile"] <= c["crowd_ls_pctile_low"])
        need = c["crowd_min_signals"]
        out["crowded"] = "longs" if lg >= need and lg > sh else "shorts" if sh >= need and sh > lg else None
        out["long_signals"], out["short_signals"] = int(lg), int(sh)
        return out

    def ready(self, t):
        k = self.hour_idx(t); j = self.idx5(t)
        return k is not None and j is not None and k >= self.c["ema_slow"] and self.atr_med[k] is not None and self.adx[k] is not None and self.rsi5[j] is not None and j >= 3

    def hour_idx(self, t):
        i = bisect.bisect_right(self.bt, t - 3600) - 1           # last bar with open <= t-3600 (closed by t)
        return i if i >= 0 and self.bt[i] + 3600 <= t else None

    def idx5(self, t):
        i = bisect.bisect_right(self.t5, t - 300) - 1             # last 5-min candle closed by t
        return i if i >= 0 and self.t5[i] + 300 <= t else None

def votes(ctx, t, last_stop_ts):
    """Returns decision, {voter: (call, reason, confidence)}, atr, crowd metrics, trend info."""
    c = ctx.c; k = ctx.hour_idx(t); j = ctx.idx5(t); cl = ctx.cl[k]; atr = ctx.atr[k]; V = {}
    fi = bisect.bisect_right(ctx.ft, t) - 1; fr = ctx.fund[ctx.ft[fi]] if fi >= 0 else None
    cr = ctx.crowding(t, fr); crowded = cr["crowded"]
    # ---- Theo's rules context (each toggleable; fired rules are logged) ----
    fired = []; T = lambda r: c.get(r, False)
    p24 = (cl / ctx.cl[k - 24] - 1) * 100 if k >= 24 else 0.0; oi24 = cr.get("oi_24h_pct"); fpct = fr * 100 if fr is not None else None
    r1_no_long = r1_no_short = r1_thin = False; healthy = None
    if T("theo_r1_price_oi_funding") and oi24 is not None and fpct is not None:
        if p24 >= c["r1_price_move_pct"] and oi24 >= c["r1_oi_rise_pct"] and fpct >= c["r1_funding_spike_pct"]: r1_no_long = True; fired.append("R1 crowded longs: don't chase")
        if p24 <= -c["r1_price_move_pct"] and oi24 >= c["r1_oi_rise_pct"] and fpct < 0: r1_no_short = True; fired.append("R1 squeeze loading: don't chase shorts")
        if p24 >= c["r1_price_move_pct"] and oi24 <= c["r1_oi_fall_pct"]: r1_thin = True; fired.append("R1 thin rally: lower long confidence")
        if p24 >= c["r1_price_move_pct"] and oi24 > 0 and fpct < c["r1_funding_spike_pct"]: healthy = "up"
        elif p24 <= -c["r1_price_move_pct"] and oi24 > 0 and 0 <= fpct < c["r1_funding_spike_pct"]: healthy = "down"
    r2_no_long = r2_no_short = False
    if T("theo_r2_crowding_veto"):
        ann = fpct * 3 * 365 if fpct is not None else None; ls = cr.get("ls_ratio")
        if (ann is not None and ann > c["r2_funding_ann_pct"]) or (ls is not None and ls > c["r2_ls_high"]): r2_no_long = True
        if (ann is not None and ann < -c["r2_funding_ann_pct"]) or (ls is not None and ls < c["r2_ls_low"]): r2_no_short = True
    e4 = ctx.ema200_4h(t) if T("theo_r3_4h_ema200") else None
    r6 = T("theo_r6_oi_chop") and oi24 is not None and oi24 >= c["r6_oi_rise_pct"] and abs(p24) < c["r6_flat_price_pct"]
    r5 = ctx.rsi5[j - 3:j + 1]
    rsi_up = min(r5[:-1]) < c["scout_rsi5_low"] and r5[-1] > r5[-2]; rsi_dn = max(r5[:-1]) > c["scout_rsi5_high"] and r5[-1] < r5[-2]
    # 1 long scout
    up = ctx.e20[k] > ctx.e50[k] and cl > ctx.e50[k]
    trig = []
    if up and rsi_up: trig.append(f"5m RSI pullback {min(r5[:-1]):.0f}->{r5[-1]:.0f}")
    if up and ctx.hist[k] < 0 and ctx.hist[k] > ctx.hist[k - 1] > ctx.hist[k - 2]: trig.append("MACD turning up")
    greed = cr.get("fng") is not None and cr["fng"] > c["fng_greed_above"]; fear = cr.get("fng") is not None and cr["fng"] < c["fng_fear_below"]
    if trig and r1_no_long: V["long_scout"] = ("IDLE", "R1: price+OI up with funding spiking, not chasing longs", 0)
    elif trig and greed and len(trig) < 2: V["long_scout"] = ("IDLE", f"extreme greed (F&G {cr['fng']}): one trigger not enough", 0)
    elif trig: V["long_scout"] = ("LONG", "uptrend + " + " + ".join(trig), 0.8 if len(trig) > 1 else 0.6)
    elif crowded == "shorts" and (rsi_up or ctx.cl5[j] > ctx.e20[k]): V["long_scout"] = ("LONG", "contrarian: shorts crowded, price turning up", 0.5)
    else: V["long_scout"] = ("IDLE", "no uptrend" if not up else "uptrend, no pullback/reversal", 0)
    # 2 short scout
    dn = ctx.e20[k] < ctx.e50[k] and cl < ctx.e50[k]
    lo24 = min(b[3] for b in ctx.bars[max(0, k - c["breakdown_hours"] + 1):k + 1])
    trig = []
    if dn and rsi_dn: trig.append(f"5m RSI bounce {max(r5[:-1]):.0f}->{r5[-1]:.0f}")
    if dn and ctx.cl5[j] < lo24: trig.append(f"breakdown below 24h low {lo24:.5g}")
    if dn and ctx.hist[k] > 0 and ctx.hist[k] < ctx.hist[k - 1] < ctx.hist[k - 2]: trig.append("MACD turning down")
    if trig and r1_no_short: V["short_scout"] = ("IDLE", "R1: price down + OI up + negative funding = squeeze loading, not chasing shorts", 0)
    elif trig and fear and len(trig) < 2: V["short_scout"] = ("IDLE", f"extreme fear (F&G {cr['fng']}): one trigger not enough", 0)
    elif trig: V["short_scout"] = ("SHORT", "downtrend + " + " + ".join(trig), 0.8 if len(trig) > 1 else 0.6)
    elif crowded == "longs" and (rsi_dn or ctx.cl5[j] < ctx.e20[k]): V["short_scout"] = ("SHORT", "contrarian: longs crowded, price turning down", 0.5)
    else: V["short_scout"] = ("IDLE", "no downtrend" if not dn else "downtrend, no bounce/breakdown", 0)
    # 3 idle guard
    flags = []
    if ctx.adx[k] < c["guard_adx_min"]: flags.append(f"choppy ADX {ctx.adx[k]:.0f}")
    if atr / cl > c["guard_atr_vs_median"] * ctx.atr_med[k]: flags.append(f"wide ATR {atr / cl * 100:.2f}% vs median {ctx.atr_med[k] * 100:.2f}%")
    if ctx.atr5[j - 1] and ctx.rng5[j] > c["guard_spike_atr5"] * ctx.atr5[j - 1]: flags.append("5m volatility spike")
    if fr is not None and abs(fr) * 100 >= c["guard_funding_abs_pct"]: flags.append(f"funding extreme {fr * 100:.3f}%")
    if last_stop_ts is not None and t - last_stop_ts < c["guard_cooldown_h"] * 3600: flags.append("cooldown after stop-out")
    if r6: flags.append(f"R6 OI +{oi24:.1f}%/24h with price flat ({p24:+.1f}%): leverage building in chop"); fired.append("R6 OI chop")
    big = "LONG" if ctx.e50[k] > ctx.e200[k] else "SHORT"
    if big == "LONG" and (r1_no_long or r2_no_long): flags.append("R1/R2: won't side with crowded longs")
    if big == "SHORT" and (r1_no_short or r2_no_short): flags.append("R1/R2: won't side with crowded shorts")
    if flags: V["idle_guard"] = ("IDLE", "; ".join(flags), 0)
    elif crowded == "longs" and big == "LONG": V["idle_guard"] = ("IDLE", "longs crowded: won't join the crowd", 0)
    elif crowded == "shorts" and big == "SHORT": V["idle_guard"] = ("IDLE", "shorts crowded: won't join the crowd", 0)
    else: V["idle_guard"] = (big, f"no red flags, big trend {'up' if big == 'LONG' else 'down'}" + (f", {crowded} crowded" if crowded else ""), 0.8 if ctx.adx[k] >= 30 else 0.6)
    # 4 chart reader
    n = c["chart_swing_bars"]; sh = [x for x in ctx.sh if x[0] + n <= k]; sl = [x for x in ctx.sl if x[0] + n <= k]
    vote = ("IDLE", "no clear structure", 0)
    if len(sl) >= 2 and sl[-1][0] + n >= k - c["chart_div_recent_bars"] and sl[-1][1] < sl[-2][1] and sl[-1][2] > sl[-2][2]:
        vote = ("LONG", "bullish RSI divergence at swing low", 0.8)
    elif len(sh) >= 2 and sh[-1][0] + n >= k - c["chart_div_recent_bars"] and sh[-1][1] > sh[-2][1] and sh[-1][2] < sh[-2][2]:
        vote = ("SHORT", "bearish RSI divergence at swing high", 0.8)
    elif len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] > sh[-2][1] and sl[-1][1] > sl[-2][1] and cl > ctx.e50[k]:
        vote = ("LONG", "higher highs + higher lows above EMA50", 0.7)
    elif len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] < sh[-2][1] and sl[-1][1] < sl[-2][1] and cl < ctx.e50[k]:
        vote = ("SHORT", "lower highs + lower lows below EMA50", 0.7)
    elif sl and ctx.e50[k] > ctx.e200[k] and 0 <= cl - sl[-1][1] <= c["chart_sr_atr"] * atr:
        vote = ("LONG", f"at support {sl[-1][1]:.5g}", 0.6)
    elif sh and ctx.e50[k] < ctx.e200[k] and 0 <= sh[-1][1] - cl <= c["chart_sr_atr"] * atr:
        vote = ("SHORT", f"at resistance {sh[-1][1]:.5g}", 0.6)
    if vote[0] == "LONG" and e4 == "below": vote = ("IDLE", "R3: last 4h close below the 4h EMA200, no new longs", 0); fired.append("R3 no longs below 4h EMA200")
    elif vote[0] == "SHORT" and e4 == "above": vote = ("IDLE", "R3: last 4h close above the 4h EMA200, no new shorts", 0); fired.append("R3 no shorts above 4h EMA200")
    V["chart_reader"] = vote
    if r1_thin: V = {k2: (v[0], v[1], max(0.0, v[2] - c["r1_thin_rally_conf_cut"])) if v[0] == "LONG" else v for k2, v in V.items()}
    nl = sum(v[0] == "LONG" for v in V.values()); ns = sum(v[0] == "SHORT" for v in V.values())
    decision = "LONG" if nl >= 3 else "SHORT" if ns >= 3 else "TIE" if nl == 2 and ns == 2 else "IDLE"
    if decision == "LONG" and r2_no_long: decision = "IDLE"; fired.append("R2 veto LONG (funding/ratio crowded)")
    if decision == "SHORT" and r2_no_short: decision = "IDLE"; fired.append("R2 veto SHORT (funding/ratio crowded)")
    if decision == "LONG" and e4 == "below": decision = "IDLE"; fired.append("R3 veto LONG")
    if decision == "SHORT" and e4 == "above": decision = "IDLE"; fired.append("R3 veto SHORT")
    trend = {"t1h": "up" if ctx.e50[k] > ctx.e200[k] else "down", "t4h": ctx.trend4h(t), "healthy": healthy, "p24": round(p24, 2),
             "ema200_4h": e4, "fired": fired}
    return decision, V, atr, cr, trend

def in_blackout(t, cfg):
    if not EVENTS: return False
    w = cfg["r4_window_min"] * 60; i = bisect.bisect_right(EVENTS, t + w) - 1
    return i >= 0 and EVENTS[i] - w <= t < EVENTS[i] + w

def proxy_votes(ctx, t, last_stop_ts=None):
    """Automated stand-ins for the team, following each teammate's own spec exactly (used when someone has not voted, and as
    the all-proxy committee line). Same return shape as votes().
    Casey (LONG voter): long-scout trigger (1h EMA20 > EMA50 and close > EMA50, plus a 5-min RSI pullback or MACD turning up),
      vetoed by Theo R1 (price +1%/24h, OI +5%, funding >= 0.03%: crowded longs chasing a pump) and R3 (last 4h close below the
      4h EMA200). Extreme fear (F&G < 25) raises confidence 0.6 -> 0.75.
    Pip (SHORT voter): SHORT only when the last 4h close is below the 4h EMA200 AND R1 crowded longs with price stalling
      (|price 24h| < 1%, OI +5%, funding >= 0.03%); stands down (IDLE) whenever funding is negative.
    Theo (IDLE voter): IDLE on R2 (funding beyond +-27% annualised or long/short ratio > 1.8 / < 0.55, for the crowded side),
      R4 (news blackout) or R6 (OI +5% with price flat). Otherwise sides with the 1h big trend (EMA50 vs EMA200), never with a
      side R2 flags as crowded.
    Remy (chart reader): structure only (higher highs + higher lows above EMA50 = LONG; lower highs + lower lows below EMA50 =
      SHORT) plus R3 (no LONG below the 4h EMA200, no SHORT above)."""
    c = ctx.c; k = ctx.hour_idx(t); j = ctx.idx5(t); cl = ctx.cl[k]; atr = ctx.atr[k]; V = {}
    fi = bisect.bisect_right(ctx.ft, t) - 1; fr = ctx.fund[ctx.ft[fi]] if fi >= 0 else None
    cr = ctx.crowding(t, fr); fpct = fr * 100 if fr is not None else None; oi24 = cr.get("oi_24h_pct")
    p24 = (cl / ctx.cl[k - 24] - 1) * 100 if k >= 24 else 0.0; e4 = ctx.ema200_4h(t); fired = []
    r5 = ctx.rsi5[j - 3:j + 1]
    oi_up = oi24 is not None and oi24 >= c["r1_oi_rise_pct"]; f_hi = fpct is not None and fpct >= c["r1_funding_spike_pct"]
    # Casey
    up = ctx.e20[k] > ctx.e50[k] and cl > ctx.e50[k]
    trig = (up and min(r5[:-1]) < c["scout_rsi5_low"] and r5[-1] > r5[-2]) or (up and ctx.hist[k] < 0 and ctx.hist[k] > ctx.hist[k - 1] > ctx.hist[k - 2])
    if not trig: V["casey"] = ("IDLE", "no uptrend pullback/reversal", 0)
    elif p24 >= c["r1_price_move_pct"] and oi_up and f_hi: V["casey"] = ("IDLE", "R1: longs chasing a pump", 0); fired.append("casey R1")
    elif e4 == "below": V["casey"] = ("IDLE", "R3: 4h close below EMA200", 0); fired.append("casey R3")
    else:
        fear = cr.get("fng") is not None and cr["fng"] < c["fng_fear_below"]
        V["casey"] = ("LONG", "uptrend pullback/reversal" + (f", extreme fear F&G {cr['fng']}" if fear else ""), 0.75 if fear else 0.6)
    # Pip
    if fpct is not None and fpct < 0: V["pip"] = ("IDLE", f"funding negative {fpct:.4f}%: stand down", 0)
    elif e4 == "below" and abs(p24) < c["r1_price_move_pct"] and oi_up and f_hi:
        V["pip"] = ("SHORT", f"below 4h EMA200 + crowded longs stalling (price {p24:+.1f}%, OI {oi24:+.1f}%, funding {fpct:.3f}%)", 0.7); fired.append("pip R1+R3 short")
    else: V["pip"] = ("IDLE", "no crowded-longs setup below the 4h EMA200", 0)
    # Theo
    ann = fpct * 3 * 365 if fpct is not None else None; ls = cr.get("ls_ratio")
    long_crowd = (ann is not None and ann > c["r2_funding_ann_pct"]) or (ls is not None and ls > c["r2_ls_high"])
    short_crowd = (ann is not None and ann < -c["r2_funding_ann_pct"]) or (ls is not None and ls < c["r2_ls_low"])
    big = "LONG" if ctx.e50[k] > ctx.e200[k] else "SHORT"
    if in_blackout(t, c): V["theo"] = ("IDLE", "R4 news blackout", 0); fired.append("theo R4")
    elif oi24 is not None and oi24 >= c["r6_oi_rise_pct"] and abs(p24) < c["r6_flat_price_pct"]: V["theo"] = ("IDLE", "R6 OI rising in chop", 0); fired.append("theo R6")
    elif (big == "LONG" and long_crowd) or (big == "SHORT" and short_crowd): V["theo"] = ("IDLE", f"R2 crowded {'longs' if big == 'LONG' else 'shorts'} (funding ann {ann and round(ann, 1)}%, L/S {ls})", 0); fired.append("theo R2")
    else: V["theo"] = (big, f"no R2/R4/R6 flags, big trend {'up' if big == 'LONG' else 'down'}", 0.6)
    # Remy
    n = c["chart_swing_bars"]; sh = [x for x in ctx.sh if x[0] + n <= k]; sl = [x for x in ctx.sl if x[0] + n <= k]
    if len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] > sh[-2][1] and sl[-1][1] > sl[-2][1] and cl > ctx.e50[k]:
        V["remy"] = ("IDLE", "R3: HH/HL but 4h close below EMA200", 0) if e4 == "below" else ("LONG", "higher highs + higher lows above EMA50", 0.7)
    elif len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] < sh[-2][1] and sl[-1][1] < sl[-2][1] and cl < ctx.e50[k]:
        V["remy"] = ("IDLE", "R3: LH/LL but 4h close above EMA200", 0) if e4 == "above" else ("SHORT", "lower highs + lower lows below EMA50", 0.7)
    else: V["remy"] = ("IDLE", "no clear structure", 0)
    if V["remy"][1].startswith("R3"): fired.append("remy R3")
    nl = sum(v[0] == "LONG" for v in V.values()); ns = sum(v[0] == "SHORT" for v in V.values())
    decision = "LONG" if nl >= 3 else "SHORT" if ns >= 3 else "TIE" if nl == 2 and ns == 2 else "IDLE"
    healthy = None
    if oi24 is not None and fpct is not None:
        if p24 >= c["r1_price_move_pct"] and oi24 > 0 and fpct < c["r1_funding_spike_pct"]: healthy = "up"
        elif p24 <= -c["r1_price_move_pct"] and oi24 > 0 and 0 <= fpct < c["r1_funding_spike_pct"]: healthy = "down"
    trend = {"t1h": "up" if ctx.e50[k] > ctx.e200[k] else "down", "t4h": ctx.trend4h(t), "healthy": healthy, "p24": round(p24, 2), "ema200_4h": e4, "fired": fired}
    return decision, V, atr, cr, trend

def mix_leverage(cfg, decision, confs, n_agree, trend):
    """2x by default; 5x when all 4 agree, or avg confidence of the agreeing voters >= 0.75 with 1h and 4h trends aligned."""
    want = "up" if decision == "LONG" else "down"
    aligned = trend.get("t1h") == want and trend.get("t4h") == want
    avg = sum(confs) / len(confs) if confs else 0
    strong = n_agree == 4 or (avg >= cfg["mix_conf_min"] and aligned)
    if cfg.get("theo_r5_5x_stop_cap") and trend.get("healthy") != want: strong = False   # R5: 5x only in an R1 healthy trend
    return (cfg["mix_high"] if strong else cfg["mix_base"]), round(avg, 3), aligned

def new_state(cfg):
    st = ta.new_state(cfg); st.update(last_stop_ts=None, ties=[], shadows=[], decisions={"LONG": 0, "SHORT": 0, "TIE": 0, "IDLE": 0})
    return st

def _shadow_step(sh, cfg, t, path, ts):
    """Advance one open shadow (hypothetical) position; returns True when it is closed."""
    s = sh["st"]
    if s["pos"] is None: return True
    if t - sh["opened_t"] >= cfg["shadow_max_hours"] * 3600:
        ta.close_pos(s, cfg, path[0], "TIMEOUT", ts); return True
    ta.step(s, cfg, t, list(path), {}, ts)
    return s["pos"] is None

def step(st, cfg, ctx, t, path, ts, fund_rate=None, vote_log=None, tie_log=None):
    """One closed 5-min candle opening at t: funding, committee vote (every 15 min), position update, shadows."""
    ev = []
    if t % 28800 == 0 and t > (st.get("last_funding_ts") or 0):
        e = ta.funding(st, t, fund_rate if fund_rate is not None else 0.0001, path[0], ts)
        if e: ev.append(e)
        for sh in st["shadows"]: ta.funding(sh["st"], t, fund_rate if fund_rate is not None else 0.0001, path[0], ts)
    sig = {}
    blackout = False
    if cfg.get("theo_r4_news_blackout") and in_blackout(t, cfg):   # from 15 min before to the close of the first 15-min candle after
            blackout = True
            if st["pos"]:
                ev.append(dict(ta.close_pos(st, cfg, path[0], "NEWS_FLAT", ts), why="R4 news blackout"))
                st["news_flats"] = st.get("news_flats", 0) + 1
    if t % (cfg["vote_every_min"] * 60) == 0 and ctx.ready(t):
        dec, V, atr, cr, trend = (proxy_votes if cfg.get("voters") == "proxy" else votes)(ctx, t, st.get("last_stop_ts"))
        st["decisions"][dec] += 1
        lev = None
        if dec in ("LONG", "SHORT"):
            agree = [v for v in V.values() if v[0] == dec]
            if cfg.get("sizing") == "mix": lev, avgc, aligned = mix_leverage(cfg, dec, [v[2] for v in agree], len(agree), trend)
        if blackout and dec in ("LONG", "SHORT", "TIE"): trend["fired"].append(f"R4 news blackout ({dec} skipped)"); dec = "IDLE"; lev = None
        if cr.get("crowded"): st["crowded_votes"] = st.get("crowded_votes", 0) + 1
        for f in trend["fired"]:
            key = f.split(" ")[0]; st.setdefault("rules_fired", {}); st["rules_fired"][key] = st["rules_fired"].get(key, 0) + 1
        if vote_log is not None:
            vote_log.append({"ts": ts, "decision": dec, "in_position": st["pos"]["side"] if st["pos"] else "FLAT",
                             **{f"{k}": v[0] for k, v in V.items()}, **{f"{k}_why": v[1] for k, v in V.items()},
                             **{f"{k}_conf": v[2] for k, v in V.items()}, **{f"crowd_{k}": v for k, v in cr.items()},
                             "trend_1h": trend["t1h"], "trend_4h": trend["t4h"], "ema200_4h": trend["ema200_4h"], "price_24h_pct": trend["p24"],
                             "r1_healthy_trend": trend["healthy"], "theo_rules_fired": "; ".join(trend["fired"]), "mix_leverage": lev or ""})
        if dec in ("LONG", "SHORT") and not st["pos"]:
            eff = lev or cfg["leverage"]; a_use = atr
            if cfg.get("theo_r5_5x_stop_cap") and eff >= 5:      # R5: stop <= 2x ATR and <= 10% from entry
                a_use = min(atr, cfg["r5_stop_max_atr"] * atr / cfg["stop_atr"], cfg["r5_stop_max_pct"] / 100 * path[0] / cfg["stop_atr"])
            sig = {t: {"signal": dec, "atr": a_use, "trend": "", "why": "committee " + "+".join(k for k, v in V.items() if v[0] == dec)}}
            if lev: sig[t]["leverage"] = lev
        elif dec == "TIE" and not st["pos"] and not blackout:
            tie = {"ts": ts, "price": path[0], "atr": atr, **{k: f"{v[0]}: {v[1]}" for k, v in V.items()}, "crowded": cr.get("crowded") or ""}
            for side in ("LONG", "SHORT"):
                s = ta.new_state(dict(cfg, budget_usd=100)); ta.open_pos(s, cfg, side, path[0], atr, ts, "shadow")
                st["shadows"].append({"tie_ts": ts, "side": side, "opened_t": t, "st": s})
            st["ties"].append(tie)
            if tie_log is not None: tie_log.append(tie)
    before = st["pos"]
    out = ta.step(st, cfg, t, list(path), sig, ts)
    for e in out:
        if e["event"].startswith(("STOP_LOSS", "LIQUIDATION")): st["last_stop_ts"] = t + 300
    ev += out
    still = []
    for sh in st["shadows"]:
        if _shadow_step(sh, cfg, t, path, ts):
            res = sh["st"]["cash"] - 100
            for tie in st["ties"]:
                if tie["ts"] == sh["tie_ts"]: tie[f"if_{sh['side'].lower()}_usd"] = round(res, 4)
        else: still.append(sh)
    st["shadows"] = still
    return ev
