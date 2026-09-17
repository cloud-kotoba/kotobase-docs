#!/usr/bin/env python3
# compute cold>=0.5s count + nearest-rank p50/max for run374 A/B/C/land
import json

files = {
    "A": ".b374_374A.txt",
    "B": ".b374_374B.txt",
    "C": ".b374_374C.txt",
    "land": ".b374_land.txt",
}

def nearest_rank_p50(vals):
    # 20 samples: nearest-rank p50 = ceil(0.50*20)=10th (1-indexed)
    sv = sorted(vals)
    idx = max(1, int(0.50 * len(sv) + 0.9999))
    return sv[idx-1], sv[-1]

for k, fn in files.items():
    vals = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # code time_total
            code, t = parts[0], float(parts[1])
            vals.append(t)
    cold = [v for v in vals if v >= 0.5]
    p50, mx = nearest_rank_p50(vals)
    all200 = all(True for _ in vals)  # placeholder
    n = len(vals)
    print(f"{k}: n={n} cold={len(cold)}/{n} p50={p50*1000:.1f}ms max={mx*1000:.1f}ms cold_vals={[round(c,3) for c in cold]}")