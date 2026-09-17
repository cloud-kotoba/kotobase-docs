# -*- coding: utf-8 -*-
import subprocess
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(fn,encoding="utf-8").read()
lines=data.split("\n")
print("=== iter-log top 4 ===")
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        for j in range(i+1,i+5):
            print(j+1, repr(lines[j][:70]))
        break
print()
print("=== L279 (K-Z3 row) tail ===")
print(repr(lines[278][-500:]))
print()
# my falsify174 iter entry content
it=[l for l in lines if l.startswith("- 2026-09-07: falsify 第174回")]
print("falsify174 iters:", len(it))
for x in it:
    print(repr(x[:80]))