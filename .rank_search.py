#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()
import re
pats = ["run250", "run251", "run252", "run253", "22時台", "21時台通算", "run239", "run244"]
out = []
for i, ln in enumerate(lines, 1):
    for p in pats:
        if p in ln:
            out.append("%d|%s" % (i, ln.rstrip()[:200]))
            break
with io.open("/tmp/rank_search.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("done")