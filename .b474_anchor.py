#!/usr/bin/env python3
# report line 404 (1-indexed) tail chars + count occurrence of key marker, for safe append
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
print("nlines", len(lines))
idx = 403
L = lines[idx]
print("len404", len(L))
print("tail120", repr(L[-120:]))
print("cnt_run473", len(L.split("run473")) - 1)
print("ends with rank専門?", L.rstrip().endswith("(rank 専門)。"))
print("last80", repr(L[-80:]))