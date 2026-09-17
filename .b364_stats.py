#!/usr/bin/env python3
import sys
import statistics
for fn in sys.argv[1:]:
    times = []
    codes = set()
    try:
        f = open(fn)
    except FileNotFoundError:
        print(fn + " MISSING")
        continue
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        codes.add(parts[0])
        times.append(float(parts[1]))
    f.close()
    ts = sorted(times)
    n = len(ts)
    cnt = 0
    for t in ts:
        if t >= 0.5:
            cnt = cnt + 1
    frac = 0
    if n:
        frac = cnt * 100.0 / n
    med = "-"
    mn = "-"
    mx = "-"
    if n:
        med = "%.3fs" % ts[n//2]
        mn = "%.3fs" % ts[0]
        mx = "%.3fs" % ts[-1]
    print("%s: n=%d cold=%d (~%.1f%%) codes=%s p50(nr)=%s min=%s max=%s" % (
        fn, n, cnt, frac, codes, med, mn, mx))