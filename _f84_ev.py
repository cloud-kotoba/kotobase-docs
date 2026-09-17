import re
p = 'query-cosientist.md'
s = open(p).read()
# locate K-Z3 row line
lines = s.split('\n')
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
        break
if idx is None:
    open('_f84_ev_out.txt', 'w').write('NO_KZ3_ROW\n')
else:
    line = lines[idx]
    # append evidence before trailing status cells? docs use evidence column; previous bots appended at end of row line.
    ev = " falsify 第84回 (12:34, 12時台 2セット目): run209A–C cold 7/60 (~11.7%) — 全 7 件が run209A 冒頭集中 (0.870–1.824s, 即消失), B/C 0/20, warm p50 43.9ms, control (/signup) cold 0/20 p50 52.5ms で分離成立 — 12時台通算 7/120 (~5.8%), 11時台 ~7.5% と同水準の低位帯"
    lines[idx] = line + ev
    open(p, 'w').write('\n'.join(lines))
    open('_f84_ev_out.txt', 'w').write(f'OK row {idx}\n')
