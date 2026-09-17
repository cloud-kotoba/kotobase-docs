#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
FN = 'query-cosientist.md'
data = io.open(FN, encoding='utf-8').read()
mac = '\u0304'
data = data.replace(' ' + mac + '9/180', ' 9/180')
data = data.replace('per ' + mac + '20', 'per  20')
with io.open(FN, 'w', encoding='utf-8') as f:
    f.write(data)
print('fix applied; remaining macrons:', data.count(mac))