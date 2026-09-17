#!/usr/bin/env python3
# K-Z3 run530 stats: cold>=0.5s count, nearest-rank p50, min/max per run + landing
import sys, os

def load(path):
    vals=[]
    codes={}
    for line in open(path, encoding='utf-8'):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<3: continue
        idx=int(parts[0]); code=parts[1]; t=float(parts[2])
        codes[code]=codes.get(code,0)+1
        vals.append((idx,code,t))
    return vals,codes

def p50(vals):
    s=sorted(vals)
    n=len(s)
    # nearest-rank p50: smallest value at or above 50% rank
    rank=max(1, int(0.50*n)+ (1 if (0.50*n)!=int(0.50*n) else 0))
    # nearest-rank percentile: ceil(n*p/100), 1-indexed
    import math
    k=int(math.ceil(0.50*n))
    k=max(1,min(n,k))
    return s[k-1], k

def report(label, path):
    vals,codes=load(path)
    tt=[v[2] for v in vals]
    cold=[v for v in vals if v[2]>=0.5]
    pv,k=p50(vals)
    cold_pos=[v[0] for v in cold]
    out="%s: n=%d codes=%s p50=%.4fs%%(k=%d) min=%.4fs max=%.4fs cold(>=0.5s)=%d/20 cold_pos=%s" % (
        label,len(vals),codes,pv[2],k,min(tt),max(tt),len(cold),cold_pos)
    print(out)

for lbl,p in [("A",".b530_A.ttfb"),("B",".b530_B.ttfb"),("C",".b530_C.ttfb"),("land",".b530_landing.ttfb")]:
    report(lbl,p)