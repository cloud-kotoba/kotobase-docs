import sys, math
def stats(path, thr=0.5):
    rows=[l.split() for l in open(path) if l.strip()]
    vals=[]
    n200=0
    for r in rows:
        try:
            v=float(r[1])
        except Exception:
            v=float(r[0])
        vals.append(v)
        if r[0]=='200': n200+=1
    s=sorted(vals)
    n=len(s)
    p50=lambda q: s[max(0,math.ceil(q*n)-1)]
    cold=[v for v in vals if v>=thr]
    return n,n200,p50(0.50),p50(0.95),min(s),max(s),len(cold),sorted(cold)
for f in sys.argv[1:]:
    try:
        n,ok,p50,p95,mn,mx,c,colds=stats(f)
        print(f"{f}: n={n} codes200={ok}/{n} cold(>=0.5s)={c}/{n} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms min={mn*1000:.1f}ms max={mx*1000:.1f}ms colds={[round(v,3) for v in colds]}")
    except Exception as e:
        print(f"{f}: ERROR {e}")