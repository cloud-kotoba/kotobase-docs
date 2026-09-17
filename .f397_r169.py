import re
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
# find iterlog before-head line 367; rank 169 is after head
for i,ln in enumerate(lines):
    if ln.startswith("- 2026-09-07: rank 第169回"):
        nxt=lines[i+1] if i+1<len(lines) else "(end)"
        print("rank169 line idx",i)
        print("---NEXT line---")
        print(repr(nxt[:400]))
        break