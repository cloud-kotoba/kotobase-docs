import re
src = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f76_run196_out.txt').read().splitlines()
markers = {}
order = ['run196A', 'run196B', 'run196C', 'landing control']
for name in order:
    markers[name] = src.index(f'=== {name} search ===' if 'run' in name else f'=== {name} ===')
bounds = []
for idx, name in enumerate(order):
    start = markers[name] + 1
    end = markers[order[idx + 1]] if idx + 1 < len(order) else len(src)
    bounds.append((name, start, end))
lines = []
for name, s, e in bounds:
    vals = []
    ok = 0
    for line in src[s:e]:
        m = re.match(r'^(\d{3}) (\d+\.\d+)$', line.strip())
        if m:
            ok += m.group(1) == '200'
            vals.append(float(m.group(2)))
    vals.sort()
    n = len(vals)
    cold = sum(1 for v in vals if v >= 0.5)
    p50 = vals[n // 2] * 1000 if n else 0
    mx = vals[-1] * 1000 if n else 0
    lines.append(f"{name}: n={n} ok={ok} cold(>=0.5s)={cold} p50={p50:.0f}ms max={mx:.0f}ms")
out = '\n'.join(lines)
open('/tmp/f76_final2.txt', 'w').write(out + '\n')
print(out)
