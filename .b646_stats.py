lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b646_raw.txt').read().split('\n')

def parse():
    runs = {'A': [], 'B': [], 'C': []}
    control = []
    cur = None
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if ln == 'WARMUP_END':
            cur = runs['A']; continue
        if ln == 'RUN_END_A':
            cur = runs['B']; continue
        if ln == 'RUN_END_B':
            cur = runs['C']; continue
        if ln == 'RUN_END_C':
            cur = control; continue
        if ln == 'ALL_END':
            break
        if cur is None:
            continue
        p = ln.split()
        if len(p) == 2:
            cur.append((int(p[0]), float(p[1]) * 1000.0))
    return runs, control

def stats(name, xs):
    codes = [c for c, _ in xs]
    ts = sorted(t for _, t in xs)
    n = len(ts)
    p50 = ts[max(0, int(0.50 * n + 0.5) - 1)]
    p95 = ts[max(0, int(0.95 * n + 0.5) - 1)]
    cold = [t for t in ts if t >= 500.0]
    cr = (f'{min(cold):.1f}-{max(cold):.1f}ms' if cold else 'n/a')
    print(f'{name}: n={n} non200={sum(1 for c in codes if c != 200)} '
          f'cold {len(cold)}/{n} ({100.0*len(cold)/n:.1f}%) range={cr} '
          f'p50={p50:.1f}ms p95={p95:.1f}ms max={max(ts):.1f}ms')

runs, control = parse()
print('valid:', all(len(runs[k]) == 20 for k in runs) and len(control) == 20)
for k in ('A', 'B', 'C'):
    stats('run646' + k, runs[k])
stats('control', control)
