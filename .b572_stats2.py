#!/usr/bin/env python3
import statistics
for s in ['A','B','C','ctl']:
    xs = sorted(float(x) for x in open('.b572_%s.ttfb' % s).read().split())
    print(s, 'p50=%.1fms p95=%.1fms max=%.4fs n=%d' % (statistics.median(xs)*1000, xs[int(0.95*len(xs))]*1000 if len(xs)>1 else xs[-1]*1000, xs[-1], len(xs)))
