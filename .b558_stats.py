import statistics
def stats(p):
    v=[float(x) for x in open(p) if x.strip()]
    v.sort()
    cold=[x for x in v if x>=0.5]
    return len(v), len(cold), round(statistics.median(v)*1000,1), round(max(v)*1000,1), [round(c*1000,1) for c in cold]
for p in ['.b558_A.ttfb','.b558_B.ttfb','.b558_C.ttfb','.b558_ctl.ttfb']:
    print(p, stats(p))
