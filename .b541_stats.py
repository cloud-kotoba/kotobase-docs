import sys, statistics, collections, math

def parse(fn):
    vals=[]; codes=[]; cold=[]
    for idx,line in enumerate(open(fn, encoding='utf-8'), start=1):
        line=line.strip()
        if not line: continue
        parts=line.split()
        if len(parts)<2: continue
        code=parts[0]; ttfb=float(parts[1])
        codes.append(code)
        vals.append(ttfb)
        if ttfb>=0.5: cold.append(idx)
    vals_sorted=sorted(vals)
    n=len(vals_sorted)
    if n>0:
        idx=int(math.ceil(0.5*n))-1
        p50=vals_sorted[idx]
    else:
        p50=float('nan')
    n_non200=sum(1 for c in codes if c!='200')
    code_counter=collections.Counter(codes)
    return dict(n=n, p50=p50, coldpos=cold,
                maxv=max(vals) if vals else float('nan'),
                n_cold=len(cold), n_non200=n_non200, codes=dict(code_counter))

base=sys.argv[1]
res={}
for name in ['A','B','C','landing']:
    res[name]=parse('%s_%s.raw'%(base,name))

lines=[]
for name in ['A','B','C','landing']:
    d=res[name]
    lines.append('%s n=%d p50=%.4f max=%.4f cold=%d/%d cold_idx=%s non200=%d codes=%s'%(
        name, d['n'], d['p50'], d['maxv'], d['n_cold'], d['n'],
        d['coldpos'], d['n_non200'], d['codes']))
print('\n'.join(lines))
