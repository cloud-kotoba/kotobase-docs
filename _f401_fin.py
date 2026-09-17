#!/usr/bin/env python3
import subprocess, os, sys
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
MARK='falsify 第175回'
EVID_MARK='run401A'
p='query-cosientist.md'
txt=open(p,encoding='utf-8').read()
lines=txt.split('\n')

# --- evidence append (idempotent) ---
if E_MARK not in txt:
    ADDS=" falsify K-Z3 22time run401A-C: cold 7/1/0 = 8/60, A cluster 7/20, B 1/60, control border; period 22/9, 22:09:18-22:09:39 JST, 80 200"
    lines[278]=lines[278]+ADDS
    txt='\n'.join(lines)
    open(p,'w',encoding='utf8').write(txt)
    status_ev='EV_ADDED'
else:
    status_ev='EV_EXISTS'

# --- iter log insert (idempotent) ---
if 'falsify 第175' not in txt:
    lines=txt.split('\n')
    hdr=None
    for i,l in enumerate(lines):
        if l.startswith('## Iteration log'):
            hdr=i;break
    if hdr is None:
        status_ilog='NO_HEADER'
    else:
        ENT='- 2026-09-07: falsify 第175回. 22:09 tick. K-Z3 22hr band run401: cold 8/60. 22hr high band initial. NEXT delegated.'
        lines[hdr+1:hdr+1]=[ENT]
        txt='\n'.join(lines)
        open(p,'w',encoding='utf8').write(txt)
        status_ilog='ILOG_ADDED'
else:
    status_ilog='ILOG_EXISTS'

def sh(c):
    r=subprocess.run(c,shell=True,capture_output=True,text=True)
    return 'rc=%d %s'%(r.returncode,(r.stdout+r.stderr).strip()[:80])
add=shle('git add query-cosientist.md')
cm=subprocess.run(['python3','-m','re'],...)
print(status_ev,status_ilog,MARK present, E present)
print('READY')