#!/usr/bin/env python3
import sys, statistics

def p50(v):
    s = sorted(v)
    n = len(s)
    if n == 0: return None
    m = (n - 1) // 2
    return s[m]

lines = open('/home/x/_f100_run230_out.txt' if False else sys.argv[1]).read().splitlines()
# parse run230X / control lines: "key http_code time_total"
from collections import defaultdict
groups = defaultdict(list)
codes = defaultdict(list)
for ln in lines:
    p = ln.split()
    if len(p) != 3: continue
    key, code, t = p[0], p[1], p[2]
    try:
        tv = float(t)
    except ValueError:
        continue
    codes[key].append(code)
    groups[key].append(tv)

for key in sorted(groups.keys()):
    v = groups[key]
    c = codes[key]
    cold = sum(1 for x in v if x >= 0.5)
    non200 = sum(1 for x in c if x != '200')
    print(f"{key} n={len(v)} cold(>=0.5s)={cold} non200={non200} p50={p50(v):.6f} min={min(v):.6f} max={max(v):.6f}")