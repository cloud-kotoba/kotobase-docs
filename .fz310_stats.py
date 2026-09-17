#!/usr/bin/env python3
import statistics
raw = open('/tmp/fz310.raw').read().splitlines()
groups = {}
for ln in raw:
    p = ln.split()
    if len(p) < 4:
        continue
    label, num, t, http = p[0], p[1], p[2], p[3]
    groups.setdefault(label, []).append((int(num), float(t), int(http)))
COLD = 0.5
for label in ['A', 'B', 'C', 'CTRL']:
    g = groups.get(label, [])
    g.sort()
    vals = [t for _, t, _ in g]
    colds = [(i, t) for i, t, h in g if t >= COLD]
    http_ok = all(h == 200 for _, _, h in g)
    p50 = statistics.median(vals) if vals else 0
    print(f"{label} n={len(g)} cold={len(colds)} {colds} p50={p50*1000:.1f}ms max={max(vals)*1000:.1f}ms http200_all={http_ok}")