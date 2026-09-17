#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
data = io.open('query-cosientist.md', encoding='utf-8').read()
lines = data.split('\n')
def combined(s):
    return [(hex(ord(c)), c) for c in s if 0x0300 <= ord(c) <= 0x036F]
evline = lines[278]  # K-Z3 row (1-based 279)
c = combined(evline)
print('L279 combined hits:', c if c else 'none')
print('L279 tail len:', len(evline), 'ends:', evline[-120:])
for i in range(408, 416):
    c = combined(lines[i])
    if c:
        print('line', i + 1, 'combined:', c)
print('OK check')