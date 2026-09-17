# -*- coding: utf-8 -*-
# Locate lines in query-cosientist.md
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, ln in enumerate(lines):
    s = ln.rstrip()
    if s.startswith("| K-Z3 |") or s.startswith("| K-Z2 |") or s.startswith("| K-Q1 |") or s.startswith("## Iteration log") or s.startswith("=== NEXT"):
        print(i, repr(s[:130]))