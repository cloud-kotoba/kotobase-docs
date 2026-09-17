#!/usr/bin/env python3
# fix stale HEAD reference in falsify 第159回 iter-log entry.
path = "query-cosientist.md"
raw = open(path, encoding="utf-8").read()
old = "HEAD 1ee1193b = bench 第146回 (11:30, K-Z3 11時台 run341 cold 7/60, NEXT run342) = remote net-kotobase/main 一致"
new = "HEAD 8c5d4b5 = rank 第148回 (typo-fix; in-flight で bench 第146回 1ee1193b → rank 第148回 8c5d4b5 へ前進) = remote net-kotobase/main 一致"
n = raw.count(old)
print("matches:", n)
if n == 1:
    raw = raw.replace(old, new)
    open(path, "w", encoding="utf-8").write(raw)
    print("FIXED")
else:
    print("ABORT: expected exactly 1 match")