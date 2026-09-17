#!/usr/bin/env python3
fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
# isolate the K-Z3 row line
anchor = "| K-Z3 | worker | K-Z1/K-Z2"
i = s.index(anchor)
nl = s.index("\n", i)
row = s[i:nl]
# run419 occurrences inside row
import re
occ = [m.start() for m in re.finditer("run419", row)]
print("run419 occurrences in row:", len(occ)
# suspicious chars in row: combining marks U+0300-U+036f, zero-width U+200b-U+200d, bidi etc
bad = [c for c in row if ord(c) in range(0x300,0x370) or ord(c) in (0x200b,0x200c,0x200d,0xfeff) or ord(c) in range(0x2060,0x2070))
print("bad chars in row:", len(bad)
# tail around the appended run419 evidence (last 1200 chars)
print("=== ROW TAIL 1200 ===")
print(row[-1200:])