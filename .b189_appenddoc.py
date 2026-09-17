#!/usr/bin/env python3
doc='query-cosientist.md'
ev='.b189_run424_evidence.txt'
with open(doc,'r',encoding='utf-8')as f:
    d=f.read()
with open(ev,'r',encoding='utf-8')as f:
    e=f.read()
if 'run424' in d:
    print('already-present')
else:
    with open(doc,'a',encoding='utf-8')as f:
        f.write('\n'+e+'\n')
    print('appended-to-doc')