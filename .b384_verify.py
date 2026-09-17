fn = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(fn, encoding="utf-8").read()
lines = data.split("\n")
idx = None
for i in range(len(lines)):
    if lines[i].startswith("| K-Z3 |"):
        idx = i
        break
row = lines[idx]
print("run384 occurrences:", row.count("run384"))
print("tilde-in-adds-region:", row[-1300:].count("\u0303"))
print("has '= 20/240':", "= 20/240" in row)
print("has '= 7/60':", "= 7/60" in row)
print("has ' per 20 =':", " per 20 =" in row)
print("tail repr follows:")
print(repr(row[-450:]))