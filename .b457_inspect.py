import io
path = 'query-cosientist.md'
lines = open(path, encoding='utf-8').read().split('\n')
# find K-Z3 hypothesis row (starts with '| K-Z3 |')
for i, ln in enumerate(lines, 1):
    if ln.startswith('| K-Z3 |'):
        print('KZ3_ROW_LINE', i)
        print('LINE_END', repr(ln[-120:]))
        print('STARTS_WITH', repr(ln[:40]))
        break
# count evidence entries already present referencing run456/457
kz3 = lines[i-1]
import re
for r in ['run450','run451','run452','run453','run454','run455','run456','run457']:
    print(r, kz3.count(r))
# iter log header
for i, ln in enumerate(lines, 1):
    if ln.strip() == '## Iteration log':
        print('ITERHDR_LINE', i)
        print('NEXT_LINE', repr(lines[i][:80]) if i < len(lines) else None)
        break
print('TOTAL_LINES', len(lines))