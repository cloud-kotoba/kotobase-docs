#!/usr/bin/env python3
import sys
path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# locate K-Z3 table row (starts with | K-Z3 |)
kz3 = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        kz3 = i
        break
print('KZ3_LINE_1INDEX', kz3+1)
if kz3 is not None:
    content = lines[kz3]
    print('KZ3_LEN', len(content))
    print('KZ3_TAIL', repr(content[-200:]))

# locate Iteration log header
for i, l in enumerate(lines):
    if l.startswith('## Iteration log'):
        print('ILOG_LINE_1INDEX', i+1)
        for j in range(i+1, min(i+3, len(lines))):
            print('AFTER_ILOG_%d' % (j+1), lines[j][:60])
        break