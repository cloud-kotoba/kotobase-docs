#!/usr/bin/env python3
# probe: find K-Z3 hypothesis row (line starting with "| K-Z3 | worker |")
# and print its line number + tail, plus iteration-log header position.
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
res = []
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        res.append("KZ3_ROW line=%d len=%d start=%r tail90=%r" % (i+1, len(l), l[:22], l[-90:]))
    if l.strip() == "## Iteration log":
        res.append("ITER_HDR line=%d" % (i+1))
    if l.startswith("| K-Q1 |") or l.startswith("| K-S1 |") or l.startswith("| K-S2 |") or l.startswith("| K-Z2 |"):
        res.append("OTHER_ROW line=%d start=%r" % (i+1, l[:14]))
with open("/tmp/b472_probe.txt","w",encoding="utf-8") as f:
    f.write("\n".join(res)+"\n")
print("ok")