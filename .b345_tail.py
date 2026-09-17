#!/usr/bin/env python3
import subprocess
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
# L279 is index 278
l=lines[278]
print("L279 len", len(l))
print("L279 tail repr:", repr(l[-400:]))