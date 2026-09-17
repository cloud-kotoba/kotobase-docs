#!/usr/bin/env python3
"""K-Z3 run105 aggregation: cold(>=0.5s) count + p50 + control."""
import re, statistics, json

OUT = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run105_out.txt"
res = {}
cur = None
for line in open(OUT):
    m = re.match(r"=== run(\S+) search", line)
    if m:
        cur = "run" + m.group(1)
        res[cur] = []
        continue
    if line.startswith("=== landing"):
        cur = "landing"
        res[cur] = []
        continue
    m = re.match(r"(\d{3}) ([\d.]+)", line.strip())
    if m and cur:
        res[cur].append((int(m.group(1)), float(m.group(2))))

summary = {}
for k, v in res.items():
    codes = [c for c, _ in v]
    t = sorted(t for _, t in v)
    cold = [t for t in t if t >= 0.5]
    summary[k] = {
        "n": len(v), "ok200": codes.count(200),
        "cold_ge_0.5s": len(cold),
        "cold_list": cold,
        "p50": round(statistics.median(t), 3),
        "min": round(t[0], 3), "max": round(t[-1], 3),
    }
print(json.dumps(summary, indent=1))
