#!/usr/bin/env python3
f="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(f,encoding="utf-8").read().split("\n")
kz3=lines[278]
print("len:", len(kz3))
print("last 25:", repr(kz3[-25:]))
print("has run326 near end:", "run326" in kz3[-1500:])
print("tail 1500 chars:")
print(kz3[-1500:])