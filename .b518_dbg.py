#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
ki = None
ii = None
for j, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and ki is None:
        ki = j
    if ln.strip().startswith("## Iteration log")and ii is None:
        ii = j
print("ki", ki, "ii", ii, "ki==ii+1?", ki == ii+1)
if ii is not None:
    k = ii+1
    s = lines[k]
    print("nxt line", k, "len", len(s), "has518", ("run518" in s), repr(s[:80]))