sets = {}
cur = None
ctrl = []
src = '.b532k_run649_results.txt'
lines = open(src).read().strip().split('\n')
for line in lines:
    s = line.strip()
    if not s:
        continue
    if s.startswith('---SET'):
        cur = s.split()[1]
        sets.setdefault(cur, [])
        continue
    if s.startswith('---CONTROL'):
        cur = 'CTRL'
        continue
    if s.startswith('END '):
        continue
    parts = s.split()
    code, t = parts[0], float(parts[1])
    if cur == 'CTRL':
        ctrl.append((code, t))
    elif cur:
        sets[cur].append((code, t))

out = []
def stats(pairs):
    codes = [c for c, _ in pairs]
    ts = sorted(t for _, t in pairs)
    n = len(ts)
    p50 = ts[max(0, int(n * 0.50 + 0.5) - 1)] if ts else None
    cold = sum(1 for t in ts if t >= 0.5)
    return codes.count('200'), n, p50, cold, ts

for k in ['A', 'B', 'C']:
    c, n, p50, cold, ts = stats(sets[k])
    out.append("SET %s: ok=%d/%d p50=%.1fms cold(>=0.5s)=%d min=%.1f max=%.1f" % (k, c, n, p50 * 1000, cold, ts[0] * 1000, ts[-1] * 1000))
    out.append("  ttfb_ms=" + ",".join("%.1f" % (t * 1000) for t in ts))
c, n, p50, cold, ts = stats(ctrl)
out.append("CONTROL: ok=%d/%d p50=%.1fms cold(>=0.5s)=%d min=%.1f max=%.1f" % (c, n, p50 * 1000, cold, ts[0] * 1000, ts[-1] * 1000))
allc = sets['A'] + sets['B'] + sets['C']
c, n, p50, cold, ts = stats(allc)
out.append("TOTAL: ok=%d/%d cold=%d/60 (%.1f%%) overall_p50=%.1fms" % (c, n, cold, cold / 60 * 100, p50 * 1000))
open('/tmp/b532k_stats.txt', 'w').write("\n".join(out) + "\n")
