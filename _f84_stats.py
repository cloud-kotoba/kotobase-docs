import re, statistics
cold = []
warm = []
ctrl_cold = []
ctrl_all = []
for line in open('_f84_run209_out.txt'):
    m = re.match(r'(run209[A-C]|control) (\d+) ([\d.]+)', line.strip())
    if not m:
        continue
    tag, code, t = m.group(1), int(m.group(2)), float(m.group(3))
    if tag == 'control':
        ctrl_all.append(t)
    else:
        warm.append((tag, t))
        if t > 0.5:
            cold.append((tag, t))
times = [t for _, t in warm]
ctimes = ctrl_all
out = []
out.append(f"cold(>500ms) {len(cold)}/{len(times)}: {cold[:10]}")
if times:
    out.append(f"warm n={len(times)} p50={statistics.median(times)*1000:.1f}ms max={max(times)*1000:.1f}ms")
if ctimes:
    out.append(f"control n={len(ctimes)} p50={statistics.median(ctimes)*1000:.1f}ms max={max(ctimes)*1000:.1f}ms cold={sum(1 for t in ctimes if t>0.5)}")
head = open('_f84_run209_out.txt').read().splitlines()
out.append(f"span: {head[0]} .. {head[-1]}")
open('_f84_stats_out.txt', 'w').write("\n".join(out) + "\n")
