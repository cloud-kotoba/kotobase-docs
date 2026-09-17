import statistics as st
from collections import defaultdict

lines = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f102_run233_out.txt').read().splitlines()
groups = defaultdict(list)
for ln in lines:
    parts = ln.split()
    if len(parts) != 3:
        continue
    label, code, tt = parts[0], parts[1], float(parts[2])
    if code != '200':
        continue
    groups[label].append(tt)

def pct(seq, p):
    s = sorted(seq)
    if not s: return None
    k = (len(s)-1)*p
    f = int(k); c = f+1 if f+1 < len(s) else f
    lo = s[f]; hi = s[c]
    return lo + (hi-lo)*(k-f)

COLD = 0.5
for label in ['run233A','run233B','run233C','control']:
    v = groups[label]
    n = len(v)
    cold = [x for x in v if x >= COLD]
    warm = [x for x in v if x < COLD]
    print(f"{label}: n={n} cold>={COLD}: {len(cold)}/{n} cold_vals={[round(x,3) for x in cold]}")
    print(f"  p50(all)={pct(v,0.5)*1000:.1f}ms max={max(v)*1000:.1f}ms p50(warm)={pct(warm,0.5)*1000 if warm else None:.1f}ms" if warm else
          f"  p50(all)={pct(v,0.5)*1000:.1f}ms max={max(v)*1000:.1f}ms")