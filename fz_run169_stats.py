import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run169_out.txt"
lines = open(path).read().splitlines()
print("start:", lines[0])
section = None
stats = {}
for ln in lines[1:]:
    m = re.match(r"=== (\S+)", ln)
    if m:
        section = m.group(1)
        stats[section] = []
        continue
    if ln.startswith("end"):
        print("end:", ln)
        continue
    if section and ln.strip():
        parts = ln.split()
        if len(parts) >= 2:
            code, ttfb = parts[0], float(parts[1])
            stats[section].append((code, ttfb))

for sec, vals in stats.items():
    codes = [c for c, _ in vals]
    times = sorted(t for _, t in vals)
    n = len(times)
    cold = [t for t in times if t >= 0.5]
    p50 = times[n // 2] if n else 0
    p90 = times[int(n * 0.9)] if n else 0
    print(f"{sec}: n={n} ok200={codes.count('200')} cold(>=0.5s)={len(cold)} "
          f"p50={p50:.3f} p90={p90:.3f} max={times[-1]:.3f} min={times[0]:.3f}")
