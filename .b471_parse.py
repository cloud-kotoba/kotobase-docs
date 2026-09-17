#!/usr/bin/env python3
# parse .b471_out.txt into per-run .ttfb files (one float per line)
OUT = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b471_out.txt"
import os
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b471"
cur = None
buckets = {}
with open(OUT, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith("=== run"):
            rid = line.split()[1]  # e.g. run471A
            cur = rid[-1]  # A/B/C
            buckets.setdefault(cur, [])
        elif line.startswith("=== landing"):
            cur = "landing"
            buckets.setdefault(cur, [])
        elif line.startswith("done"):
            break
        else:
            parts = line.split()
            if len(parts) == 2:
                buckets.setdefault(cur, []).append((parts[0], parts[1]))
for k, v in buckets.items():
    with open(base + "_" + k + ".raw", "w", encoding="utf-8") as f:
        for code, ttfb in v:
            f.write("%s %s\n" % (code, ttfb))
    with open(base + "_" + k + ".ttfb", "w", encoding="utf-8") as f:
        for code, ttfb in v:
            f.write(ttfb + "\n")
    with open(base + "_" + k + ".code", "w", encoding="utf-8") as f:
        for code, ttfb in v:
            f.write(code + "\n")
print("buckets:", {k: len(v) for k, v in buckets.items()})