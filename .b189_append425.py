#!/usr/bin/env python3
doc='query-cosientist.md'
ev='.b189_run425_evidence.txt'
with open(doc,'r',encoding='utf-8')as f:
    d=f.read()
with open(ev,'r',encoding='utf-8')as f:
    e=f.read()
if 'run425' in d:
    print('run425-already-present')
else:
    with open(doc,'a',encoding='utf-8')as f:
        f.write('\n'+e+'\n')
    with open(doc,'r',encoding='utf-8')as f:
        chk=f.read()
    print('run425-present-after-write' if 'run425' in chk else 'WRITE-FAILED-verify')
    # dirty-line count for reporting
    print('run425-count', chk.count('run425'))