#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(path,encoding='utf-8').read().split('\n')
# find K-Z3 evidence line (the one starting with "| K-Z3 |")
found=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        found=i+1
print("K-Z3 line number:", found, "len chars:", len(lines[found-1]))
print("END(120):", lines[found-1][-120:])
print()
# iterlog header
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        print("iterlog header line:", i+1)
        print("next line:", lines[i+1][:100])
        break