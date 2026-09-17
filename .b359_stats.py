#!/usr/bin/env python3
# bench K-Z3 run359 stats: cold>=0.5s TTFB, nearest-rank p50, per-file max.
# same method contract as prior runs.
import sys, statistics

def parse(fn):
    rows=[]
    codes=[]
    with open(fn) as f:
        for line in f:
            p=line.split()
            if len(p)>=2:
                codes.append(int(p[0]))
                rows.append(float(p[1]))
    return rows, codes

def report(fn):
    rows, codes = parse(fn)
    cold = [r for r in rows if r >= 0.5]
    n = len(rows)
    # nearest-rank p50 = ceil(0.50*n)-th smallest (1-indexed)
    s = sorted(rows)
    p50 = s[max(0,min(n-1, int(0.50*n + 0.999999) - 1))] if n else float('nan')
    mx = max(rows) if rows else float('nan')
    nz = sum(1 for c in codes if c==200)
    print("%s: n=%d ok=%d/%d coldcount=%d p50=%.4fs max=%.4fs cold=%s" % (
        fn, n, nz, n, len(cold), p50, mx, ["%.4f"%x for x in sorted(cold)[:10]]))

for fn in [".b359_359A.txt",".b359_359B.txt",".b359_359C.txt",".b359_land.txt"]:
    report(fn)