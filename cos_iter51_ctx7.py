src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
import re
for m in re.finditer(r'assoc-response-kv-stats', src):
    print(m.start())
i = src.find("defn run-read")
print("run-read at", i)
print(src[i:i+700])
