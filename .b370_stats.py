#!/usr/bin/env python3
import statistics, json, sys

def load(path):
    rows=[]
    for line in open(path):
        line=line.strip()
        if not line: continue
        parts=line.split()
        code=parts[0]; ttfb=float(parts[1])
        rows.append((code,ttfb))
    return rows

def cold_count(rows, thresh=0.5):
    c=0; vals=[]
    for code,ttfb in rows:
        if ttfb>=thresh: c+=1
        vals.append(ttfb)
    return c, vals

files={'A':'.b370_370A.txt','B':'.b370_370B.txt','C':'.b370_370C.txt','land':'.b370_land.txt'}
out={'files':{},'summary':{}}
total_cold=0; total_n=0; landc=0; landvals=[]
for k,f in files.items():
    rows=load(f)
    codes=[r[0] for r in rows]
    non200=[c for c in codes if c!='200']
    c,vals=cold_count(rows)
    svals=sorted(vals)
    def nrp(p):
        idx=max(0, int(round(p/100.0*len(svals)))-1) if False else max(0, round(p/100.0*(len(svals)-1)))
        return svals[int(idx)]
    p50=nrp(50)
    p95=nrp(95)
    mx=max(vals)
    mn=min(vals)
    med=statistics.median(vals)
    out['files'][k]={'n':len(rows),'non200':non200,'cold':c,'p50':round(p50,4),'p95':round(p95,4),'min':round(mn,4),'max':round(mx,4),'median':round(med,4)}
    if k!='land':
        total_cold+=c; total_n+=len(rows)
    else:
        landc=c; landvals=vals
pct=round(100.0*total_cold/total_n,2)
out['summary']={'search_total_cold':total_cold,'search_total_n':total_n,'cold_pct':pct,'land_cold':landc}
print(json.dumps(out, ensure_ascii=False, indent=2))