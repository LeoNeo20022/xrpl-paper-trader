#!/usr/bin/env python3
"""PAPER-ONLY 'team committee' ledger: takes LONG / SHORT / IDLE votes from teammates (Casey, Pip, Theo, Remy) written to a
shared file on the box, applies the same 3-of-4 rule and tie handling as the rule-based committee, and simulates positions
with the same engine (ta.py: fees, slippage, funding both ways, isolated-margin liquidation). No keys, orders or wallets.

Run on the box (teammates write to the box, not GitHub), e.g. every 15 min:
    python3 leverage/team_committee.py [--votes /home/box/shared/strategy-lab/votes.csv] [--commit]
Votes file columns: timestamp_utc,voter,coin,call,confidence,stop_price,note   (see the README next to it)
Rules:
- Rounds every 15 min (:00 :15 :30 :45 UTC), per coin. A voter's call = its LATEST row for that coin timestamped strictly
  before the round and no more than 60 min before it. No valid row = IDLE ("no vote").
- Rows timestamped in the future, or before a round this script has already processed (backdated), are rejected and listed in
  leverage/team/rejected_votes.csv.
- >= 3 of 4 LONG (or SHORT) -> the team opens if flat. Exactly 2 LONG vs 2 SHORT -> TIE: flat, logged to team_ties.csv with
  shadow 'if long' / 'if short' results (48h max); the same set of votes is logged as one tie, not every round. Anything else -> stay out.
- Stops: team = median stop_price of the agreeing voters that is on the right side of price and within 25%; otherwise
  1.5 x 1h ATR(14). Target = 2 x the stop distance. One position at a time per account.
- Scoring: team at 2x and 5x per coin; each voter's OWN account (opens on its own LONG/SHORT call with its own stop, 2:1 target);
  the rule-based committee live lines (com_*); staying idle ($100, $0); holding the coin since this ledger started.
- Missing votes: a voter with no valid row for a round is replaced by its automated PROXY (committee.proxy_votes, built
  from each teammate's spec: Casey = long trigger + R1/R3, Pip = crowded-longs short below the 4h EMA200, Theo = R2/R4/R6,
  Remy = structure + R3). Proxy calls are marked "(proxy)" in team_decisions.csv. Each voter account follows the voter's
  effective call (own row if present, else proxy).
- 'mix' team account: 2x, or 5x when all 4 agree, or the agreeing voters' average confidence (blank = 0.5) >= 0.75 with the
  1h (EMA50 vs EMA200) and 4h (EMA20 vs EMA50) trends aligned.
- Each run writes the latest crowding snapshot (funding, OI change, long/short account ratio, Fear & Greed) to
  /home/box/shared/strategy-lab/crowding.json and crowding.md so voters can read it before voting; it is also logged per round."""
import json, os, csv, sys, time, hashlib, subprocess, statistics
from datetime import datetime, timezone
import ta, committee, levdata, stars
from committee_runner import history
FNG = levdata.fear_greed()

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "team"); STATE = os.path.join(OUT, "team_state.json")
VOTES_DEFAULT = "/home/box/shared/strategy-lab/votes.csv"
CC = json.load(open(os.path.join(HERE, "committee_config.json")))
COINS = {"XRP": "XRPUSDT", "BTC": "BTCUSDT"}; VOTERS = ["casey", "pip", "theo", "remy"]; LEVS = [2, 5]
SHARED = "/home/box/shared/strategy-lab"
VALID_MIN = 60; ROUND = 900
EV = ["ts", "account", "event", "price", "qty_xrp", "notional_usd", "margin_usd", "fee_usd", "stop", "target", "liq_price", "why",
      "trade_net_usd", "funding_usd", "rate", "margin_lost_usd", "label"]

def iso(u): return datetime.fromtimestamp(u, timezone.utc).isoformat(timespec="seconds")
def parse_ts(s):
    d = datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
    return (d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp()
def append(p, row, fields):
    new = not os.path.exists(p)
    with open(p, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if new: w.writeheader()
        w.writerow(row)

def read_votes(path, st, now):
    ok, bad = [], []
    if not os.path.exists(path): return ok, bad
    with open(path, newline="") as f:
        for n, r in enumerate(csv.DictReader(f), start=2):
            h = hashlib.sha1(json.dumps(r, sort_keys=True).encode()).hexdigest()
            try:
                t = parse_ts(r["timestamp_utc"]); v = r["voter"].strip().lower(); c = r["coin"].strip().upper(); call = r["call"].strip().upper()
                if v not in VOTERS: raise ValueError(f"unknown voter {v!r}")
                if c not in COINS: raise ValueError(f"coin must be XRP or BTC, got {c!r}")
                if call not in ("LONG", "SHORT", "IDLE"): raise ValueError(f"call must be LONG/SHORT/IDLE, got {call!r}")
                conf = float(r["confidence"]) if (r.get("confidence") or "").strip() else None
                if conf is not None and not 0 <= conf <= 1: raise ValueError("confidence must be 0-1")
                sp = float(r["stop_price"]) if (r.get("stop_price") or "").strip() else None
                if t > now + 60: raise ValueError("timestamp is in the future")
                if h not in st["seen"]:
                    last_round = st["coins"].get(c, {}).get("last_round_ts")
                    if last_round is not None and t < last_round: raise ValueError(f"backdated: arrived after round {iso(last_round)} already ran")
                    st["seen"][h] = iso(now)
                ok.append({"t": t, "voter": v, "coin": c, "call": call, "confidence": conf, "stop_price": sp, "note": (r.get("note") or "").strip(), "line": n})
            except Exception as e:
                if h in st["seen"] and "backdated" not in str(e): continue
                st["seen"].setdefault(h, "rejected")
                bad.append({"line": n, "row": json.dumps(r), "reason": str(e)})
    return ok, bad

def call_at(votes, coin, voter, T):
    vs = [v for v in votes if v["coin"] == coin and v["voter"] == voter and T - VALID_MIN * 60 <= v["t"] < T]
    return max(vs, key=lambda v: (v["t"], v["line"])) if vs else None

def stop_dist(side, price, stops, atr, lev=2):
    good = [s for s in stops if s and ((s < price) if side == "LONG" else (s > price)) and abs(price - s) / price <= 0.25]
    d, how = (abs(price - statistics.median(good)), "voter stop") if good else (1.5 * atr, "1.5x ATR")
    if lev >= 5 and d > min(2 * atr, 0.10 * price):   # Theo R5: at 5x the stop is at most 2x ATR and 10% from entry
        d, how = min(2 * atr, 0.10 * price), how + " capped by R5"
    return d, how

def new_acct(): return committee.new_state(dict(CC["common"], budget_usd=100))

def main():
    now = time.time(); args = sys.argv[1:]
    vpath = args[args.index("--votes") + 1] if "--votes" in args else VOTES_DEFAULT
    os.makedirs(OUT, exist_ok=True)
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"started": iso(now), "seen": {}, "coins": {}, "accounts": {}}
    votes, bad = read_votes(vpath, st, now)
    with open(os.path.join(OUT, "rejected_votes.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["line", "reason", "row"]); w.writeheader(); w.writerows(bad)
    with open(os.path.join(OUT, "votes_accepted.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["timestamp_utc", "voter", "coin", "call", "confidence", "stop_price", "note"]); w.writeheader()
        for v in sorted(votes, key=lambda v: v["t"]): w.writerow({"timestamp_utc": iso(v["t"]), **{k: v[k] for k in ("voter", "coin", "call", "confidence", "stop_price", "note")}})
    score = []; snaps = {}
    try:   # Stars Aligned (4/4, 10x XRP): failure-isolated, never blocks the 3-of-4 lines
        S = st.setdefault("stars", {"started": None, "accounts": {}, "unanimous": 0, "real_votes": 0, "proxy_votes": 0, "all_real": 0,
                                    "opened": 0, "blackout_skips": 0, "in_position_skips": 0})
        for b in stars.BUDGETS: S["accounts"].setdefault(stars.name(b), ta.new_state(stars.cfg(CC["common"], b)))
    except Exception as e:
        print("stars setup failed (other lines unaffected):", repr(e)); S = None
    for coin, sym in COINS.items():
        try:
            src, bars, c5 = history(sym, now)
            cs = st["coins"].get(coin)
            if cs is None:
                p0 = c5[-1][1][-1]
                cs = st["coins"][coin] = {"started": iso(c5[-1][0] + 300), "start_price": p0, "last_candle_ts": c5[-1][0], "last_close": p0, "last_round_ts": None}
            fund, fsrc = levdata.funding_since(now - 5 * 86400, sym)
            crowd, csrc = levdata.crowd_live(sym)
            ctx = committee.Context(c5, bars, fund, dict(CC["common"], mmr_pct=CC["common"]["mmr_pct"][sym]), crowd, FNG[0])
            fi = max([x for x in fund if x <= now], default=None)
            snaps[coin] = dict(ctx.crowding(int(now) // 300 * 300, fund.get(fi)), symbol=sym, sources=f"crowd {csrc}, F&G {FNG[1]}, funding {fsrc}", ts=iso(now),
                               trend_1h=ctx.trend4h and ("up" if ctx.e50[-1] > ctx.e200[-1] else "down"), trend_4h=ctx.trend4h(int(now) // 3600 * 3600))
            ind = ta.indicators(bars, dict(CC["common"], rsi_long_below=40, rsi_short_above=60))   # only ATR is used here
            atr_at = lambda T: (ind.get(max([k for k in ind if k <= T], default=None)) or {}).get("atr")
            names = [f"team_{coin}_{l}x" for l in LEVS] + [f"team_{coin}_mix"] + [f"{v}_{coin}_{l}x" for v in VOTERS for l in LEVS]
            for n in names: st["accounts"].setdefault(n, new_acct())
            new = [(t, p) for t, p in c5 if t > cs["last_candle_ts"]]
            for t, path in new:
                tsx = iso(t); rate = fund.get(t, levdata.FUNDING_ASSUMED); sig = {}
                if t % 28800 == 0:
                    for n in names:
                        a = st["accounts"][n]
                        if t > (a.get("last_funding_ts") or 0):
                            e = ta.funding(a, t, rate, path[0], tsx)
                            if e: append(os.path.join(OUT, "team_events.csv"), dict(e, account=n, label="PAPER-NOT-REAL"), EV)
                            for sh in a["shadows"]: ta.funding(sh["st"], t, rate, path[0], tsx)
                if t % ROUND == 0:
                    cs["last_round_ts"] = t; atr = atr_at(t); price = path[0]
                    calls = {v: call_at(votes, coin, v, t) for v in VOTERS}
                    ptrend = {}; pcr = {}
                    if ctx.ready(t):
                        _, PV, _, pcr, ptrend = committee.proxy_votes(ctx, t)
                        for v in VOTERS:
                            if calls[v] is None:
                                calls[v] = {"t": t, "voter": v, "coin": coin, "call": PV[v][0], "confidence": PV[v][2] or None,
                                            "stop_price": None, "note": "proxy: " + PV[v][1], "line": -1, "proxy": True}
                    cv = {v: (c["call"] if c else "IDLE") for v, c in calls.items()}
                    nl = sum(x == "LONG" for x in cv.values()); ns = sum(x == "SHORT" for x in cv.values())
                    dec = "LONG" if nl >= 3 else "SHORT" if ns >= 3 else "TIE" if nl == 2 and ns == 2 else "IDLE"
                    crw = ctx.crowding(t, fund.get(max([x for x in fund if x <= t], default=None)))
                    if any(c and not c.get("proxy") for c in calls.values()) or (calls and dec != "IDLE"):
                        append(os.path.join(OUT, "team_decisions.csv"), {"ts": tsx, "coin": coin, "price": price, "decision": dec,
                               **{f"crowd_{k}": crw.get(k) for k in ("funding_pct", "oi_24h_pct", "ls_ratio", "ls_pctile", "fng", "crowded")},
                               **{v: (f"{c['call']} ({c['confidence']})" + (" (proxy)" if c.get("proxy") else "") if c else "IDLE (no vote)") for v, c in calls.items()},
                               **{f"{v}_note": (c["note"] if c else "") for v, c in calls.items()}},
                               ["ts", "coin", "price", "decision"] + VOTERS + [f"{v}_note" for v in VOTERS]
                               + [f"crowd_{k}" for k in ("funding_pct", "oi_24h_pct", "ls_ratio", "ls_pctile", "fng", "crowded")])
                    if coin == "XRP" and S is not None:
                        try:
                            scalls = stars.standins(calls, pcr, ptrend.get("ema200_4h"), CC["common"])   # Stars-only stand-ins
                            side = stars.unanimous(scalls)
                            if side:
                                nr = sum(1 for c in scalls.values() if c and not c.get("proxy")); S["unanimous"] += 1
                                S["real_votes"] += nr; S["proxy_votes"] += 4 - nr; S["all_real"] += nr == 4
                                busy = any(a["pos"] for a in S["accounts"].values())
                                action = "IN_POSITION" if busy else "OPEN"   # no news blackout for Stars (removed 2026-10-27)
                                if action == "OPEN":
                                    S["opened"] += 1
                                    for b in stars.BUDGETS: sig[stars.name(b)] = stars.signal(t, price, side, f"stars 4/4 {side} ({nr} real, {4 - nr} proxy)")
                                else: S["blackout_skips" if action == "NEWS_BLACKOUT" else "in_position_skips"] += 1
                                reason = {"IN_POSITION": "already in a Stars trade", "NEWS_BLACKOUT": "news blackout (3h of a calendar event or high news item)"}.get(action, "")
                                row = {"ts_utc": tsx, "direction": side, "result": "OPENED" if action == "OPEN" else "BLOCKED", "block_reason": reason,
                                       "price_at_vote": price, "real_votes": nr, "proxy_votes": 4 - nr}
                                for v in VOTERS:
                                    c = scalls[v]; row.update({f"{v}_call": c["call"], f"{v}_source": ("stars stand-in" if c.get("standin") else "proxy") if c.get("proxy") else "real",
                                                              f"{v}_conf": "" if c.get("confidence") is None else c["confidence"], f"{v}_note": c.get("note", "")})
                                S.setdefault("log", []).append(row)
                                if action == "OPEN": S["open_row"] = len(S["log"]) - 1
                        except Exception as e: print("stars round failed (other lines unaffected):", repr(e))
                    if atr:
                        for l in LEVS + ["mix"]:
                            an = f"team_{coin}_{l}" + ("" if l == "mix" else "x"); a = st["accounts"][an]; a["decisions"][dec] += 1
                            if dec in ("LONG", "SHORT") and not a["pos"]:
                                d, how = stop_dist(dec, price, [c["stop_price"] for c in calls.values() if c and c["call"] == dec], atr, 5 if l in (5, "mix") else l)
                                sig[an] = {t: {"signal": dec, "atr": d / 1.5, "trend": "", "why": f"team {'+'.join(v for v in VOTERS if cv[v] == dec)}, {how}"}}
                                if l == "mix":
                                    tr = ptrend
                                    confs = [c["confidence"] if c["confidence"] is not None else 0.5 for c in calls.values() if c and c["call"] == dec]
                                    lv, avg, al = committee.mix_leverage(dict(CC["common"]), dec, confs, len(confs), tr)
                                    if lv < 5: d, how = stop_dist(dec, price, [c["stop_price"] for c in calls.values() if c and c["call"] == dec], atr, 2); sig[an][t]["atr"] = d / 1.5
                                    sig[an][t].update(leverage=lv, why=sig[an][t]["why"] + f", mix {lv}x (avg conf {avg}, trends aligned {al})")
                            elif dec == "TIE" and not a["pos"] and l != "mix" and a.get("last_tie_key") != json.dumps({v: c["line"] for v, c in calls.items() if c}):
                                a["last_tie_key"] = json.dumps({v: c["line"] for v, c in calls.items() if c})   # one tie per distinct set of votes
                                cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym])
                                tie = {"ts": tsx, "coin": coin, "leverage": l, "price": price, **{v: cv[v] for v in VOTERS}}
                                for side in ("LONG", "SHORT"):
                                    s = ta.new_state(dict(cfg, budget_usd=100)); ta.open_pos(s, cfg, side, price, atr, tsx, "shadow")
                                    a["shadows"].append({"tie_ts": tsx, "side": side, "opened_t": t, "st": s})
                                a["ties"].append(tie)
                            for v in (VOTERS if l != "mix" else []):   # voters have 2x/5x accounts only
                                c = calls[v]; b = st["accounts"][f"{v}_{coin}_{l}x"]
                                if c and c["call"] in ("LONG", "SHORT") and not b["pos"]:
                                    d, how = stop_dist(c["call"], price, [c["stop_price"]], atr, l)
                                    sig[f"{v}_{coin}_{l}x"] = {t: {"signal": c["call"], "atr": d / 1.5, "trend": "", "why": f"{v}{' proxy' if c.get('proxy') else ''} call, {how}"}}
                for n in names:
                    l = 2 if n.endswith("mix") else int(n.split("_")[-1][:-1]); cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym]); a = st["accounts"][n]
                    for e in ta.step(a, cfg, t, list(path), sig.get(n, {}), tsx):
                        if e["event"].startswith(("STOP_LOSS", "LIQUIDATION")): a["last_stop_ts"] = t + 300
                        append(os.path.join(OUT, "team_events.csv"), dict(e, account=n, label="PAPER-NOT-REAL"), EV)
                    keep = []
                    for sh in a["shadows"]:
                        if committee._shadow_step(sh, cfg, t, path, tsx):
                            for tie in a["ties"]:
                                if tie["ts"] == sh["tie_ts"]: tie[f"if_{sh['side'].lower()}_usd"] = round(sh["st"]["cash"] - 100, 4)
                        else: keep.append(sh)
                    a["shadows"] = keep
                if coin == "XRP" and S is not None:
                    try:
                        if S["started"] is None: S["started"] = tsx; S["start_price"] = path[0]
                        for b in stars.BUDGETS:
                            n = stars.name(b); a = S["accounts"][n]; scfg = stars.cfg(CC["common"], b)
                            if t % 28800 == 0 and t > (a.get("last_funding_ts") or 0):
                                e = ta.funding(a, t, rate, path[0], tsx)
                                if e: append(os.path.join(OUT, "team_events.csv"), dict(e, account=n, label="PAPER-NOT-REAL"), EV)
                            pre = a["pos"]["start_cash"] if a["pos"] else a["cash"]
                            for e in ta.step(a, scfg, t, list(path), sig.get(n, {}), tsx):
                                append(os.path.join(OUT, "team_events.csv"), dict(e, account=n, label="PAPER-NOT-REAL"), EV)
                                r = S["log"][S["open_row"]] if S.get("open_row") is not None and S["open_row"] < len(S.get("log", [])) else None
                                if r is None: continue
                                if e["event"].startswith("OPEN_"): r["entry_price"] = e["price"]; r[f"liq_price_{b}"] = e.get("liq_price", "")
                                elif e["event"].startswith(("TAKE_PROFIT", "STOP_LOSS", "LIQUIDATION")):
                                    r.update(exit_ts_utc=tsx, exit_price=e["price"], exit_reason=e["event"].rsplit("_", 1)[0])
                                    r[f"pnl_{b}"] = e["trade_net_usd"] if "trade_net_usd" in e else round(-pre, 4)
                        if S.get("open_row") is not None and all(not S["accounts"][stars.name(b)]["pos"] for b in stars.BUDGETS) \
                                and "exit_price" in S["log"][S["open_row"]]: S["open_row"] = None
                    except Exception as e: print("stars step failed (other lines unaffected):", repr(e))
            if new: cs["last_candle_ts"] = new[-1][0]; cs["last_close"] = new[-1][1][-1]
            price = cs["last_close"]; hold = 100 / (cs["start_price"] * 1.0005) * price
            for n in names:
                l = "mix" if n.endswith("mix") else int(n.split("_")[-1][:-1]); cfg = dict(CC["common"], leverage=2 if l == "mix" else l, mmr_pct=CC["common"]["mmr_pct"][sym]); a = st["accounts"][n]
                score.append({"account": n, "who": n.split("_")[0], "coin": coin, "lev": l, "value": ta.equity(a, price, cfg), "hold": hold,
                              "trades": a["trades"], "wins": a["wins"], "longs": a["longs"], "shorts": a["shorts"], "liq": a["liquidations"],
                              "dd": a["max_dd_pct"], "fees": a["fees_usd"] + a["funding_usd"], "pos": a["pos"]["side"] if a["pos"] else "FLAT", "ties": len(a["ties"])})
            for l in [f"{x}" for x in LEVS + ["mix"]] + [f"proxy_{x}" for x in LEVS + ["mix"]]:   # committee live lines (rule-based and proxy) (Actions), own start date
                p = os.path.join(HERE, "state", f"com_{coin.lower()}_{l}" + ("" if l.endswith("mix") else "x") + ".json"); mp = os.path.join(HERE, "state", "committee_market.json")
                if os.path.exists(p) and os.path.exists(mp):
                    a = json.load(open(p)); m = json.load(open(mp)).get(coin.lower(), {})
                    cfg = dict(CC["common"], leverage=2 if l.endswith("mix") else int(l.split("_")[-1]), mmr_pct=CC["common"]["mmr_pct"][sym])
                    score.append({"account": f"com_{coin.lower()}_{l}" + ("" if l.endswith("mix") else "x"), "who": "proxy committee (Actions)" if l.startswith("proxy") else "rule-based committee", "coin": coin, "lev": l, "value": ta.equity(a, price, cfg),
                                  "hold": m.get("baseline_units", 0) * price, "trades": a["trades"], "wins": a["wins"], "longs": a["longs"], "shorts": a["shorts"],
                                  "liq": a["liquidations"], "dd": a["max_dd_pct"], "fees": a["fees_usd"] + a["funding_usd"], "pos": a["pos"]["side"] if a["pos"] else "FLAT",
                                  "ties": len(a["ties"]), "note": f"since {m.get('started')}"})
            score.append({"account": f"idle_{coin}", "who": "stay idle", "coin": coin, "lev": "—", "value": 100.0, "hold": hold, "trades": 0, "wins": 0,
                          "longs": 0, "shorts": 0, "liq": 0, "dd": 0.0, "fees": 0.0, "pos": "FLAT", "ties": 0})
        except Exception as e:
            print(f"team committee {coin} failed (other coin unaffected):", repr(e))
    ties = [dict(t, account=n, user_vote="") for n, a in st["accounts"].items() if n.startswith("team_") for t in a["ties"]]
    with open(os.path.join(OUT, "team_ties.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["ts", "account", "coin", "leverage", "price"] + VOTERS + ["if_long_usd", "if_short_usd", "user_vote"], extrasaction="ignore")
        w.writeheader(); w.writerows(ties)
    json.dump(st, open(STATE, "w"), indent=1)
    if snaps:
        json.dump(snaps, open(os.path.join(OUT, "crowding_latest.json"), "w"), indent=1)
        md = ["# Crowding snapshot (read before voting)", "", f"Updated {iso(now)}. PAPER research data, not advice.", "",
              "| Coin | Funding %/8h | OI change 24h % | Long/short accounts | L/S percentile (7d) | Fear & Greed | Crowded? | 1h trend | 4h trend |", "|---|---|---|---|---|---|---|---|---|"]
        for c, x in snaps.items():
            md.append(f"| {c} | {x['funding_pct']} | {x['oi_24h_pct']} | {x['ls_ratio']} | {x['ls_pctile']} | {x['fng']} | **{x['crowded'] or 'no'}** | {x['trend_1h']} | {x['trend_4h']} |")
        md += ["", "Crowded longs = at least 2 of: funding >= +0.03%/8h, OI up >= 5% in 24h, long/short account ratio >= 80th percentile of 7 days, "
               "Fear & Greed > 75. Crowded shorts mirror (funding <= -0.01%, OI up >= 5%, ratio <= 20th percentile, Fear & Greed < 25). "
               "Crowded sides often unwind in liquidation cascades: the rule-based idle guard won't join the crowd and the opposite scout gets a contrarian trigger.",
               "", f"Sources: {'; '.join(c + ': ' + x['sources'] for c, x in snaps.items())}"]
        try:
            os.makedirs(SHARED, exist_ok=True)
            for fn, body in (("crowding.json", json.dumps(snaps, indent=1)), ("crowding.md", "\n".join(md) + "\n")):
                p = os.path.join(SHARED, fn); open(p, "w").write(body); os.chmod(p, 0o666)
        except Exception as e: print("could not write shared crowding snapshot:", e)
    L = ["# Team committee ledger (PAPER-NOT-REAL)", "",
         f"Votes file on the box: `{vpath}`. Ledger started {st['started']}; last run {iso(now)}. Accepted votes: {len(votes)}, rejected: {len(bad)} "
         "(see `rejected_votes.csv`). 3 of 4 must agree; 2-2 LONG/SHORT = tie (flat, shadows in `team_ties.csv`). $100 per account, isolated margin, "
         "same fees/funding/liquidation as leverage_ta. Value = if closed now.", "",
         "| Account | Who | Coin | Lev | **Value** | **P/L** | vs holding the coin | Trades (wins) | Longs/shorts | Ties | Fees+funding | Liquidations | Max DD | Now |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in score:
        L.append(f"| `{r['account']}` | {r['who']}{' (' + r['note'] + ')' if r.get('note') else ''} | {r['coin']} | {r['lev']} | **${r['value']:.2f}** | **{r['value'] - 100:+.2f}** | "
                 f"{r['value'] - r['hold']:+.2f} | {r['trades']} ({r['wins']}) | {r['longs']}/{r['shorts']} | {r['ties']} | ${r['fees']:.2f} | {r['liq']} | {r['dd']:.1f}% | {r['pos']} |")
    try:   # every 4/4 moment (opened or blocked), with exit and P/L per size once closed: shared log + repo copy
        if S is not None:
            F = ["ts_utc", "direction", "result", "block_reason", "price_at_vote", "entry_price", "exit_ts_utc", "exit_price", "exit_reason"] + \
                [f"pnl_{b}" for b in stars.BUDGETS] + [f"liq_price_{b}" for b in stars.BUDGETS] + ["real_votes", "proxy_votes"] + \
                [f"{v}_{k}" for v in VOTERS for k in ("call", "source", "conf", "note")]
            for fp in (os.path.join(SHARED, "stars_aligned_log.csv"), os.path.join(OUT, "stars_aligned_log.csv")):
                try:
                    with open(fp, "w", newline="") as f:
                        w = csv.DictWriter(f, fieldnames=F, extrasaction="ignore"); w.writeheader(); w.writerows(S.get("log", []))
                except Exception as e: print("stars log write failed:", fp, repr(e))
    except Exception as e: print("stars log failed (other lines unaffected):", repr(e))
    try:
        if S is not None and S.get("started"):
            px = st["coins"]["XRP"]["last_close"]
            L += ["", "## Stars Aligned (curiosity line, PAPER-NOT-REAL): XRP 10x, only on a 4 of 4 vote", "",
                  f"Started {S['started']}. TP +{stars.TP_PCT:g}% / stop -{stars.STOP_PCT:g}% price move, isolated margin, Binance-style XRPUSDT rules (offshore-rules paper only; "
                  "Kraken US's 17% maintenance margin cannot do 10x). No news blackout. Stars-only stand-ins: Casey's proxy may vote SHORT (4h below EMA200 + crowded longs), Pip's may vote LONG (4h above EMA200, crowding clear, funding calm). "
                  f"Unanimous rounds: {S['unanimous']} (votes real {S['real_votes']} / proxy {S['proxy_votes']}; all-real rounds {S['all_real']}); "
                  f"opened {S['opened']}, skipped for news {S['blackout_skips']}, already in a trade {S['in_position_skips']}. Every 4/4 moment: `/home/box/shared/strategy-lab/stars_aligned_log.csv` (copy: `leverage/team/stars_aligned_log.csv`).", "",
                  "| Account | Value | P/L | Trades (wins) | Longs/shorts | Fees+funding | Liquidations | Max DD | Now |", "|---|---|---|---|---|---|---|---|---|"]
            for b in stars.BUDGETS:
                n = stars.name(b); a = S["accounts"][n]; v = ta.equity(a, px, stars.cfg(CC["common"], b))
                L.append(f"| `{n}` | ${v:.2f} | {v - b:+.2f} | {a['trades']} ({a['wins']}) | {a['longs']}/{a['shorts']} | ${a['fees_usd'] + a['funding_usd']:.2f} | "
                         f"{a['liquidations']} | {a['max_dd_pct']:.1f}% | {a['pos']['side'] if a['pos'] else 'FLAT'} |")
    except Exception as e: print("stars summary failed (other lines unaffected):", repr(e))
    open(os.path.join(OUT, "TEAM_SUMMARY.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    if "--commit" in args:
        g = lambda *c: subprocess.run(["git", "-C", ROOT, *c], capture_output=True, text=True)
        g("pull", "--rebase", "--autostash", "-q"); g("add", "leverage/team")
        if g("diff", "--cached", "--quiet").returncode:
            g("commit", "-q", "-m", f"team committee ledger {iso(now)}")
            env = {k: v for k, v in os.environ.items() if k != "GH_TOKEN"}
            r = subprocess.run(["git", "-C", ROOT, "-c", "credential.helper=", "-c", "credential.helper=!env -u GH_TOKEN gh auth git-credential", "push", "origin", "HEAD"],
                               capture_output=True, text=True, env=env)
            print("push:", r.returncode, r.stderr.strip()[-200:])

if __name__ == "__main__":
    main()
