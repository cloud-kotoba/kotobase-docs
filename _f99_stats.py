import re, statistics
lines = open('_f99_run228_out.txt').read().splitlines()
data = {}
cur = None
for ln in lines:
    m = re.match(r'^(run228[A-C]|control) 200 ([\d.]+)$', ln)
    if m:
        data.setdefault(m.group(1), []).append(float(m.group(2)))
for k in ['run228A','run228B','run228C','control']:
    v = sorted(data[k])
    p50 = v[len(v)//2] if len(v)%2 else (v[len(v)//2-1]+v[len(v)//2])/2
    cold = [x for x in v if x >= 0.5]
    p95 = v[int(0.95*len(v))-1] if len(v) else None
    print(f"{k} n={len(v)} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={max(v)*1000:.1f}ms cold(>=0.5s)={len(cold)} {['%.3f'%c for c in cold]}")