import re, statistics
lines = open('kz3_run153_out.txt').read().splitlines()
runs = {}
cur = None
for l in lines:
    m = re.match(r'=== run(\S+) search ===', l)
    if m:
        cur = 'run' + m.group(1); runs[cur] = []
        continue
    if l.startswith('=== landing'):
        cur = 'control'; runs[cur] = []
        continue
    m = re.match(r'(\d{3}) ([\d.]+)', l)
    if m and cur:
        runs[cur].append((m.group(1), float(m.group(2))))
out = []
for k, v in runs.items():
    ts = sorted(t for _, t in v)
    cold = sum(1 for _, t in v if t >= 1.0)
    p50 = statistics.median(ts)
    out.append(f"{k}: n={len(v)} cold(>=1s)={cold}/{len(v)} p50={p50*1000:.1f}ms max={max(ts)*1000:.1f}ms")
open('kz3_run153_calc.txt', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
