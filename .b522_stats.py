#!/usr/bin/env python3
import math
def nearest_rank_p50(vals):
    s = sorted(vals); n = len(s); return s[max(1, math.ceil(0.50*n)) - 1]
def load(path):
    out = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try: out.append(float(line))
            except ValueError: continue
    return out
runs = {'A':'run522A','B':'run522B','C':'run522C'}
for rk, rn in sorted(runs.items()):
    vals = load(f'.b522_run522_{rk}.ttfb')
    cold = [v for v in vals if v >= 0.5]
    print(f'{rn}: n={len(vals)} cold={len(cold)}/{len(vals)} p50={1000*nearest_rank_p50(vals):.1f}ms max={1000*max(vals):.1f}ms cold={sorted(cold)}')
lv = load('.b522_run522_landing.ttfb')
lc = [v for v in lv if v >= 0.5]
print(f'landing: n={len(lv)} cold={len(lc)}/{len(lv)} p50={1000*nearest_rank_p50(lv):.1f}ms max={1000*max(lv):.1f}ms')