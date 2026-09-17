#!/usr/bin/env python3
import sys
def load(f):
    rows=[]
    for line in open(f):
        line=line.strip()
        if not line: continue
        code,t=line.split()
        rows.append(float(t))
    return rows
def stats(name, f):
    v=load(f)
    v=sorted(v)
    n=len(v)
    cold=sum(1 for x in v if x>=0.5)
    p50=v[(n-1)//2] if n else 0
    p95=v[int((n-1)*0.95)] if n else 0
    mx=v[-1] if n else 0
    all200 = sum(1 for line in open(f) if line.strip().startswith('200'))==n
    print(f"{name}: n={n} all200={all200} cold(>=0.5)={cold}/{n} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={mx*1000:.1f}ms")
for run in ['A','B','C']:
    stats(f"run298{run}", f"_fz298_298{run}.txt")
stats("control(land)", "_fz298_land298.txt")
s=0
for run in ['A','B','C']:
    s+=sum(1 for x in load(f"_fz298_298{run}.txt") if x>=0.5)
print(f"SEARCH TOTAL cold sum (3x20=60): {s}/60")