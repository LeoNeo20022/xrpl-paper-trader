"""Public, keyless market data for the PAPER leverage line. No API keys, no accounts.
Order of sources (Binance futures endpoints return HTTP 451 from US IPs, so they usually fail on GitHub's US runners):
  5-min prices : fapi.binance.com XRPUSDT perp klines -> data-api.binance.vision XRPUSDT SPOT klines -> OKX XRP-USDT-SWAP candles
  funding      : fapi.binance.com fundingRate -> OKX XRP-USDT-SWAP funding history (proxy) -> assumed 0.01% per 8h
  backtest     : data.binance.vision public archive (real Binance USDⓈ-M XRPUSDT 5-min klines + monthly funding files)."""
import io, json, csv, zipfile, urllib.request

UA = {"User-Agent": "xrpl-paper-trader leverage (paper only)"}
FUNDING_ASSUMED = 0.0001          # Binance's default/base rate per 8h when nothing else is reachable

def _get(url, timeout=20):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()

def _okx(symbol): return symbol.replace("USDT", "") + "-USDT-SWAP"

def _path(o, h, l, c):
    return (o, h, l, c) if c < o else (o, l, h, c)

def klines_since(after_ts, now, symbol="XRPUSDT"):
    """Closed 5-min candles with open time > after_ts: (source, [(t, path)])."""
    start_ms = (int(after_ts) + 300) * 1000
    srcs = [("binance_futures_perp", f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval=5m&limit=1500&startTime={start_ms}"),
            ("binance_spot_data_api", f"https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval=5m&limit=1000&startTime={start_ms}")]
    errs = []
    for name, url in srcs:
        try:
            rows = json.loads(_get(url))
            out = [(int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows]
            return name, [(t, p) for t, p in out if t > after_ts and t + 300 <= now]
        except Exception as e:
            errs.append(f"{name}: {e}")
    try:   # OKX: newest first, max 300 per page (enough for ~25 h of catch-up)
        rows = json.loads(_get(f"https://www.okx.com/api/v5/market/candles?instId={_okx(symbol)}&bar=5m&limit=300"))["data"]
        out = sorted((int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows if r[8] == "1")
        return "okx_swap", [(t, p) for t, p in out if t > after_ts and t + 300 <= now]
    except Exception as e:
        errs.append(f"okx: {e}")
    raise RuntimeError("; ".join(errs))

def funding_since(after_ts, symbol="XRPUSDT"):
    """{funding_time_unix(rounded to the hour): rate}, source name."""
    try:
        rows = json.loads(_get(f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={symbol}&limit=1000&startTime={(int(after_ts) + 1) * 1000}"))
        return {int(r["fundingTime"]) // 1000 // 3600 * 3600: float(r["fundingRate"]) for r in rows}, "binance_futures"
    except Exception as e:
        print("binance funding unavailable:", str(e)[:120])
    try:
        out, after = {}, ""
        for _ in range(5):
            d = json.loads(_get(f"https://www.okx.com/api/v5/public/funding-rate-history?instId={_okx(symbol)}&limit=100" + after))["data"]
            if not d: break
            for r in d: out[int(r["fundingTime"]) // 1000 // 3600 * 3600] = float(r.get("realizedRate") or r["fundingRate"])
            oldest = min(int(r["fundingTime"]) for r in d)
            if oldest // 1000 <= after_ts: break
            after = f"&after={oldest}"
        return {t: r for t, r in out.items() if t > after_ts}, "okx_proxy"
    except Exception as e:
        print("okx funding unavailable:", str(e)[:120])
    return {}, "assumed_0.01pct"

def archive_klines(day, symbol="XRPUSDT", period="daily"):
    """Real Binance USDⓈ-M XRPUSDT perp 5-min klines for one UTC day (YYYY-MM-DD) from data.binance.vision."""
    z = zipfile.ZipFile(io.BytesIO(_get(f"https://data.binance.vision/data/futures/um/{period}/klines/{symbol}/5m/{symbol}-5m-{day}.zip", 60)))
    rows = list(csv.reader(io.TextIOWrapper(z.open(z.namelist()[0]))))
    return [(int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows if r[0].isdigit()]

def archive_funding(month, symbol="XRPUSDT"):
    """Real Binance XRPUSDT funding for one month (YYYY-MM); only complete months are published."""
    z = zipfile.ZipFile(io.BytesIO(_get(f"https://data.binance.vision/data/futures/um/monthly/fundingRate/{symbol}/{symbol}-fundingRate-{month}.zip", 60)))
    rows = list(csv.reader(io.TextIOWrapper(z.open(z.namelist()[0]))))
    return {int(r[0]) // 1000 // 3600 * 3600: float(r[2]) for r in rows if r[0].isdigit()}

# ---------------- crowding (positioning) data, keyless ----------------
# Live: OKX public "rubik" statistics (reachable from US runners):
#   long/short ACCOUNT ratio, all OKX contracts of the coin, hourly, ~30 days: /api/v5/rubik/stat/contracts/long-short-account-ratio
#   open interest in COINS of the USDT perp, hourly, 100 h:                   /api/v5/rubik/stat/contracts/open-interest-history
# Fallbacks: Binance /futures/data/* (HTTP 451 from the US) -> data.binance.vision daily "metrics" files (lag ~1 day) -> none
#   (crowding then counts as unknown and has no effect on the votes).
# Backtests: data.binance.vision daily metrics (Binance count_long_short_ratio + sum_open_interest, 5-min, history back to 2024).
def crowd_live(symbol):
    """{hour_ts: {"ls": account long/short ratio, "oi": open interest in coins}}, source."""
    ccy = symbol.replace("USDT", "")
    try:
        ls = json.loads(_get(f"https://www.okx.com/api/v5/rubik/stat/contracts/long-short-account-ratio?ccy={ccy}&period=1H"))["data"]
        oi = json.loads(_get(f"https://www.okx.com/api/v5/rubik/stat/contracts/open-interest-history?instId={_okx(symbol)}&period=1H&limit=100"))["data"]
        out = {}
        for t, r in ls: out.setdefault(int(t) // 1000, {})["ls"] = float(r)
        for r in oi: out.setdefault(int(r[0]) // 1000, {})["oi"] = float(r[2])
        if ls and oi: return out, "okx_rubik"
    except Exception as e:
        print(symbol, "okx rubik unavailable:", str(e)[:100])
    try:
        ls = json.loads(_get(f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol={symbol}&period=1h&limit=500"))
        oi = json.loads(_get(f"https://fapi.binance.com/futures/data/openInterestHist?symbol={symbol}&period=1h&limit=500"))
        out = {}
        for r in ls: out.setdefault(int(r["timestamp"]) // 1000, {})["ls"] = float(r["longShortRatio"])
        for r in oi: out.setdefault(int(r["timestamp"]) // 1000, {})["oi"] = float(r["sumOpenInterest"])
        return out, "binance_futures_data"
    except Exception as e:
        print(symbol, "binance futures/data unavailable:", str(e)[:80])
    try:
        import datetime as _dt
        out = {}
        for i in range(9, 0, -1):
            out.update(archive_metrics((_dt.date.today() - _dt.timedelta(days=i)).isoformat(), symbol))
        return out, "binance_archive_metrics_lagged"
    except Exception as e:
        print(symbol, "metrics archive unavailable:", str(e)[:80])
    return {}, "none"

def archive_metrics(day, symbol="XRPUSDT"):
    """Binance daily metrics file -> hourly {hour_ts: {"ls": count_long_short_ratio, "oi": sum_open_interest}} (value at the top of each hour)."""
    import datetime as _dt
    z = zipfile.ZipFile(io.BytesIO(_get(f"https://data.binance.vision/data/futures/um/daily/metrics/{symbol}/{symbol}-metrics-{day}.zip", 60)))
    out = {}
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]))):
        t = int(_dt.datetime.fromisoformat(r["create_time"]).replace(tzinfo=_dt.timezone.utc).timestamp())
        h = t // 3600 * 3600
        if h not in out or t - h < out[h]["_d"]:
            out[h] = {"ls": float(r["count_long_short_ratio"] or 0) or None, "oi": float(r["sum_open_interest"] or 0) or None, "_d": t - h}
    return {h: {"ls": v["ls"], "oi": v["oi"]} for h, v in out.items()}

def fear_greed():
    """Crypto Fear & Greed Index, daily, full history: {day_ts_utc: value 0-100}, source. Keyless (alternative.me)."""
    try:
        d = json.loads(_get("https://api.alternative.me/fng/?limit=0"))["data"]
        return {int(r["timestamp"]): int(r["value"]) for r in d}, "alternative.me"
    except Exception as e:
        print("fear & greed unavailable:", str(e)[:100]); return {}, "none"
