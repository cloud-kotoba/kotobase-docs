#!/usr/bin/env python3
def parse(f):
    out=[]
    for line in open(f):
        line=line.strip()
        if not line: continue
        p=line.split()
        out.append((p[0], float(p[1])))
    return out
for base,c in [('.b351','A'),('.b351','B'),('.b351','C')]:
    r=parse(base+'_351'+c+'.txt')
    cold=[(i+1, t) for i,(code,t) in enumerate(r) if code=='200' and t>=0.5]
    print(f"run351{c}: cold positions/values {cold}")
lr=parse('.b351_land.txt')
print("control cold:", [(i+1,t) for i,(code,t) in enumerate(lr) if code=='200' and t>=0.5])