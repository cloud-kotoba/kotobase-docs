#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.read().split("\n")
out = []
out.append("=== run412 / run413 / run414 mentions ===")
for i, l in enumerate(lines, 1):
    for r in ["run412", "run413", "run414", "run415"]:
        if r in l:
            out.append(f"L{i} [{r}]: {l[:260]}")
res = "\n".join(out)
with open("/tmp/bench_run.txt", "w", encoding="utf-8") as f:
    f.write(res)
print("ok", len(res))