#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
print("run273 count:", txt.count("run273"))
print("run274 count:", txt.count("run274"))
print("run272 count:", txt.count("run272"))
print("--- 24hr totals mentioned ---")
import re
for m in re.finditer(r"24\u6642\u53f0\u901a\u7b97[^\n]{0,80}", txt):
    print(repr(m.group(0)[:90]))
print("--- 18/420? ---", "18/420" in txt, " 16/360?", "16/360" in txt)
# Find any evidence rows mentioning run273 or run274 in the K-Z3 column
i = txt.find("bench 2026-09-07 (\u7b2c110\u56de")
print("iter110 idx", i)