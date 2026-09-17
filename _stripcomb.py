#!/usr/bin/env python3
c = open('query-cosientist.md', encoding='utf-8').read()
ch = chr(0x308)
lines = c.split('\n')
for i, l in enumerate(lines):
    if ch in l:
        idx = l.index(ch)
        print('line', i+1, 'col', idx, 'ctx', repr(l[max(0,idx-30):idx+8]))
# strip all combining chars from the whole file
clean = c.replace(ch, '')
open('query-cosientist.md', 'w', encoding='utf-8').write(clean)
print('stripped', c.count(ch), 'occurrences')