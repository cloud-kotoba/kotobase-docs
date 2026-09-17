#!/usr/bin/env python3
import re, statistics, sys
f='_f90_run216_out.txt'
lines=open(f).read().splitlines()
data={}
for ln in lines:
    m=re.match(r'(run216[A-C]|control)\s+200\s+([0-9.]+)', ln)
    if m:
        data.setdefault(m.group(1),[]).append(float(m.group(2)))
def stat(vals):
    vals=sorted(vals)
    n=len(vals)
    p50=vals[(n-1)//2] if n else 0
    return n, len([x for x in vals if x>1.0]), min(vals), p50, max(vals)
for k in ['run216A','run216B','run216C','control']:
    if k in data:
        n,c,lo,p50,hi=stat(data[k])
        print(f"{k}: n={n} cold(>1s)={c} min={lo:.3f} p50={p50*1000:.1f}ms max={hi:.3f}")
# cold by query index across runs, identify sporadic position
for k in ['run216A','run216B','run216C']:
    for i,v in enumerate(data[k],1):
        if v>1.0:
            print(f"  {k}[{i}] cold {v:.3f}")
allc=[v for k in ['run216A','run216B','run216C'] for v in data[k]]
n,c,lo,p50,hi=stat(allc)
print(f"TOTAL search: n={n} cold={c} p50={p50*1000:.1f}ms max={hi:.3f} -> cold rate {c}/{n} ~{100*c/n:.1f}%")