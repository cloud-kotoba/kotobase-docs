# -*- coding: utf-8 -*-
import io, re
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()
for n in [198, 199, 200, 205, 206, 207, 208]:
    pat = re.compile(r"bench\s+第%s回" % n)
    print("bench 第%d回 -> %d occurrences" % (n, len(pat.findall(c))))
# also count run475 actual measurement refs (A-C)
print("run475A refs:", c.count("run475A"))
print("run475B refs:", c.count("run475B"))
print("run475C refs:", c.count("run475C"))