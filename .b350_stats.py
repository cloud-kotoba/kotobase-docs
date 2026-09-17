#!/usr/bin/env python3
import math
def load(fn):
    rows=[]
    with open(fn) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split()
            if len(parts)>=2 and parts[0].isdigit():
                rows.append((int(parts[0]), float(parts[1])))
    return rows

def rank_pct(sorted_vals):  # nearest-rank percentile: p50 = value at ceil(0.5*n)
    n=len(sorted_vals)
    idx=max(1, math.ceil(0.5*n))-1
    return sorted_vals[idx]

for label,fn in [("A",".b350_350A.txt"),("B",".b350_350B.txt"),("C",".b350_350C.txt"),("land",".b350_land.txt")]:
    rows=load(fn)
    codes=[r[0] for r in rows]
    times=[r[1] for r in rows]
    non200=[c for c in codes if c!=200]
    cold=[t for t in times if t>=0.5]
    s=sorted(times)
    p50=rank_pct(s)
    print(f"{label}: n={len(rows)} non200={len(non200)} cold(>=0.5s)={len(cold)} p50={p50*1000:.1f}ms max={max(times)*1000:.1f}ms")
    if cold:
        print(f"   cold vals: {['%.4fs'%c for c in cold]}")
print("=== all non200 check ===")
for label,fn in [("A",".b350_350A.txt"),("B",".b350_350B.txt"),("C",".b350_350C.txt"),("land",".b350_land.txt")]:
    rows=load(fn)
    non=[(i+1,c) for i,(c,t) in enumerate(rows) if c!=200]
    print(f"{label} non200: {non if non else 'none'}")