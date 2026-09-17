#!/usr/bin/env python3
import sys, statistics

def load(path):
    vals = []
    for line in open(path):
        parts = line.split()
        if len(parts) >= 3:
            try:
                vals.append(float(parts[2]))
            except ValueError:
                pass
    return vals

def nearest_rank_p50(sorted_vals):
    # nearest-rank: ceil(0.50 * n) 1-indexed
    n = len(sorted_vals)
    idx = max(1, round(0.50 * n + 0.5)) - 1 + 1  # ceil
    import math
    k = math.ceil(0.50 * n)
    return sorted_vals[k-1]

for name in ["_b91_run222A.txt","_b91_run222B.txt","_b91_run222C.txt","_b91_land222.txt"]:
    vals = load(name)
    sv = sorted(vals)
    cold = [v for v in vals if v >= 0.5]
    warm = [v for v in vals if v < 0.5]
    wp50 = nearest_rank_p50(sorted(warm)) if warm else None
    print(f"{name}: n={len(vals)} cold(>=0.5s)={len(cold)}/{len(vals)} "
          f"p50(all)={nearest_rank_p50(sv):.4f}s warm_p50={wp50:.4f}s "
          f"min={min(vals):.4f} max={max(vals):.4f}")
    if cold:
        for c in cold:
            print(f"    cold: {c:.4f}s")