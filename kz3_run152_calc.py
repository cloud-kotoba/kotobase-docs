import re, statistics
from collections import Counter

def parse(path):
    runs = {}
    cur = None
    for line in open(path):
        m = re.match(r"=== run(\S+) search ===", line)
        if m:
            cur = m.group(1); runs[cur] = []
            continue
        if line.startswith("=== landing"):
            cur = "landing"; runs[cur] = []
            continue
        m = re.match(r"(\d{3}) ([\d.]+)", line)
        if m and cur:
            runs[cur].append((int(m.group(1)), float(m.group(2))))
    return runs

runs = parse("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run152_out.txt")
lines = []
for k, v in runs.items():
    codes = Counter(c for c, _ in v)
    tt = sorted(t for _, t in v)
    cold = [t for t in tt if t >= 0.5]
    p50 = tt[len(tt)//2 - 1] if tt else 0
    p95 = tt[max(0, int(round(0.95*len(tt)))-1)]
    lines.append(f"{k}: n={len(v)} codes={dict(codes)} cold(>=0.5s)={len(cold)}/{len(v)} cold_vals={[round(x,3) for x in cold]} p50={p50:.3f}s p95={p95:.3f}s max={tt[-1]:.3f}s")
total_cold = 0; total_n = 0
for k, v in runs.items():
    if k == "landing":
        continue
    total_cold += sum(1 for _, t in v if t >= 0.5); total_n += len(v)
lines.append(f"search total: cold {total_cold}/{total_n} ({100*total_cold/total_n:.1f}%)")
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run152_calc.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines))
