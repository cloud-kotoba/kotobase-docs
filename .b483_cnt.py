# -*- coding: utf-8 -*-
import io
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC,"r",encoding="utf-8") as f:
    t=f.read()
# report counts of key markers
for m in ["第210回","第216回","run483","run484","1.9558s","22/300","27/360","25/300"]:
    print("%s : %d" % (m, t.count(m)))
# locate my bench block (unique by 第210回)
i=t.find("第210回")
print("210_idx", i)
if i>0:
    print("CTX:", t[i-40:i+120].replace("\n","\\n"))
