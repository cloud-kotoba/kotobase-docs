#!/usr/bin/env python3
import re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
print("TOTAL LINES", len(lines))
for i,l in enumerate(lines,1):
    if "NEXT" in l and ("K-" in l):
        print(f"NEXTLINE {i}: {l[:200]}")
# print iter log header and first few entries
for i,l in enumerate(lines,1):
    if l.strip()=="## Iteration log":
        print("ITERLOG at",i)
        for j in range(i, min(i+6,len(lines))):
            print(f"  {j}: {lines[j-1][:150]}")
        break
