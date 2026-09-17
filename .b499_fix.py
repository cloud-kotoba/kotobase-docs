# -*- coding: utf-8 -*-
import io
p = '.b499_append.py'
with io.open(p, 'r', encoding='utf-8') as f:
    s = f.read()
old = 'opend 詳細は K-Z3 evidence 欄 (L279 末尾追)。'
new = '詳細は K-Z3 evidence 欄 (L279 末尾追記)。'
assert old in s, 'anchor missing'
s = s.replace(old, new)
with io.open(p, 'w', encoding='utf-8') as f:
    f.write(s)
print('fixed')