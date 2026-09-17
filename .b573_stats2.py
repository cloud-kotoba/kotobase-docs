#!/usr/bin/env python3
import statistics
for s in ['A','B','C','ctl']:
    xs=[float(x) for x in open('.b573_%s.ttfb'%s).read().split()]
    print(s, 'n=%d cold=%d p50=%.1fms max=%.4f' % (len(xs), len([x for x in xs if x>=0.5]), statistics.median(xs)*1000, max(xs)))
