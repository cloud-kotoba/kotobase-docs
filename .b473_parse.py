#!/usr/bin/env python3
# parse .b473_out.txt into per-run .ttfb/.code files (one value per line)
OUT = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b473_out.txt"
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b473"
cur = None
buckets = {}
with open(OUT, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith("=== run"):
            rid = line.split()[1]
            cur = rid[-1]
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
with open("/tmp/b473_buckets.txt", "w", encoding="utf-8") as dbg:
    dbg.write("buckets: " + repr({k: len(v) for k, v in buckets.items()}) + "\n")
for k, v in buckets.items():
    with open(base + "_" + k + ".ttfb", "w", encoding="utf-8") as f:
        for code, ttfb in v:
            f.write(ttfb + "\n")
    with open(base + "_" + k + ".code", "w", encoding="utf-8") as f:
        for code, ttfb in v:
            f.write(code + "\n")
print("ok")