#!/usr/bin/env python3
import sys, statistics

def load(path):
    rows=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split()
            if len(parts)<2: continue
            try:
                code=int(parts[0]); ttf=float(parts[1])
            except ValueError:
                continue
            rows.append((code,ttf))
    return rows

def p50(vals):
    s=sorted(vals)
    n=len(s)
    if n==0: return None
    return s[(n-1)//2]

for label in ['run290A','run290B','run290C','land290']:
    rows=load(f'_fz290_{label}.txt')
    codes={}
    for c,_ in rows: codes[c]=codes.get(c,0)+1
    ttfs=[t for _,t in rows]
    cold=[t for t in ttfs if t>=0.5]
    print(f"{label}: n={len(rows)} codes={codes} cold(>=0.5s)={len(cold)}/{len(rows)} p50={p50(ttfs)} max={max(ttfs) if ttfs else None} cold_vals={['%.4f'%t for t in cold]}")