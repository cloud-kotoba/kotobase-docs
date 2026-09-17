import re, sys

def stats(path):
    lines = open(path).read().splitlines()
    runs = {}
    ctrl = []
    cur = None
    for ln in lines:
        m = re.match(r'=== run161(\w) search', ln)
        if m:
            cur = 'run161' + m.group(1); runs[cur] = []
            continue
        if ln.startswith('=== landing'):
            cur = None; continue
        m = re.match(r'161(\w) (\d+) ([\d.]+) (\d+)', ln)
        if m:
            runs['run161' + m.group(1)].append((float(m.group(3)), int(m.group(4))))
            continue
        m = re.match(r'LC (\d+) ([\d.]+) (\d+)', ln)
        if m:
            ctrl.append((float(m.group(2)), int(m.group(3))))

    def nr_p(vals, p):
        s = sorted(vals)
        import math
        idx = max(1, math.ceil(p / 100 * len(s)))
        return s[idx - 1]

    print('dates:', lines[0], '|', lines[-1])
    cold_total = 0; n_total = 0
    for r, v in runs.items():
        ttfbs = [t for t, c in v]
        codes = set(c for _, c in v)
        cold = [t for t in ttfbs if t >= 0.5]
        p50 = nr_p(ttfbs, 50)
        cold_total += len(cold); n_total += len(ttfbs)
        print(f'{r}: n={len(v)} codes={codes} cold(>=0.5s)={len(cold)}/{len(v)} '
              f'cold_vals={cold} p50={p50:.3f}s min={min(ttfbs):.3f} max={max(ttfbs):.3f}')
    ttfbs = [t for t, c in ctrl]
    codes = set(c for _, c in ctrl)
    cold = [t for t in ttfbs if t >= 0.5]
    print(f'landing control: n={len(ctrl)} codes={codes} cold={len(cold)}/{len(ctrl)} '
          f'cold_vals={cold} p50={nr_p(ttfbs,50):.3f}s max={max(ttfbs):.3f}')
    print(f'search cold total: {cold_total}/{n_total} ({100*cold_total/n_total:.1f}%)')

stats('bench53_run161_out.txt')
