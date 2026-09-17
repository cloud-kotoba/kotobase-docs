#!/usr/bin/env python3
import sys
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().split("\n")
def show(idx):
    print(f"--- [{idx}] len={len(lines[idx])}")
    print(repr(lines[idx][-800:]))
for i in [290, 291, 357, 358, 359]:
    show(i)