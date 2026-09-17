import glob, statistics
def stats(name):
    vals = []
    lines = open(f'.b579_run{name}.txttfb').read().split()
    for x in lines:
        try: vals.append(float(x))
        except ValueError: pass
    if not vals: return f'{name}: no data'
    cold = [v for v in vals if v >= 0.5]
    vals_s = sorted(vals)
    p50 = vals_s[len(vals_s)//2]
    p95 = vals_s[min(len(vals_s)-1, int(len(vals_s)*0.95))]
    return f'{name}: n={len(vals)} cold={len(cold)} ({cold if cold else "-"}) p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms max={max(vals)*1000:.1f}ms'
out = [stats(n) for n in 'ABC']
cv = []
for x in open('.b579_control.txttfb').read().split():
    try: cv.append(float(x))
    except ValueError: pass
if cv:
    coldc = [v for v in cv if v >= 0.5]
    cv_s = sorted(cv)
    out.append(f'CONTROL: n={len(cv)} cold={len(coldc)} ({coldc if coldc else "-"}) p50={cv_s[len(cv_s)//2]*1000:.1f}ms max={max(cv)*1000:.1f}ms')
open('.b579_stats.txt','w').write('\n'.join(out)+'\n')
