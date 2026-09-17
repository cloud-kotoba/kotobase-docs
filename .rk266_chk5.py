import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
# inspect: what does the diff to HEAD look like after my failed run? (file was not written due to assert)
# find all header contexts again briefly
lines = s.split('\n')
for i, ln in enumerate(lines, 1):
    if '## Iteration log' in ln:
        print(i, repr(ln[:60]))
