fn = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(fn, encoding="utf-8").read()
lines = data.split("\n")
idx = None
for i in range(len(lines)):
    if lines[i].startswith("| K-Z3 |"):
        idx = i
        break
row = lines[idx]
n = row.count("\u0303")
if n > 0:
    row = row.replace("\u0303", "")
    lines[idx] = row
    open(fn, "w", encoding="utf-8").write("\n".join(lines))
    print("removed %d tildes" % n)
else:
    print("no tildes present")