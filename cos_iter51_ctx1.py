import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
i = src.find("assoc-response-kv-stats")
print(src[i-400:i+200])
