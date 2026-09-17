s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/physical_index_dispatch.cljs").read()
i = s.find("defn handle-with")
print(s[i+4500:i+6200])
