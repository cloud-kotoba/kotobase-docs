import json
import math

def parse(fn):
    out=[]
    for line in open(fn):
        parts=line.split()
        if len(parts)<2:
            continue
        try:
            out.append((parts[0], float(parts[1])))
        except Exception:
            pass
    return out

def pct(x, p):
    n=len(x)
    if n==0:
        return None
    r=int(math.ceil(p/100.0*n)))
    r=max(1,min(n,r))
    return round(x[r-1], 4)

def stat(v):
    ts=[]
    for c,t in v:
        ts.append(t)
    x=sorted(ts)
    cold=[]
    for t in ts:
        if t>=0.5:
            cold.append(t)
    ok=True
    for c,t in v:
        if c!='200':
            ok=False
    o={
        'n': len(ts),
        'ok200': ok,
        'cold': len(cold),
        'coldvals': [round(t,4) for t in cold],
        'p50': pct(x, 50),
        'p95': pct(x, 95),
        'mn': round(min(ts}, 4) if ts else None,
        'mx': round(max(ts}, 4) if ts else None,
    }
    return o

runs={}
for r in ['A','B','C']:
    runs[r]=stat(parse('.b411_411%s.txt'%r))
runs['land']=stat(parse('.b411_land.txt'))
print(json.dumps(runs, indent=1, ensure_ascii=False)))