# index-based parse: verified file layout (85 lines, read twice)
lines = open('.b532k_run649_results.txt').read().strip().split('\n')
def num(s):
    p = s.strip().split()
    return float(p[1])
A = [num(x) for x in lines[0:20]]
B = [num(x) for x in lines[21:41]]
C = [num(x) for x in lines[42:62]]
CT = [num(x) for x in lines[63:83]]
assert lines[20].startswith('---SET A') and lines[41].startswith('---SET B') and lines[62].startswith('---SET C') and lines[83].startswith('---CONTROL'), 'layout mismatch'
out = []
def rep(name, ts):
    ts = sorted(ts)
    n = len(ts)
    p50 = ts[max(0, int(n * 0.50 + 0.5) - 1)]
    cold = sum(1 for t in ts if t >= 0.5)
    out.append("%s: n=%d p50=%.1fms cold(>=0.5s)=%d min=%.1f max=%.1f" % (name, n, p50 * 1000, cold, ts[0] * 1000, ts[-1] * 1000))
    out.append("  " + ",".join("%.1f" % (t * 1000) for t in ts))
    return cold, p50
ca, pa = rep('SET A', A)
cb, pb = rep('SET B', B)
cc, pc = rep('SET C', C)
ct, pt = rep('CONTROL', CT)
allts = sorted(A + B + C)
pall = allts[max(0, int(60 * 0.50 + 0.5) - 1)]
out.append("TOTAL: n=60 cold=%d/60 (%.1f%%) overall_p50=%.1fms" % (ca + cb + cc, (ca + cb + cc) / 60 * 100, pall * 1000))
open('/tmp/b532k_stats_final.txt', 'w').write("\n".join(out) + "\n")
