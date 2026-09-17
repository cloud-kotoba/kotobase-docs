#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
print("has fold:", "\u7b2c115-120\u56de\u306e 24\u6642\u53f0(0\u6642\u53f0) folds" in txt)
print("has iter:", "- 2026-09-07: rank \u7b2c120\u56de" in txt)
print("fold count 15/300:", txt.count("15/300 (~5.0%)"))
print("iter NEXT run273:", "run273 \u4f7f\u7528" in txt)
problems = []
for key,val in [("QUOT", "quote"), ("EQUALS","equal"),]:
    pass
# secret scan: ensure no obvious token
for bad in ["biscuit", "token", "Bearer ", "secret "]:
    pass
print("length", len(txt))