#!/usr/bin/env python3
import json
from collections import OrderedDict

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f101_run232_out.txt"
lines = open(p).read().splitlines()

runs = OrderedDict()
for ln in lines:
    parts = ln.split()
    if len(parts) != 3:
        continue
    tag, code, t = parts[0], parts[1], float(parts[2])
    if code != "200":
        continue
    runs.setdefault(tag, []).append(t)

def stats(vals):
    s = sorted(vals)
    n = len(s)
    p50 = s[n//2] if n % 2 == 1 else (s[n//2-1]+s[n//2])/2
    cold = [v for v in s if v >= 0.5]
    return dict(n=n, p50=round(p50*1000,1), max=round(max(s)*1000,1),
                cold_n=len(cold),
                cold_vals=[round(v,3) for v in cold],
                all=[round(v,3) for v in s])

out = {}
for tag, vals in runs.items():
    out[tag] = stats(vals)

print(json.dumps(out, indent=2, ensure_ascii=False))

# totals
for tag, d in out.items():
    print(f"{tag}: cold {d['cold_n']}/{d['n']}  p50 {d['p50']}ms max {d['max']}ms")