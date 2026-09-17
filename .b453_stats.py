import sys

def nearest_rank_p50(vals):
    s = sorted(vals)
    idx = max(1, int(0.50*len(s)) if (0.50*len(s)) == int(0.50*len(s)) and int(0.50*len(s))>=1 else int(0.50*len(s))+1)
    if idx-1 >= len(s):
        idx = len(s)
    return s[idx-1]

def stats(path):
    vals = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                v = float(line)
            except ValueError:
                continue
            if v < 0:
                continue
            vals.append(v)
    if not vals:
        return None
    s = sorted(vals)
    n = len(s)
    cold = [v for v in s if v >= 0.5]
    import statistics
    return {
        'n': n,
        'cold': len(cold),
        'p50': nearest_rank_p50(s),
        'min': s[0],
        'max': s[-1],
        'p95': s[max(0, min(n-1, int(0.95*n)-1))],
    }

for label, path in [('run453A', '.b453_run453A.ttfb'),
                    ('run453B', '.b453_run453B.ttfb'),
                    ('run453C', '.b453_run453C.ttfb'),
                    ('landing', '.b453_landing.ttfb')]:
    r = stats(path)
    if r is None:
        print(f'{label}: NO DATA')
    else:
        print(f"{label}: n={r['n']} cold(>=0.5s)={r['cold']} p50={r['p50']*1000:.1f}ms p95={r['p95']*1000:.1f}ms min={r['min']*1000:.1f}ms max={r['max']*1000:.1f}ms")