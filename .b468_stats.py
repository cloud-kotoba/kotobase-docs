#!/usr/bin/env python3
import math, sys, os

BASE = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def nearest_rank_p50(vals):
    s = sorted(vals)
    r = int(math.ceil(0.5 * len(s)))  # nearest-rank, p=50 -> rank index (1-based)
    return s[r-1]

def load(fn):
    with open(fn, "r", encoding="utf-8") as f:
        return [float(x) for x in f.read().split()]

names = ["468A", "468B", "468C", "landing"]
data = {}
for n in names:
    fn = os.path.join(BASE, ".b468_%s.ttfb" % n)
    if not os.path.exists(fn):
        print("MISSING %s" % fn); sys.exit(1)
    data[n] = load(fn)

out = []
total_cold = 0
for n in names:
    vals = data[n]
    cold = [v for v in vals if v >= 0.5]
    p50 = nearest_rank_p50(vals)
    if n != "landing":
        total_cold += len(cold)
    warm = [v for v in vals if v < 0.5]
    warm_p50 = nearest_rank_p50(warm) if warm else 0.0
    out.append("%s: n=%d cold(>=0.5s)=%d (positions %s) p50=%.1fms warm_p50=%.1fms min=%.1fms max=%.1fms all=%s" % (
        n, len(vals), len(cold),
        [i+1 for i,v in enumerate(vals) if v>=0.5],
        p50*1000, warm_p50*1000, min(vals)*1000, max(vals)*1000,
        [round(v*1000,1) for v in vals]))
out.append("TOTAL: cold %d/60 (%.1f%%)" % (total_cold, total_cold/60*100))
print("\n".join(out))
with open("/tmp/bench_468_stats.out", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("written")