import re
src = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f76_run196_out.txt').read().splitlines()
i = 0
summary = []
while i < len(src):
    line = src[i]
    m = re.match(r'=== (run\w+|landing control) ===', line)
    if m:
        vals = []
        codes = []
        j = i + 1
        while j < len(src) and re.match(r'^\d{3} ', src[j]):
            code, t = src[j].split()
            codes.append(code)
            vals.append(float(t))
            j += 1
        vals.sort()
        n = len(vals)
        p50 = vals[n // 2] if n else 0
        cold = sum(1 for v in vals if v >= 0.5)
        summary.append(f"{m.group(1)}: n={n} ok={codes.count('200')} cold(>=0.5s)={cold} p50={p50*1000:.0f}ms max={vals[-1]*1000 if vals else 0:.0f}ms")
        i = j
    else:
        i += 1
out = '\n'.join(summary)
open('/tmp/f76_stats.txt', 'w').write(out + '\n')
print(out)
