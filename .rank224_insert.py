#!/usr/bin/env python3
import io, sys, os

DOC = "query-cosientist.md"
ENTRY = ".rank224_entry.txt"

with io.open(ENTRY, "r", encoding="utf-8") as f:
    entry = f.read().rstrip("\n")

with io.open(DOC, "r", encoding="utf-8") as f:
    text = f.read()

HDR = "## Iteration log\n"
assert text.count(HDR) == 1, "header count != 1: %d" % text.count(HDR)
pos = text.index(HDR)
after = pos + len(HDR)
# Require the header be followed by the previous newest entry (falsify 第228回).
head_tail = text[after:after+140]
assert "falsify 第228回" in head_tail, "anchor mismatch: %r" % head_tail[:80]
new = text[:after] + entry + "\n" + text[after:]
with io.open(DOC, "w", encoding="utf-8") as f:
    f.write(new)
print("INSERTED ok")