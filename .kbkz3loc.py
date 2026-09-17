#!/usr/bin/env python3
import io
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt=io.open(p,encoding='utf-8').read()
if txt.startswith('\ufeff'):
    txt=txt[1:]
lines=txt.split('\n')
out=[]
kz3=None
for i,l in enumerate(lines):
    if kz3 is None:
        if l.startswith('| K-Z3 '):
            kz3=i+1
            out.append('L%d len=%d' % (i+1,len(l)))
            out.append('HEAD200:'+l[:200].replace('\r',''))
            out.append('TAIL220:'+l[-220:].replace('\r',''))
out.append('NOLINECOUNT=%d' % len(lines))
w=io.open('/tmp/.kbkz3out.txt','w',encoding='utf-8')
w.write('\n'.join(out)+'\n')
w.close()