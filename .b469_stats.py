import sys, statistics, re
from collections import OrderedDict

def load(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    return [float(x) for x in lines]

base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b469"
files = {
    "A": base + "_A.ttfb",
    "B": base + "_B.ttfb",
    "C": base + "_C.ttfb",
    "landing": base + "_landing.ttfb",
}

def nrank_pct(vals, p=50):
    # nearest-rank percentile: ceil(p/100 * n)th smallest (1-indexed)
    s = sorted(vals)
    n = len(s)
    idx = int((p / 100.0) * n + 0.999999)  # ceil
    if idx < 1: idx = 1
    if idx > n: idx = n
    return s[idx - 1]

THRESH = 0.5
out = []
for k in ["A", "B", "C", "landing"]:
    vals = load(files[k])
    p50 = nrank_pct(vals, 50)
    cold = [v for v in vals if v >= THRESH]
    out.append((k, len(vals), len(cold), p50, max(vals) if vals else 0.0, sorted(cold)[:8]))

for k, n, ncold, p50, mx, coldvals in out:
    cv = ", ".join("%.4f" % v for v in coldvals)
    print("RUN%s n=%d cold=%d/%d p50=%.4fs max=%.4fs cold_vals:[%s]" % (k, n, ncold, n, p50, mx, cv))

# total search cold
tot_cold = sum(c for (k,n,c,p,m,cv) in out if k in ("A","B","C"))
tot_n = sum(n for (k,n,c,p,m,cv) in out if k in ("A","B","C"))
print("SEARCH_TOTAL cold=%d/%d (~%.1f%%)" % (tot_cold, tot_n, 100.0*tot_cold/tot_n))
land = [o for o in out if o[0]=="landing"][0]
print("LANDING cold=%d/%d p50=%.4fs max=%.4fs" % (land[2], land[1], land[3], land[4]))
# row counts
for k in ["A","B","C","landing"]:
    print("CT_%s=%d" % (k, len(load(files[k]))))