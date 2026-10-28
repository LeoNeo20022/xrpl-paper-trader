"""Swell 7-day backtest: XRP close on Swell end date -> close 7 days later.
Data: Bitstamp public OHLC xrpusd daily (UTC closes). Paper research only."""
import json, urllib.request, datetime as dt, statistics as st
ENDS = {2017:"2017-10-18",2018:"2018-10-02",2019:"2019-11-08",2020:"2020-10-15",2021:"2021-10-01",
        2022:"2022-11-17",2023:"2023-11-09",2024:"2024-10-16",2025:"2025-11-05"}
closes = {}
start = int(dt.datetime(2017,1,1,tzinfo=dt.timezone.utc).timestamp())
while True:
    u=f"https://www.bitstamp.net/api/v2/ohlc/xrpusd/?step=86400&limit=1000&start={start}"
    rows=json.load(urllib.request.urlopen(u))["data"]["ohlc"]
    for r in rows: closes[dt.datetime.fromtimestamp(int(r["timestamp"]),dt.timezone.utc).date()]=float(r["close"])
    last=int(rows[-1]["timestamp"])
    if len(rows)<1000: break
    start=last+86400
res=[]
for y,d in ENDS.items():
    d0=dt.date.fromisoformat(d); d7=d0+dt.timedelta(7)
    c0,c7=closes.get(d0),closes.get(d7)
    res.append((y,d,c0,c7,None if not(c0 and c7) else (c7/c0-1)*100))
rets=[r[4] for r in res if r[4] is not None]
print("| Year | Swell end | Close | +7d close | 7d % |\n|---|---|---|---|---|")
for y,d,c0,c7,p in res: print(f"| {y} | {d} | {c0} | {c7} | {p:+.2f}% |")
print(f"\nDown {sum(p<0 for p in rets)}/{len(rets)}, mean {st.mean(rets):+.2f}%, median {st.median(rets):+.2f}%")
base=[]
for d,c in closes.items():
    if dt.date(2017,10,1)<=d<=dt.date(2025,12,31) and (d+dt.timedelta(7)) in closes:
        base.append((closes[d+dt.timedelta(7)]/c-1)*100)
print(f"Baseline Oct-2017..2025, all {len(base)} overlapping 7d windows: down {sum(b<0 for b in base)/len(base)*100:.1f}%, mean {st.mean(base):+.2f}%, median {st.median(base):+.2f}%")
