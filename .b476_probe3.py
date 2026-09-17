import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
c = io.open(path, encoding="utf-8").read()
p = c.find("※ falsify 2026-09-03")
print("pos", p)
print("---150 before---")
print(repr(c[p - 150:p]))
print("---80 after---")
print(repr(c[p:p + 80]))