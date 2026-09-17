p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(p).read()
lines=s.split('\n')
for idx,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print(repr(l[-80:]))
        break