#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

FN = 'query-cosientist.md'
with io.open(FN, encoding='utf-8') as f:
    data = f.read()
mac = '\u0304'
n = data.count(mac)
data = data.replace(mac, '')
with io.open(FN, 'w', encoding='utf-8') as f:
    f.write(data)
print('removed', n, 'macrons; remaining:', data.count(mac)))