#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
l=lines[278]
print("L279 len", len(l))
print("tail500:", l[-500:])
print("---run345 present?", "run345" in l, " run346?", "run346" in l)