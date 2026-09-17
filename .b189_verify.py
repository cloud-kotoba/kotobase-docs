#!/usr/bin/env python3
data = open('query-cosientist.md', encoding='utf-8').read()
print('run425 count', data.count('run425'))
print('iterlog header count', data.count('## Iteration log'))
i = data.find('| K-Z3 |')
j = data.find('\n', i)
tail = data[j-160:j]
print('row tail contains run425:', 'run425A cold 0/20' in tail)
print(repr(tail[-140:])))
h = '## Iteration log\n'
hp = data.find(h
print('top iter entry:', repr(data[hp:hp+80]])))