import statistics
def stats(p):
    v=[float(x) for x in open(p) if x.strip()]
    v.sort()
    cold=[x for x in v if x>=0.5]
    return len(v), len(cold), round(statistics.median(v)*1000,1), round(max(v)*1000,1), [round(c*1000,1) for c in cold]
for p in ['.b566_A.ttfb','.b566_B.ttfb','.b566_C.ttfb','.b566_ctl.ttfb']:
    print(p, stats(p))
