import sys, statistics

def load(p):
    rows=[]
    for line in open(p):
        line=line.strip()
        if not line: continue
        code, lat = line.split()
        rows.append(float(lat))
    return rows

def p50(xs):
    s=sorted(xs)
    n=len(s)
    if n==0: return None
    if n%2==1: return s[n//2]
    return (s[n//2-1]+s[n//2])/2.0

for name in ["A","B","C"]:
    path=f".b375_375{name}.txt"
    xs=load(path)
    cold=sum(1 for v in xs if v>=0.5)
    print(f"run375{name}: n={len(xs)} cold={cold} p50={p50(xs):.3f} max={max(xs):.3f} min={min(xs):.3f}")
xs=load(".b375_land.txt")
cold=sum(1 for v in xs if v>=0.5)
print(f"land: n={len(xs)} cold={cold} p50={p50(xs):.3f} max={max(xs):.3f} min={min(xs):.3f}")