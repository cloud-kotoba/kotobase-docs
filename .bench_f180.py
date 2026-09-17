#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.read().split("\n")
found = False
for i, l in enumerate(lines):
    if "falsify 第180回" in l:
        found = True
        print(f"===== L{i+1} full ({len(l)} chars) =====")
        print(l)
        break
if not found:
    print("NOT FOUND")