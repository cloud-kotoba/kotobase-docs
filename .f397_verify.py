# -*- coding: utf-8 -*-
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
print("L279 len",len(lines[278]))
print("L279 tail:",repr(lines[278][-320:]))
print()
for i,ln in enumerate(lines):
    if ln.startswith("- 2026-09-07: falsify 第174回"):
        print("iter174 at line",i+1, repr(ln[:60]))
print("iter head:", [i+1 for i,l in enumerate(lines) if l.strip()=="## Iteration log"])
# count dupes
import re
c=open(fn,encoding="utf-8").read()
print("count run397A",c.count("run397A"))
print("count '第174回'",c.count("第174回"))