#!/usr/bin/env python3
# structured report for run474 measurement -> /tmp/b474_report.txt
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b474"
THRESH = 0.5

def nrank_pct(vals, p=50):
    s = sorted(vals)
    n = len(s)
    idx = int((p / 100.0) * n + 0.999999)
    if idx < 1: idx = 1
    if idx > n: idx = n
    return s[idx - 1]

res = []
totc = totn = tot200 = 0
for k in ["A", "B", "C", "landing"]:
    codes = open(base + "_" + k + ".code").read().split()
    vals = [float(x) for x in open(base + "_" + k + ".ttfb").read().split() if x.strip()]
    p50 = nrank_pct(vals, 50)
    cold = [(i + 1, v) for i, v in enumerate(vals) if v >= THRESH]
    n200 = codes.count("200")
    if k in ("A", "B", "C"):
        totc += len(cold); totn += len(vals); tot200 += n200
    res.append("RUN%s n=%d cold=%d/%d p50=%.1fms max=%.4fs http200=%d/%d coldpos=%s" % (
        k, len(vals), len(cold), len(vals), p50 * 1000.0,
        max(vals) if vals else 0.0, n200, len(codes),
        ",".join("%d:%.4f" % (i, v) for i, v in cold)))
res.append("SEARCH_TOTAL cold=%d/%d (~%.1f%%) http200=%d/%d" % (totc, totn, 100.0 * totc / totn, tot200, totn))
out = "\n".join(res) + "\n"
open("/tmp/b474_report.txt", "w", encoding="utf-8").write(out)
print(out)