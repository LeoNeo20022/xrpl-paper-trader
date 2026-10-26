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
  the rule-based committee live lines (com_*); staying idle ($100, $0); holding the coin since this ledger started."""
import json, os, csv, sys, time, hashlib, subprocess, statistics
from datetime import datetime, timezone
import ta, committee, levdata
from committee_runner import history

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "team"); STATE = os.path.join(OUT, "team_state.json")
VOTES_DEFAULT = "/home/box/shared/strategy-lab/votes.csv"
CC = json.load(open(os.path.join(HERE, "committee_config.json")))
COINS = {"XRP": "XRPUSDT", "BTC": "BTCUSDT"}; VOTERS = ["casey", "pip", "theo", "remy"]; LEVS = [2, 5]
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

def stop_dist(side, price, stops, atr):
    good = [s for s in stops if s and ((s < price) if side == "LONG" else (s > price)) and abs(price - s) / price <= 0.25]
    return (abs(price - statistics.median(good)), "voter stop") if good else (1.5 * atr, "1.5x ATR")

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
    score = []
    for coin, sym in COINS.items():
        try:
            src, bars, c5 = history(sym, now)
            cs = st["coins"].get(coin)
            if cs is None:
                p0 = c5[-1][1][-1]
                cs = st["coins"][coin] = {"started": iso(c5[-1][0] + 300), "start_price": p0, "last_candle_ts": c5[-1][0], "last_close": p0, "last_round_ts": None}
            fund, _ = levdata.funding_since(now - 5 * 86400, sym)
            ind = ta.indicators(bars, dict(CC["common"], rsi_long_below=40, rsi_short_above=60))   # only ATR is used here
            atr_at = lambda T: (ind.get(max([k for k in ind if k <= T], default=None)) or {}).get("atr")
            names = [f"team_{coin}_{l}x" for l in LEVS] + [f"{v}_{coin}_{l}x" for v in VOTERS for l in LEVS]
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
                    cv = {v: (c["call"] if c else "IDLE") for v, c in calls.items()}
                    nl = sum(x == "LONG" for x in cv.values()); ns = sum(x == "SHORT" for x in cv.values())
                    dec = "LONG" if nl >= 3 else "SHORT" if ns >= 3 else "TIE" if nl == 2 and ns == 2 else "IDLE"
                    if any(calls.values()):
                        append(os.path.join(OUT, "team_decisions.csv"), {"ts": tsx, "coin": coin, "price": price, "decision": dec,
                               **{v: (f"{c['call']} ({c['confidence']})" if c else "IDLE (no vote)") for v, c in calls.items()},
                               **{f"{v}_note": (c["note"] if c else "") for v, c in calls.items()}},
                               ["ts", "coin", "price", "decision"] + VOTERS + [f"{v}_note" for v in VOTERS])
                    if atr:
                        for l in LEVS:
                            a = st["accounts"][f"team_{coin}_{l}x"]; a["decisions"][dec] += 1
                            if dec in ("LONG", "SHORT") and not a["pos"]:
                                d, how = stop_dist(dec, price, [c["stop_price"] for c in calls.values() if c and c["call"] == dec], atr)
                                sig[f"team_{coin}_{l}x"] = {t: {"signal": dec, "atr": d / 1.5, "trend": "", "why": f"team {'+'.join(v for v in VOTERS if cv[v] == dec)}, {how}"}}
                            elif dec == "TIE" and not a["pos"] and a.get("last_tie_key") != json.dumps({v: c["line"] for v, c in calls.items() if c}):
                                a["last_tie_key"] = json.dumps({v: c["line"] for v, c in calls.items() if c})   # one tie per distinct set of votes
                                cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym])
                                tie = {"ts": tsx, "coin": coin, "leverage": l, "price": price, **{v: cv[v] for v in VOTERS}}
                                for side in ("LONG", "SHORT"):
                                    s = ta.new_state(dict(cfg, budget_usd=100)); ta.open_pos(s, cfg, side, price, atr, tsx, "shadow")
                                    a["shadows"].append({"tie_ts": tsx, "side": side, "opened_t": t, "st": s})
                                a["ties"].append(tie)
                            for v in VOTERS:
                                c = calls[v]; b = st["accounts"][f"{v}_{coin}_{l}x"]
                                if c and c["call"] in ("LONG", "SHORT") and not b["pos"]:
                                    d, how = stop_dist(c["call"], price, [c["stop_price"]], atr)
                                    sig[f"{v}_{coin}_{l}x"] = {t: {"signal": c["call"], "atr": d / 1.5, "trend": "", "why": f"{v} call, {how}"}}
                for n in names:
                    l = int(n.split("_")[-1][:-1]); cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym]); a = st["accounts"][n]
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
            if new: cs["last_candle_ts"] = new[-1][0]; cs["last_close"] = new[-1][1][-1]
            price = cs["last_close"]; hold = 100 / (cs["start_price"] * 1.0005) * price
            for n in names:
                l = int(n.split("_")[-1][:-1]); cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym]); a = st["accounts"][n]
                score.append({"account": n, "who": n.split("_")[0], "coin": coin, "lev": l, "value": ta.equity(a, price, cfg), "hold": hold,
                              "trades": a["trades"], "wins": a["wins"], "longs": a["longs"], "shorts": a["shorts"], "liq": a["liquidations"],
                              "dd": a["max_dd_pct"], "fees": a["fees_usd"] + a["funding_usd"], "pos": a["pos"]["side"] if a["pos"] else "FLAT", "ties": len(a["ties"])})
            for l in LEVS:   # rule-based committee live line (Actions), own start date
                p = os.path.join(HERE, "state", f"com_{coin.lower()}_{l}x.json"); mp = os.path.join(HERE, "state", "committee_market.json")
                if os.path.exists(p) and os.path.exists(mp):
                    a = json.load(open(p)); m = json.load(open(mp)).get(coin.lower(), {})
                    cfg = dict(CC["common"], leverage=l, mmr_pct=CC["common"]["mmr_pct"][sym])
                    score.append({"account": f"com_{coin.lower()}_{l}x", "who": "rule-based committee", "coin": coin, "lev": l, "value": ta.equity(a, price, cfg),
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
    L = ["# Team committee ledger (PAPER-NOT-REAL)", "",
         f"Votes file on the box: `{vpath}`. Ledger started {st['started']}; last run {iso(now)}. Accepted votes: {len(votes)}, rejected: {len(bad)} "
         "(see `rejected_votes.csv`). 3 of 4 must agree; 2-2 LONG/SHORT = tie (flat, shadows in `team_ties.csv`). $100 per account, isolated margin, "
         "same fees/funding/liquidation as leverage_ta. Value = if closed now.", "",
         "| Account | Who | Coin | Lev | **Value** | **P/L** | vs holding the coin | Trades (wins) | Longs/shorts | Ties | Fees+funding | Liquidations | Max DD | Now |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in score:
        L.append(f"| `{r['account']}` | {r['who']}{' (' + r['note'] + ')' if r.get('note') else ''} | {r['coin']} | {r['lev']} | **${r['value']:.2f}** | **{r['value'] - 100:+.2f}** | "
                 f"{r['value'] - r['hold']:+.2f} | {r['trades']} ({r['wins']}) | {r['longs']}/{r['shorts']} | {r['ties']} | ${r['fees']:.2f} | {r['liq']} | {r['dd']:.1f}% | {r['pos']} |")
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
