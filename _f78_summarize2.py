import re, json
cold = {r: [] for r in 'ABC'}
warm = {r: [] for r in 'ABC'}
ctrl = []
codes = {}
for line in open('_f78_run201b_out.txt'):
    line = line.strip()
    m = re.match(r'(\S+) (\d{3}) ([\d.]+)', line)
    if not m:
        continue
    code = m.group(2)
    t = float(m.group(3))
    codes[code] = codes.get(code, 0) + 1
    if line.startswith('run201'):
        r = line[6]
        (warm if t < 0.5 else cold)[r].append(t)
    elif line.startswith('control'):
        ctrl.append(t)
def pct(xs, p):
    xs = sorted(xs)
    return xs[max(0, round(p/100*(len(xs)+1))-1)] if xs else None
out = {'codes': codes}
for r in 'ABC':
    allv = warm[r] + cold[r]
    out[r] = dict(n=len(allv), cold=len(cold[r]), cold_times=cold[r],
                  warm_p50=pct(warm[r], 50), warm_max=max(warm[r]) if warm[r] else None,
                  p50=pct(allv, 50), max_t=max(allv) if allv else None)
out['control'] = dict(n=len(ctrl), cold=sum(1 for t in ctrl if t >= 0.5),
                      p50=pct(ctrl, 50), max_t=max(ctrl))
print(json.dumps(out, ensure_ascii=False))
