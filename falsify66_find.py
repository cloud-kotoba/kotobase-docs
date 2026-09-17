import re
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(p).read().splitlines()
for i, l in enumerate(lines):
    if '| K-Z3' in l:
        print(f"{i+1}: {l}")
    if 'K-Z2' in l and l.startswith('|'):
        print(f"{i+1}: {l}")
