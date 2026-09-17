#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.read().split("\n")
# print L370-377 in full
for i in range(369, 377):
    if i < len(lines):
        print(f"===== L{i+1} =====")
        print(lines[i][:3000])
        print()