# -*- coding: utf-8 -*-
import io
with io.open('query-cosientist.md', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        print('KZ3 row line =', i + 1)
        print('len=', len(l))
        print('tail120=', repr(l[-120:]))
        break
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        print('iter header line =', i + 1)
        print('after header starts:', repr(lines[i + 1][:80]))
        break