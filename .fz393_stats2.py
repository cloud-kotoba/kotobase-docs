#!/usr/bin/env python3
import sys, statistics

def stats(path, label, cold_thresh=0.5):
    rows = []
    for line in open(path):
        line = line.strip()
        if not line: continue
        parts = line.split()
        if len(parts) < 2: continue
        rows.append((parts[0], float(parts[1])))
    codes = [r[0] for r in rows]
    ttfbs = sorted(r[1] for r in rows)
    n = len(ttfbs)
    nok = codes.count('200')
    coldpos = [(i+1, v) for i,v in enumerate(r[1] for r in rows) ]
    cold = [(i+1, v) for i,v in enumerate([r[1] for r in rows]) if v >= cold_thresh]
    def pct(p):
        if not ttfbs: return 0.0
        idx = min(n-1, max(0, int((p/100.0)*n)-1))
        return ttfbs[idx]
    cpos = "/".join(f"{p}:{v:.4f}s" for p,v in cold) if cold else "-"
    print(f"{label}: n={n} 200={nok} cold(>=0.5s)={len(cold)} p50={pct(50)*1000:.1f}ms p95={pct(95)*1000:.1f}ms min={ttfbs[0]*1000:.1f}ms max={ttfbs[-1]*1000:.1f}ms | coldpos: {cpos}")

for f,lab in [(".fz393_393A.txt","393A"),(".fz393_393B.txt","393B"),(".fz393_393C.txt","393C"),(".fz393_land.txt","land")]:
    stats(f, lab)