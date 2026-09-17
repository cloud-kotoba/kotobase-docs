#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        seg = line[860:890]
        print(seg)
        print("<<END>>")
        # also check the character right after the line (next line)
