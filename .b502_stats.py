#!/usr/bin/env python3
import os
BASE="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def load(d):
    out=[]
    for line in open(os.path.join(BASE,d,"resp.txt")):
        line=line.strip().replace("\u200b","")
        if not line: continue
        parts=line.split()
        if len(parts)>=2:
            try:
                code=int(parts[0]); tt=float(parts[1])
                out.append((code,tt))
            except ValueError: pass
    return out

def p50(v):
    s=sorted(v); n=len(s)
    if n==0: return None
    return s[(n-1)//2]

def neat(ms):
    if ms is None: return "n/a"
    if ms>=1000: return f"{ms/1000:.3f}s"
    return f"{ms:.1f}ms"

groups=["runA","runB","runC","control"]
allstats={}
for g in groups:
    data=load(f".run502_raw/{g}")
    codes={}
    for c,t in data: codes[c]=codes.get(c,0)+1
    tt=[t*1000 for c,t in data]
    cold=[t for c,t in data if t>=0.5]
    allstats[g]=dict(n=len(data),codes=codes,p50=p50(tt),max=max(tt) if tt else None,cold=len(cold),coldvals=[round(t,4) for t in cold])
    print(f"{g}: n={len(data)} codes={codes} p50={neat(p50(tt))}ms max={neat(max(tt)) if tt else 'n/a'} cold={len(cold)}/20")
    if cold:
        print(f"   cold: {[round(t,3) for t in cold]}s")
# totals
sc=[allstats[g] for g in ["runA","runB","runC"]]
tcold=sum(s["cold"] for s in sc); total=sum(s["n"] for s in sc)
print(f"SEARCH total cold={tcold}/{total} (~{tcold/total*100:.1f}%)")
cc=allstats["control"]
print(f"CONTROL total cold={cc['cold']}/20")
# max after runA
for g in groups:
    s=allstats[g]
    print(f"{g} pos cold indices+T:", )
    data=load(f".run502_raw/{g}")
    for i,(c,t) in enumerate(data,1):
        if t>=0.5:
            print(f"   pos{i} {round(t,4)}s")