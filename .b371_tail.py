import sys
lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')
l=lines[278]
print('LINE_LEN',len(l))
print('TAIL:',repr(l[-900:]))