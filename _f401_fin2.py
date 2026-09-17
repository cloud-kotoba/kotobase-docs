#!/usr/bin/env python3
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
p='query-cosientist.md'
txt=open(p,encoding='utf-8').read()
EM='run:401A'
lines=txt.split('\n')

# evidence append once
if EM not in txt:
    AD=" falsify 2026-09-07 K-Z3 22hr band run401A-C: cold>=0.5s 7/1/0=8/60 (~13.3%); A cluster 7/20 1.16-2.63s, B 1/60, C0; control 0.654s border; 22:09-22:39 JST; 80/80=200"
    lines[278]=lines[278]+AD
    txt='\n'.join(lines)
    open(p,'w',encoding='utf-8').write(txt)
    EV='EV:ADDED'
else:
    EV='EV:exists'

# itlog insert idempotent
if 'falsify 175' not in txt:
    lines=txt.split('\n')
    h=None
    for i,l in enumerate:
        if l.startswith('## Iteration log'):
            h=i;break
    if h is not None:
        lines[h+1:h+1]=['- falsify 175: run401 K-Z3 22hr cold 8']
        open(p,'w',encoding='utf-8').write('\n'.join(lines))
        IL='ILOG:ADDED'
    else:
        IL='ILOG:NOHEADER'
else:
    IL='ILOG:'

def g(c):
    r=subprocess.run(c,shell=True,capture_output=True,text=True)
    return r.returncode
write('/tmp/fin.txt', ...)