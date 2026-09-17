#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding='utf-8') as f:
    lines = f.readlines()
out = []
out.append(f"total_lines={len(lines)}")
for i, ln in enumerate(lines):
    s = ln.strip()
    if s.startswith("## Iteration log"):
        out.append(f"ITER_HEADER at {i+1}")
    if "cosientist 第124回" in s:
        out.append(f"cosientist124 at {i+1}: {s[:80]}")
    if "run356A" in s:
        out.append(f"run356A at {i+1}: {s[:80]}")
# show structure lines 355-370
out.append("--- structure 355..370 ---")
for i in range(354, min(375, len(lines))):
    out.append(f"{i+1}|{lines[i][:85].rstrip()}")
with open("/tmp/verify_out.txt", "w", encoding='utf-8') as f:
    f.write("\n".join(out))
print("written")