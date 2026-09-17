import sys
def stats(path, thr=0.5):
    vals=[float(l.split()[0]) for l in open(path) if l.strip()]
    s=sorted(vals)
    n=len(s)
    import math
    p50=s[max(0,math.ceil(0.50*n)-1)]
    p95=s[max(0,math.ceil(0.95*n)-1)]
    cold=[v for v in vals if v>=thr]
    return n,p50,p95,min(s),max(s),len(cold),[round(v,3) for v in cold]
for f in sys.argv[1:]:
    n,p50,p95,mn,mx,c,colds=stats(f)
    print(f"{f}: n={n} cold(>={0.5}s)={c}/{n} p50={p50*1000:.0f}ms p95={p95*1000:.0f}ms min={mn*1000:.0f}ms max={mx*1000:.0f}ms colds={colds}")
# landing control with http codes
vals=[l.split() for l in open('_b88_land.txt') if l.strip()]
t=[float(a) for a,b in vals]
codes=[b for a,b in vals]
s=sorted(t); import math
print(f"land: n={len(t)} codes_ok={codes.count('200')}/{len(t)} cold={sum(1 for v in t if v>=0.5)}/{len(t)} p50={s[math.ceil(0.5*len(t))-1]*1000:.0f}ms max={max(t)*1000:.0f}ms")
