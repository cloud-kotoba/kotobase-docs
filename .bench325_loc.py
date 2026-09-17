import re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(p) as f:
    lines=f.read().split('\n')
# find line with K-Z3 row start (starts with | K-Z3 |)
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print('K-Z3 row starts line', i+1)
        print('len', len(l))
        # tail of this line
        print('TAIL:', repr(l[-400:]))
        break
# find iterlog marker
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        print('iterlog at', i+1)
        break