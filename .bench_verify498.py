# -*- coding: utf-8 -*-
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
c498 = 0
for ln in lines:
    c498 += ln.count("run498")
out.append("run498_count=%d" % c498)

# iter header position and first 2 lines after it
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        out.append("iter_header_line=%d" % (i+1))
        out.append("ITER1=%s" % lines[i+1].rstrip("\n")[:300])
        out.append("ITER2=%s" % lines[i+2].rstrip("\n")[:200])
        break

# K-Z3 row tail
for i, ln in enumerate(lines):
    if "| K-Z3 | worker |" in ln:
        tail = ln.rstrip()
        out.append("kz3_row_endswith_pipe=%s" % tail.endswith("|"))
        out.append("kz3_rows=%d" % ln.count("run"))
        out.append("kz3_tail200=%r" % tail[-200:])
        break

with io.open("/tmp/bench_verify498.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))