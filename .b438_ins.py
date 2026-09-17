#!/usr/bin/env python3
fn='query-cosientist.md'
txt=open(fn,encoding='utf-8').read()
ev_anchor='\n## Iteration log'
ev_add=open('.b438_ev.txt',encoding='utf-8').read()
ilog_anchor='## Iteration log\n'
ilog_entry=open('.b438_ilog.txt',encoding='utf-8').read()
assert txt.count(ev_anchor)==1,'ev anchor not unique'
assert txt.count(ilog_anchor)==1,'ilog anchor not unique'
txt=txt.replace(ev_anchor, ev_add+ev_anchor)
txt=txt.replace(ilog_anchor, ilog_anchor+ilog_entry+'\n')
open(fn,'w',encoding='utf-8').write(txt)
print('inserted falsify194 run438 ok')
print('done')