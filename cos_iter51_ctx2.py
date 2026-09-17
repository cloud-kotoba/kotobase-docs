import re
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
for m in re.finditer(r'\(assoc-response-kv-stats', src):
    start = src.rfind('\n', 0, m.start()-300)
    print("=== match at", m.start(), "===")
    print(src[max(0,m.start()-250):m.start()+80].replace('\n', ' | ')[-260:])
