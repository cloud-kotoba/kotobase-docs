#!/usr/bin/env python3
import math

def nearest_rank_p50(vals):
    s = sorted(vals)
    n = len(s)
    idx = max(1, math.ceil(0.50*n)) - 1
    return s[idx]
def load(path):
    out = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                v = float(line)
            except ValueError:
                continue
            out.append(v)
    return out

runs = {'A': 'run529A', 'B': 'run529B', 'C': 'run529C'}
total_cold = 0
total_n = 0
for rk, rn in sorted(runs.items()):
    vals = load('.b529_run529_%s.ttfb' % rk)
    cold = [v for v in vals if v >= 0.5]
    total_cold += len(cold)
    total_n += len(vals)
    p50 = nearest_rank_p50(vals)
    cold_str = ' '.join('%.4f' % v for v in sorted(cold)) if cold else 'none'
    print('%s: n=%d cold=%d/%d p50=%.1fms max=%.1fms cold_vals=[%s]' % (rn, len(vals), len(cold), len(vals), 1000*p50, 1000*max(vals), cold_str))

lv = load('.b529_run529_landing.ttfb')
lcold = [v for v in lv if v >=  0.5]
lp50 = nearest_rank_p50(lv)
cold_str = ' '.join('%.4f' % v for v in sorted(lcold)) if lcold else 'none'
print('landing_control: n=%d cold=%d/%d p50=%.1fms max=%.1fms cold_vals=[%s]' % (len(lv), len(lcold), len(lv), 1000*lp50, 1000*max(lv), cold_str))
print('TOTAL_SEARCH_COLD=%d/%d' % (total_cold, total_n))
la = load('.b529_run529_A.ttfb'); lb = load('.b529_run529_B.ttfb'); lc = load('.b529_run529_C.ttfb')
ca = [i+1 for i,v in enumerate(la) if v >=  0.5]
cb = [i+1 for i,v in enumerate(lb) if v >= 0.5]
cc = [i+1 for i,v in enumerate(lc) if v >=  0.5]
print('cold_pos A=%s B=%s C=%s' % (ca, cb, cc))