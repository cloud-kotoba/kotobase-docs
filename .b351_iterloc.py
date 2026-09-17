#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
# locate "## Iteration log"
for n,l in enumerate(lines):
    if l.strip().startswith('## Iteration log'):
        print(f"Iteration log header at line {n+1}")
        for i in range(n, n+3):
            print(f"  L{i+1}: {lines[i][:120]}")
        break