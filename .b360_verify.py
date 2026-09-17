#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=io.open(p,encoding="utf-8").read().split("\n")
l=lines[278]
print("L279 len", len(l))
print("TAIL300 >>>", l[-300:], "<<<")
assert "run360A cold 単発 1.1969s" in l, "run360A marker missing"
assert "run360 (1/60)" in l, "run360 total missing"
print("EVIDENCE OK")