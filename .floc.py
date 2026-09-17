#!/usr/bin/env python3
import sys, re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
# find K-Z3 hypothesis row
idx = None
for i, l in enumerate(lines, start=1):
    if l.startswith("| K-Z3 | worker |"):
        idx = i
        break
print("KZ3_ROW_LINE=", idx)
print("TOTAL_LINES=", len(lines))
# iter-log location
node = None
for i, l in enumerate(lines, start=1):
    if l.strip() == "## Iteration log":
        node = i
        break
print("ITERLOG_LINE=", node)
# print line numbers of last few iter entries (newest first, us. noted)