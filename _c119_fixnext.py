#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    txt = f.read()

old = "次 run ID は run297 使用)。"
new = "次 run ID は run299 使用)。"
# only fix inside my cosientist 第119回 entry (the latest), leave rank 第130回 historical NEXT intact.
# my entry is the FIRST occurrence right after "## Iteration log" header
marker = "## Iteration log"
i = txt.find(marker)
if i < 0:
    print("header not found"); raise SystemExit(1)
seg = txt[i+len(marker):]
if old in seg:
    seg2 = seg.replace(old, new, 1)
    txt = txt[:i+len(marker)] + seg2
    print("fixed NEXT run id -> run299")
else:
    print("old string not found in first segment; checking whole")
    if old in txt:
        txt = txt.replace(old, new, 1)
        print("fixed whole-file occurrence")
    else:
        print("NOT FOUND, no change")

with open(path, "w", encoding="utf-8") as f:
    f.write(txt)