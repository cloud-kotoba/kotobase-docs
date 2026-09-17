import statistics
base='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
tot_cold=0; tot=0; lines=[]; all200=True
for s in ['A','B','C']:
    recs=[]
    for ln in open(base+f'.b569_{s}.ttfb'):
        c,t=ln.split(); recs.append((c,float(t)))
    ts=sorted(t for c,t in recs)
    codes=set(c for c,t in recs)
    cold=sum(1 for c,t in recs if t>=0.5)
    p50=ts[len(ts)//2]; p95=ts[min(int(len(ts)*0.95),len(ts)-1)]
    lines.append(f"run569{s}: codes {'/'.join(sorted(codes))} n={len(ts)} cold={cold}/20 p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={ts[-1]*1000:.1f}ms")
    tot_cold+=cold; tot+=len(ts)
    if codes!={'200'}: all200=False
recs=[]
for ln in open(base+'.b569_ctl.ttfb'):
    c,t=ln.split(); recs.append((c,float(t)))
ts=sorted(t for c,t in recs); codes=set(c for c,t in recs)
cold=sum(1 for c,t in recs if t>=0.5)
lines.append(f"control: codes {'/'.join(sorted(codes))} n={len(ts)} cold={cold}/20 p50={ts[len(ts)//2]*1000:.1f}ms max={ts[-1]*1000:.1f}ms")
print('\n'.join(lines))
print(f"TOTAL cold {tot_cold}/{tot} all200={all200}")
