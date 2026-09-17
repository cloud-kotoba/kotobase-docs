#!/usr/bin/env python3
import io, math, os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
names = ["run520A", "run520B", "run520C", "landing"]

def parse(p):
    codes=[]; vals=[]
    try:
        f=io.open(p, encoding="utf-8")
    except IOError:
        return codes, vals
    for ln in f:
        s=ln.strip()
        if not s: continue
        parts=s.split(None,2)
        if len(parts)<2: continue
        try:
            c=int(parts[0]); t=float(parts[1])
        except ValueError:
            continue
        codes.append(c); vals.append(t)
    f.close()
    return codes, vals

res=[]
for name in names:
    p=base+"/.b520_"+name+".ttfb"
    codes, vals = parse(p)
    n=len(vals)
    non200=n-codes.count(200)
    cold=len([v for v in vals if v>=0.5])
    if not vals:

        res.append("%s: n=0 non200=0 cold=0 p50=nan max=nan" % name)
        continue
    sv=sorted(vals)
    pos=int(math.ceil(0.5*n))-1
    if pos<0: pos=0
    p50=sv[pos]
    mx=max(vals)
    res.append("%s: n=%d non200=%d cold=%d p50=%.4f max=%.4f" % (name, n, non200, cold, p50, mx))

out="\n".join(res)
w=io.open("/tmp/b520_stats_out.txt","w",encoding="utf-8")
w.write(out+"\n"); w.close()
print(out)