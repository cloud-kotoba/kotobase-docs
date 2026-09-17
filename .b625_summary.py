import json
raw = open('/tmp/falsify_run625.json').read()
d = json.loads(raw.split('\nexit=')[0])
print('ts:', d['ts'])
for lab, g in d['groups'].items():
    bad = [c for c in g['codes'] if c != '200']
    print(lab, 'n=', len(g['codes']), 'non200:', bad, 'cold_ms:', [round(c*1000,1) for c in g['cold']], 'p50_ms:', g['p50_ms'], 'p95_ms:', g['p95_ms'], 'max_ms:', g['max_ms'])
