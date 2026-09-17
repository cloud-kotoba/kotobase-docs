#!/usr/bin/env python3
import re
data = open('query-cosientist.md', encoding='utf-8').read()
h = '## Iteration log\n'
i = data.find(h)
print('header at', i)
print(repr(data[i:i+120]))
print('first entry starts rightafter header:', data[i-1:i+1])