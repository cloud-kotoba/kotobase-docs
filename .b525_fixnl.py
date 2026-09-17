# -*- coding: utf-8 -*-
import io
P='query-cosientist.md'
t=io.open(P,'r',encoding='utf-8').read()
t=t.replace('\u200b','').replace('\u200c','').replace('\u200d','')
old='次セットは run526)。- 2026-09-09: rank'
new='次セットは run526)。\n- 2026-09-09: rank'
c=t.count(old)
assert c==1, ('anchor count', c)
t=t.replace(old,new)
io.open(P,'w',encoding='utf-8').write(t)
print('fixed newline; run525=', t.count('run525'))