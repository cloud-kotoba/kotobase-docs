#!/usr/bin/env python3
path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
kz3 = [ln for ln in lines if ln.startswith('| K-Z3 |')][0]
import re
# count run521 refs in K-Z3 row
print('KZ3 run521 count=', kz3.count('run521'))
# find positions/markers
for m in re.finditer(r'run521', kz3):
    s = max(0, m.start()-120)
    print('...', kz3[s:m.end()+40].replace('\n',' '))
    print('---')