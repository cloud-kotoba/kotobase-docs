#!/usr/bin/env python3
import sys, statistics
def p50_rank(vals):
    s = sorted(vals)
    n = len(s)
    # nearest-rank p50: ceil(0.5*n), 1-indexed -> index ceil(0.5*n)-1
    import math
    idx = math.ceil(0.5*n) - 1
    return s[idx]
groups = {}
for line in open('/tmp/bench311.raw'):
    parts = line.split()
    if len(parts) < 4: continue
    label, idx, t, code = parts[0], int(parts[1]), float(parts[2]), parts[3]
    groups.setdefault(label, []).append((idx, t, code))
COLD = 0.5
for label in ['A','B','C','CTRL']:
    items = groups.get(label, [])
    vals = [t for _,t,c in items if c=='200']
    cold = [(i,t) for i,t,_ in items if t >= COLD]
    codes = {c for _,_,c in items}
    print(f"{label}: n={len(vals)} p50={p50_rank(vals)*1000:.1f}ms max={max(vals)*1000:.1f}ms "
          f"cold={len(cold)}/20 codes={codes}")
    for i,t in cold:
        print(f"   cold idx{i}: {t:.4f}s")