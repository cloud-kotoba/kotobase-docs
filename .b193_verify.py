# -*- coding: utf-8 -*-
import io
s = io.open('query-cosientist.md', encoding='utf-8').read()
h = '## Iteration log' + chr(10)
p = s.find(h)
print('ilog_pos=', p)
print('ilog_head=', repr(s[p:p+330]))
z = s.find('| K-Z3 |')
q = s.find(chr(10), z)
print('zrow_line=', repr(s[z:z+80]))
print('zrow_tail=', repr(s[q-260:q]]))
