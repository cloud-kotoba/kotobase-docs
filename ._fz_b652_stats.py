import math, glob, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = open('._fz_b652_stats_out.txt','w')
def nearest_rank(sorted_vals, q):
    # nearest-rank: ceil(q*n)
    n = len(sorted_vals)
    idx = max(1, math.ceil(q*n))
    return sorted_vals[idx-1]
for name in ['search_A','search_B','search_C','control']:
    vals = []
    codes = {}
    positions = []
    with open(f'._fz_b652_{name}.txt') as f:
        for i, line in enumerate(f, 1):
            parts = line.split()
            if len(parts) != 2: continue
            code, ttfb = parts[0], float(parts[1])
            codes[code] = codes.get(code,0)+1
            vals.append(ttfb)
            if ttfb >= 0.5:
                positions.append((i, round(ttfb*1000,1)))
    vals.sort()
    if vals:
        out.write(f"{name}: n={len(vals)} codes={codes} cold(>=0.5s)={len(positions)} "
                  f"p50={round(nearest_rank(vals,0.5)*1000,1)}ms p95={round(nearest_rank(vals,0.95)*1000,1)}ms "
                  f"max={round(vals[-1]*1000,1)}ms cold_positions={positions}\n")
out.close()
