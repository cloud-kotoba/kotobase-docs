#!/usr/bin/env python3
import sys
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        print("LEN", len(line))
        seg = line[800:2600]
        print(seg)
        print("<<SEG_END len", len(seg), ">>")
