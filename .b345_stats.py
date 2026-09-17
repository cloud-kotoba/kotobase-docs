#!/usr/bin/env python3
import glob, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def stats(fn,label):
    rows=[]
    for line in open(fn):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        try:
            code=int(parts[0]); t=float(parts[1])
        except ValueError:
            continue
        rows.append((code,t))
    codes=[r[0] for r in rows]
    ts=[r[1] for r in rows]
    ts_sorted=sorted(ts)
    n=len(ts_sorted)
    p50=ts_sorted[n//2] if n else 0
    mn=min(ts) if ts else 0
    mx=max(ts) if ts else 0
    cold=[t for t in ts if t>=0.5]
    non200=[c for c in codes if c!=200]
    print(f"{label}: n={n} non200={len(non200)} cold(>=0.5s)={len(cold)} p50={p50*1000:.1f}ms max={mx*1000:.1f}ms")
    print(f"   cold_vals={[round(t,4) for t in cold]}")
for a in ["A","B","C"]:
    stats(f".b345_345{a}.txt", f"run345{a}")
stats(".b345_land.txt","control-land")
