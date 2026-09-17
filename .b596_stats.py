import glob, re, sys
def p50(xs):
    xs = sorted(xs)
    import math
    n = len(xs)
    return xs[max(0, math.ceil(0.5*n)-1)]
def stats(path):
    cold = warm = 0
    codes = {}
    vals = []
    coldvals = []
    with open(path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3: continue
            code, t = parts[-2], float(parts[-1])
            codes[code] = codes.get(code, 0) + 1
            if code != '200':
                continue
            vals.append(t)
            if t >= 0.5:
                cold += 1
                coldvals.append(t)
            else:
                warm += 1
    mx = max(vals) if vals else 0
    p95 = sorted(vals)[max(0, int(len(vals)*0.95)-1)] if vals else 0
    return cold, warm, codes, (p50(vals)*1000 if vals else 0), p95*1000, mx*1000, coldvals

B = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b596/'
out = open(B + 'stats.txt', 'w')
tot_cold = 0
for g in 'ABC':
    c, w, codes, p5, p95, mx, cv = stats(B + f'run596{g}.raw')
    tot_cold += c
    print(f'run596{g}: cold>=0.5s {c}/20 warm {w}/20 codes={codes} p50={p5:.1f}ms p95={p95:.1f}ms max={mx:.1f}ms coldvals={[round(x*1000) for x in cv]}', file=out)
c, w, codes, p5, p95, mx, cv = stats(B + 'control596.raw')
print(f'control: cold {c}/20 warm {w}/20 codes={codes} p50={p5:.1f}ms p95={p95:.1f}ms max={mx:.1f}ms coldvals={[round(x*1000) for x in cv]}', file=out)
print(f'TOTAL search cold: {tot_cold}/60 ({tot_cold/60*100:.1f}%)', file=out)
out.close()
print('done')
