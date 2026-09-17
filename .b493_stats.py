#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nearest-rank percentile + cold(>=0.5s) count for a .ttfb list
import sys

def stats(path):
    vals = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                vals.append(float(ln))
    vals.sort()
    n = len(vals)
    def pct(p):
        # nearest-rank: k = ceil(p/100 * n); 1-indexed
        k = int(p / 100.0 * n)
        if k < 1:
            k = 1
        return vals[k-1]
    cold = sum(1 for v in vals if v >= 0.5)
    res = {
        "n": n,
        "p50": round(pct(50), 4),
        "p95": round(pct(95), 4),
        "min": round(vals[0], 4),
        "max": round(vals[-1], 4),
        "cold": cold,
    }
    return res

for p in sys.argv[1:]:
    print(p, stats(p))