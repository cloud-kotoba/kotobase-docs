# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
row = lines[278]
print("LEN=", len(row))
# print last 3500 chars of the row
print("=== TAIL of K-Z3 row ===")
print(row[-3500:])