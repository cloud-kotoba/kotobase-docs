import re, statistics
data = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/falsify66_run175_out.txt').read().splitlines()
runs = {}
cur = None
for line in data:
    m = re.match(r'=== (run175(\w)|landing control)', line)
    if m:
        cur = m.group(2) if m.group(2) else 'LC'
        runs[cur] = []
        continue
    m = re.match(r'\S+ \d+ ([\d.]+) (\d+)', line)
    if m and cur:
        runs[cur].append((float(m.group(1)), m.group(2)))
out = []
for k, vals in runs.items():
    ts = [t for t, c in vals]
    codes = set(c for _, c in vals)
    cold = [t for t in ts if t >= 0.5]
    out.append(f"{k}: n={len(ts)} codes={codes} cold(>=0.5s)={len(cold)} {['%.3f'%t for t in cold]} p50={statistics.median(ts)*1000:.0f}ms max_excl_cold={(max([t for t in ts if t<0.5], default=0))*1000:.0f}ms")
open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/falsify66_run175_summary.txt','w').write('\n'.join(out)+'\n')
