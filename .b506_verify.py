#!/usr/bin/env python3
import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(P, encoding="utf-8").read()
lines = txt.split("\n")
print("run506_count:", txt.count("run506"))
print("run507_count:", txt.count("run507"))
print("bench 222_count:", txt.count("第222回"))
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z3 |") and "run506" in ln:
        print("KZ3_ROW_LINE", i, "has_run506=YES")
        print("  tail:", ln[-260:])
for i, ln in enumerate(lines, 1):
    if ln.startswith("- 2026-09-08: bench 第222回"):
        print("ILOG_ENTRY_LINE", i, ":", ln[:120])
        break
print("HDR_COUNT:", txt.count("## Iteration log"))