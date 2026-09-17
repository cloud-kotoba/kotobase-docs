import sys

def load(p):
    rows=[]
    for line in open(p):
        line=line.strip()
        if not line: continue
        code, lat = line.split()
        rows.append((code, float(lat)))
    return rows

def p50(xs):
    s=sorted(xs)
    n=len(s)
    if n==0: return None
    if n%2==1: return s[n//2]
    return (s[n//2-1]+s[n//2])/2.0

ok=0
for name in ["A","B","C"]:
    path=f".b377_377{name}.txt"
    rows=load(path)
    xs=[v for c,v in rows]
    cold=sum(1 for v in xs if v>=0.5)
    non200=[c for c,v in rows if c!="200"]
    print(f"run377{name}: n={len(xs)} cold={cold} p50={p50(xs):.3f} max={max(xs):.3f} min={min(xs):.3f} non200={non200}")
    ok += sum(1 for c,v in rows if c=="200")
rows=load(".b377_land.txt")
xs=[v for c,v in rows]
cold=sum(1 for v in xs if v>=0.5)
non200=[c for c,v in rows if c!="200"]
print(f"land: n={len(xs)} cold={cold} p50={p50(xs):.3f} max={max(xs):.3f} min={min(xs):.3f} non200={non200}")
ok += sum(1 for c,v in rows if c=="200")
print(f"TOTAL_200={ok}")