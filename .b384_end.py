fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i; break
s=lines[idx]
print("END100="+repr(s[-100:]))