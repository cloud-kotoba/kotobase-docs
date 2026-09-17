#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        print("HDR", i+1)
        for j in range(i, min(i+8,len(lines))):
            print(f"{j+1}| {lines[j][:90]}")
        break
print("run347 count in L279:", lines[278].count("run347"))