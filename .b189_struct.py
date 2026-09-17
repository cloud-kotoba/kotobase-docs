#!/usr/bin/env python3
data = open('query-cosientist.md', encoding='utf-8').read()
print('LEN', len(data))
i = data.find('| K-Z3 |')
j = data.find('\n', i)
row = data[i:j]
sz = len(row)
print('KZ3 row spans', sz, 'chars')
print('iterlog at', data.find('## Iteration log'), 'KZ3 row end at', j)
print('last 400 chars:')
print(repr(data[-400:]))