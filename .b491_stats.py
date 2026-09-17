# bench K-Z3 run491 stats: nearest-rank p50, cold>=0.5s, http200
import os
B = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b491"
OUTF = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b491_stats_out.txt"
THRESH = 0.5

def load_ttfb(path):
    with open(path) as f:
        return [float(x) for x in f if x.strip()]

def load_codes(path):
    with open(path) as f:
        return [x.strip() for x in f if x.strip()]

def nrank_pct(vals, p=50):
    s = sorted(vals)
    n = len(s)
    idx = int(p / 100.0 * n + 0.999999)
    if idx < 1: idx = 1
    if idx > n: idx = n
    return s[idx-1]

out = []
tot_cold = tot_n = tot_200 = 0
for k in ["A", "B", "C", "landing"]:
    ttfb = load_ttfb(B + "_" + k + ".ttfb")
    codes = load_codes(B + "_" + k + ".code")
    n = len(ttfb)
    n200 = codes.count("200")
    cold = [v for v in ttfb if v >= THRESH]
    p50 = nrank_pct(ttfb, 50)
    mx = max(ttfb) if ttfb else 0.0
    line = "RUN%s n=%d cold=%d/%d p50=%.4fs max=%.4fs http200=%d/%d cold_vals:[%s]" % (
        k, n, len(cold), n, p50, mx, n200, len(codes),
        ", ".join("%.4f" % v for v in sorted(cold)))
    out.append(line)
    if k in ("A", "B", "C"):
        tot_cold += len(cold); tot_n += n; tot_200 += n200
sumline = "SEARCH_TOTAL cold=%d/%d (~%.1f%%) http200=%d/%d" % (tot_cold, tot_n, 100.0*tot_cold/tot_n, tot_200, tot_n)
out.append(sumline)
land = [o for o in out if o.startswith("RUNlanding")][0]
out.append(land)
with open(OUTF, "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print("DONE")