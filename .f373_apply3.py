# -*- coding: utf-8 -*-
base='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
p=base+'query-cosientist.md'
ADDS=open(base+'.f373_adds.txt',encoding='utf-8').read().strip()
ILOG=open(base+'.f373_ilog.txt',encoding='utf-8').read().rstrip('\n')

def clean(x):
    x=x.replace('per중 20','per 20')
    x=x.replace('別接続 curl,l,','別接続 curl,').replace('別接続 curl,l,,','別接続 curl,')
    x=x.replace('B/C  ̃0/40','B/C 0/40').replace('run373C cold  ̃0/20','run373C cold 0/20')
    x=x.replace('全 80/80  ̃200','全 80/80 200').replace('secret 不含 —  curl ーのみ','secret 不含 — curl のみ')
    x=x.replace(' ̃0/20',' 0/20')
    return x
ADDS=clean(ADDS)
ILOG=clean(ILOG)

s=open(p,encoding='utf-8').read()
lines=s.split('\n')

k=None
i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('| K-Z3 | worker |'):
        k=i
        break
    i=i+1
if k is None:
    raise SystemExit('K-Z3 row not found')

lines[k]=lines[k].rstrip()+ADDS

idx=lines.index('## Iteration log')
lines.insert(idx+1,ILOG)

open(p,'w',encoding='utf-8').write('\n'.join(lines))
print('DONE k',k)
print('LEN',len(lines[k]))
print('TAIL',lines[k][-60:])
print('ITER',lines[idx+1][:60])