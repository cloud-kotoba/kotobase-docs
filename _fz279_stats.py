#!/usr/bin/env python3
import re, sys, statistics
THRESH=0.5
rows={}
for ln in open('/tmp/fz279.raw'):
    parts=ln.split()
    if len(parts)<3: continue
    lab,i=parts[0],parts[1]
    t=float(parts[2]); code=parts[3]
    rows.setdefault(lab,[]).append((int(i),t,code))
for lab in ['A','B','C','CTRL']:
    rs=rows.get(lab,[])
    rs.sort()
    times=[r[1] for r in rs]
    codes=[r[2] for r in rs]
    cold=[r for r in rs if r[1]>=THRESH]
    noncold=[r[1] for r in rs if r[1]<THRESH]
    p50=statistics.median(times) if times else 0
    n200=codes.count('200')
    maxc=max(times) if times else 0
    wp50=statistics.median(noncold) if noncold else 0
    wmax=max(noncold) if noncold else 0
    coldpos=[r[0] for r in cold]
    desc=""
    if cold:
        cstr="; ".join(f"{r[1]:.4f}s@{r[0]}" for r in cold)
        desc=f" cold={len(cold)}/20 [{cstr}]"
    print(f"{lab}: n={len(rs)} total_cold={len(cold)} total_p50={p50*1000:.1f}ms max={maxc*1000:.1f}ms n200={n200}{desc}")
# overall search A+B+C
scold=sum(len([r for r in rows.get(l,[]) if r[1]>=THRESH]) for l in ['A','B','C'])
print(f"SEARCH_TOTAL_COLD={scold}/60  (~{scold*100/60:.1f}%)")
print(f"CTRL_TOTAL_COLD={len(rows.get('CTRL',[])) and len([r for r in rows['CTRL'] if r[1]>=THRESH])}/20")