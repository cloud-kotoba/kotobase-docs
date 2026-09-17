#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
l279 = lines[279-1]
print("L279_LEN=", len(l279))
print("L279_TAIL=", repr(l279[-450:]))
print("--- ITER header area (L357-360) ---")
for i in range(356, 362):
    if i <= len(lines):
        print(f"{i}: {repr(lines[i-1][:200])}")