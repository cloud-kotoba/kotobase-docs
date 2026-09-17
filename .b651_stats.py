#!/usr/bin/env python3
import io, os, statistics

def parse(path):
    rows = []
    for line in io.open(path, 'r', encoding='utf-8'):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        rows.append((parts[0], float(parts[1])))
    return rows

def nn(arr, q):
    arr = sorted(arr)
    k = max(1, int(-(-len(arr) * q // 1)))
    return arr[k - 1]

out = io.open('.b651_stats_out.txt', 'w', encoding='utf-8')
tot_cold = 0
for tag in ['A', 'B', 'C']:
    rows = parse('.b651_%s.txt' % tag)
    codes = [c for c, t in rows]
    ts = [t for c, t in rows]
    n = len(rows)
    cold = sum(1 for t in ts if t >= 0.5)
    tot_cold += cold
    out.write("run651%s n=%d codes_non200=%d cold=%d p50=%.1fms p90=%.1fms max=%.1fms\n" % (
        tag, n, sum(1 for c in codes if c != '200'), cold, nn(ts, .5) * 1000, nn(ts, .9) * 1000, max(ts) * 1000))
    colds = [t for t in ts if t >= 0.5]
    if colds:
        out.write("  cold vals(ms): %s\n" % ", ".join("%.1f" % (t * 1000) for t in colds))
out.write("TOTAL cold %d/60\n" % tot_cold)
rows = parse('.b651_land.txt')
ts = [t for c, t in rows]
codes = [c for c, t in rows]
cold = sum(1 for t in ts if t >= 0.5)
out.write("CONTROL n=%d codes_non200=%d cold=%d p50=%.1fms p90=%.1fms max=%.1fms\n" % (
    len(rows), sum(1 for c in codes if c != '200'), cold, nn(ts, .5) * 1000, nn(ts, .9) * 1000, max(ts) * 1000))
colds = [t for t in ts if t >= 0.5]
if colds:
    out.write("  ctrl cold vals(ms): %s\n" % ", ".join("%.1f" % (t * 1000) for t in colds))
out.close()
