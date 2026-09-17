#!/usr/bin/env python3
path='query-cosientist.md'
with open(path,'r',encoding='utf-8') as f: lines=f.readlines()
kz3=[ln for ln in lines if ln.startswith('| K-Z3 |')][0]
print('=== K-Z3 row tail ===')
print(repr(kz3[-520:]))
print('=== IL line ===')
for i,ln in enumerate(lines):
    if ln.startswith('- 2026-09-09: falsify 第232回'):
        print('line', i+1, repr(ln))
        break