import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run98_out.txt"
lines = open(path).read().splitlines()
groups = {}
cur = None
for ln in lines:
    m = re.match(r"=== run(\w+) search ===", ln)
    if m:
        cur = "run" + m.group(1)
        groups[cur] = []
        continue
    if ln.startswith("=== landing"):
        cur = "landing"
        groups[cur] = []
        continue
    if ln.strip() and cur:
        code, t = ln.split()
        groups[cur].append((code, float(t)))

for name, vals in groups.items():
    codes = [c for c, _ in vals]
    times = sorted(t for _, t in vals)
    n = len(times)
    cold = sum(1 for t in times if t >= 0.5)
    p50 = times[max(0, -(-n * 50 // 100) - 1)]  # nearest-rank
    print(f"{name}: n={n} all200={all(c=='200' for c in codes)} cold(>=0.5s) {cold}/{n} p50 {p50:.3f}s min {times[0]:.3f} max {times[-1]:.3f}")
