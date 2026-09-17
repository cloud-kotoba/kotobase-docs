import math

def load(path):
    rows=[]
    with open(path) as f:
        for ln in f:
            ln=ln.strip()
            if not ln: continue
            p=ln.split()
            try:
                if len(p)>=2:
                    code=int(p[0]); ttfb=float(p[1])
                else:
                    code=200; ttfb=float(p[0])
            except Exception:
                continue
            rows.append((code,ttfb))
    return rows

def pct(v,q):
    if not v: return 0
    s=sorted(v)
    idx=math.ceil(q/100.0*len(s))-1
    idx=max(0,min(len(s)-1,idx))
    return s[idx]

def analyze(tag,path):
    rows=load(path)
    codes=[r[0] for r in rows]
    ttfbs=[r[1] for r in rows]
    cold=[t for t in ttfbs if t>=0.5]
    non200=[c for c in codes if c!=200]
    p50=pct(ttfbs,50)
    mx=max(ttfbs) if ttfbs else 0
    return dict(tag=tag,n=len(rows),
                non200=non200,
                cold=len(cold), p50=round(p50,4), mx=round(mx,4),
                coldvals=[round(t,4) for t in cold])

res=[]
for tag in ['A','B','C']:
    res.append(analyze(tag,'.b544_run544%s.ttfb'%tag))
res.append(analyze('landing','.b544_landing.ttfb'))
out=[]
se=[r for r in res if r['tag'] in ('A','B','C')]
tot_cold=sum(r['cold'] for r in se)
tot_n=sum(r['n'] for r in se)
tot_200=[r['non200'] for r in se]
for r in res:
    out.append("RUN%s n=%d cold=%d/%d non200=%s p50=%.4fs max=%.4fs coldvals=[%s]"%(
        r['tag'],r['n'],r['cold'],r['n'],r['non200'],r['p50'],r['mx'],", ".join("%.4f"%c for c in sorted(r['coldvals']))))
out.append("SEARCH_TOTAL cold=%d/%d (~%.1f%%) non200=%s"%(tot_cold,tot_n,100.0*tot_cold/tot_n,sorted(set(x for sub in tot_200 for x in sub))))
with open('.b544_stats_out.txt','w',encoding='utf-8') as f:
    f.write("\n".join(out)+"\n")