#!/usr/bin/env python3
# dump the tail of the K-Z3 physical row line (the giant cell) for inspection/append point
fn = "query-cosientist.md"
rowline = None
ridx = None
with open(fn, encoding="utf-8") as f:
    for i, ln in enumerate(f):
        if ln.rstrip("\n").lstrip().startswith("| K-Z3 | worker |"):
            rowline = ln.rstrip("\n")
            ridx = i
            break
if rowline is None:
    print("NOT FOUND")
else:
    print("ROWLINE_INDEX(0based)=", ridx)
    print("ROWLINE_CHARS=", len(rowline))
    print("TAIL1600:")
    print(rowline[-1600:])