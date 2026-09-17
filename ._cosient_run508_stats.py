#!/usr/bin/env python3
import sys, statistics, os

def analyze(path, label):
    vals = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if s:
                vals.append(float(s))
    vals_sorted = sorted(vals)
    n = len(vals_sorted)
    cold = [v for v in vals_sorted if v >= 0.5]
    # nearest-rank p50
    if n == 0:
        p50 = float('nan')
    else:
        idx = int((50.0/100.0)*n + 0.5) - 1
        if idx < 0: idx = 0
        if idx >= n: idx = n-1
        p50 = vals_sorted[idx]
    mx = max(vals) if vals else float('nan')
    print(f"{label}: n={n} cold(>=0.5s)={len(cold)}/{n} p50={p50*1000:.1f}ms max={mx*1000:.1f}ms")

base = "/tmp/cosient_run508"
for r in ["A","B","C"]:
    analyze(os.path.join(base, f"run{r}.raw"), f"run508{r}")
analyze(os.path.join(base, "land.raw"), "control")
