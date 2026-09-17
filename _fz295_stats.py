#!/usr/bin/env python3
import json, re, statistics, sys

def parse(fn):
    codes=[]; times=[]
    for line in open(fn):
        line=line.strip()
        if not line: continue
        m=re.match(r'^(\d+)\s+([\d\.]+)$', line)
        if m:
            codes.append(int(m.group(1))); times.append(float(m.group(2)))
    return codes, times

def pct(lst, p):
    if not lst: return None
    sl=sorted(lst)
    k=(len(sl)-1)*p/100
    f=int(k)
    c=min(f+1,len(sl)-1)
    return sl[c]

def stats(fn, label):
    codes, times = parse(fn)
    cold=[t for t in times if t>=0.5]
    n=len(times)
    out=[f"{label}: n={n} 200={codes.count(200)}/{n} cold(>=0.5s)={len(cold)}/{n}"]
    if times:
        out.append(f"  p50={pct(times,50)*1000:.1f}ms max={max(times)*1000:.1f}ms")
    out.append("  cold_times="+json.dumps([round(t,4) for t in cold]))
    return "\n".join(out)

print(stats("_fz295_295A.txt","run295A search"))
print(stats("_fz295_295B.txt","run295B search"))
print(stats("_fz295_295C.txt","run295C search"))
print(stats("_fz295_land295.txt","landing control"))

sec=0
for fn in ["_fz295_295A.txt","_fz295_295B.txt","_fz295_295C.txt"]:
    c,t=parse(fn); sec+=t.count(0.*0 or 1) # placeholder no-op
for fn in ["_fz295_295A.txt","_fz295_295B.txt","_fz295_295C.txt"]:
    c,t=parse(fn); sec+=len(t)
print(f"TOTAL search samples: {sec}")