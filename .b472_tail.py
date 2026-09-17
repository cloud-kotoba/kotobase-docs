#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
row = next(l for l in lines if l.startswith("| K-Z3 | worker |"))
res = []
res.append("kz3_row_len=%d" % len(row))
res.append("run470_count=%d" % row.count("run470"))
res.append("run471_count=%d" % row.count("run471"))
res.append("---TAIL400---")
res.append(row[-400:])
with open("/tmp/b472_tail.txt","w",encoding="utf-8") as f:
    f.write("\n".join(res)+"\n")
print("ok")