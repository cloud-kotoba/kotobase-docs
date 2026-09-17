#!/usr/bin/env python3
import re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(p,encoding='utf-8').read()
lines=s.split('\n')
print("run441 count:", s.count('run441'))
print("total lines:", len(lines))
# find the K-Z3 hypothesis row (starts with | K-Z3 |
for i,ln in enumerate(lines,1):
    if ln.startswith('| K-Z3 '):
        print("K-Z3 hypothesis row at line", i, "len", len(ln))
        print("TAIL:", repr(ln[-180:]))
        break