import re, statistics
cold = []
warm = []
ctrl = []
non200 = 0
for line in open('_f86_run212_out.txt'):
    m = re.match(r'(run212[A-C]|control) (\d+) ([\d.]+)', line.strip())
    if not m:
        continue
    tag, code, t = m.group(1), int(m.group(2)), float(m.group(3))
    if code != 200:
        non200 += 1
    if tag == 'control':
        ctrl.append(t)
    else:
        warm.append((tag, t))
        if t > 0.5:
            cold.append((tag, t))
times = [t for _, t in warm]
per = {}
for tag, t in warm:
    d = per.setdefault(tag, [])
    d.append(t)
out = []
for tag in sorted(per):
    d = per[tag]
    out.append(f"{tag}: n={len(d)} cold={sum(1 for x in d if x>0.5)} p50={statistics.median(d)*1000:.1f}ms max={max(d)*1000:.1f}ms")
out.append(f"total cold={len(cold)}/{len(times)} non200={non200}")
out.append("cold latencies: " + ", ".join(f"{t:.3f}s" for t in sorted(t for _, t in cold)))
if ctrl:
    out.append(f"control: n={len(ctrl)} p50={statistics.median(ctrl)*1000:.1f}ms max={max(ctrl)*1000:.1f}ms cold={sum(1 for t in ctrl if t>0.5)}")
head = open('_f86_run212_out.txt').read().splitlines()
out.append(f"span: {head[0]} .. {head[-1]}")
open('_f86_stats_out.txt', 'w').write("\n".join(out) + "\n")
