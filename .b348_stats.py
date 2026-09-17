#!/usr/bin/env python3
# bench K-Z3 12hr run348 stats: cold>=0.5s count + nearest-rank p50.
import sys, statistics

def load(path):
    rows=[]
    for line in open(path):
        p=line.split()
        rows.append((int(p[0]), float(p[1])))
    return rows

def report(tag, rows):
    times=sorted(t[1] for t in rows)
    cold=[t for t in times if t>=0.5]
    # nearest-rank p50: ceil(0.5*n)-th smallest (1-indexed)
    n=len(times)
    idx=max(1, round(0.5*n))
    p50=times[idx-1]
    print(f"{tag}: n={n} cold={len(cold)} ({len(cold)}/{n}) p50={p50:.4f} max={times[-1]:.4f} min={times[0]:.4f}")

for f in [".b348_348A.txt",".b348_348B.txt",".b348_348C.txt",".b348_land.txt"]:
    report(f, load(f))

# combined search sets A+B+C
combined=[]
for f in [".b348_348A.txt",".b348_348B.txt",".b348_348C.txt"]:
    combined+=load(f)
report("COMBINED(A+B+C)", combined)