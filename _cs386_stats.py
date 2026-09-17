#!/usr/bin/env python3
import sys
def nr_p50(vals):
    s=sorted(vals); n=len(s)
    idx=int(0.5*n+0.999999); idx=max(1,idx)
    return s[idx-1]
def stats(fn, cutoff=0.5):
    cold=[]; warm=[]; rows=[]
    with open(fn) as f:
        for line in f:
            parts=line.split()
            if len(parts)<2: continue
            try: code=int(parts[0]); ttfb=float(parts[1])
            except ValueError: continue
            rows.append((code,ttfb))
            if code!=200: continue
            if ttfb>=cutoff: cold.append(ttfb)
            else: warm.append(ttfb)
    n200=sum(1 for c,t in rows if c==200)
    pct = (100.0*n200/len(rows)) if rows else 0.0
    pct = round(pct,1)
    out="n=%d n200=%d(%s%%)" % (len(rows),n200,pct)
    out += " cold%d=%d/%d" % (int(cutoff*1000),len(cold),len(rows))
    if cold: out += " cold_vals=" + str([round(x,4) for x in sorted(cold)])
    if warm: out += " p50=%.1fms max=%.1fms" % (nr_p50(warm)*1000, max(warm)*1000)
    else: out += " warm={}"
    return out
for fn in sys.argv[1:]:
    print(fn.replace('.txt',''),"::",stats(fn))