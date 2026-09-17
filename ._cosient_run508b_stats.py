#!/usr/bin/env python3
import sys, os

def analyze(path, label):
    rows = []
    with open(path) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                code = p[0]; ttfb = float(p[1])
                rows.append((code, ttfb))
    codes = {}
    for code, _ in rows:
        codes[code] = codes.get(code, 0) + 1
    vals_sorted = sorted([ttfb for _, ttfb in rows])
    n = len(vals_sorted)
    cold = [v for v in vals_sorted if v >= 0.5]
    if n == 0:
        p50 = float('nan')
    else:
        idx = int((50.0/100.0)*n + 0.5) - 1
        idx = max(0, min(idx, n-1))
        p50 = vals_sorted[idx]
    mx = max(vals_sorted) if vals_sorted else float('nan')
    print(f"{label}: n={n} codes={codes} cold(>=0.5s)={len(cold)}/{n} p50={p50*1000:.1f}ms max={mx*1000:.1f}ms")

base = "/tmp/cosient_run508v2"
for r in ["A","B","C"]:
    analyze(os.path.join(base, f"run{r}.raw"), f"run508{r}")
analyze(os.path.join(base, "land.raw"), "control")
