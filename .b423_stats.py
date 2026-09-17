import re
import math

pat = re.compile(r'^(\d{3}) (\S+) (\S+)$')

def load(fn):
    rows = []
    for line in open(fn):
        m = pat.match(line.strip())
        if not m:
            continue
        code = m.group(1)
        ttfb = float(m.group(2))
        total = float(m.group(3))
        rows.append([code, ttfb, total])
    return rows

def p50(xs):
    n = len(xs)
    if n == 0:
        return 0.0
    s = sorted(xs)
    rank = int(math.ceil(n * 0.5))
    if rank < 1:
        rank = 1
    return s[rank - 1]

files = [".b423_run423_A.txt", ".b423_run423_B.txt", ".b423_run423_C.txt", ".b423_run423_land.txt"]
names = ["run423A", "run423B", "run423C", "landing"]

tot_cold = 0
land_cold = 0
lines = []

for i in range(len(files)):
    fn = files[i]
    name = names[i]
    rows = load(fn)
    n = len(rows)
    ok = 0
    ttfb = []
    for r in rows:
        if r[0] == "200":
            ok = ok + 1
        ttfb.append(r[1])
    coldn = 0
    for t in ttfb:
        if t >= 0.5:
            coldn = coldn + 1
    p =p50(ttfb)
    mx = max(ttfb) if ttfb else 0.0
    line = "%s n=%d code200=%d/%d cold=%d/%d p50=%.1fms max=%.1fms" % (name, n, ok, n, coldn, n, p*1000.0, mx*1000.0)
    lines.append(line)
    if name == "landing":
        land_cold = coldn
    else:
        tot_cold = tot_cold + coldn

if land_cold == 0:
    verdict = "control clean separation (cold level confined to search side)"
else:
    verdict = "not-separated (landing/control also shows cold)"

lines.append("---VERDICT---")
lines.append("search cold total=%d/60; landing cold=%d/20 -> %s" % (tot_cold, land_cold, verdict))

with open(".b423_stats_out.txt","w") as f:
    f.write("\n".join(lines))
    f.write("\n")

for L in lines:
    print(L)