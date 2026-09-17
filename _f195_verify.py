#!/usr/bin/env python3
import re
path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(path,encoding='utf-8').read()
print('run440 count:', s.count('run440'))
print('run441 count:', s.count('run441'))
print('K-Z3 row key count:', s.count('| K-Z3 | worker |'))
print('iterlog header count:', s.count('\n## Iteration log'))
i=s.find('\n## Iteration log\n')
print('iterlog first line:', repr(s[i+len('\n## Iteration log\n'):i+len('\n## Iteration log\n')+120]))
ki=s.find('| K-Z3 | worker |')
nl=s.find('\n',ki)
tail=s[ki:nl]
print('K-Z3 row tail last 200:', repr(tail[-200:]))
# check dup evidence marker of my run
m=s.count('falsify 2026-09-08 (第195回')
print('my run marker count:', m)