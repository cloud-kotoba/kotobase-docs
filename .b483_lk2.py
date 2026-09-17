# -*- coding: utf-8 -*-
import io
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC,"r",encoding="utf-8") as f:
    t=f.read()
# find my bench block: search for "第210回" occurrences and show context
import re
idxs=[m.start() for m in re.finditer("第210回", t)]
print("occurrences of 第210回:", len(idxs))
for k,i in enumerate(idxs):
    # show 150 chars after
    seg=t[i:i+150].replace("\n"," ")
    print("[%d] ...%s..." % (k, seg))
print("=== count 1.9558 :", t.count("1.9558"))
print("=== count run484 :", t.count("run484"))
print("=== my bench iter entry (第210回。16:54) present?:", t.count("第210回。16:54"))
print("total chars:", len(t))