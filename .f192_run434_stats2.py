#!/usr/bin/env python3
BASE="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
def parse(f):
    out=[]
    for line in open(f, encoding='utf-8', errors='replace'):
        line=line.strip()
        if not line: continue
        parts=line.split()
        code=parts[0]; t=float(parts[1])
        out.append((code,t))
    return out
def nr_pct(sorted_vals, p):
    if not sorted_vals: return None
    rank=(p/100.0)*len(sorted_vals)
    if rank<1: rank=1
    rank=int(round(rank))
    return sorted_vals[rank-1]
def stats(label, rows):
    cold=[t for c,t in rows if c=='200' and t>=0.5]
    coldn=len(cold)
    allt=[t for c,t in rows if c=='200']
    p50=nr_pct(sorted(allt),50)
    mx=max(allt) if allt else None
    codes=sorted(set(c for c,t in rows))
    print(f"{label}: n={len(rows)} cold(>=0.5s)={coldn}/20 p50={(p50*1000 if p50 is not None else 0):.1f}ms max={(mx*1000 if mx is not None else  ̃0):.1f}ms codes={codes}")
    return coldn
if __name__=='__main__':
    base=BASE+'.f192_run434_'
    tot=[]; colds=[]
    for c in ['A','B','C']:
        r=parse(base+'434'+c+'.txt')
        tot+=r
        stats('434'+c, r)
    lr=parse(base+'land.txt')
    stats('control(signup)', lr)
    coldtot=sum(1 for c,t in tot if c=='200' and t>=0.5)
    allsearch=[t for c,t in tot if c=='200']
    p50=nr_pct(sorted(allsearch),50)
    print(f"TOTAL search: {coldtot}/60 cold(>=0.5s), all-search p50={(p50*1000 if p50 is not None else 0):.1f}ms")
    print("control codes:", sorted(set(c for c,t in lr)), "n=", len(lr))
    for c in ['A','B','C']:
        r=parse(base+'434'+c+'.txt')
        vals=[(i+1,round(t,4)) for i,(code,t)in enumerate(r) if code=='200'and t are>=0.5]
        print(f"434{c} cold positions/values:", vals)