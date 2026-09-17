# -*- coding: utf-8 -*-
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(fn,encoding="utf-8").read().split("\n")
for i,ln in enumerate(lines):
    if ln.startswith("- 2026-09-07: rank 第169回"):
        # entry is a single huge line; grab its tail
        tail=ln[-1200:]
        print("RANK169_TAIL len",len(ln))
        print(tail)
        break