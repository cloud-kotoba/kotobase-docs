import re, statistics, sys
cold=0; tot=0
rows={'SRCH':{},'CTRL':{}}
for line in open('.b635_run.txt'):
    parts=line.split()
    if len(parts)<4: continue
    kind_rep, idx, code, t = parts[0], int(parts[1]), parts[2], float(parts[3])
    kind, rep = kind_rep.rsplit('_',1)
    rows[kind].setdefault(rep,[]).append((idx,code,t*1000))
for kind in ('SRCH','CTRL'):
    for rep in sorted(rows[kind]):
        ts=[x for x in rows[kind][rep]]
        codes=[c for _,c,_ in ts]
        times=[t for _,_,t in ts]
        colds=[(i,t) for i,c,t in ts if t>=500]
        colds.sort()
        n=len(ts)
        srt=sorted(times); p50=srt[n//2] if n%2 else (srt[n//2-1]+srt[n//2])/2
        p95=srt[min(n-1,int(round(0.95*n))-1)] if n>1 else srt[0]
        nonc=[t for t in times if t<500]
        warm_p50 = sorted(nonc)[len(nonc)//2] if nonc else -1
        print(f"{kind}_{rep} n={n} ok={codes.count('200')} cold={len(colds)} colds={[f'{i}:{t:.0f}ms' for i,t in colds]} p50={p50:.1f} p95={p95:.1f} max={max(times):.1f} warm_p50={warm_p50:.1f}")
sc=sum(len([1 for _,c,t in v if c=='200' and t>=500]) for v in rows['SRCH'].values())
sn=sum(len(v) for v in rows['SRCH'].values())
cc=sum(len([1 for _,c,t in v if c=='200' and t>=500]) for v in rows['CTRL'].values())
cn=sum(len(v) for v in rows['CTRL'].values())
print(f"TOTAL search cold {sc}/{sn} ctrl cold {cc}/{cn}")
