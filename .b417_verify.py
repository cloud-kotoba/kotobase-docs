import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    data = f.read()
print("run417_total", data.count("run417"))
print("row_279_count", data.count("| K-Z3 | worker |"))
lines = data.split("\n")
ln = lines[278]
t60 = ln[-60:]
print("L279LEN", len(ln))
print("L279TAIL60", repr(t60))
h = lines[279]
h10 = h[:10]
print("L280HEAD10", repr(h10))