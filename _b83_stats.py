import re, statistics
per_run = {}
cold = []
warm = []
ctrl_all = []
for line in open('_b83_run210_out.txt'):
    m = re.match(r'(run210[A-C]|control) (\d+) ([\d.]+)', line.strip())
    if not m:
        continue
    tag, code, t = m.group(1), int(m.group(2)), float(m.group(3))
    if tag == 'control':
        ctrl_all.append((code, t))
    else:
        per_run.setdefault(tag, []).append((code, t))
        warm.append((tag, t))
        if t > 0.5:
            cold.append((tag, t))
out = []
for r in 'ABC':
    ts = per_run.get('run210' + r, [])
    ok = [t for c, t in ts if c == 200]
    out.append(f"run210{r}: n={len(ts)} 200={len(ok)} cold={sum(1 for t in ok if t>0.5)} p50={statistics.median(ok)*1000:.1f}ms max={max(ok)*1000:.1f}ms" if ts else f"run210{r}: MISSING")
okc = [t for c, t in ctrl_all if c == 200]
out.append(f"control: n={len(ctrl_all)} 200={len(okc)} cold={sum(1 for t in okc if t>0.5)} p50={statistics.median(okc)*1000:.1f}ms max={max(okc)*1000:.1f}ms" if ctrl_all else "control: MISSING")
out.append(f"total cold(>500ms) {len(cold)}/{len(warm)}: {cold[:12]}")
head = open('_b83_run210_out.txt').read().splitlines()
out.append(f"span: {head[0]} .. {head[-1]}")
open('_b83_stats_out.txt', 'w').write("\n".join(out) + "\n")
