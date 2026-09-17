#!/usr/bin/env python3
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().split("\n")
for i,l in enumerate(lines):
    if l.strip() == "## Iteration log":
        print("iterlog header at L", i+1)
        print("next line L", i+2, "first 100:", repr(lines[i+1][:100]))
        break
# verify no duplicate
c = sum(1 for l in lines if l.strip()=="## Iteration log")
print("iterlog header count:", c)
# verify L279 uniqueness
print("K-Z3 row count:", sum(1 for l in lines if l.startswith("| K-Z3 |")))