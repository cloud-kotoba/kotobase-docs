#!/usr/bin/env python3
import io
MD = "query-cosientist.md"
txt = io.open(MD, "r", encoding="utf-8").read()
idx = txt.index("## Iteration log\n")
tail = txt[idx:idx+900]
# find where 'run397 使用)。' ends and whether bench177 follows on same line
import re
m = re.search(r"使用\)\).?-.{0,40}bench 第177回", txt[idx:idx+12000])
print("merged marker found:", bool(m))
# print the chars around the first '。-' occurrence after 使用)。
s = txt.index("使用)。", idx)
print("TAIL after 使用)。:", repr(txt[s:s+90]))
# total entry count
lines = [l for l in txt[idx:].splitlines() if l.startswith("- 2026-09-07")]
print("entry count:", len(lines))
print("bench177 anywhere:", "bench 第177回。20:58" in txt, "| bench177 iter title:", txt.count(": bench 第177回。"))