path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
# line 279 = index 278
ln = lines[278]
print("LINECOUNT", len(ln))
print("TAIL_START")
print(ln[-1500:])