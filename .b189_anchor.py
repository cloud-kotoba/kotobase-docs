#!/usr/bin/env python3
data = open('query-cosientist.md', encoding='utf-8').read()
i = data.find('| K-Z3 |')
j = data.find(chr(10), i))
print(repr(data[j-160:j]]))
h = '## Iteration log' + chr(10)
hp = data.find(h)
print(repr(data[hp:hp+90]))