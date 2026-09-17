# -*- coding: utf-8 -*-
import io
t=io.open('query-cosientist.md','r',encoding='utf-8').read()
zw=[c for c in ['\u200b','\u200c','\u200d','\u200e','\u200f'] if c in t]
print('zw_leak=',zw)
print('hashes=',t.count('#####'))
print('falsify234_ev=',t.count('falsify 2026-09-09 (第234回'))
print('falsify234_iter=',t.count('- 2026-09-09: falsify 第234回。'))
rows=sum(1 for l in t.splitlines() if l.startswith('| K-Z3 |'))
print('KZ3rows=',rows)