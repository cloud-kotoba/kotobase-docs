#!/usr/bin/env python3
import re, io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []
with open(p, encoding="utf-8") as f:
    txt = f.read()

lines = txt.split("\n")
# last iter-log bullets
bullets = [l for l in lines if re.match(r"^- 2026-09-0[78]:", l)]
out.append("=== LAST 4 ITER-LOG BULLETS ===")
for b in bullets[-4:]:
    out.append(b[:1200])
out.append("")

# run410 / run411
out.append("=== run410/run411 mentions (context) ===")
for i, l in enumerate(lines, 1):
    if "run411" in l or "run410" in l:
        out.append(f"L{i}: {l[:500]}")
out.append("")

# Iteration log section start line + rank 175 line
out.append("=== rank/bench/falsify latest commit subjects in-file ===")
for i, l in enumerate(lines, 1):
    if re.search(r"(rank 第1[0-9][0-9]回|bench 第1[0-9][0-9]回|falsify 第1[0-9][0-9]回):", l):
        if "2026-09-07" in l or "2026-09-08" in l:
            out.append(f"L{i}: {l[:600]}")

res = "\n".join(out)
with open("/tmp/bench_state.txt", "w", encoding="utf-8") as f:
    f.write(res)
print("written", len(res))