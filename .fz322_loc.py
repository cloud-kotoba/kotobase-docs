#!/usr/bin/env python3
# -*- coding: utf-8 -*-
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")
import sys
for i in range(109, 122):
    l = lines[i]
    print(f"L{i+1} len={len(l)} | {l[:100]}")
# Find K-Z3 hypothesis row content tail
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 "):
        print("---K-Z3 row L%d---" % (i+1))
        print("LEN", len(l))
        print("TAIL:", l[-1600:])
        break