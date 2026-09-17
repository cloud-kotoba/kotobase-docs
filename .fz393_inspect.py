#!/usr/bin/env python3
import sys
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().split("\n")
line = lines[278]  # 0-indexed, L279 = index 278
print("LINE 279 length:", len(line))
print("LAST 120 chars of L279:")
print(repr(line[-120:]))
print("Occurrence check K-Z3 row start:", line.count("| K-Z3 |"))