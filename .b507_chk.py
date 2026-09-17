# -*- coding: utf-8 -*-
import io, re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(p, encoding="utf-8").read()
for token in ["run507", "run506", "run505", "run504", "第222回", "第223回", "第224回", "第225回", "第226回"]:
    cnt = len(re.findall(re.escape(token), txt))
    print("%s : %d" % (token, cnt))