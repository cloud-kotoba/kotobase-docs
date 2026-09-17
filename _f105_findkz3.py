import io
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p).read().split('\n')
for idx,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print("K-Z3 row at line index", idx, "len", len(l))
        print("HEAD:", l[:120])
        print("TAIL:", l[-400:])
        break
else:
    print("K-Z3 row not found")
# also show last 60 chars of the overall doc? not needed