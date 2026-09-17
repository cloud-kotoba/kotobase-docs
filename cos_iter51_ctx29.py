import re
s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/js/kotobase-graph-database-worker.js").read()
print("len", len(s))
for pat in ["x-kotobase-kv-stats", "block-fetch-stats-summary", ";distinct=", "l1="]:
    print(pat, s.count(pat))
