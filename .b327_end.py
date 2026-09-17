#!/usr/bin/env python3
f="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(f,encoding="utf-8").read().split("\n")
kz3=lines[278]
print("=== last 60 repr ===")
print(repr(kz3[-60:]))
print("=== last pipe relationships ===")
# find all pipe indices
import re
idxs=[m.start() for m in re.finditer(r"\|", kz3)]
print("num pipes:", len(idxs), "last 3 idx:", idxs[-3:])
print("chars after last pipe:", repr(kz3[idxs[-1]+1:]))
print("=== line 359 full head ===")
print(lines[358][:20])