import json, math

def parse(fn):
    vals=[]
    for ln in open(fn):
        ln=ln.strip()
        if not ln or ln.startswith('===') or ln.startswith('readdone') or ln.startswith('runner'): continue
        parts=ln.split()
        if len(parts)>=2:
            try:
                vals.append((parts[0], float(parts[1]))
            except Exception:
                pass
    return vals

runs={}
for r in ['A','B','C']:
    runs[r]=parse('.b421_run421_%s.txt'%r)
land=parse('.b421_run421_land.txt')

def nr_at(vals, p:
    s=sorted(vals)
    n=len(s)
    r=max(1, (p*n+99)//100)
    return s[r-1]

def stats(vals:
    tt=[v for c,v in vals]
    codes=[c for c,v in vals]
    cold=[t for t in tt if t>=0.5]
    d=n
    d['ok200']=all(c=='200' for c in codes)
    d['cold']=len(cold)
    d['coldvals']=[round(t,4) for t in cold]
    d['p50']=round(nr_at(tt,50),4)
    d['p95']=round(nr_at(tt,95),4)
    d['mn']=round(min(tt,4)
    d['mx']=round(max(tt,4)
    return d

out={}
for r in ['A','B','C']:
    out[r]=stats(runs[r])
out['land']=stats(land)
print(json.dumps(out, indent=1, ensure_ascii=False)))