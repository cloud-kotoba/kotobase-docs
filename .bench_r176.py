#!/usr/bin/env python3
import subprocess
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.read().split("\n")
for i, l in enumerate(lines, 1):
    if l.startswith("- 2026-09-08: rank 第176回"):
        print(f"===== L{i} rank176 full ({len(l)}) =====")
        print(l)
        break
else:
    print("NOT FOUND")