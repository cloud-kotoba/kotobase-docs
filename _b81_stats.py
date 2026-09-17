import re, statistics
lines = open('_b81_run206_out.txt').read().splitlines()
runs = {}
for l in lines:
    m = re.match(r'(run206[ABC]|control) (\d+) ([\d.]+)', l)
    if m:
        runs.setdefault(m.group(1), []).append((int(m.group(2)), float(m.group(3))))
for k, v in runs.items():
    ts = sorted(t for c, t in v)
    codes = [c for c, t in v]
    cold = [t for t in ts if t >= 0.5]
    n = len(ts)
    # nearest-rank p50, p95
    import math
    def nr(p):
        idx = max(1, math.ceil(p * n))
        return ts[idx - 1]
    print(k, 'n', n, '200', codes.count(200), 'cold', len(cold),
          'p50 %.3f' % nr(0.5), 'p95 %.3f' % nr(0.95),
          'max %.3f' % ts[-1], 'coldvals', ['%.3f' % t for t in cold])
