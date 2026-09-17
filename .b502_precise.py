#!/usr/bin/env python3
import os
BASE="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def load(d):
    out=[]
    for line in open(os.path.join(BASE,d,"resp.txt")):
        p=line.strip().split()
        if len(p)>=2:
            try: out.append((int(p[0]),float(p[1])*1000))
            except ValueError: pass
    return out
for g in ["runA","runB","runC","control"]:
    data=load(f".run502_raw/{g}")
    codes={}
    for c,t in data: codes[c]=codes.get(c,0)+1
    v=sorted(t for c,t in data)
    n=len(v); p50=v[(n-1)//2]; p95=v[int(n*0.95)-1] if n else None
    cold=[t for c,t in data if t>=0.5*1000]
    coldpos=[(i+1,round(t/1000,4)) for i,(c,t) in enumerate(data) if t>=0.5*1000]
    print(f"{g}: n={n} codes={codes} p50={p50:.1f}ms p95={p95:.1f}ms max={v[-1]:.1f}ms cold={len(cold)} coldpos={coldpos}")