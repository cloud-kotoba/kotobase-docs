import statistics

def load(path):
    with open(path) as f:
        return [float(x) for x in f if x.strip()]

def nrank_pct(vals, p=50):
    s = sorted(vals)
    n = len(s)
    idx = int((p / 100.0) * n + 0.999999)
    if idx < 1: idx = 1
    if idx > n: idx = n
    return s[idx - 1]

base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b473"
files = {"A": base+"_A.ttfb", "B": base+"_B.ttfb", "C": base+"_C.ttfb", "landing": base+"_landing.ttfb"}
THRESH = 0.5
out = []
for k in ["A","B","C","landing"]:
    vals = load(files[k])
    p50 = nrank_pct(vals, 50)
    cold = [v for v in vals if v >= THRESH]
    codes = open(base+"_"+k+".code").read().split()
    n200 = codes.count("200")
    out.append((k, len(vals), len(cold), p50, max(vals) if vals else 0.0, sorted(cold)[:8], n200, len(codes)))
res = []
for k,n,ncold,p50,mx,cv,n200,ntot in out:
    line = "RUN%s n=%d cold=%d/%d p50=%.4fs max=%.4fs http200=%d/%d cold_vals:[%s]" % (k,n,ncold,n,p50,mx,n200,ntot,", ".join("%.4f"%v for v in cv))
    res.append(line)
    print(line)
tot_cold = sum(c for (k,n,c,p,m,cv,a,b) in out if k in ("A","B","C"))
tot_n = sum(n for (k,n,c,p,m,cv,a,b) in out if k in ("A","B","C"))
tot_200 = sum(a for (k,n,c,p,m,cv,a,b) in out if k in ("A","B","C"))
sumline = "SEARCH_TOTAL cold=%d/%d (~%.1f%%) http200=%d/%d" % (tot_cold,tot_n,100.0*tot_cold/tot_n,tot_200,tot_n)
res.append(sumline)
print(sumline)
land = [o for o in out if o[0]=="landing"][0]
landline = "LANDING cold=%d/%d p50=%.4fs max=%.4fs http200=%d/%d" % (land[2],land[1],land[3],land[4],land[6],land[7])
res.append(landline)
print(landline)
with open("/tmp/b473_stats.txt","w",encoding="utf-8") as f:
    f.write("\n".join(res)+"\n")