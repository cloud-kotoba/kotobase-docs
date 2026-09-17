#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
l = lines[278]
with open("/tmp/b473_tailrow.txt", "w", encoding="utf-8") as f:
    f.write("LEN %d\n" % len(l))
    f.write("TAIL1200 %r\n" % l[-1200:])
    f.write("FIRST60 %r\n" % l[:60])
print("ok")