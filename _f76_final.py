import re
src = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f76_run196_out.txt').read().splitlines()
blocks = {'run196A': [], 'run196B': [], 'run196C': [], 'landing control': []}
cur = None
for line in src:
    m = re.match(r'=== (\S+)( search)? ===', line)
    if m and m.group(1) in blocks:
        cur = m.group(1)
        continue
    if cur and re.match(r'^\d{3} \d', line):
        code, t = line.split()
        blocks[cur].append((code, float(t)))
lines = []
for name in ['run196A', 'run196B', 'run196C', 'landing control']:
    data = blocks[name]
    vals = sorted(t for _, t in data)
    n = len(vals)
    ok = sum(1 for c, _ in data if c == '200')
    cold = sum(1 for v in vals if v >= 0.5)
    p50 = vals[n // 2] * 1000 if n else 0
    mx = vals[-1] * 1000 if n else 0
    lines.append(f"{name}: n={n} ok={ok} cold(>=0.5s)={cold} p50={p50:.0f}ms max={mx:.0f}ms")
out = '\n'.join(lines)
open('/tmp/f76_final.txt', 'w').write(out + '\n')
print(out)
