#!/usr/bin/env python3
# K-Z3 run543 stats: cold>=0.5s count, nearest-rank p50, min/max per run + landing
import os, math

def load(path):
    vals=[]; codes={}
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
    s=sorted(v[2] for v in vals)
    n=len(s)
    k=int(math.ceil(0.50*n)); k=max(1,min(n,k))
    return s[k-1], k

def report(label, path):
    vals,codes=load(path)
    tt=[v[2] for v in vals]
    cold=[v for v in vals if v[2]>=0.5]
    pv,k=p50(vals)
    cold_pos=[v[0] for v in cold]
    out="%s: n=%d codes=%s p50=%.4fs(k=%d) min=%.4fs max=%.4fs cold(>=0.5s)=%d cold_pos=%s" % (
        label,len(vals),codes,pv,k,min(tt),max(tt),len(cold),cold_pos)
    print(out)
    return len(cold)

tot=0
for lbl,p in [("A",".b543_A.ttfb"),("B",".b543_B.ttfb"),("C",".b543_C.ttfb"),("land",".b543_landing.ttfb")]:
    tot+=report(lbl,p)
print("TOTAL_COLD=%d" % tot)