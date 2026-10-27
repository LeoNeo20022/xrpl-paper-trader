"""PAPER research only (no keys, no orders, no wallets): what did a winning 10x 'Stars Aligned' moment look like beforehand?
Every closed 1h bar (4h closes are a subset) is a candidate entry, LONG and SHORT, simulated with the same ta.py engine and
Stars settings as backtest_stars.py: XRPUSDT 10x isolated, TP +3% / stop -1.5% price move, Binance-style taker/maker fees,
slippage, 8-hourly funding, liquidation. Winner = take-profit hit first (7-day cap; open after 7 days = not a winner).
Data (same sources as backtest_stars.py / backtest_committee.py):
  last 60 days  = Binance USDⓈ-M XRPUSDT perp 5-min archive (data.binance.vision; 110 days loaded so the 4h EMA200 is warm),
                  real Binance funding (monthly files + live/OKX proxy for the current month);
  Oct 2024-Mar 2025 rally = saved Bitstamp 5-min file (data/bitstamp_5m_2024-10_2025-03.csv). Funding here = real Binance XRPUSDT
                  monthly funding files (backtest_stars.py assumes a flat 0.01%/8h; real history is used here because funding is a feature).
  crowding = Binance daily 'metrics' (open interest + count long/short ratio), Fear & Greed = Theo's saved daily file
  (/home/box/shared/strategy-lab/fear_greed_history.csv), events = events_calendar.csv.
Features are read at the entry time with no look-ahead (committee.Context / proxy_votes / stars.standins).
Rule search: single signs and pairs of signs, fit on one period, then checked unchanged on the other.
Outputs (this folder): candidates_*.csv, sign_table.md, rules.md, top_moves.csv; summary printed."""
import os, sys, csv, io, json, zipfile, pickle, bisect, itertools, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)); LEV = os.path.dirname(HERE); sys.path.insert(0, LEV)
import levdata
FNG_FILE = "/home/box/shared/strategy-lab/fear_greed_history.csv"
def _fng_file():
    out = {}
    for r in csv.DictReader(open(FNG_FILE)):
        out[int(dt.datetime.fromisoformat(r["date"]).replace(tzinfo=dt.timezone.utc).timestamp())] = int(r["fng_value"])
    return out, "theo_file"
levdata.fear_greed = _fng_file           # use Theo's saved history, no API call
import ta, committee, stars
import backtest_committee as bc

SYM = "XRPUSDT"; CACHE = "/tmp/stars_fp_cache.pkl"; MAXH = 7 * 24; NOW = dt.datetime.now(dt.timezone.utc)
iso = lambda u: dt.datetime.fromtimestamp(u, dt.timezone.utc).strftime("%Y-%m-%d %H:%M")
PT = dt.timezone(dt.timedelta(hours=-7))

def _kl_vol(day):
    z = zipfile.ZipFile(io.BytesIO(levdata._get(f"https://data.binance.vision/data/futures/um/daily/klines/{SYM}/5m/{SYM}-5m-{day}.zip", 60)))
    return [(int(r[0]) // 1000, *map(float, r[1:6])) for r in csv.reader(io.TextIOWrapper(z.open(z.namelist()[0]))) if r[0].isdigit()]

def _kl_safe(d):
    try: return _kl_vol(d)
    except Exception as e: print('missing day', d, e); return []

def load():
    if os.path.exists(CACHE) and (dt.datetime.now().timestamp() - os.path.getmtime(CACHE)) < 86400: return pickle.load(open(CACHE, "rb"))
    from concurrent.futures import ThreadPoolExecutor
    today = NOW.date(); days = [(today - dt.timedelta(days=i)).isoformat() for i in range(110, 0, -1)]
    with ThreadPoolExecutor(12) as ex: res = list(ex.map(_kl_safe, days))
    rows = sorted({r[0]: r for x in res for r in x}.values())
    rec = [(t, levdata._path(o, h, l, c)) for t, o, h, l, c, v in rows]; rvol = {t: v for t, o, h, l, c, v in rows}
    fund, _ = levdata.funding_since(rec[0][0] - 1, SYM)
    for m in sorted({d[:7] for d in days}):
        try: fund.update(levdata.archive_funding(m, SYM))
        except Exception: pass
    old, ovol = [], {}
    for r in csv.DictReader(open(os.path.join(LEV, "..", "data", "bitstamp_5m_2024-10_2025-03.csv"))):
        t = int(dt.datetime.fromisoformat(r["t"]).timestamp()); o, h, l, c = (float(r[k]) for k in "ohlc")
        old.append((t, levdata._path(o, h, l, c))); ovol[t] = float(r["volume"] or 0)
    ofund = {}
    for m in ("2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04"):
        try: ofund.update(levdata.archive_funding(m, SYM))
        except Exception as e: print("funding missing", m, e)
    d = dict(rec=rec, rvol=rvol, fund=fund, old=sorted(old), ovol=ovol, ofund=ofund, rmet=bc.metrics(SYM, rec), omet=bc.metrics(SYM, old))
    pickle.dump(d, open(CACHE, "wb")); return d

def simulate(cs, idx, fund, side):
    """Stars trade opened at the open of candle idx (= close of the signal hour). Returns outcome dict."""
    C = bc.CC["common"]; cfg = stars.cfg(C, 100); a = ta.new_state(cfg); t0 = cs[idx][0]; sig = stars.signal(t0, cs[idx][1][0], side, "fp")
    lo = 1.0; mfe = 0.0; e0 = None
    for j in range(idx, min(len(cs), idx + MAXH * 12)):
        t, path = cs[j]
        if t % 28800 == 0 and j > idx: ta.funding(a, t, fund.get(t, levdata.FUNDING_ASSUMED), path[0], iso(t))
        ev = ta.step(a, cfg, t, list(path), sig, iso(t))
        if e0 is None and a["pos"]: e0 = a["pos"]["entry"]
        if e0: mfe = max(mfe, max((p / e0 - 1) * 100 if side == "LONG" else (1 - p / e0) * 100 for p in path))
        lo = min(lo, a.get("min_equity", 100) / 100)
        if not a["pos"] and j > idx or (ev and not a["pos"]):
            kind = next((e["event"] for e in ev if not e["event"].startswith(("OPEN", "FUND"))), "?")
            return dict(win=kind.startswith("TAKE"), kind=kind.split("_")[0], ret=a["cash"] / 100 - 1, exit_t=t + 300, minq=lo, hours=(t + 300 - t0) / 3600)
    px = cs[min(len(cs), idx + MAXH * 12) - 1][1][-1]
    return dict(win=False, kind="TIMEOUT" if idx + MAXH * 12 <= len(cs) else "OPEN_AT_END", ret=ta.equity(a, px, cfg) / 100 - 1,
                exit_t=cs[min(len(cs), idx + MAXH * 12) - 1][0] + 300, minq=lo, hours=MAXH)

def mfe24(cs, idx, side):
    e = cs[idx][1][0]; ps = [p for _, path in cs[idx: idx + 288] for p in path]
    return (max(ps) / e - 1) * 100 if side == "LONG" else (1 - min(ps) / e) * 100

def features(ctx, t, vol1h, bars):
    k = ctx.hour_idx(t); C = ctx.c
    dec, V, atr, cr, trend = committee.proxy_votes(ctx, t)
    calls = stars.standins({v: {"call": V[v][0], "proxy": True} for v in ("casey", "pip", "theo", "remy")}, cr, trend.get("ema200_4h"), C)
    cl = ctx.cl[k]; i4 = bisect.bisect_right(ctx.b4t, t - 14400) - 1
    hi24 = max(b[2] for b in bars[k - 24:k]); lo24 = min(b[3] for b in bars[k - 24:k])
    vs = [vol1h.get(bars[j][0], 0) for j in range(k - 168, k)]; vs = sorted(x for x in vs if x > 0)
    vr = vol1h.get(bars[k][0], 0) / vs[len(vs) // 2] if vs else None
    ev = committee.EVENTS; ei = bisect.bisect_right(ev, t) - 1
    since = (t - ev[ei]) / 3600 if ei >= 0 else None; until = (ev[ei + 1] - t) / 3600 if ei + 1 < len(ev) else None
    h = dt.datetime.fromtimestamp(t, dt.timezone.utc)
    f = dict(t=t, utc=iso(t), is4h=t % 14400 == 0, price=round(cl, 5),
             ema200_4h=trend.get("ema200_4h") or "unknown",
             dist_ema200_4h_pct=round((ctx.c4[i4] / ctx.e4_200[i4] - 1) * 100, 2) if i4 >= 200 else None,
             trend1h="up" if ctx.e50[k] > ctx.e200[k] else "down", trend4h=trend.get("t4h") or "unknown",
             rsi1h=round(ctx.rsi[k], 1) if ctx.rsi[k] is not None else None,
             ema20_slope6h_pct=round((ctx.e20[k] / ctx.e20[k - 6] - 1) * 100, 2),
             p24_pct=trend["p24"], breakout24=("up" if cl > hi24 else "down" if cl < lo24 else "none"),
             vol_ratio=round(vr, 2) if vr else None, atr_vs_med=round(ctx.atr[k] / cl / ctx.atr_med[k], 2) if ctx.atr_med[k] else None,
             funding_pct=cr.get("funding_pct"), oi24_pct=cr.get("oi_24h_pct"), ls_ratio=cr.get("ls_ratio"), ls_pctile=cr.get("ls_pctile"),
             fng=cr.get("fng"), crowded=cr.get("crowded") or "none", hour_utc=h.hour, weekend=h.weekday() >= 5,
             h_since_event=round(since, 1) if since is not None else None, h_until_event=round(until, 1) if until is not None else None)
    for v in ("casey", "pip", "theo", "remy"): f[v] = calls[v]["call"]; f[v + "_standin"] = bool(calls[v].get("standin"))
    return f

def period(name, cs, vol, fund, met, start, end):
    bars = ta.bars_1h(cs); vol1h = {}
    for t, v in vol.items(): vol1h[t // 3600 * 3600] = vol1h.get(t // 3600 * 3600, 0) + v
    ctx = committee.Context(cs, bars, fund, bc.base(SYM, True, True), met, bc.FNG)
    pos = {t: i for i, (t, _) in enumerate(cs)}; rows = []
    for t in range(start // 3600 * 3600, end, 3600):
        if t not in pos or not ctx.ready(t) or ctx.hour_idx(t) < 200: continue
        f = features(ctx, t, vol1h, bars); f["period"] = name
        for side in ("LONG", "SHORT"):
            o = simulate(cs, pos[t], fund, side)
            f[side + "_win"] = o["win"]; f[side + "_kind"] = o["kind"]; f[side + "_ret"] = round(o["ret"], 4); f[side + "_exit_t"] = o["exit_t"]
            f[side + "_minq"] = round(o["minq"], 4); f[side + "_hours"] = round(o["hours"], 2); f[side + "_mfe24"] = round(mfe24(cs, pos[t], side), 2)
        rows.append(f)
    print(name, len(rows), "candidate hours", flush=True)
    return rows

# ---------------- signs (side-aware binary conditions) ----------------
def nz(x, d=0): return d if x is None else x
SIGNS = {
 "4h close above EMA200": lambda r: r["ema200_4h"] == "above", "4h close below EMA200": lambda r: r["ema200_4h"] == "below",
 "4h far above EMA200 (>+10%)": lambda r: nz(r["dist_ema200_4h_pct"]) > 10, "4h far below EMA200 (<-10%)": lambda r: nz(r["dist_ema200_4h_pct"]) < -10,
 "1h trend up (EMA50>EMA200)": lambda r: r["trend1h"] == "up", "1h trend down": lambda r: r["trend1h"] == "down",
 "4h trend up (EMA20>EMA50)": lambda r: r["trend4h"] == "up", "4h trend down": lambda r: r["trend4h"] == "down",
 "RSI<30": lambda r: nz(r["rsi1h"], 50) < 30, "RSI 30-45": lambda r: 30 <= nz(r["rsi1h"], 50) < 45, "RSI 45-55": lambda r: 45 <= nz(r["rsi1h"], 50) < 55,
 "RSI 55-70": lambda r: 55 <= nz(r["rsi1h"], 50) < 70, "RSI>70": lambda r: nz(r["rsi1h"], 50) >= 70,
 "EMA20 rising >0.5%/6h": lambda r: r["ema20_slope6h_pct"] > 0.5, "EMA20 falling >0.5%/6h": lambda r: r["ema20_slope6h_pct"] < -0.5,
 "EMA20 flat (+-0.2%/6h)": lambda r: abs(r["ema20_slope6h_pct"]) <= 0.2,
 "breakout above 24h high": lambda r: r["breakout24"] == "up", "breakdown below 24h low": lambda r: r["breakout24"] == "down",
 "24h move > +5%": lambda r: r["p24_pct"] > 5, "24h move < -5%": lambda r: r["p24_pct"] < -5, "24h move flat (+-1%)": lambda r: abs(r["p24_pct"]) < 1,
 "volume spike >2x": lambda r: nz(r["vol_ratio"]) > 2, "volume quiet <0.7x": lambda r: r["vol_ratio"] is not None and r["vol_ratio"] < 0.7,
 "volatility hot (ATR >1.5x median)": lambda r: nz(r["atr_vs_med"], 1) > 1.5, "volatility quiet (ATR <0.8x median)": lambda r: nz(r["atr_vs_med"], 1) < 0.8,
 "funding high (>=0.03%)": lambda r: nz(r["funding_pct"]) >= 0.03, "funding negative": lambda r: nz(r["funding_pct"]) < 0,
 "funding calm (0 to 0.01%)": lambda r: r["funding_pct"] is not None and 0 <= r["funding_pct"] <= 0.01,
 "OI +5% in 24h": lambda r: nz(r["oi24_pct"]) >= 5, "OI -5% in 24h": lambda r: nz(r["oi24_pct"]) <= -5,
 "L/S ratio top 20% of week": lambda r: nz(r["ls_pctile"], 50) >= 80, "L/S ratio bottom 20% of week": lambda r: nz(r["ls_pctile"], 50) <= 20,
 "crowded longs": lambda r: r["crowded"] == "longs", "crowded shorts": lambda r: r["crowded"] == "shorts",
 "F&G extreme fear <25": lambda r: nz(r["fng"], 50) < 25, "F&G fear 25-45": lambda r: 25 <= nz(r["fng"], 50) < 45,
 "F&G greed 55-75": lambda r: 55 <= nz(r["fng"], 50) <= 75, "F&G extreme greed >75": lambda r: nz(r["fng"], 50) > 75,
 "hour 00-04 UTC (5-9pm PT)": lambda r: r["hour_utc"] < 4, "hour 04-08 UTC (9pm-1am PT)": lambda r: 4 <= r["hour_utc"] < 8,
 "hour 08-12 UTC (1-5am PT)": lambda r: 8 <= r["hour_utc"] < 12, "hour 12-16 UTC (5-9am PT)": lambda r: 12 <= r["hour_utc"] < 16,
 "hour 16-20 UTC (9am-1pm PT)": lambda r: 16 <= r["hour_utc"] < 20, "hour 20-24 UTC (1-5pm PT)": lambda r: r["hour_utc"] >= 20,
 "weekend": lambda r: r["weekend"], "4h candle close": lambda r: r["is4h"],
 "event in last 24h": lambda r: r["h_since_event"] is not None and r["h_since_event"] <= 24,
 "event in next 24h": lambda r: r["h_until_event"] is not None and r["h_until_event"] <= 24,
 "Casey votes LONG": lambda r: r["casey"] == "LONG", "Casey votes SHORT (stand-in)": lambda r: r["casey"] == "SHORT",
 "Pip votes SHORT": lambda r: r["pip"] == "SHORT", "Pip votes LONG (stand-in)": lambda r: r["pip"] == "LONG",
 "Theo votes LONG": lambda r: r["theo"] == "LONG", "Theo votes SHORT": lambda r: r["theo"] == "SHORT", "Theo IDLE": lambda r: r["theo"] == "IDLE",
 "Remy votes LONG": lambda r: r["remy"] == "LONG", "Remy votes SHORT": lambda r: r["remy"] == "SHORT",
}
def nvotes(r, side): return sum(r[v] == side for v in ("casey", "pip", "theo", "remy"))
for _s in ("LONG", "SHORT"):
    for _n in (2, 3): SIGNS[f"{_n}+ voters say {_s}"] = (lambda s, n: lambda r: nvotes(r, s) >= n)(_s, _n)

def stat(rows, side, cond=None):
    sel = [r for r in rows if cond is None or cond(r)]; w = sum(r[side + "_win"] for r in sel)
    return len(sel), w

def seq(rows, side, cond):
    """One position at a time, a fresh $100 stake at 10x per trade (no compounding), take a signal hour only when flat.
    Worst drawdown = biggest drop of the running P/L in dollars, counting the worst point inside each trade."""
    pl, peak, dd, busy, n, w, liq = 0.0, 0.0, 0.0, 0, 0, 0, 0
    for r in rows:
        if r["t"] < busy or not cond(r) or r[side + "_kind"] == "OPEN_AT_END": continue
        n += 1; w += r[side + "_win"]; liq += r[side + "_kind"] == "LIQUIDATION"
        dd = max(dd, peak - (pl - 100 * (1 - r[side + "_minq"]))); pl += 100 * r[side + "_ret"]; peak = max(peak, pl); dd = max(dd, peak - pl)
        busy = r[side + "_exit_t"]
    return dict(trades=n, wins=w, wr=w / n if n else 0, pl=pl, dd=dd, liq=liq)

def fmt_seq(s): return f"{s['trades']} trades, {s['wr'] * 100:.0f}% wins, ${s['pl']:+.0f}, worst drawdown -${s['dd']:.0f}" + (f", {s['liq']} liquidations" if s["liq"] else "")


# ---- fingerprints: built only from signs that beat break-even in BOTH periods (>=30 hours each); checked per sub-period ----
FINGERPRINTS = [
 ("F1 positioning surge LONG: OI +5% in 24h", "LONG", lambda r: nz(r["oi24_pct"]) >= 5),
 ("F2 squeeze LONG: crowded shorts, or OI +5% with 4h above EMA200", "LONG", lambda r: r["crowded"] == "shorts" or (nz(r["oi24_pct"]) >= 5 and r["ema200_4h"] == "above")),
 ("F3 failed-pullback SHORT: Casey's long trigger fires but funding is not hot (<0.03%)", "SHORT", lambda r: r["casey"] == "LONG" and nz(r["funding_pct"]) < 0.03),
 ("ref: current Stars rule (4/4 incl. stand-ins) LONG", "LONG", lambda r: nvotes(r, "LONG") == 4),
 ("ref: current Stars rule (4/4 incl. stand-ins) SHORT", "SHORT", lambda r: nvotes(r, "SHORT") == 4),
 ("ref: any hour, LONG", "LONG", lambda r: True), ("ref: any hour, SHORT", "SHORT", lambda r: True),
]
def fingerprints(R, O):
    cut = int(dt.datetime(2025, 1, 1, tzinfo=dt.timezone.utc).timestamp())
    parts = [("Rally A Oct-Dec 2024", [r for r in O if r["t"] < cut]), ("Rally B Jan-Mar 2025", [r for r in O if r["t"] >= cut]), ("Last 60 days", R)]
    be = stars.breakeven(bc.CC["common"])[2]
    L = [f"# Fingerprint rules: PAPER, 10x, TP +3% / stop -1.5%, $100 per trade (no compounding), one trade at a time, after fees/slippage/funding. Break-even win rate {be * 100:.0f}%.",
         "Signs were picked because they beat break-even in BOTH the rally and the last 60 days (so this is NOT a clean out-of-sample test; the clean one is rules.md).",
         "", "| Rule | " + " | ".join(p for p, _ in parts) + " |", "|---|" + "---|" * len(parts)]
    for name, side, fn in FINGERPRINTS:
        L.append(f"| {name} | " + " | ".join(fmt_seq(seq(rows, side, fn)) for _, rows in parts) + " |")
    open(os.path.join(HERE, "fingerprints.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))

def main():
    d = load()
    end_r = d["rec"][-1][0] + 300; R = period("last60d", d["rec"], d["rvol"], d["fund"], d["rmet"], end_r - 60 * 86400, end_r - 3600)
    O = period("rally_2024_25", d["old"], d["ovol"], d["ofund"], d["omet"], d["old"][0][0], d["old"][-1][0] - 3600)
    for nm, rows in (("last60d", R), ("rally_2024_25", O)):
        with open(os.path.join(HERE, f"candidates_{nm}.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    fingerprints(R, O)
    P = {"last60d": R, "rally": O}; out = []
    be = stars.breakeven(bc.CC["common"])[2]
    out.append(f"# Sign table (PAPER research). Break-even win rate after fees: {be * 100:.0f}%\n")
    out.append("Win rate = share of candidate hours where a 10x Stars trade (TP +3% / stop -1.5%) hit TP first. 'in W' / 'in L' = share of all winners / losers that showed the sign. Lift = win rate with the sign / base win rate.\n")
    for side in ("LONG", "SHORT"):
        for pn, rows in P.items():
            n, w = stat(rows, side)
            out.append(f"\n## {side}, {pn}: {n} candidate hours, {w} winners, {n - w} losers, base win rate {w / n * 100:.0f}%\n")
            out.append("| Sign | Hours | Wins | Losses | Win rate | Lift | in W | in L |\n|---|---|---|---|---|---|---|---|")
            tab = []
            for s, fn in SIGNS.items():
                ns, ws = stat(rows, side, fn)
                if ns < 15: continue
                tab.append((ws / ns, s, ns, ws))
            for wr, s, ns, ws in sorted(tab, reverse=True):
                out.append(f"| {s} | {ns} | {ws} | {ns - ws} | {wr * 100:.0f}% | {wr / (w / n):.2f} | {ws / w * 100:.0f}% | {(ns - ws) / (n - w) * 100:.0f}% |")
    open(os.path.join(HERE, "sign_table.md"), "w").write("\n".join(out) + "\n")
    # ---- rule search: 1-2 signs, fit on one period, check on the other ----
    names = list(SIGNS); ru = [f"# Fingerprint rules (fit on one period, tested unchanged on the other). Break-even {be * 100:.0f}%\n"]
    best = []
    for fit, test in (("rally", "last60d"), ("last60d", "rally")):
        for side in ("LONG", "SHORT"):
            cands = []
            for k in (1, 2):
                for combo in itertools.combinations(names, k):
                    fn = (lambda cs: lambda r: all(SIGNS[c](r) for c in cs))(combo)
                    ns, ws = stat(P[fit], side, fn)
                    if ns < 40: continue
                    cands.append((ws / ns, combo, fn))
            cands.sort(key=lambda x: -x[0]); picked = []
            for wr, combo, fn in cands:
                if len(picked) == 3: break
                if any(set(combo) & set(p[1]) for p in picked): continue        # keep the top picks different
                sf, st_ = seq(P[fit], side, fn), seq(P[test], side, fn)
                if sf["trades"] < 8: continue
                picked.append((wr, combo, fn, sf, st_))
            ru.append(f"\n## Fit on {fit}, test on {test}, {side}\n")
            for wr, combo, fn, sf, st_ in picked:
                ru.append(f"- **{side} when {' + '.join(combo)}**\n  - fit ({fit}): {fmt_seq(sf)}\n  - test ({test}): {fmt_seq(st_)}")
                best.append((fit, side, combo, sf, st_))
    open(os.path.join(HERE, "rules.md"), "w").write("\n".join(ru) + "\n")
    json.dump([dict(fit=f, side=s, rule=list(c), fit_stats=a, test_stats=b) for f, s, c, a, b in best], open(os.path.join(HERE, "rules.json"), "w"), indent=1)
    # ---- top moves (episodes) for Riley ----
    ev = []
    for pn, rows in P.items():
        for side in ("LONG", "SHORT"):
            last = None
            for r in rows:
                if not r[side + "_win"]: last = None; continue
                if last and r["t"] - last["t_end"] <= 3 * 3600: last["t_end"] = r["t"]; last["mfe"] = max(last["mfe"], r[side + "_mfe24"]); last["n"] += 1; continue
                last = dict(period=pn, side=side, t=r["t"], t_end=r["t"], mfe=r[side + "_mfe24"], n=1, r=r); ev.append(last)
    tops = []
    for pn in P:
        for side in ("LONG", "SHORT"):
            seen, k = set(), 0
            for e in sorted([e for e in ev if e["period"] == pn and e["side"] == side], key=lambda e: -e["mfe"]):
                day = iso(e["t"])[:10]
                if day in seen: continue                      # one row per UTC day: the day's biggest move
                seen.add(day); tops.append(e); k += 1
                if k == 12: break
    with open(os.path.join(HERE, "top_moves.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["period", "side", "first_winning_entry_utc", "first_winning_entry_pt", "last_winning_entry_utc", "winning_entry_hours", "entry_price",
                    "best_move_within_24h_pct", "hours_to_tp", "ema200_4h", "rsi1h", "p24_pct", "breakout24", "vol_ratio", "funding_pct", "oi24_pct", "ls_pctile", "fng", "crowded",
                    "votes_casey_pip_theo_remy", "nearest_calendar_event_h_since", "nearest_calendar_event_h_until", "news_check (Riley)"])
        for e in sorted(tops, key=lambda e: (e["period"], e["side"], -e["mfe"])):
            r = e["r"]; s = e["side"]
            w.writerow([e["period"], s, iso(e["t"]), dt.datetime.fromtimestamp(e["t"], PT).strftime("%Y-%m-%d %H:%M PT"), iso(e["t_end"]), e["n"], r["price"],
                        round(e["mfe"], 2), r[s + "_hours"], r["ema200_4h"], r["rsi1h"], r["p24_pct"], r["breakout24"], r["vol_ratio"], r["funding_pct"], r["oi24_pct"], r["ls_pctile"],
                        r["fng"], r["crowded"], "/".join(r[v] for v in ("casey", "pip", "theo", "remy")), r["h_since_event"], r["h_until_event"], ""])
    for pn, rows in P.items():
        for side in ("LONG", "SHORT"):
            n, wn = stat(rows, side); print(pn, side, n, wn, f"{wn / n * 100:.0f}%", "episodes", sum(1 for e in ev if e["period"] == pn and e["side"] == side))

if __name__ == "__main__":
    main()
