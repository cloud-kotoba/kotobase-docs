#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")
print("run321 count:", s.count("run321A\u2013C"))
print("run320A count:", s.count("run320A\u2013C"))
l279 = lines[278]
print("L279 len:", len(l279))
print("L279 tail:", repr(l279[-300:]))
# iter log region
for i in range(357, 361):
    print(f"{i+1}: {repr(lines[i][:120])}")