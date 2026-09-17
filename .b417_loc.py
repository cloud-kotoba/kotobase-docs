import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    data = f.read()
lines = data.split("\n")
ln = lines[278]
print("LINE279_LEN", len(ln))
print("TAIL", repr(ln[-500:])))
print("LINE280_HEAD", repr(lines[279][:60])))