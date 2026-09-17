#!/usr/bin/env python3
import io
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt=io.open(p,encoding='utf-8').read()
if txt.startswith('\ufeff'):
    txt=txt[1:]
lines=txt.split('\n')
out=[]
# find Iteration log section
iloc=None
for i,l in enumerate(lines):
    if l.strip().startswith('## Iteration log'):
        iloc=i+1
        break
out.append('ITERLOG_SEC_L=%d' % iloc)
if iloc:
    start=iloc  # 1-based
    # print first 6 lines after heading
    for j in range(start, min(start+6, len(lines)+1)):
        frag=lines[j-1]
        out.append('L%d:%s' % (j, frag[:150].replace('\r','')))
w=io.open('/tmp/.kbiterout.txt','w',encoding='utf-8')
w.write('\n'.join(out)+'\n')
w.close()