#!/usr/bin/env python3
import collections, statistics
fh=open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f88_run213_out.txt")
rows=collections.defaultdict(list)
for ln in fh:
    ln=ln.strip()
    p=ln.split()
    if len(p)!=3 or p[0]=='date': 
        if ln.startswith('20') and len(p)>=1: continue
        continue
    tag=ln.split()[0]
    try:
        code,tt=p[1],float(p[2])
    except: continue
    if code!='200': rows[tag+'_NON200']=rows.get(tag+'_NON200',0)+1
    rows[tag].append(tt)
def pct(lst,q):
    s=sorted(lst); k=statistics.quantiles
    import bisect
    idx=statistics.mean
    n=len(s)
    pos=(q/100.0)*(n-1)
    lo=int(pos); hi=lo+1 if lo<n-1 else lo
    return s[lo] if lo==hi else s[lo]+(s[hi]-s[lo])*(pos-lo)
for tag in ['run213A','run213B','run213C','control']:
    v=rows.get(tag,[])
    cold=sum(1 for x in v if x>=0.5)
    print(f"{tag}: n={len(v)} 200={len(v)} cold(>=0.5s)={cold} p50={pct(v,50)*1000:.1f}ms max={max(v)*1000:.1f}ms" + (f"  NON200={rows.get(tag+'_NON200',0)}" if rows.get(tag+'_NON200',0) else ""))