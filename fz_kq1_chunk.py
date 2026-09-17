#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
for i, line in enumerate(txt, 1):
    if line.startswith("| K-Q1 "):
        # print in 200-char chunks
        for j in range(0, len(line), 200):
            print(f"CHUNK {j}: {line[j:j+200]}")
