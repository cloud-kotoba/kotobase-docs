import re, json, statistics
cold = {r: [] for r in 'ABC'}
warm = {r: [] for r in 'ABC'}
ctrl = []
for line in open('_f78_run201_out.txt'):
    line = line.strip()
    m = re.match(r'run201([ABC]) (\d{3}) ([\d.]+)', line)
    if m:
        t = float(m.group(3))
        (warm if t < 0.5 else cold)[m.group(1)].append(t)
        continue
    m = re.match(r'control (\d{3}) ([\d.]+)', line)
    if m:
        ctrl.append((m.group(1), float(m.group(2))))
def pct(xs, p):
    xs = sorted(xs)
    return xs[max(0, round(p/100*(len(xs)+1))-1)] if xs else None
out = {}
for r in 'ABC':
    allv = warm[r] + cold[r]
    out[r] = dict(n=len(allv), cold=len(cold[r]),
                  cold_times=cold[r],
                  warm_p50=pct(warm[r], 50) if warm[r] else None,
                  warm_max=max(warm[r]) if warm[r] else None,
                  p50=pct(allv, 50), max_t=max(allv) if allv else None)
out['control'] = dict(n=len(ctrl), codes=collections.Counter(c for c, _ in ctrl) if False else None,
                      cold=sum(1 for _, t in ctrl if t >= 0.5),
                      p50=pct([t for _, t in ctrl], 50), max_t=max(t for _, t in ctrl))
codes = {}
for line in open('_f78_run201_out.txt'):
    m = re.match(r'\S+ (\d{3}) ', line.strip())
    if m: codes[m.group(1)] = codes.get(m.group(1), 0) + 1
out['codes'] = codes
print(json.dumps(out, ensure_ascii=False))
