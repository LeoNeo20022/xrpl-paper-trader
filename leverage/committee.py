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
Exits: stop 1.5x 1h ATR14, target 3x ATR14, one position at a time (same as leverage_ta)."""
import bisect
import ta

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
    def __init__(self, c5, bars, fund, c):
        self.c, self.c5, self.bars = c, c5, bars
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
    c = ctx.c; k = ctx.hour_idx(t); j = ctx.idx5(t); cl = ctx.cl[k]; atr = ctx.atr[k]; V = {}
    # 1 long scout
    up = ctx.e20[k] > ctx.e50[k] and cl > ctx.e50[k]
    r5 = ctx.rsi5[j - 3:j + 1]
    if up and min(r5[:-1]) < c["scout_rsi5_low"] and r5[-1] > r5[-2]: V["long_scout"] = ("LONG", f"uptrend + 5m RSI pullback {min(r5[:-1]):.0f}->{r5[-1]:.0f}")
    elif up and ctx.hist[k] < 0 and ctx.hist[k] > ctx.hist[k - 1] > ctx.hist[k - 2]: V["long_scout"] = ("LONG", "uptrend + MACD turning up")
    else: V["long_scout"] = ("IDLE", "no uptrend" if not up else "uptrend, no pullback/reversal")
    # 2 short scout
    dn = ctx.e20[k] < ctx.e50[k] and cl < ctx.e50[k]
    lo24 = min(b[3] for b in ctx.bars[max(0, k - c["breakdown_hours"] + 1):k + 1])
    if dn and max(r5[:-1]) > c["scout_rsi5_high"] and r5[-1] < r5[-2]: V["short_scout"] = ("SHORT", f"downtrend + 5m RSI bounce {max(r5[:-1]):.0f}->{r5[-1]:.0f}")
    elif dn and ctx.cl5[j] < lo24: V["short_scout"] = ("SHORT", f"downtrend + breakdown below 24h low {lo24:.4g}")
    elif dn and ctx.hist[k] > 0 and ctx.hist[k] < ctx.hist[k - 1] < ctx.hist[k - 2]: V["short_scout"] = ("SHORT", "downtrend + MACD turning down")
    else: V["short_scout"] = ("IDLE", "no downtrend" if not dn else "downtrend, no bounce/breakdown")
    # 3 idle guard
    fi = bisect.bisect_right(ctx.ft, t) - 1; fr = ctx.fund[ctx.ft[fi]] if fi >= 0 else None
    flags = []
    if ctx.adx[k] < c["guard_adx_min"]: flags.append(f"choppy ADX {ctx.adx[k]:.0f}")
    if atr / cl > c["guard_atr_vs_median"] * ctx.atr_med[k]: flags.append(f"wide ATR {atr / cl * 100:.2f}% vs median {ctx.atr_med[k] * 100:.2f}%")
    if ctx.atr5[j - 1] and ctx.rng5[j] > c["guard_spike_atr5"] * ctx.atr5[j - 1]: flags.append("5m volatility spike")
    if fr is not None and abs(fr) * 100 >= c["guard_funding_abs_pct"]: flags.append(f"funding extreme {fr * 100:.3f}%")
    if last_stop_ts is not None and t - last_stop_ts < c["guard_cooldown_h"] * 3600: flags.append("cooldown after stop-out")
    if flags: V["idle_guard"] = ("IDLE", "; ".join(flags))
    else: V["idle_guard"] = ("LONG", "no red flags, big trend up") if ctx.e50[k] > ctx.e200[k] else ("SHORT", "no red flags, big trend down")
    # 4 chart reader
    n = c["chart_swing_bars"]; sh = [s for s in ctx.sh if s[0] + n <= k]; sl = [s for s in ctx.sl if s[0] + n <= k]
    vote = ("IDLE", "no clear structure")
    if len(sl) >= 2 and sl[-1][0] + n >= k - c["chart_div_recent_bars"] and sl[-1][1] < sl[-2][1] and sl[-1][2] > sl[-2][2]:
        vote = ("LONG", "bullish RSI divergence at swing low")
    elif len(sh) >= 2 and sh[-1][0] + n >= k - c["chart_div_recent_bars"] and sh[-1][1] > sh[-2][1] and sh[-1][2] < sh[-2][2]:
        vote = ("SHORT", "bearish RSI divergence at swing high")
    elif len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] > sh[-2][1] and sl[-1][1] > sl[-2][1] and cl > ctx.e50[k]:
        vote = ("LONG", "higher highs + higher lows above EMA50")
    elif len(sh) >= 2 and len(sl) >= 2 and sh[-1][1] < sh[-2][1] and sl[-1][1] < sl[-2][1] and cl < ctx.e50[k]:
        vote = ("SHORT", "lower highs + lower lows below EMA50")
    elif sl and ctx.e50[k] > ctx.e200[k] and 0 <= cl - sl[-1][1] <= c["chart_sr_atr"] * atr:
        vote = ("LONG", f"at support {sl[-1][1]:.4g}")
    elif sh and ctx.e50[k] < ctx.e200[k] and 0 <= sh[-1][1] - cl <= c["chart_sr_atr"] * atr:
        vote = ("SHORT", f"at resistance {sh[-1][1]:.4g}")
    V["chart_reader"] = vote
    nl = sum(v[0] == "LONG" for v in V.values()); ns = sum(v[0] == "SHORT" for v in V.values())
    decision = "LONG" if nl >= 3 else "SHORT" if ns >= 3 else "TIE" if nl == 2 and ns == 2 else "IDLE"
    return decision, V, atr

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
    if t % (cfg["vote_every_min"] * 60) == 0 and ctx.ready(t):
        dec, V, atr = votes(ctx, t, st.get("last_stop_ts"))
        st["decisions"][dec] += 1
        if vote_log is not None:
            vote_log.append({"ts": ts, "decision": dec, "in_position": st["pos"]["side"] if st["pos"] else "FLAT",
                             **{f"{k}": v[0] for k, v in V.items()}, **{f"{k}_why": v[1] for k, v in V.items()}})
        if dec in ("LONG", "SHORT") and not st["pos"]:
            sig = {t: {"signal": dec, "atr": atr, "trend": "", "why": "committee " + "+".join(k for k, v in V.items() if v[0] == dec)}}
        elif dec == "TIE" and not st["pos"]:
            tie = {"ts": ts, "price": path[0], "atr": atr, **{k: f"{v[0]}: {v[1]}" for k, v in V.items()}}
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
