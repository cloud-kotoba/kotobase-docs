#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        # split by evidence separator: columns are | ID | area | hypothesis | status | evidence |
        parts = line.split(" | ")
        print("=== HYPOTHESIS COL ===")
        print(parts[2])
        print("=== STATUS COL ===")
        print(parts[3])
        print("=== EVIDENCE COL (full) ===")
        print(parts[4].rstrip(" |"))
