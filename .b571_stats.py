import statistics
res={}
for s in ['A','B','C']:
    vals=[float(x) for x in open(f'.b571_{s}.ttfb').read().split() if x.strip()]
    cold=[v for v in vals if v>=0.5]
    res[s]=(len(vals),len(cold),statistics.median(sorted(vals))[0] if False else sorted(vals)[len(vals)//2-1:(len(vals)//2)+1])
    res[s]=(len(vals),len(cold),sorted(vals)[(len(vals)-1)//2],max(vals))
    # positions of cold
    pos=[i+1 for i,v in enumerate(vals) if v>=0.5]
    res[s]=(len(vals),len(cold),sorted(vals)[(len(vals)-1)//2],max(vals),pos,[round(v,4) for v in cold])
ctl=[float(x) for x in open('.b571_ctl.ttfb').read().split() if x.strip()]
coldc=[v for v in ctl if v>=0.5]
posc=[i+1 for i,v in enumerate(ctl) if v>=0.5]
print('CTL',len(ctl),len(coldc),sorted(ctl)[(len(ctl)-1)//2],max(ctl),posc,[round(v,4) for v in coldc])
for s in ['A','B','C']:
    print(s,res[s])
tot=sum(res[s][1] for s in 'ABC')
print('cold total',tot,'/60')
