import sys, statistics

def p50(vals):
    # nearest-rank percentile
    s = sorted(vals)
    idx = max(0, int(0.5*len(s)) - (0 if len(s)%2==0 else 0))
    # nearest-rank: floor? use ceil(0.5*n)
    import math
    pos = math.ceil(0.5*len(s))  # 1-indexed
    return s[pos-1]

lines = open('/tmp/run523_raw.txt').read().splitlines()
runs = {'A':[], 'B':[], 'C':[]}
ctrl = []
for ln in lines:
    if ln.startswith('SEARCH_'):
        parts = ln.split()
        # SEARCH_A_1 200 1.285667
        lab = parts[0].split('_')[1]
        code = parts[1]
        ttfb = float(parts[2])
        runs[lab].append((code, ttfb))
    elif ln.startswith('CTRL_'):
        parts = ln.split()
        code = parts[1]
        ttfb = float(parts[2])
        ctrl.append((code, ttfb))

THRESH = 0.5
for lab in ['A','B','C']:
    d = runs[lab]
    codes = [x[0] for x in d]
    ttfbs = [x[1] for x in d]
    cold = [x for x in ttfbs if x >= THRESH]
    warm = [x for x in ttfbs if x < THRESH]
    print(f"run523{lab}: n={len(d)} 200={codes.count('200')}/{len(d)} cold={len(cold)}/{len(d)} p50={p50(ttfbs)*1000:.1f}ms warm_p50={p50(warm)*1000:.1f}ms max={max(ttfbs)*1000:.1f}ms cold_vals={[round(x,3) for x in cold]}")

dc = ctrl
codes = [x[0] for x in dc]
ttfbs = [x[1] for x in dc]
cold = [x for x in ttfbs if x >= THRESH]
warm = [x for x in ttfbs if x < THRESH]
print(f"control: n={len(dc)} 200={codes.count('200')}/{len(dc)} cold={len(cold)}/{len(dc)} p50={p50(ttfbs)*1000:.1f}ms max={max(ttfbs)*1000:.1f}ms")
print(f"TOTAL search cold = {sum(1 for x in 'ABC' for cc in runs[x] if cc[1]>=THRESH)}/60")
