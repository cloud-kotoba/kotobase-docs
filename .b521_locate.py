#!/usr/bin/env python3
import io
path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        print('KZ3_ROW_LINE=', i+1, 'len=', len(ln))
        print('KZ3_TAIL=', repr(ln[-160:]))
    if ln.startswith('## Iteration log'):
        print('ITERLOG_HEADER_LINE=', i+1)
        print('NEXT_AFTER_HEAD=', repr(lines[i+1][:200]) if i+1 < len(lines) else 'EOF')
# count run521
cnt = sum(ln.count('run521') for ln in lines)
print('RUN521_OCCURRENCE_COUNT=', cnt)
cnt2 = sum(ln.count('run520') for ln in lines)
print('RUN520_OCCURRENCE_COUNT=', cnt2)