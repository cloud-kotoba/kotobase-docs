import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
c = io.open(path, encoding="utf-8").read()
lines = c.split("\n")
# line index 278 (0-based) = file line 279
ln = lines[278]
print("line279 length", len(ln))
print("---last 250---")
print(repr(ln[-250:]))