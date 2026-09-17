#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []
with io.open(p, encoding="utf-8") as fh:
    lines = fh.readlines()
out.append("TOTAL_LINES %d" % len(lines))
for i, ln in enumerate(lines, 1):
    if ln.startswith("## Iteration log"):
        out.append("HDR %d" % i)
        out.append("AFTER_HDR_FIRST60 %r" % lines[i][:60])
        out.append("AFTER_HDR_HAS_B182 %s" % ("bench 第182回" in lines[i]))
        break
for i, ln in enumerate(lines, 1):
    if ln.lstrip().startswith("| K-Z3 |"):
        out.append("KZ3_LINE %d LEN %d" % (i, len(ln)))
        out.append("KZ3_HAS_B182 %s" % ("第182回" in ln))
        out.append("KZ3_TAIL %r" % ln[-120:])
        break
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b402_verify.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")