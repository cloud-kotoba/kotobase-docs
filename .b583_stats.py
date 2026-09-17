import sys

def stats(path, label_filter=None):
    rows = []
    with open(path) as f:
        for line in f:
            parts = line.split()
            if len(parts) < 3:
                continue
            lab, pos, rest = parts[0], parts[1], parts[2:]
            if label_filter and lab != label_filter:
                continue
            code, t = rest[0], rest[1]
            rows.append((int(pos), int(code), float(t)))
    rows.sort()
    ts = sorted(r[2] for r in rows)
    codes = [r[1] for r in rows]
    cold = [r for r in rows if r[2] >= 0.5]
    n = len(ts)
    p50 = ts[n // 2 - 1] if n % 2 == 0 else ts[n // 2]
    p95 = ts[int(0.95 * n) - 1] if n >= 20 else ts[-1]
    return (n, codes.count(200), len(cold), [round(r[2], 4) for r in cold],
            [r[0] for r in cold], round(p50, 4), round(p95, 4), round(ts[-1], 4), round(ts[0], 4))

for lab in ['A', 'B', 'C']:
    print('run583%s' % lab, stats('/tmp/.b583_search.tsv', lab))
print('CTL', stats('/tmp/.b583_ctl.tsv', 'CTL'))
