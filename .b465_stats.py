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

runs = {'A': 'run465A', 'B': 'run465B', 'C': 'run465C'}
total_cold = 0
total_n = 0
for rk, rn in sorted(runs.items()):
    vals = load(f'.b465_run465_{rk}.ttfb')
    cold = [v for v in vals if v >= 0.5]
    total_cold += len(cold)
    total_n += len(vals)
    p50 = nearest_rank_p50(vals)
    cold_str = ' '.join(f'{v:.4f}' for v in sorted(cold)) if cold else 'none'
    print(f'{rn}: n={len(vals)} cold(>=0.5s)={len(cold)}/{len(vals)} p50={1000*p50:.1f}ms max={1000*max(vals):.1f}ms cold_vals=[{cold_str}]')

lv = load('.b465_run465_landing.ttfb')
lcold = [v for v in lv if v >= 0.5]
lp50 = nearest_rank_p50(lv)
cold_str = ' '.join(f'{v:.4f}' for v in sorted(lcold)) if lcold else 'none'
print(f'landing_control: n={len(lv)} cold={len(lcold)}/{len(lv)} p50={1000*lp50:.1f}ms max={1000*max(lv):.1f}ms cold_vals=[{cold_str}]')
print(f'TOTAL_COLD {total_cold}/{total_n} ({100.0*total_cold/total_n:.1f}%)')