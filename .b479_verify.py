# -*- coding: utf-8 -*-
import os
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
print("disk bytes:", os.path.getsize(P))
s=open(P,encoding="utf-8").read()
print("python chars:", len(s))
# check run479 evidence and ilog present
print("run479 in row:", "run479A 散発クラスタ 5/20" in s)
print("ilog run479:", "bench 第208回。16:06 JST tick" in s)
print("K-Z3 header still:", s.count("| K-Z3 | worker |"))
print("iter header still:", s.count("## Iteration log"))
# structural sanity: row 278 intact and contains original run194
print("early content run194:", "run194A cold(>=0.5s)" in s)
print("early content run4:", "run4 10/20" in s)
print("tail cosientist140:", s.rstrip().endswith("(rank 専門)。"))
print("lengths ok:", 1184749 == len(s))