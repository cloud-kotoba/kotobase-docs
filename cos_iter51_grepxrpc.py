import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
for m in re.finditer(r'.*kv-stats.*', src):
    print(m.group(0).strip()[:160])
