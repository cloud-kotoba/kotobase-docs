#!/usr/bin/env python3
import re
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        print("LINE", i, "len", len(line))
        print(line[:3000])
        print("...TAIL...")
        print(line[-3000:])
