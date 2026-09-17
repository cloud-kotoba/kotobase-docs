#!/usr/bin/env python3
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().split("\n")
l279 = lines[278]
print("check --CC in L279:", "run393A\u2013C\u2013C" in l279)
print("check run393A-C once:", l279.count("run393A"))
tail = l279[-700:]
print("L279 tail:")
print(tail)
print("=== iter-log first entry ===")
print(lines[368][:400])