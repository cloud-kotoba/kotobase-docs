import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
for i, ln in enumerate(lines, 1):
    if '## Iteration log' in ln:
        prev = lines[i-2][:80] if i >= 2 else ''
        nxt = lines[i][:80]
        print(i, '| prev:', repr(prev))
        print('  ', '| next:', repr(nxt))
