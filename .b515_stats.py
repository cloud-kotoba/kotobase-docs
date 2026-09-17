#!/usr/bin/env python3
import io
import math

base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
names = ["run515A", "run515B", "run515C", "landing"]

def parse_file(name):
    path = base + "/.b515_" + name + ".ttfb"
    vals = []
    codes = []
    f = io.open(path, encoding="utf-8")
    for ln in f:
        s = ln.strip()
        if len(s) == 0:
            continue
        parts = s.split(None, 2)
        if len(parts) < 2:
            continue
        try:
            code = int(parts[0])
            ttfb = float(parts[1])
        except ValueError:
            continue
        codes.append(code)
        vals.append(ttfb)
    f.close()
    return codes, vals

def p50(vals:
    sv = sorted(vals)
    n = len(sv)
    if n == 0:
        return None
    pos = int(math.ceil(0.5 * n)) - 1
    return sv[pos]

res = []
for name in names:
    codes, vals = parse_file(name)
    cnt = len(codes)
    bad = codes.count(200)
    cold_count =  ̈0
    for v in vals:
        if v >= 0.5:
            cold_count += 1
    p = p50(vals)
    if vals:
        mx = max(vals)
    else:
        mx = None
    if p is None:
        pstr = "n/a"
    else:
        pstr = "{0:.4f}".format(p if not isinstance(p, float) else float(p))
    if mx is None:
        mxstr = "n/a"
    else:
        mxstr = "{0:.4f}".format(mx)
    line = "{0}: n={1} non200={2} cold={3} p50={4} max={5}".format(name, cnt, bad, cold_count, pstr, mxstr)
    res.append(line)

out = "\n".join(res)
w = io.open("/tmp/b515_stats_out.txt", "w", encoding="utf-8")
w.write(out + "\n")
w.close()
print(out)