#!/usr/bin/env python3
import re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
for i in (360,361,362):
    ln=lines[i] if i < len(lines) else ""
    # print last 500 chars of each
    print(f"=== line {i+1} tail ===")
    print(ln[-700:])
    print()
# find run351 occurrences with context
print("=== run351 matches ===")
for n,l in enumerate(lines):
    if 'run351' in l:
        j=l.find('run351')
        print(n+1, '...'+l[max(0,j-120):j+60]+'...')