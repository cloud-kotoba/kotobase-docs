# -*- coding: utf-8 -*-
import io
PATH = 'query-cosientist.md'
Z = ['\u200b', '\u200c', '\u200d', '\u200e', '\u200f']
def scrub(t):
    for c in Z:
        t = t.replace(c, '')
    return t.replace('#####', '')

ev = scrub(io.open('.b525_ev.txt', 'r', encoding='utf-8').read().strip())
itv = scrub(io.open('.b525_iter.txt', 'r', encoding='utf-8').read().strip())

data = io.open(PATH, 'r', encoding='utf-8').read()
lines = data.splitlines(1)
assert lines[278].startswith('| K-Z3 |')
assert 'run525' not in lines[278]
lines[278] = lines[278][:-1] + ' ' + ev + lines[278][-1:]

hdr = None
for i, l in enumerate(lines):
    if l.strip().startswith('## Iteration log'):
        hdr = i
        break
assert hdr is not None
nxt = lines[hdr+1]
assert nxt.strip().startswith('- 2026-09-09: rank ')
lines.insert(hdr+1, itv)
io.open(PATH, 'w', encoding='utf-8').write(''.join(lines))

chk = io.open(PATH, 'r', encoding='utf-8').read()
bad = [c for c in Z if c in chk]
if '#####' in chk: bad.append('hashes')
print('done problems=', bad)
print('run525_in_doc=', chk.count('run525'))