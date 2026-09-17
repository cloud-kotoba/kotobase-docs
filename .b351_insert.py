#!/usr/bin/env python3
import io, sys

f = "query-cosientist.md"
entry = open(".b351_entry.txt", encoding="utf-8").read().rstrip("\n")
with io.open(f, encoding="utf-8") as fh:
    data = fh.read()

anchor = "## Iteration log\n- 2026-09-07: bench 第157回。14:53 JST tick。"
assert data.count(anchor) == 1, "anchor count = %d" % data.count(anchor)
replacement = "## Iteration log\n" + entry + "\n" + anchor
data = data.replace(anchor, replacement, 1)

with io.open(f, "w", encoding="utf-8") as fh:
    fh.write(data)

print("inserted ok")