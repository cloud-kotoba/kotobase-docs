import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
c = io.open(path, encoding="utf-8").read()
# run475 uniqueness: "run475A heavy 6/20 (1.06"
key = "run475A heavy 6/20"
p = c.find(key)
print("key524 pos", p)
if p >= 0:
    print("---250 before---")
    print(repr(c[p-250:p]))
    print("---350 after---")
    print(repr(c[p:p+350]))