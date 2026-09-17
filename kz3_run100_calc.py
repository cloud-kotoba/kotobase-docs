import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run99_out.txt"
runs = {}
cur = None
for line in open(path):
    m = re.match(r"=== run(\w+) search ===", line)
    if m:
        cur = m.group(1)
        runs[cur] = []
    elif line.startswith("=== landing control ==="):
        cur = "CTRL"
        runs[cur] = []
    else:
        m = re.match(r"(\d{3}) ([\d.]+)", line.strip())
        if m and cur:
            runs[cur].append((int(m.group(1)), float(m.group(2))))

def p50(xs):
    xs = sorted(xs)
    n = len(xs)
    import math
    k = math.ceil(0.5 * n)
    return xs[max(k - 1, 0)]

for rid in ["99A", "99B", "99C", "CTRL"]:
    data = runs[rid]
    codes = [c for c, t in data]
    ts = [t for c, t in data]
    cold = [t for t in ts if t >= 0.5]
    warm = [t for t in ts if t < 0.5]
    print(f"run{rid}: n={len(data)} ok200={codes.count(200)} cold(>=0.5s)={len(cold)} "
          f"coldvals={sorted(cold)} warmP50={p50(warm)*1000:.0f}ms "
          f"warmRange=({min(warm)*1000:.0f}-{max(warm)*1000:.0f}ms) "
          f"allP50={p50(ts)*1000:.0f}ms")
