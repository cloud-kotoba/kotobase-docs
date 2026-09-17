#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
# verify run352 in line 279 tail and iterlog entry present
print("line 279 tail has run352:", 'run352' in lines[278][-2000:])
print("L279 new evidence lex short tail:", lines[278][-260:])
print()
for n,l in enumerate(lines):
    if l.strip().startswith('## Iteration log'):
        print(f"IL header L{n+1}")
        print("L361:", lines[n+1][:90])
        print("has bench 151:", 'bench 第151回' in lines[n+1])
        break