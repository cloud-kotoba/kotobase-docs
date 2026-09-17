#!/usr/bin/env python3
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
for i, line in enumerate(lines):
    if line.startswith("| K-Q1 "):
        print("LINE", i + 1, "len", len(line))
        print("tail:", repr(line[-80:]))
        break
