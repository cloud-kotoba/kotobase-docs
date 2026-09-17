# -*- coding: utf-8 -*-
# Dump K-Z3 row (line 278) and iter-log top (405+)
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("=== LINE 278 (K-Z3 row) ===")
print(lines[278])
print("=== LEN ===", len(lines[278]))
print("=== iter-log lines 405-412 ===")
for i in range(405, min(412, len(lines))):
    print(i, repr(lines[i][:200]))