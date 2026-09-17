# -*- coding: utf-8 -*-
s=open('query-cosientist.md',encoding='utf-8').read()
i=s.find('## Iteration log')
seg=s[i:i+4200]
open('/tmp/rank_top.txt','w',encoding='utf-8').write(seg)