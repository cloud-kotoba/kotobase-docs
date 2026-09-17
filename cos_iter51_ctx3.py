import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
# find route/table that dispatches xrpc endpoints; print def around 15771 context start
seg = src[13000:17000]
routes = re.findall(r'"ai\.gftd\.apps\.kotobase\.datomic\.[a-z-]+"', seg)
print(routes)
