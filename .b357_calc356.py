#!/usr/bin/env python3
base="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b356_"
def parse(f):
    out=[]
    for line in open(f, encoding='utf-8', errors='replace'):
        line=line.strip()
        if not line: continue
        parts=line.split()
        out.append((parts[0],float(parts[1])))
    return out
def nr_pct(vals,p):
    if not vals: return None
    rank=int(round((p/100.0)*len(vals)))
    if rank<1: rank=1
    return vals[rank-1]
tot=[]
for c in ['A','B','C']:
    r=parse(base+'356'+c+'.txt')
    tot+=r
    allt=[t for cc,t in r if cc=='200']
    cold=[t for cc,t in r if cc=='200' and t>=0.5]
    print(f"356{c}: cold={len(cold)}/20 p50={(nr_pct(sorted(allt),50)*1000):.1f}ms max={(max(allt)*1000):.1f}ms")
lr=parse(base+'land.txt')
allt=[t for cc,t in lr if cc=='200']
cold=[t for cc,t in lr if cc=='200' and t>=0.5]
print(f"control: cold={len(cold)}/20 p50={(nr_pct(sorted(allt),50)*1000):.1f}ms max={(max(allt)*1000):.1f}ms")
coldtot=sum(1 for cc,t in tot if cc=='200' and t>=0.5)
print(f"TOTAL search: {coldtot}/60 cold(>=0.5s)")
for c in ['A','B','C']:
    r=parse(base+'356'+c+'.txt')
    vals=[(i+1,round(t,4)) for i,(cc,t) in enumerate(r) if cc=='200' and t>=0.5]
    print(f"356{c} cold positions/values:", vals)