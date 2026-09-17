#!/usr/bin/env python3
fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
targetlist = ["̃", ""]
for c in targetlist:
:
    if c in s:
        s = s.replace(c, "")
        print("removed", len(c))
open(fn, "w", encoding="utf-8").write(s