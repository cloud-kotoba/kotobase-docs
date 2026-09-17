#!/usr/bin/env python3
doc = 'query-cosientist.md'
ev = '.b189_run425_evidence.txt'
with open(doc, 'r', encoding='utf-8') as f:
    d = f.read()
with open(ev, 'r', encoding='utf-8') as f:
    e = f.read()
with open(doc, 'a', encoding='utf-8') as f:
    f.write('\n' + e + '\n')
with open(doc, 'r', encoding='utf-8') as f:
    chk = f.read()
print('run425-committed-ev?', chk.count('run425') > 1)