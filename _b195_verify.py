#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")
# K-Z3 hypothesis row tail
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z3 "):
        print("ROW", i, "len", len(ln))
        print("TAIL:", repr(ln[-200:]))
        break
print("---ITER---")
for i in range(404, 409):
    print(i+1, ":", repr(lines[i][:120]))