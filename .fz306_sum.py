import sys
from collections import OrderedDict
import math

rows = OrderedDict()
for line in open('/tmp/fz306.raw'):
    parts = line.split()
    if len(parts) != 4:
        continue
    label, idx, t, code = parts[0], int(parts[1]), float(parts[2]), int(parts[3])
    rows.setdefault(label, []).append((idx, t, code))

def pct(sorted_vals, p):
    n = len(sorted_vals)
    pos = int(math.ceil((p / 100.0) * n)) - 1
    pos = max(0, min(n-1, pos))
    return sorted_vals[pos]

tot_cold = 0
tot_all = 0
warm_vals_all = []
for label, items in rows.items():
    vals = [t for (_, t, _) in items]
    codes = {c for (_, _, c) in items}
    sv = sorted(vals)
    cold = [t for t in vals if t >= 0.5]
    n = len(vals)
    p50 = pct(sv, 50)
    p95 = pct(sv, 95)
    mx = max(vals)
    mn = min(vals)
    tot_cold += len(cold)
    tot_all += n
    warm = [t for t in vals if t < 0.5]
    if warm:
        warm_vals_all.extend([(label,i) for i,(t) in enumerate(warm)])
    print(f"{label}: n={n} cold(>=0.5s)={len(cold)}/{n} p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms min={mn*1000:.1f}ms max={mx*1000:.1f}ms codes={codes}")
    print(f"   cold times: {[f'{x:.3f}s' for x in cold]}")
    coldpos = [idx for (idx,t,c) in items if t >= 0.5]
    if coldpos:
        print(f"   cold idx: {coldpos}")

print(f"TOTAL cold={tot_cold}/{tot_all} ({100.0*tot_cold/tot_all:.1f}%)")