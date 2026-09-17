#!/usr/bin/env python3
import statistics
res = {}
for s in ['A','B','C','ctl']:
    f = '.b572_%s.ttfb' % s
    xs = [float(x) for x in open(f).read().split()]
    ok = len(xs)
    cold = [x for x in xs if x >= 0.5]
    p50 = statistics.median(xs)
    xs_s = sorted(xs)
    p95 = xs_s[min(len(xs_s)-1, int(0.95*len(xs_s)))]
    res[s] = dict(ok=ok, cold=len(cold), coldv=[round(x,4) for x in cold], p50=round(p50,1), p95=round(p95,1), mx=round(max(xs),4), mn=round(min(xs),4))
tot_cold = sum(res[s]['cold'] for s in ['A','B','C'])
print(res)
print('total cold %d/60' % tot_cold)
