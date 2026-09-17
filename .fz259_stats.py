import re
# falsify 259th: parse ttfb files, compute stats
def stats(path):
    vals=[]; codes={}
    for line in open(path):
        line=line.strip()
        if not line: continue
        m=line.split()
        codes[m[0]]=codes.get(m[0],0)+1
        vals.append(float(m[1]))
    vals.sort()
    n=len(vals)
    p50=vals[n//2] if n%2 else (vals[n//2-1]+vals[n//2])/2
    cold=[v for v in vals if v>=0.5]
    print(f"{path}: n={n} codes={codes} p50={p50*1000:.1f}ms max={vals[-1]*1000:.1f}ms cold>=0.5s: {len(cold)} {['%.4f'%v for v in cold]}")
    return n, codes, p50, len(cold)
tot_cold=0; tot=0; ok=True
for S in ['A','B','C']:
    n,codes,p50,cold=stats(f".fz259_run574{S}.ttfb")
    tot+=n; tot_cold+=cold
    if codes.get('200',0)!=n: ok=False
stats(".fz259_landing.ttfb")
print(f"TOTAL query: {tot_cold}/{tot} ({100*tot_cold/tot:.1f}%) all200={ok}")
