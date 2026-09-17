#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []
with io.open(p, encoding="utf-8") as fh:
    lines = fh.readlines()
out.append("TOTAL_LINES %d" % len(lines))
for i, ln in enumerate(lines, 1):
    if ln.lstrip().startswith("| K-Z3 |"):
        out.append("KZ3_LINE %d LEN %d" % (i, len(ln)))
        out.append("KZ3_TAIL " + repr(ln[-160:]))
        break
for i, ln in enumerate(lines, 1):
    if ln.startswith("## Iteration log"):
        out.append("HDR_LINE %d %r" % (i, ln))
        out.append("NEXT_LINE %r" % lines[i])
        break
out.append("LINE370_FIRST80 " + repr(lines[369][:80]) if len(lines) > 369 else "NA")
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b402_dump.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")