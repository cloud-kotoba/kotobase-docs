import statistics

def nrank_pct(vals, p=50):
    s = sorted(vals)
    n = len(s)
    idx = int((p / 100.0) * n + 0.999999)
    if idx < 1: idx = 1
    if idx > n: idx = n
    return s[idx - 1]

base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b480"
THRESH = 0.5
out = []
for k in ["A", "B", "C", "landing"]:
    raw = open(base + "_" + k + ".raw").read().split()
    # raw lines: "<code> <ttfb>" interleaved (20 lines per run)
    codes = raw[0::2]
    vals = [float(x) for x in raw[1::2]]
    p50 = nrank_pct(vals, 50)
    cold = sorted([v for v in vals if v >= THRESH])
    n200 = codes.count("200")
    out.append((k, len(vals), len(cold), p50, max(vals) if vals else 0.0, cold, n200, len(codes)))
res = []
for k, n, ncold, p50, mx, cv, n200, ntot in out:
    line = "RUN%s n=%d cold=%d/%d p50=%.4fs max=%.4fs http200=%d/%d cold_vals:[%s]" % (k, n, ncold, n, p50, mx, n200, ntot, ", ".join("%.4f" % v for v in cv))
    res.append(line)
    print(line)
tc = sum(c for (k, n, c, p, m, cv, a, b) in out if k in ("A", "B", "C"))
tn = sum(n for (k, n, c, p, m, cv, a, b) in out if k in ("A", "B", "C"))
t200 = sum(a for (k, n, c, p, m, cv, a, b) in out if k in ("A", "B", "C"))
sl = "SEARCH_TOTAL cold=%d/%d (~%.1f%%) http200=%d/%d" % (tc, tn, 100.0 * tc / tn, t200, tn)
res.append(sl)
print(sl)
land = [o for o in out if o[0] == "landing"][0]
ll = "LANDING cold=%d/%d p50=%.4fs max=%.4fs http200=%d/%d" % (land[2], land[1], land[3], land[4], land[6], land[7])
res.append(ll)
print(ll)
with open("/tmp/b480_stats.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(res) + "\n")