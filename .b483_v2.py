# -*- coding: utf-8 -*-
import io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC,"r",encoding="utf-8") as f:
    t=f.read()
print("len=%d" % len(t))
print("run484A:%d" % t.count("run484A"))
print("run484=%d" % t.count("run484"))
print("1.9558=%d" % t.count("1.9558"))
print("1.1902=%d" % t.count("1.1902"))
h=t.find("## Iteration log")
print("--- iter head (first entry 300) ---")
print(t[h:h+300])