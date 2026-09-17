#!/usr/bin/env python3
import io
path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        print(i, repr(l[-80:]), len(l))
        break
