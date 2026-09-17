#!/usr/bin/env python3
import os
base = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
md = os.path.join(base, 'query-cosientist.md')
with open(md, 'r', encoding='utf-8') as f:
    content = f.read()
with open(os.path.join(base, '.b197_run444_evidence.txt'), 'r', encoding='utf-8') as f:
    ev = f.read().rstrip('\n')
with open(os.path.join(base, '.b197_run444_iter.txt'), 'r', encoding='utf-8') as f:
    it = f.read().rstrip('\n')
for a, b in [('\u200b',''), ('\u200c',''), ('\u200d',''), ('\u200e',''), ('\u00ad',''), ('\u2060',''), ('\ufeff','')]:
    ev = ev.replace(a, b)
    it = it.replace(a, b)
lines = content.split('\n')
kidx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        kidx = i
        break
if kidx is None:
    raise SystemExit('K-Z3 row not found')
lines[kidx] = lines[kidx] + ev
content = '\n'.join(lines)
marker = '\n## Iteration log\n'
idx = content.find(marker)
if idx < 0:
    raise SystemExit('Iteration log header not found')
pos = idx + len(marker)
content = content[:pos] + it + '\n' + content[pos:]
with open(md, 'w', encoding='utf-8') as f:
    f.write(content)
print('OK kidx=%d' % (kidx))