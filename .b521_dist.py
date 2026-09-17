#!/usr/bin/env python3
path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, ln in enumerate(lines):
    c = ln.count('run521')
    if c:
        seg = ln[ln.find('run521')-10:ln.find('run521')+15].replace('\n',' ')
        print(f'line {i+1}: run521 x{c} :: ...{seg}...')
print('---- 第232回 lines ----')
for i, ln in enumerate(lines):
    if '第232回' in ln:
        print(f'line {i+1}: count={ln.count("第232回")}')