p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
l = lines[402]
i = l.rfind("run470")
with open("/tmp/b471_tail.txt", "w", encoding="utf-8") as f:
    f.write("idx=%d len=%d lines=%d\n" % (i, len(l), len(lines)))
    if i >= 0:
        f.write("TAIL500>>> " + l[i:i+500] + "\n")
print("ok")