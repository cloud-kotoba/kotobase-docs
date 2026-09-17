#!/usr/bin/env python3
import io, sys
path = "query-cosientist.md"
lines = io.open(path, encoding="utf-8").read().splitlines(keepends=True)
# K-Z3 opening hypothesis row: line starting with "| K-Z3 |"
for idx, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        print(f"KZ3_ROW_LINE={idx+1} len={len(ln)}")
        print("TAIL>>>", ln[-600:])
        break
# Iteration log header
for idx, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        print(f"ITERLOG_HEADER_LINE={idx+1}")
        print("NEXT_LINE>>>", lines[idx+1][:80] if idx+1 < len(lines) else "EOF")
        break