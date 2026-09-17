s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/physical_index_dispatch.cljs").read()
print("len", len(s))
i = s.find("defn handle-with")
print("handle-with at", i)
# print tail 1500 chars
print(s[-1800:])
