#!/usr/bin/env python3
import re, sys
P='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(P,encoding='utf-8').read().split('\n')
kz3=None
for i,ln in enumerate(lines):
    if re.match(r'^\s*\| K-Z3 \s*\|', ln):
        kz3=i; break
print('KZ3_ROW', kz3)
if kz3 is not None:
    seg=lines[kz3]
    print('KZ3_ROW_LEN', len(seg))
    print('KZ3_TAIL', repr(seg[-80:]))
ilog=None
for i,ln in enumerate(lines):
    if ln.strip()=='## Iteration log':
        ilog=i; break
print('ILOG_AT', ilog)
print('NEXT_LINE', repr(lines[ilog+1][:60]) if ilog is not None and ilog+1<len(lines) else 'none')