#!/usr/bin/env python3
import re, math
from statistics import median

def parse(path):
    rows=[]
    for line in open(path):
        line=line.strip()
        if not line: continue
        parts=line.split()
        code=parts[0]; ttf=float(parts[1])
        rows.append((code,ttf))
    return rows

files=[('A','_f401_401A.txt'),('B','_f401_401B.txt'),('C','_f401_401C.txt')]
tot_cold=0; tot_n=0; codes={}
for name,path in files:
    rows=parse(path)
    cold=[t for c,t in rows if t>=0.5]
    p50=median([t for c,t in rows])
    mx=max(t for c,t in rows)
    for c,t in rows: codes[c]=codes.get(c,0)+1
    print(f"run401{name}: cold={len(cold)}/20 p50={p50*1000:.1f}ms max={mx*1000:.1f}ms cold_vals={[round(x,3) for x in cold]}")
    tot_cold+=len(cold); tot_n+=len(rows)

# landing control
lrows=parse('_f401_land.txt')
lcold=[t for c,t in lrows if t>=0.5]
lp50=median([t for c,t in lrows])
lmx=max(t for c,t in lrows)
for c,t in lrows: codes[c]=codes.get(c,0)+1
print(f"landing: cold={len(lcold)}/20 p50={lp50*1000:.1f}ms max={lmx*1000:.1f}ms cold_vals={[round(x,3) for x in lcold]}")
print(f"TOTAL search cold={tot_cold}/{tot_n} ({tot_cold/tot_n*100:.1f}%)")
print(f"HTTP codes: {codes}")
