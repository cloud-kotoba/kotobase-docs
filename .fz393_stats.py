#!/usr/bin/env python3
import sys, statistics

def stats(path, label, cold_thresh=0.5):
    rows = []
    for line in open(path):
        line = line.strip()
        if not line: continue
        parts = line.split()
        if len(parts) < 2: continue
        code = parts[0]; ttfb = float(parts[1])
        rows.append((code, ttfb))
    codes = [r[0] for r in rows]
    ttfbs = sorted(r[1] for r in rows)
    n = len(ttfbs)
    nok = codes.count('200')
    cold = sum(1 for r in rows if r[1] >= cold_thresh)
    def pct(p):
        if not ttfbs: return 0.0
        idx = int((p/100.0)*n) - 1
        if idx < 0: idx = 0
        if idx >= n: idx = n-1
        return ttfbs[idx]
    return dict(label=label, n=n, ok=nok, cold=cold,
                p50=pct(50), p95=pct(95), mn=ttfbs[0] if ttfbs else 0,
                mx=ttfbs[-1] if ttfbs else 0)

for f,lab in [(sys.argv[1],sys.argv[2])]:
    d = stats(f, lab)
    print(f"{d['label']}: n={d['n']} 200={d['ok']} cold(>=0.5s)={d['cold']} p50={d['p50']*1000:.1f}ms p95={d['p95']*1000:.1f}ms min={d['mn']*1000:.1f}ms max={d['mx']*1000:.1f}ms")

# cold position detail
import collections
for f in sys.argv[1::2]:
    rows=[]
    for i,line in enumerate(open(f),1):
        parts=line.split()
        if len(parts)>=2 and float(parts[1])>=0.5:
            rows.append((i,float(parts[1])))
    if rows:
        pos="/".join(f"{p}:{v:.4f}s" for p,v in rows)
        print(f"  {f} COLD positions: {pos}")