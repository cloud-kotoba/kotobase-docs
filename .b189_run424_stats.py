#!/usr/bin/env python3
import os
base = '.b189_run424'

def load(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            p = ln.split()
            if len(p) < 3:
                continue
            try:
                code = int(p[1])
                t = float(p[2])
                rows.append((code, t))
            except Exception:
                pass
    return rows

def stats(tag):
    rows = load(base + '_' + tag + '.txt')
    codes = [c for c, _ in rows]
    times = [t for _, t in rows]
    cold = [t for t in times if t >=  0.5]
    warm = [t for t in times if t < 0.5]
    res = {}
    res['n'] = len(rows)
    res['all200'] = all(c ==  200 for c in codes)
    res['cold'] = len(cold)
    res['cold_max'] = max(cold) if cold else  0.0
    res['cold_list'] = [round(t, 3) for t in sorted(cold, reverse=True)[:5]]
    if warm:
        w = sorted(warm)
        res['p50'] = round(w[(len(w)-1)//2]*1000)
        idx95 = int(0.95*len(w))-1
        if idx95 <  0: idx95 =  0
        if idx95 > len(w)-1: idx95 = len(w)-1
        res['p95'] = round(w[idx95]*1000)
        res['warm_min'] = round(min(warm)*1000)
        res['warm_max'] = round(max(warm)*1000)
    else:
        res['p50'] = None
        res['p95'] = None
    return res

out = []
for tag in ['A', 'B', 'C', 'landing']:
    s = stats(tag)
    out.append((tag, s))

for tag, s in out:
    line = "%s: n=%d all200=%s cold=%d/%d coldmax=%.3fs " % (tag, s['n'], s['all200'], s['cold'], s['n'], s['cold_max'])
    if s['cold_list']:
        line += ' cold_list=' + ','.join(map(str, s['cold_list']))
    if s['p50'] is not None:
        line += "warm_p50=%dms p95=%dms min=%d max=%d " % (s['p50'], s['p95'], s['warm_min'], s['warm_max'])
    print(line)

allOK = all(s['all200'] for _, s in out[:4])
if allOK:
    tc = sum(s['cold'] for _, s in out[:3])
    pct = (tc*100) // 60
    print("TOTAL search cold %d/60 (%d%%)" % (tc, pct))
else:
    print("NON-200 present - inspect")
