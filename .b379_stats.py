#!/usr/bin/env python3
import math, statistics, json
base="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b379_"
def stats(path):
    vals=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            if line:
                try: vals.append(float(line))
                except: pass
    vals.sort()
    n=len(vals)
    def nearest_pct(p):
        if not vals: return None
        idx=int(math.ceil((p/100.0)*n)-1)
        idx=max(0,min(n-1,idx))
        return vals[idx]
    cold=sum(1 for v in vals if v>=0.5)
    return dict(n=n, p50=nearest_pct(50), p95=nearest_pct(95),
                p99=nearest_pct(99), min=vals[0] if vals else None,
                max=vals[-1] if vals else None, cold=cold, cold_pct=round(100.0*cold/n,1) if n else None)
res={}
for run in ["A","B","C","land"]:
    res[run]=stats(base+run+".txt")
json.dump(res, open(base+"stats.json","w"), indent=2)
print(json.dumps(res, indent=2))