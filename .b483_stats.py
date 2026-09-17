import os
d = "/tmp/bs483_1788854046"
def stats(name):
    vals=[]
    with open(os.path.join(d, name+"_ttfb.txt")) as f:
        for line in f:
            line=line.strip()
            if line: vals.append(float(line))
    vals.sort()
    n=len(vals)
    cold=sum(1 for v in vals if v>=0.5)
    def pct(p):
        idx=max(1,int(round(n*p/100.0))) if n>=1 else 1
        idx=max(1,min(n,idx))
        return vals[idx-1]
    p50=pct(50)
    mx=vals[-1] if vals else 0.0
    return dict(n=n, cold=cold, p50=p50, max=mx, all=vals)
out={}
for k in ["run483A","run483B","run483C","run483ctrl"]:
    out[k]=stats(k)
    s=out[k]
    print("%s n=%d cold=%d p50=%.4f max=%.4f" % (k,s["n"],s["cold"],s["p50"],s["max"]))
    print("  vals=" + " ".join("%.3f"%v for v in s["all"]))
tot_cold=out["run483A"]["cold"]+out["run483B"]["cold"]+out["run483C"]["cold"]
print("TOTAL search cold /60 = %d" % tot_cold)
print("control cold /20 = %d" % out["run483ctrl"]["cold"])