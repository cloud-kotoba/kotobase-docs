import re, statistics as st
rows = [l.split() for l in open('_f77_run200_out.txt') if l.strip()]
times = {}
for l in open('_f77_run200_out.txt'):
    m = re.match(r'(run200[ABC]|control)\s+(\d+)\s+([\d.]+)', l.strip())
    if m:
        times.setdefault(m.group(1), []).append((m.group(2), float(m.group(3))))
out = []
for k, v in times.items():
    codes = [c for c, t in v]
    ts = [t for c, t in v]
    cold = [t for c, t in v if t > 0.507]
    out.append(f"{k}: n={len(v)} non200={codes.count('200') and 0 if all(c=='200' for c in codes) else [c for c in codes if c!='200']} cold(>0.507s)={len(cold)} max={max(ts):.3f}s p50={st.median(ts)*1000:.0f}ms p90={sorted(ts)[int(len(ts)*0.9)]*1000:.0f}ms")
print('\n'.join(out))
