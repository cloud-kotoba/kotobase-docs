# -*- coding: utf-8 -*-
import io
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("total_lines=%d" % len(lines))
print("run483A-C count=%d" % sum(1 for l in lines if "run483A" in l))
print("run483 count=%d" % sum(1 for l in lines if "run483" in l))
print("run484 count=%d" % sum(1 for l in lines if "run484" in l))
# find iteration log header
hdrs = [i for i,l in enumerate(lines) if l.strip().startswith("## Iteration log")]
print("iter_hdr_lines=%s" % hdrs)
if hdrs:
    h = hdrs[0]
    print("--- after header (next 5 lines, first 150 chars each) ---")
    for i in range(h+1, min(h+6, len(lines))):
        print("%d: %s" % (i+1, lines[i].strip()[:150]))
# K-Z3 row
kz3 = [i for i,l in enumerate(lines) if l.startswith("| K-Z3 |")]
print("kz3_row_lines=%s" % kz3)
