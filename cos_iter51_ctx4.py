import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
hits = [(m.start(), m.group(0)) for m in re.finditer(r'datomic[a-z.-]*|q\b', src[:12000])][:0]
for m in re.finditer(r'"[a-z0-9./-]*(?:q|transact)[a-z0-9./-]*"', src):
    print(m.start(), m.group(0))
