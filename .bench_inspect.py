# -*- coding: utf-8 -*-
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(DOC, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
# 1. K-Z3 row = line 279 (index 278). Print tail (last 1500 chars)
row = lines[278]
out.append("=== L279 row length: %d chars ===" % len(row))
out.append("=== L279 tail (last 1800 chars) ===")
out.append(row.rstrip("\n")[-1800:])
out.append("")
out.append("=== lines containing run467 ===")
for i, ln in enumerate(lines, 1):
    if "run467" in ln:
        out.append("L%d: ...%s..." % (i, ln[:120].replace("\n","")))
out.append("")
out.append("=== iter-log header region L400-L410 ===")
for i in range(400, 411):
    ln = lines[i-1].rstrip("\n")
    out.append("L%d|%s" % (i, ln[:300]))
out.append("")
out.append("=== DONE ===")
with open("/tmp/bench_inspect.out", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("written", len(out))