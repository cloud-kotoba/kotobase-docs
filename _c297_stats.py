#!/usr/bin/env python3
import re, glob, sys

def load(fn):
    rows=[]
    for line in open(fn):
        m=re.match(r'(\d+)\s+([\d.]+)',line.strip())
        if m:
            code=int(m.group(1)); t=float(m.group(2))
            rows.append((code,t))
    return rows

def stats(fn,label):
    rows=load(fn)
    if not rows:
        print(f"{label}: NO ROWS"); return None
    codes=[r[0] for r in rows]
    ts=[r[1] for r in rows]
    n=len(ts)
    cold=[t for t in ts if t>=0.5]
    ts_sorted=sorted(ts)
    p50=ts_sorted[(n-1)//2] if n else 0
    ps=[]
    rows_sorted=sorted(rows,key=lambda r:r[1])
    def nearest(p):
        idx=max(0,int((p/100.0)*n)-1)
        return rows_sorted[idx][1] if rows_sorted else 0
    p95=nearest(95)
    mx=max(ts)
    print(f"{label}: n={n} all200={all(c==200 for c in codes)} cold(>=0.5)={len(cold)}/{n} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={mx*1000:.1f}ms")
    if cold:
        pos=[i+1 for i,t in enumerate(ts) if t>=0.5]
        print(f"   cold positions: {pos}  values={[round(ts[i-1]*1000,1) for i in pos]}")
    return {"cold":len(cold),"n":n}

base="_c297_"
allc=0; alln=0
for lbl,fn in [("run297A",base+"297A.txt"),("run297B",base+"297B.txt"),("run297C",base+"297C.txt"),("control(land)",base+"land297.txt")]:
    r=stats(fn,lbl)
    if r: allc+=r["cold"]; alln+=r["n"]
print(f"SEARCH TOTAL: cold {allc}/180-60? (3x20={alln})  search-side cold sum={allc}/{alln}")