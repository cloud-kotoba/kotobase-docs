import statistics, re
rows=[l.split() for l in open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f105_run237_out.txt') if re.match(r'^(run237|control)',l)]
def stats(tag):
    vals=[float(t) for k,_,t in rows if k==tag]
    cold=[v for v in vals if v>=0.5]
    warm=[v for v in vals if v<0.5]
    ss=sorted(vals)
    n=len(ss)
    def desc(name,lst):
        if not lst: return f"{name} n=0"
        return f"{name} n={len(lst)} p50={statistics.median(lst)*1000:.1f}ms min={min(lst)*1000:.1f}ms max={max(lst)*1000:.1f}ms"
    return f"  {desc('ALL',vals)} | cold(>=0.5s)={len(cold)} | {desc('warm',warm)}"
for r in ['run237A','run237B','run237C','control']:
    print(r, stats(r))
allvals=[float(t) for k,_,t in rows if k.startswith('run237')]
ss=sorted(allvals)
n=len(ss)
cold=[v for v in allvals if v>=0.5]
print("SEARCH TOTAL n",n,"cold(>=0.5)",len(cold),"(=%.2f%%)"%(100.0*len(cold)/n),"p50",ss[(n-1)//2]*1000,"ms","mean",statistics.mean(allvals)*1000,"ms")