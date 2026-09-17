#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
print("fold 18/420:", "= 18/420 (~4.3%) \u306e 7 \u30bb\u30c3\u30c8\u9023\u7d9a cold>0" in txt)
print("iter 18/420:", "18/420 (~4.3%) \u306e 7 \u30bb\u30c3\u30c8\u9023\u7d9a cold>0" in txt)
print("run273 in fold:", "\u7b2c117\u56de run273" in txt)
print("run274 in fold:", "\u7b2c111\u56de run274" in txt)
print("NEXT run275:", "run275 \u4f7f\u7528" in txt)
# stale 15/300 in rank120 fold? there may be other legit 15/300 references from bench110 evline
print("has rank120 title:", "- 2026-09-07: rank \u7b2c120\u56de\u300200:47" in txt)