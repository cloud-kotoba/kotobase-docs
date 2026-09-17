#!/usr/bin/env python3
import math, os
OUT = "/tmp/b414"

def nearest_rank_p50(vals):
    s = sorted(vals)
    n = len(s)
    k = math.ceil(0.50 * n)
    return s[k-1]

def parse(fn):
    rows = []
    with open(fn) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            try:
                ttfb = float(parts[0])
                total = float(parts[1])
                code = parts[2] if len(parts) > 2 else "?"
            except ValueError:
                continue
            rows.append((ttfb, total, code))
    return rows

for name, fn in [("A", "A.txt"), ("B", "B.txt"), ("C", "C.txt"), ("ctrl", "ctrl.txt")]:
    rows = parse(os.path.join(OUT, fn))
    if not rows:
        print(f"{name}: NO DATA")
        continue
    codes = sorted({r[2] for r in rows})
    ttfb = sorted(r[0] for r in rows)
    total = [r[1] for r in rows if r[1] >= 0]
    cold = [x for x in ttfb if x >= 0.5]
    # cold positions by index order in original file (preserve order)
    coldpos = [i+1 for i, (t, _, _) in enumerate(rows) if t >= 0.5]
    warm = [x for x in ttfb if x < 0.5]
    p50 = nearest_rank_p50(ttfb)
    warm_p50 = nearest_rank_p50(warm) if warm else float("nan")
    mx = max(ttfb)
    print(f"=== {name} n={len(rows)} codes={codes} ===")
    print(f"  cold(>=0.5s)={len(cold)}/{len(rows)}  pos(cold)={coldpos}")
    print(f"  p50(ttfb)={p50:.4f}s  warm_p50={warm_p50:.4f}s  max={mx:.4f}s")
    if cold:
        print(f"  cold values: {[round(x,4) for x in cold]}")
print("done")