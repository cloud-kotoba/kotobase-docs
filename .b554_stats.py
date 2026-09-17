#!/usr/bin/env python3
# K-Z3 12hr band run554 stats: cold(>=0.5s) count + p50/p90 per group
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def stats(path):
    with open(path) as f:
        vals = sorted(float(l) for l in f if l.strip())
    n = len(vals)
    if not n:
        return "n=0"
    cold = sum(1 for v in vals if v >= 0.5)
    p50 = vals[n // 2] if n % 2 else (vals[n // 2 - 1] + vals[n // 2]) / 2
    p90 = vals[int(n * 0.9) - 1] if int(n * 0.9) >= 1 else vals[-1]
    return "n=%d cold=%d p50=%.4f p90=%.4f max=%.4f" % (n, cold, p50, p90, vals[-1])
groups = ["A", "B", "C", "landing"]
tot_n = tot_cold = 0
for g in groups:
    p = ".b554_run554_%s.ttfb" % g
    print("run554_%s: %s" % (g, stats(p)))
for g in ["A", "B", "C"]:
    with open(".b554_run554_%s.ttfb" % g) as f:
        vals = [float(l) for l in f if l.strip()]
    tot_n += len(vals)
    tot_cold += sum(1 for v in vals if v >= 0.5)
print("run554 search total: n=%d cold=%d (%.1f%%)" % (tot_n, tot_cold, 100.0 * tot_cold / max(tot_n, 1)))
print(open(".b554_run554_t0.txt").read().strip())
