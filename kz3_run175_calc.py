import re

lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/kz3_run175_out.txt').read().splitlines()
print(lines[0], lines[1])
cur = None
groups = {}
for ln in lines:
    m = re.match(r'=== run(\S+) search', ln)
    if m:
        cur = m.group(1); groups[cur] = []
    elif 'landing' in ln:
        cur = 'L'; groups[cur] = []
    elif re.match(r'\d{3} ', ln) and cur:
        code, t = ln.split()
        groups[cur].append((code, float(t)))

for k, v in groups.items():
    ts = sorted(t for _, t in v)
    n = len(ts)
    cold = [t for t in ts if t >= 0.5]
    p50 = ts[n // 2] if n % 2 else (ts[n // 2 - 1] + ts[n // 2]) / 2
    codes = set(c for c, _ in v)
    print(f'{k}: n={n} codes={codes} cold={len(cold)} {cold} p50={p50*1000:.0f}ms max={ts[-1]*1000:.0f}ms')

tot_cold = sum(len([t for _, t in v if t >= 0.5]) for k, v in groups.items() if k != 'L')
print(f'search total cold: {tot_cold}/60')
