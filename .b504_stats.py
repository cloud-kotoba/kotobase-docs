#!/usr/bin/env python3
# K-Z3 stats for run504 (nearest-rank p50, cold>=0.5s), ASCII-safe output
import os

BASE = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.run504_raw"
COLD = 0.5

def parse(fn):
    rows = []
    with open(fn, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            code = parts[0]
            try:
                ttfb = float(parts[1])
            except ValueError:
                continue
            rows.append((code, ttfb))
    return rows

def nearest_p50(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return None
    r = int(round(0.50 * n))
    if r < 1:
        r = 1
    if r > n:
        r = n
    return s[r - 1]

def stats(fn, label):
    rows = parse(fn)
    out = []
    non200 = [r for r in rows if r[0] != "200"]
    n = len(rows)
    out.append("%s: count=%d non200=%d" % (label, n, len(non200)))
    if n == 0:
        out.append("  EMPTY (n=0 invalid)")
        return "\n".join(out)
    ttfbs = [r[1] for r in rows]
    cold_idx = [i + 1 for i, r in enumerate(rows) if r[1] >= COLD]
    cold_vals = [r[1] for r in rows if r[1] >= COLD]
    p50 = nearest_p50(ttfbs)
    mx = max(ttfbs)
    out.append("  cold>=%.2fs: %d/%d" % (COLD, len(cold_vals), n))
    if cold_vals:
        out.append("  cold_pos=%s cold_vals=%s" % (cold_idx, ["%.4f" % v for v in cold_vals]))
    out.append("  p50=%.4fs max=%.4fs" % (p50, mx))
    return "\n".join(out)

res = []
res.append(stats(os.path.join(BASE, "runA", "resp.txt"), "run504A"))
res.append(stats(os.path.join(BASE, "runB", "resp.txt"), "run504B"))
res.append(stats(os.path.join(BASE, "runC", "resp.txt"), "run504C"))
res.append(stats(os.path.join(BASE, "control", "resp.txt"), "control(signup)"))

outtext = "\n".join(res)
with open(os.path.join(BASE, "..", ".b504_stats.txt"), "w") as f:
    f.write(outtext + "\n")
print(outtext)