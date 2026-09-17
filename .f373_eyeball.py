p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
k=None
i=0
while i<len(lines):
    l=lines[i]
    if l.startswith('| K-Z3 | worker |'):
        k=i
        break
    i=i+1
print(lines[k][-700:])