import collections
rows = [l.split() for l in open('.b649_samples.txt') if l.strip()]
stats = collections.defaultdict(list)
codes = collections.defaultdict(list)
for s, n, code, dt in rows:
    stats[s].append(float(dt))
    codes[s].append(code)
out = []
total_cold = 0
for s in ['A', 'B', 'C', 'L']:
    v = stats[s]
    v.sort()
    cold = sum(1 for x in v if x >= 0.5)
    if s != 'L':
        total_cold += cold
    out.append(f"{s}: n={len(v)} codes={''.join(codes[s])} cold>=0.5s={cold}/{len(v)} min={v[0]:.3f} p50={v[len(v)//2]:.3f} max={v[-1]:.3f}")
    deep = [(i+1, x) for i, x in enumerate(stats[s]) if x >= 0.5]
    out.append(f"   cold detail (attempt_index, sec): {deep}")
out.append(f"total cold A+B+C = {total_cold}/60 = {total_cold/60:.3%}")
open('.b649_stats.txt', 'w').write('\n'.join(out) + '\n')
