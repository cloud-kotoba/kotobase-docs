#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
lines = io.open('query-cosientist.md', encoding='utf-8').read().split('\n')
mac = '\u0304'
ln = lines[409]  # line 410
pos = [i for i, c in enumerate(ln) if c == mac]
print('macron positions:', pos)
for p in pos:
    print('...', repr(ln[max(0, p-40):p+40]), '...')
print('line410 starts:', repr(ln[:120]))