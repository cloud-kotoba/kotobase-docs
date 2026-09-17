import json
def parse(fn):
    vals=[]
    for ln in open(fn):
        ln=ln.strip()
        if not ln or ln.startswith('===') or ln.startswith('readdone') or ln.startswith('runner'): continue
        parts=ln.split()
        if len(parts)>=2:
            try: vals.append((parts[0], float(parts[1])))
            except: pass
    return vals

runs={}
for r in ['A','B','C']:
    runs[r]=parse('query-cosientist.md'.replace('query-cosientist.md','.b410_410%s.txt'%r))
land=parse('.b410_land.txt')

def stats(vals):
    tt=[v for c,v in vals]
    codes=[c for c,v in vals]
    tt_s=sorted(tt)
    n=len(tt)
    # nearest-rank percentile: rank = ceil(p/100 * n), 1-indexed
    def nr(p):
        r=max(1,int(__import__('math').ceil(p/100.0*n)))
        return tt_s[r-1]
    cold=[t for t in tt if t>=0.5]
    return dict(n=n, ok200=all(c=='200' for c in codes), cold=len(cold),
                coldvals=[round(t,4) for t in cold], p50=round(nr(50),4),
                p95=round(nr(95),4), mn=round(min(tt),4), mx=round(max(tt),4))

out={r:stats(runs[r]) for r in runs}
out['land']=stats(land)
print(json.dumps(out, indent=1, ensure_ascii=False))