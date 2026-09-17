#!/usr/bin/env python3
import re, sys, collections

RAW = "/tmp/fz312.raw"
data = collections.OrderedDict()  # label -> list of (idx, ttotal, http)
for line in open(RAW):
    parts = line.split()
    if len(parts) < 3:
        continue
    label, idx, ttotal, http = parts[0], int(parts[1]), float(parts[2]), parts[3]
    data.setdefault(label, []).append((idx, ttotal, http))

def p50(xs):
    s = sorted(xs)
    n = len(s)
    return s[(n-1)//2]

for label, rows in data.items():
    tt = [r[1] for r in rows]
    codes = collections.Counter(r[2] for r in rows)
    cold = [r for r in rows if r[1] >= 0.5]
    ok = sum(1 for r in rows if r[2] == "200")
    print(f"{label}: n={len(rows)} p50={p50(tt)*1000:.1f}ms max={max(tt)*1000:.1f}ms "
          f"cold(>=0.5s)={len(cold)} ok200={ok} codes={dict(codes)}")
    for idx, t, h in cold:
        print(f"   cold idx={idx} t={t:.4f}s http={h}")

print("STATS_DONE")