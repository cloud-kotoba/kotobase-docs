import statistics
lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f75_run195_out.txt').read().strip().splitlines()
cur = None
data = {}
for l in lines:
    if l.startswith('=== run') or 'landing control' in l:
        cur = l.strip('= ').strip()
        data[cur] = []
    elif cur and l.strip():
        parts = l.split()
        if len(parts) == 2:
            try:
                data[cur].append((int(parts[0]), float(parts[1])))
            except ValueError:
                pass
out = []
for k, v in data.items():
    if not v:
        continue
    codes = [c for c, t in v]
    ts = sorted(t for c, t in v)
    cold = sum(1 for t in ts if t >= 0.5)
    p50 = statistics.median(ts)
    mx = max(ts)
    out.append(f"{k}: n={len(v)} ok={codes.count(200)} cold(>=0.5s)={cold} p50={p50*1000:.0f}ms max={mx*1000:.0f}ms")
print("\n".join(out))
open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f75_stats.txt', 'w').write("\n".join(out) + "\n")
