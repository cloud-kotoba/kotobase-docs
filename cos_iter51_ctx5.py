src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
i = src.find('"q"')
print(src[i-800:i+400])
