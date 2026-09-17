#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
fixed = s.replace("\u51b7\u51cd", "cold").replace("\u8fb5\u96e2", "\u4e56\u96e2")
open(p, "w", encoding="utf-8").write(fixed)
print("done")