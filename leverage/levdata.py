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

def _path(o, h, l, c):
    return (o, h, l, c) if c < o else (o, l, h, c)

def klines_since(after_ts, now):
    """Closed 5-min candles with open time > after_ts: (source, [(t, path)])."""
    start_ms = (int(after_ts) + 300) * 1000
    srcs = [("binance_futures_perp", f"https://fapi.binance.com/fapi/v1/klines?symbol=XRPUSDT&interval=5m&limit=1500&startTime={start_ms}"),
            ("binance_spot_data_api", f"https://data-api.binance.vision/api/v3/klines?symbol=XRPUSDT&interval=5m&limit=1000&startTime={start_ms}")]
    errs = []
    for name, url in srcs:
        try:
            rows = json.loads(_get(url))
            out = [(int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows]
            return name, [(t, p) for t, p in out if t > after_ts and t + 300 <= now]
        except Exception as e:
            errs.append(f"{name}: {e}")
    try:   # OKX: newest first, max 300 per page (enough for ~25 h of catch-up)
        rows = json.loads(_get("https://www.okx.com/api/v5/market/candles?instId=XRP-USDT-SWAP&bar=5m&limit=300"))["data"]
        out = sorted((int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows if r[8] == "1")
        return "okx_swap", [(t, p) for t, p in out if t > after_ts and t + 300 <= now]
    except Exception as e:
        errs.append(f"okx: {e}")
    raise RuntimeError("; ".join(errs))

def funding_since(after_ts):
    """{funding_time_unix(rounded to the hour): rate}, source name."""
    try:
        rows = json.loads(_get(f"https://fapi.binance.com/fapi/v1/fundingRate?symbol=XRPUSDT&limit=1000&startTime={(int(after_ts) + 1) * 1000}"))
        return {int(r["fundingTime"]) // 1000 // 3600 * 3600: float(r["fundingRate"]) for r in rows}, "binance_futures"
    except Exception as e:
        print("binance funding unavailable:", str(e)[:120])
    try:
        out, after = {}, ""
        for _ in range(5):
            d = json.loads(_get("https://www.okx.com/api/v5/public/funding-rate-history?instId=XRP-USDT-SWAP&limit=100" + after))["data"]
            if not d: break
            for r in d: out[int(r["fundingTime"]) // 1000 // 3600 * 3600] = float(r.get("realizedRate") or r["fundingRate"])
            oldest = min(int(r["fundingTime"]) for r in d)
            if oldest // 1000 <= after_ts: break
            after = f"&after={oldest}"
        return {t: r for t, r in out.items() if t > after_ts}, "okx_proxy"
    except Exception as e:
        print("okx funding unavailable:", str(e)[:120])
    return {}, "assumed_0.01pct"

def archive_klines(day):
    """Real Binance USDⓈ-M XRPUSDT perp 5-min klines for one UTC day (YYYY-MM-DD) from data.binance.vision."""
    z = zipfile.ZipFile(io.BytesIO(_get(f"https://data.binance.vision/data/futures/um/daily/klines/XRPUSDT/5m/XRPUSDT-5m-{day}.zip", 60)))
    rows = list(csv.reader(io.TextIOWrapper(z.open(z.namelist()[0]))))
    return [(int(r[0]) // 1000, _path(*map(float, r[1:5]))) for r in rows if r[0].isdigit()]

def archive_funding(month):
    """Real Binance XRPUSDT funding for one month (YYYY-MM); only complete months are published."""
    z = zipfile.ZipFile(io.BytesIO(_get(f"https://data.binance.vision/data/futures/um/monthly/fundingRate/XRPUSDT/XRPUSDT-fundingRate-{month}.zip", 60)))
    rows = list(csv.reader(io.TextIOWrapper(z.open(z.namelist()[0]))))
    return {int(r[0]) // 1000 // 3600 * 3600: float(r[2]) for r in rows if r[0].isdigit()}
