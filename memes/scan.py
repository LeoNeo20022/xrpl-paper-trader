import json, urllib.request, math
N="https://xrplcluster.com"
def q(m,p):
    r=urllib.request.Request(N,json.dumps({"method":m,"params":[p]}).encode(),{"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(r,timeout=30))["result"]
T=json.load(open('xrpscan_tokens.json'))
codes=['FUZZY','PHNIX','ARMY','BEAR','666','589','ATM','XRdoge']
BLACKHOLES={'rrrrrrrrrrrrrrrrrrrrrhoLvTp','rrrrrrrrrrrrrrrrrrrrBZbvji','rrrrrrrrrrrrrrrrrNAMEtxvNvQ','rrrrrrrrrrrrrrrrrrrn5RM1rHd'}
def amt(a): return float(a)/1e6 if isinstance(a,str) else float(a['value'])
out=[]
for c in codes:
    z=next(z for z in T if z and z['code']==c)
    cur,iss=z['currency'],z['issuer']; tok={"currency":cur,"issuer":iss}
    ai=q("account_info",{"account":iss,"ledger_index":"validated","signer_lists":True})
    a=ai["account_data"]; f=a["Flags"]
    flags={"master_disabled":bool(f&0x00100000),"global_freeze":bool(f&0x00400000),"no_freeze":bool(f&0x00200000),
           "clawback":bool(f&0x80000000),"require_auth":bool(f&0x00040000)}
    rk=a.get("RegularKey"); signers=ai.get("signer_lists") or a.get("signer_lists") or []
    black = flags["master_disabled"] and (rk is None or rk in BLACKHOLES) and not signers
    tr=a.get("TransferRate",0); tfee=0 if tr in (0,1000000000) else (tr/1e9-1)*100
    asks=q("book_offers",{"taker_gets":tok,"taker_pays":{"currency":"XRP"},"limit":300}).get("offers",[])  # sellers of token
    bids=q("book_offers",{"taker_pays":tok,"taker_gets":{"currency":"XRP"},"limit":300}).get("offers",[])  # buyers of token
    A=[];B=[]
    for o in asks:
        g=amt(o.get("taker_gets_funded",o["TakerGets"])); p=amt(o.get("taker_pays_funded",o["TakerPays"]))
        if g>0 and p>0: A.append((p/g,p))  # price XRP per token, XRP notional
    for o in bids:
        g=amt(o.get("taker_gets_funded",o["TakerGets"])); p=amt(o.get("taker_pays_funded",o["TakerPays"]))
        if g>0 and p>0: B.append((g/p,g))
    A.sort(); B.sort(reverse=True)
    amm=q("amm_info",{"asset":{"currency":"XRP"},"asset2":tok}).get("amm")
    ax=au=afee=None; ammpx=None
    if amm:
        ax=float(amm["amount"])/1e6; au=float(amm["amount2"]["value"]); afee=amm["trading_fee"]/1000; ammpx=ax/au
    if A and B: mid=(A[0][0]+B[0][0])/2; spread=(A[0][0]-B[0][0])/mid*100
    else: mid=ammpx; spread=None
    def depth(pct):
        da=sum(n for p,n in A if p<=mid*(1+pct/100)); db=sum(n for p,n in B if p>=mid*(1-pct/100))
        # AMM: XRP needed to move price by pct (constant product): x*(sqrt(1+pct)-1)
        am = ax*(math.sqrt(1+pct/100)-1) if ax else 0
        return round(da),round(db),round(am)
    out.append(dict(code=c,issuer=iss,currency=cur,transfer_fee_pct=round(tfee,3),**flags,regular_key=rk,signers=bool(signers),
        blackholed=black,clob_offers=(len(B),len(A)),best_bid=B[0][0] if B else None,best_ask=A[0][0] if A else None,
        spread_pct=round(spread,3) if spread is not None else None,mid_xrp=mid,amm_px=ammpx,
        amm_xrp=round(ax) if ax else None,amm_fee_pct=afee,amm_vs_mid_pct=round((ammpx/mid-1)*100,3) if ammpx and mid else None,
        depth1=depth(1),depth5=depth(5)))
json.dump(out,open('scan.json','w'),indent=1,default=str)
for r in out: print(r)
