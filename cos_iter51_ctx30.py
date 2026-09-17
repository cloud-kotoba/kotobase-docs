s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/js/kotobase-graph-database-worker.js").read()
i = s.find("x-kotobase-kv-stats")
print(repr(s[i-300:i+300]))
