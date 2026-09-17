#!/usr/bin/env python3
f="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(f,encoding="utf-8").read().split("\n")
print("=== iterlog head (lines 358-360) ===")
for i in (357,358,359):
    print(i+1, repr(lines[i][:60]))
print("=== K-Z3 len + run327 in line 279? ===")
kz3=lines[278]
print("len:", len(kz3), "has run327:", "run327" in kz3, "has run326:", "run326" in kz3)
print("tail 400:", kz3[-400:])