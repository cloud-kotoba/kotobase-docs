import re, statistics, json
src = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f73_run193_out.txt'
out = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f73_run193_stats.json'
cur = None
data = {}
for line in open(src):
    line = line.strip()
    m = re.match(r'=== (.+) ===', line)
    if m:
        cur = m.group(1)
        data[cur] = []
    elif line and cur:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            data[cur].append((parts[0], float(parts[1])))
res = {}
for k, v in data.items():
    tt = [t for c, t in v]
    ok = [c for c, t in v if c == '200']
    cold = sorted([t for t in tt if t >= 0.5])
    tt_s = sorted(tt)
    n = len(tt_s)
    p50 = tt_s[(n - 1) // 2] if tt_s else None
    res[k] = {'n': n, 'ok200': len(ok), 'coldCount': len(cold),
              'coldValues': [round(c * 1000) for c in cold],
              'p50ms': round(p50 * 1000, 1) if p50 else None,
              'maxMs': round(max(tt) * 1000, 1) if tt else None}
print(json.dumps(res, ensure_ascii=False, indent=1))
with open(out, 'w') as f:
    json.dump(res, f, ensure_ascii=False, indent=1)
