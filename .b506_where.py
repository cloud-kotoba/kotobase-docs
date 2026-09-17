#!/usr/bin/env python3
import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(P, encoding="utf-8").read().split("\n")
for i, ln in enumerate(lines, 1):
    if "run506" in ln:
        prefix = ln[:60]
        if ln.startswith("|"):
            print("ROW", i, "ROWSTART", repr(ln[:22]), "run506pos", ln.find("run506"))
        else:
            print("LINE", i, repr(prefix))
# also find the K-Z3 row line number regardless
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z3 |"):
        print("KZ3_HEAD_AT", i, "has506:", "run506" in ln, "has507:", "run507" in ln)
        print("  tail300:", ln[-300:])