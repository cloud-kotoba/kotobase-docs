#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
# find the line that looks like the K-Z3 evidence row (starts with '| K-Z3 |')
for n,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print(f"K-Z3 evidence at line {n+1}")
        # print first 150 and last 400 chars
        print("HEAD:", l[:200])
        print("TAIL:", l[-400:])
        break