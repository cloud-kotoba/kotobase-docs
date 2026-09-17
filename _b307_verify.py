#!/usr/bin/env python3
PATH='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(PATH, encoding='utf-8') as f:
    lines=f.readlines()
# verify iterlog entry present and newest-first
hdr=[i for i,l in enumerate(lines) if l.rstrip('\n')=='## Iteration log'][0]
print("iterlog header line", hdr+1)
print("entry right after header:")
print(lines[hdr+1][:180])
# verify K-Z3 row got run307 at end
k=[i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')][0]
tail=lines[k]
assert 'run307A' in tail and '8 例目' in tail
print("K-Z3 row contains run307:", tail[-280:])