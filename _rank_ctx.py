# -*- coding: utf-8 -*-
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
out = "/tmp/rank_234ctx.txt"
with io.open(out, "w", encoding="utf-8") as f:
    for i in range(231, 238):  # lines 232-238
        f.write(f"=== L{i+1} ===\n{lines[i]}\n")
print("ok")