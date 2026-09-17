import re, statistics
cold = {r: [] for r in 'ABC'}
warm = {r: [] for r in 'ABC'}
ctrl = []
cur = None
for line in open('_f80_run203_out.txt'):
    m = re.match(r'run203([ABC]) (\d{3}) ([\d.]+)', line)
    if m:
        r, code, t = m.group(1), m.group(2), float(m.group(3))
        (cold if t >= 0.5 else warm)[r].append((code, t))
        continue
    m = re.match(r'control (\d{3}) ([\d.]+)', line)
    if m:
        ctrl.append((m.group(1), float(m.group(2))))
out = open('/tmp/f80_stats.txt', 'w')
for r in 'ABC':
    allr = cold[r] + warm[r]
    codes = set(c for c, _ in allr)
    wt = sorted(t for _, t in warm[r])
    p50 = statistics.median(wt) if wt else float('nan')
    out.write(f"run203{r}: n={len(allr)} codes={sorted(codes)} cold={len(cold[r])} cold_times={[t for _,t in cold[r]]} warm_p50={p50:.3f}s warm_max={max(wt):.3f}s\n")
ccodes = [c for c, _ in ctrl]
ct = [t for _, t in ctrl]
out.write(f"control: n={len(ctrl)} codes={sorted(set(ccodes))} p50={statistics.median(ct):.3f}s max={max(ct):.3f}s\n")
out.write(f"total cold={sum(len(v) for v in cold.values())}/60\n")
out.close()
