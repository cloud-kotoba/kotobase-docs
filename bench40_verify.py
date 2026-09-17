doc = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
out = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench40_verify.txt","w", encoding="utf-8")
out.write("contains 第40回 K-Z3 evidence: %s\n" % ("第40回, K-Z3" in doc))
