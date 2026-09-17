# -*- coding: utf-8 -*-
import io
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC,"r",encoding="utf-8") as f:
    t=f.read()
for m in ["第210回","run483A–C","1.1902s","0.1335s","0.3265s","0.3003s","1.9558"]:
    print("%s : %d" % (m, t.count(m)))
# show all lines containing 第210回 (my distinct marker vs falsify's 第216回)
lines=t.split("\n")
for i,l in enumerate(lines):
    if "第210回" in l:
        print("line %d contains 第210回 (len %d)" % (i+1, len(l)))
        # print tail after 第210回
        idx=l.find("第210回")
        print("   tail:", l[idx:idx+400])
        print("   ---")