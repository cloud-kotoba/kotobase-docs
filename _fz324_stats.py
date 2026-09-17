#!/usr/bin/env python3
import sys, statistics

def parse(fn):
    times=[]
    for line in open(fn):
        parts=line.split()
        if len(parts)>=2 and parts[0]=='200':
            try: times.append(float(parts[1]))
            except: pass
    return times

def stats(t,label):
    if not t: 
        print(f"{label}: n=0"); return
    t.sort()
    n=len(t)
    cold=sum(1 for x in t if x>=0.5)
    p50=t[(n-1)//2] if n else 0
    if n>=2:
        p95=t[int((n-1)*0.95)]
    else:
        p95=t[-1] if t else 0
    print(f"{label}: n={n} cold>={0.5}s={cold}/20 p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms min={t[0]*1000:.1f}ms max={t[-1]*1000:.1f}ms")
    return cold

for f in ['_fz324_324A.txt','_fz324_324B.txt','_fz324_324C.txt','_fz324_land324.txt']:
    t=parse(f)
    stats(t,f)