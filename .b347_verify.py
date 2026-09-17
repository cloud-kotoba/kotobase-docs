#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(p,encoding="utf-8").read()
print("run347 count:", s.count("run347"))
print("第161回 count:", s.count("第161回"))
print("第160回 count:", s.count("第160回"))
lines=s.split("\n")
for i in range(359,365):
    print(i+1,"|",lines[i][:75])