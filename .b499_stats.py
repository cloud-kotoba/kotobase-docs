import json, math
def load(path):
    rows=[]
    with open(path) as f:
        for ln in f:
            ln=ln.strip()
            if not ln: continue
            p=ln.split()
            try:
                code=int(p[0]); ttfb=float(p[1])
            except Exception:
                continue
            rows.append((code,ttfb))
    return rows

def pct(v,q):
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
    p50=pct(ttfbs,50) if ttfbs else 0
    mx=max(ttfbs) if ttfbs else 0
    return dict(tag=tag,n=len(rows),
                non200=non200,
                cold=len(cold), p50=round(p50,4), mx=round(mx,4),
                coldvals=[round(t,4) for t in cold])

res=[]
for tag in ['A','B','C']:
    res.append(analyze(tag,'.b499_run499%s.ttfb'%tag))
res.append(analyze('landing','.b499_landing.ttfb'))
print(json.dumps(res,indent=1))