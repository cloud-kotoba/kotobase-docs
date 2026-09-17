#!/usr/bin/env python3
# cosientist K-Z3 12hr run349 stats: cold>=0.5s count + nearest-rank p50.
import sys

def load(path):
    rows=[]
    for line in open(path):
        p=line.split()
        rows.append((int(p[0]), float(p[1])))
    return rows

def report(tag, rows):
    times=sorted(t[1] for t in rows)
    cold=[t for t in times if t>=0.5]
    n=len(times)
    idx=max(1, round(0.5*n))
    p50=times[idx-1] if n else float('nan')
    print(f"{tag}: n={n} cold={len(cold)} ({len(cold)}/{n}) p50={p50:.4f} max={times[-1]:.4f} min={times[0]:.4f}")

for f in [".b349_349A.txt",".b349_349B.txt",".b349_349C.txt",".b349_land.txt"]:
    report(f, load(f))

combined=[]
for f in [".b349_349A.txt",".b349_349B.txt",".b349_349C.txt"]:
    combined+=load(f)
report("COMBINED(A+B+C)", combined)