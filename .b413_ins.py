#!/usr/bin/env python3
import io, sys

md = "docs/query-cosientist.md"

def rd(p):
    f = io.open(p, "r", encoding="utf-8")
    t = f.read()
    f.close()
    return t

c = rd(md)
ev = rd("/tmp/kb_kz3_ev.txt").strip()
il = rd("/tmp/kb_ilog.txt").strip()
a1 = rd("/tmp/kb_anchor1.txt").strip()

cnt = c.count(a1)
if cnt != 1:
    print("ANCHOR1 count", cnt)
    sys.exit(2)

newc = c.replace(a1, a1 + "\n" + ev, 1)

hdr = "## Iteration log\n"
i = newc.find(hdr)
if i < 0:
    print("header not found")
    sys.exit(3)
j = i + len(hdr)
newc = newc[:j] + il + "\n" + newc[j:]

w = io.open(md, "w", encoding="utf-8")
w.write(newc)
w.close()
print("EDITED OK size", len(newc))