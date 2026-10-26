#!/usr/bin/env python3
"""PAPER-ONLY live tracker for the rule-based committee (com_xrp_2x/5x, com_btc_2x/5x). Runs in the paper-trading workflow
after ta_runner.py, failure-isolated. Public keyless data only; no keys, logins, orders or wallets. Rules: committee.py.
Logs: leverage/logs/committee_votes_<coin>.csv (every 15-min vote of the 2x line with each voter's reason; 5x votes are the
same except for its own cooldown), leverage/logs/committee_ties.csv (2-2 LONG/SHORT splits + shadow outcomes, user_vote column
left blank for the user), leverage/logs/com_*_events.csv / _ticks.csv."""
import json, os, csv, time
from datetime import datetime, timezone
import ta, committee, levdata

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
CC = json.load(open(os.path.join(HERE, "committee_config.json")))
SDIR, LDIR = os.path.join(HERE, "state"), os.path.join(HERE, "logs")
MS = os.path.join(SDIR, "committee_market.json")
EV = ["ts", "event", "price", "qty_xrp", "notional_usd", "margin_usd", "fee_usd", "stop", "target", "liq_price", "why",
      "trade_net_usd", "funding_usd", "rate", "mkt", "margin_lost_usd", "label"]
VOTERS = ["long_scout", "short_scout", "idle_guard", "chart_reader"]
CROWD = ["funding_pct", "oi_24h_pct", "ls_ratio", "ls_pctile", "fng", "crowded", "long_signals", "short_signals"]
VOTE_FIELDS = (["ts", "coin", "decision", "in_position"] + VOTERS + [x + "_conf" for x in VOTERS] + [x + "_why" for x in VOTERS]
               + ["crowd_" + x for x in CROWD] + ["trend_1h", "trend_4h", "ema200_4h", "price_24h_pct", "r1_healthy_trend", "theo_rules_fired", "mix_leverage"])
PROXIES = ["casey", "pip", "theo", "remy"]
PROXY_FIELDS = (["ts", "coin", "decision", "in_position"] + PROXIES + [x + "_conf" for x in PROXIES] + [x + "_why" for x in PROXIES]
                + ["crowd_" + x for x in CROWD] + ["trend_1h", "trend_4h", "ema200_4h", "price_24h_pct", "r1_healthy_trend", "theo_rules_fired", "mix_leverage"])
FNG = levdata.fear_greed()
BEGIN, END = "<!-- COMMITTEE-BEGIN -->", "<!-- COMMITTEE-END -->"

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")
def load(p): return json.load(open(p)) if os.path.exists(p) else None
def save(p, o): os.makedirs(os.path.dirname(p), exist_ok=True); json.dump(o, open(p, "w"), indent=1)
def append(p, row, fields):
    os.makedirs(os.path.dirname(p), exist_ok=True); new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def history(sym, now):
    """Context data: last 1000 closed 1h candles and last 1000 closed 5-min candles (Binance spot data-api; OKX perp fallback)."""
    try:
        h = json.loads(levdata._get(f"https://data-api.binance.vision/api/v3/klines?symbol={sym}&interval=1h&limit=1000"))
        bars = [(int(r[0]) // 1000, *map(float, r[1:5])) for r in h if int(r[0]) // 1000 + 3600 <= now]
        k = json.loads(levdata._get(f"https://data-api.binance.vision/api/v3/klines?symbol={sym}&interval=5m&limit=1000"))
        c5 = [(int(r[0]) // 1000, levdata._path(*map(float, r[1:5]))) for r in k if int(r[0]) // 1000 + 300 <= now]
        return "binance_spot_data_api", bars, c5
    except Exception as e:
        print(sym, "binance data-api unavailable:", str(e)[:100])
    inst = levdata._okx(sym)
    h = json.loads(levdata._get(f"https://www.okx.com/api/v5/market/candles?instId={inst}&bar=1H&limit=300"))["data"]
    k = json.loads(levdata._get(f"https://www.okx.com/api/v5/market/candles?instId={inst}&bar=5m&limit=300"))["data"]
    return ("okx_swap", sorted((int(r[0]) // 1000, *map(float, r[1:5])) for r in h if r[8] == "1"),
            sorted((int(r[0]) // 1000, levdata._path(*map(float, r[1:5]))) for r in k if r[8] == "1"))

def main():
    now = time.time(); ts = iso(now); ms = load(MS) or {}
    rows = []; snap = {}
    for coin, sym in CC["coins"].items():
        try:
            src, bars, c5 = history(sym, now)
            m = ms.get(coin)
            fund, fsrc = levdata.funding_since(now - 5 * 86400, sym)
            crowd, csrc = levdata.crowd_live(sym); fng, gsrc = FNG
            ctx = committee.Context(c5, bars, fund, dict(CC["common"], mmr_pct=CC["common"]["mmr_pct"][sym]), crowd, fng)
            fi = max([x for x in fund if x <= now], default=None)
            snap[coin] = dict(ctx.crowding(int(now) // 300 * 300, fund.get(fi)), symbol=sym, crowd_source=csrc, fng_source=gsrc, funding_source=fsrc,
                              trend_1h=None, ts=ts)
            if m is None:
                p0 = c5[-1][1][-1]
                m = ms[coin] = {"started": iso(c5[-1][0] + 300), "start_price": p0, "last_candle_ts": c5[-1][0], "last_close": p0,
                                "baseline_units": 100 / (p0 * (1 + CC["baseline_cost_pct"] / 100))}
                print(f"committee {coin} started at {p0}")
            new = [(t, p) for t, p in c5 if t > m["last_candle_ts"]]
            price = new[-1][1][-1] if new else m["last_close"]
            for kind, lev in [(k, l) for k in ("rule", "proxy") for l in CC["leverages"]]:
                n = f"com_{coin}_" + ("proxy_" if kind == "proxy" else "") + f"{lev}" + ("" if lev == "mix" else "x")
                cfg = dict(CC["common"], leverage=lev, mmr_pct=CC["common"]["mmr_pct"][sym])
                if lev == "mix": cfg.update(leverage=CC["common"]["mix_base"], sizing="mix")
                if kind == "proxy": cfg["voters"] = "proxy"
                sp = os.path.join(SDIR, f"{n}.json"); st = load(sp); vlog, tlog, evs = [], [], []
                if st is None:   # a line added later starts at the current price
                    st = committee.new_state(cfg); st.update(started=iso(m["last_candle_ts"] + 300), start_price=m["last_close"])
                    print(f"{n} started at {m['last_close']}")
                for t, path in new:
                    evs += committee.step(st, cfg, ctx, t, path, iso(t), fund.get(t, levdata.FUNDING_ASSUMED), vlog, tlog)
                for e in evs:
                    append(os.path.join(LDIR, f"{n}_events.csv"), dict(e, label="PAPER-NOT-REAL"), EV)
                    print(("*** PAPER LIQUIDATION " if e["event"].startswith("LIQ") else "") + f"[{n}]", e)
                if lev == CC["leverages"][0]:
                    for v in vlog:
                        if kind == "rule": append(os.path.join(LDIR, f"committee_votes_{coin}.csv"), dict(v, coin=sym), VOTE_FIELDS)
                        else: append(os.path.join(LDIR, f"committee_proxy_votes_{coin}.csv"), dict(v, coin=sym), PROXY_FIELDS)
                st["last_run"] = ts; save(sp, st)
                val = ta.equity(st, price, cfg); p = st["pos"]
                hold = (100 / (st["start_price"] * 1.0005) if st.get("start_price") else m["baseline_units"]) * price
                row = {"ts": ts, "line": n, "coin": sym, "leverage": lev, "started": st.get("started", m["started"]), "mix_5x_trades": st.get("mix_high_trades", 0), "price": round(price, 6), "source": src, "funding_source": fsrc,
                       "value_usd": round(val, 4), "vs_start_usd": round(val - 100, 4), "vs_hold_usd": round(val - hold, 4),
                       "position": p["side"] if p else "FLAT", "entry": round(p["entry"], 6) if p else "", "stop": round(p["stop"], 6) if p else "",
                       "target": round(p["target"], 6) if p else "", "liq_price": round(ta.liq_price(p, cfg), 6) if p else "",
                       "trades": st["trades"], "wins": st["wins"], "longs": st["longs"], "shorts": st["shorts"], "ties": len(st["ties"]),
                       "decisions": json.dumps(st["decisions"]), "fees_usd": round(st["fees_usd"], 4), "funding_usd": round(st["funding_usd"], 4),
                       "liquidations": st["liquidations"], "max_drawdown_pct": round(st["max_dd_pct"], 2), "hold_value_usd": round(hold, 4),
                       "last_votes": json.dumps({k: vlog[-1][k] for k in (PROXIES if kind == "proxy" else VOTERS)}) if vlog else "",
                       "rules_fired": json.dumps(st.get("rules_fired", {})), "news_flats": st.get("news_flats", 0)}
                append(os.path.join(LDIR, f"{n}_ticks.csv"), row, list(row.keys())); rows.append(row)
            if new: m["last_candle_ts"] = new[-1][0]; m["last_close"] = price
            m.update(last_run=ts, source=src, funding_source=fsrc)
        except Exception as e:
            print(f"committee {coin} tick failed (other coin unaffected):", repr(e))
    save(MS, ms)
    if snap: save(os.path.join(LDIR, "crowding_latest.json"), snap)
    ties = []
    for f in sorted(os.listdir(SDIR)):
        if f.startswith("com_") and f.endswith(".json"):
            for t in load(os.path.join(SDIR, f))["ties"]: ties.append(dict(t, line=f[:-5], user_vote=""))
    if ties:
        fields = ["ts", "line", "price", "atr", "crowded"] + VOTERS + ["if_long_usd", "if_short_usd", "user_vote"]
        with open(os.path.join(LDIR, "committee_ties.csv"), "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(ties)
    if rows: write_md(ms, rows, snap)
    print(json.dumps(rows, indent=1))

def write_md(ms, rows, snap):
    L = [BEGIN, "## Separate lines: COMMITTEE, paper perps on XRP and BTC (`com_*` rule-based, `com_*_proxy_*` team proxies; PAPER-NOT-REAL)", "",
         "Rule-based: long scout, short scout, idle guard, chart reader, with crowding, Fear & Greed and Theo's rules R1-R6 (toggleable). Proxy lines: automated "
         "Casey/Pip/Theo/Remy following each teammate's spec. Votes every 15 min; 3 of 4 must agree to open; a 2-2 LONG/SHORT split is a tie "
         "(stay flat, logged to `leverage/logs/committee_ties.csv` with shadow outcomes). $100 each, isolated margin; same costs/funding/liquidation as leverage_ta.", "",
         "| Line | Started | **Value (USD, if closed now)** | Change vs $100 | **vs holding the coin** | Position (entry / stop / target / liq) | Trades (wins) | Longs / shorts | Ties | Fees + funding | **Liquidations** | Max drawdown | Last votes |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        coin = r["line"].split("_")[1]
        pos = f"{r['position']} ({r['entry']} / {r['stop']} / {r['target']} / {r['liq_price']})" if r["position"] != "FLAT" else "FLAT"
        L.append(f"| `{r['line']}`{' (5x trades: ' + str(r['mix_5x_trades']) + ')' if r['line'].endswith('mix') else ''} | {r['started']} | **${r['value_usd']:.2f}** | {r['vs_start_usd']:+.2f} | **{r['vs_hold_usd']:+.2f}** | {pos} | "
                 f"{r['trades']} ({r['wins']}) | {r['longs']} / {r['shorts']} | {r['ties']} | ${r['fees_usd'] + r['funding_usd']:.2f} | **{r['liquidations']}** | {r['max_drawdown_pct']:.1f}% | {r['last_votes'] or '—'} |")
    for coin, c in snap.items():
        L.append(f"- Crowding {c['symbol']} now: funding {c['funding_pct']}%/8h, OI 24h {c['oi_24h_pct']}%, long/short accounts {c['ls_ratio']} "
                 f"({c['ls_pctile']}th pct of 7d), Fear & Greed {c['fng']} -> **{c['crowded'] or 'not crowded'}** (sources: {c['crowd_source']}, {c['fng_source']})")
    L += ["", "Mix = 2x, stepping to 5x only on strong reads (4/4 agree, or avg confidence >= 0.75 with 1h and 4h trends aligned). "
          "Crowding = >= 2 of funding extreme, OI +5%/24h, long/short ratio extreme vs 7 days, Fear & Greed extreme.",
          "", "Backtest: `leverage/backtest_committee_output.txt`. Team committee (human/agent votes): `leverage/team/TEAM_SUMMARY.md`.", END]
    md = "\n".join(L) + "\n"
    open(os.path.join(HERE, "SUMMARY_COMMITTEE.md"), "w").write(md)
    p = os.path.join(ROOT, "SUMMARY.md"); s = open(p).read() if os.path.exists(p) else ""
    if BEGIN in s: s = s[:s.index(BEGIN)].rstrip("\n") + "\n" + (s[s.index(END) + len(END):].lstrip("\n") if END in s else "")
    open(p, "w").write(s.rstrip("\n") + "\n\n" + md)

if __name__ == "__main__":
    main()
