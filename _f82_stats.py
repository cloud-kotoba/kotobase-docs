import re, statistics
cold = {r: [] for r in 'ABC'}
warm = {r: [] for r in 'ABC'}
ctrl = []
for line in open('_f82_run205_out.txt'):
    m = re.match(r'run205([ABC]) (\d{3}) ([\d.]+)', line)
    if m:
        r, code, t = m.group(1), m.group(2), float(m.group(3))
        (cold if t >= 0.5 else warm)[r].append((code, t))
        continue
    m = re.match(r'control (\d{3}) ([\d.]+)', line)
    if m:
        ctrl.append((m.group(1), float(m.group(2))))
with open('_f82_stats_out.txt', 'w') as out:
    for r in 'ABC':
        allr = cold[r] + warm[r]
        codes = sorted(set(c for c, _ in allr))
        wt = sorted(t for _, t in warm[r])
        p50 = statistics.median(wt) if wt else float('nan')
        out.write(f"run205{r}: n={len(allr)} codes={codes} cold={len(cold[r])} cold_times={[t for _,t in cold[r]]} warm_p50={p50:.3f}s warm_max={max(wt):.3f}s\n" if wt else f"run205{r}: n={len(allr)} codes={codes} cold={len(cold[r])} cold_times={[t for _,t in cold[r]]} warm_p50=n/a\n")
    ccodes = [c for c, _ in ctrl]
    ct = [t for _, t in ctrl]
    out.write(f"control: n={len(ctrl)} codes={sorted(set(ccodes))} p50={statistics.median(ct):.3f}s max={max(ct):.3f}s\n")
    out.write(f"total cold={sum(len(v) for v in cold.values())}/60\n")
