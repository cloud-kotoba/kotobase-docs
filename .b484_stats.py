import os, statistics
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def stats(name, fname):
    vals=[]; codes={}
    with open(os.path.join(d, fname)) as f:
        for line in f:
            line=line.rstrip("\n")
            if not line: continue
            parts=line.split()
            if len(parts)>=2:
                try:
                    code=int(parts[0]); ttfb=float(parts[1])
                except ValueError:
                    continue
                codes[code]=codes.get(code,0)+1
                vals.append(ttfb)
    if not vals:
        return dict(n=0,cold=0,p50=0,max=0,codes=codes)
    vals.sort()
    n=len(vals)
    cold=sum(1 for v in vals if v>=0.5)
    def pct(p):
        idx=max(1,int(round(n*p/100.0))) if n>=1 else 1
        idx=max(1,min(n,idx))
        return vals[idx-1]
    return dict(n=n,cold=cold,p50=pct(50),max=vals[-1],codes=codes)
out={}
labels={"run484A":".b484_A.raw","run484B":".b484_B.raw","run484C":".b484_C.raw","run484ctrl":".b484_landing.raw"}
for k,f in labels.items():
    out[k]=stats(k,f)
    s=out[k]
    print("%s n=%d cold=%d p50=%.4f max=%.4f codes=%s" % (k,s["n"],s["cold"],s["p50"],s["max"],s["codes"]))
tot=out["run484A"]["cold"]+out["run484B"]["cold"]+out["run484C"]["cold"]
print("TOTAL search cold /60 = %d" % tot)
print("control cold /20 = %d" % out["run484ctrl"]["cold"])