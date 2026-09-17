src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
i = src.find('"q"', 30000)
print("q at", i)
j = src.find("assoc-response-kv-stats", i)
print("assoc after q at", j)
seg = src[i-100:i+600]
print(seg)
