#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
for n,l in enumerate(lines):
    if l.strip().startswith('## Iteration log'):
        print("IL header L", n+1)
        print("L361:", lines[n+1][:160])
        print("L362:", lines[n+2][:160])
        break
print()
print("seed check - line279 tail:", lines[278][-120:])