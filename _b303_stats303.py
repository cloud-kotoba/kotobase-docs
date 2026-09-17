#!/usr/bin/env python3
import sys, statistics
def nearest_rank_p50(vals):
    s = sorted(vals)
    n = len(s)
    # nearest-rank: ceiling(0.5 * n), 1-indexed
    idx = int((0.5 * n + 0.999999))  # ceil(0.5n)
    if idx < 1: idx = 1
    return s[idx-1]
def stats(fn, cutoff=0.5):
    cold=[]; warm=[]
    rows=[]
    with open(fn) as f:
        for line in f:
            parts=line.split()
            if len(parts)<2: continue
            try:
                code=int(parts[0]); ttfb=float(parts[1])
            except ValueError:
                continue
            rows.append((code,ttfb))
            if code!=200: continue
            if ttfb>=cutoff: cold.append(ttfb)
            else: warm.append(ttfb)
    n200=sum(1 for c,t in rows if c==200)
    npct=f"{100.0*n200/len(rows):.1f}" if rows else "NA"
    out=f"n={len(rows)} n200={n200}({npct}%)"
    out+=f" cold{cutoff}={len(cold)}/{len(rows)}"
    if cold:
        out+=f" cold_vals={[round(x,4) for x in cold]}"
    if warm:
        out+=f" warm_p50={nearest_rank_p50(warm)*1000:.1f}ms max={max(warm)*1000:.1f}ms"
    else:
        out+=" warm={}"
    return out
for fn in sys.argv[1:]:
    print(fn.replace('.txt',''), "::", stats(fn))