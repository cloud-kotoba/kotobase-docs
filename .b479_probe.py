import re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(p,encoding="utf-8").read()
lines=s.split("\n")
# find K-Z3 row end (line with longest, index 278 0-based)
row=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        row=(i,l)
        break
print("KZ3 row idx", row[0] if row else None)
rl=row[1]
print("row tail 600 chars:")
print(rl[-600:])