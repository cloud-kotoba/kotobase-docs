#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(p,encoding="utf-8").read()
print("run345 count:", s.count("run345"))
print("第160回 count:", s.count("第160回"))
# check iter log head
lines=s.split("\n")
for i in range(358,363):
    print(i+1,"|",lines[i][:80])
