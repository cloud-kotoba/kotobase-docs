#!/usr/bin/env python3
# write cold positions and status summary to /tmp/b474_final.txt (append-only)
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b474"
THRESH = 0.5
out = "/tmp/b474_final.txt"
lines = []
for k in ["A", "B", "C", "landing"]:
    vals = [float(x) for x in open(base + "_" + k + ".ttfb").read().split() if x.strip()]
    cold = [(i + 1, v) for i, v in enumerate(vals) if v >= THRESH]
    lines.append("RUN%s cold=%d/%d coldpos=%s" % (k, len(cold), len(vals), ",".join("%d:%.4f" % (i, v) for i, v in cold)))
with open(out, "a", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")