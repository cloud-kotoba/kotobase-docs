import re, statistics, sys
OUT="_f128_run281_out.txt"
data={}
order=[]
for line in open(OUT):
    line=line.strip()
    m=re.match(r'^(run281[A-C]|control)\s+(\d+)\s+([\d.]+)$', line)
    if m:
        lbl=m.group(1); t=float(m.group(3))
        if lbl not in data: data[lbl]=[]; order.append(lbl)
        data[lbl].append(t)
COLD=0.5
for lbl in order:
    v=data[lbl]
    cold=sum(1 for x in v if x>=COLD)
    p50=statistics.median(v)
    print(f"{lbl}: n={len(v)} cold={cold}/{len(v)} p50={p50*1000:.1f}ms mean={statistics.mean(v)*1000:.1f}ms max={max(v)*1000:.1f}ms coldlist={[round(x,3) for x in v if x>=COLD]}")