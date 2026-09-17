import os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def load(fn):
    rows=[]
    with open(os.path.join(base,fn)) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split()
            code=int(parts[0]); tt=float(parts[1])
            rows.append((code,tt))
    return rows
def stats(fn):
    rows=load(fn)
    n=len(rows)
    codes=[r[0] for r in rows]
    tts=[r[1] for r in rows]
    all200 = all(c==200 for c in codes)
    cold=[t for t in tts if t>=0.5]
    s=sorted(tts)
    import math
    p50_idx=max(0,math.ceil(0.50*n)-1)
    p50=s[p50_idx]
    noncold=[t for t in tts if t<0.5]
    warmp50=None
    if noncold:
        sn=sorted(noncold)
        warmp50=sn[max(0,math.ceil(0.50*len(sn))-1)]
    return dict(fn=fn,n=n,all200=all200,cold_cnt=len(cold),cold_vals=[round(t,4) for t in cold],
                p50=round(p50,4),min_=round(min(tts),4),max_=round(max(tts),4),
                warmp50=round(warmp50,4) if warmp50 else None)
out=[]
for fn in ["b367_367A.txt","b367_367B.txt","b367_367C.txt","b367_land.txt"]:
    out.append(stats("."+fn))
import json
with open(os.path.join(base,".b367_stats_out.txt"),"w") as f:
    f.write(json.dumps(out,indent=1,ensure_ascii=False))
print(json.dumps(out,indent=1,ensure_ascii=False))