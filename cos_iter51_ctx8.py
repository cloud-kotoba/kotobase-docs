src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
import re
# find where handle-q's run-read chain attaches kv-stats: search "run-read" occurrences
for m in re.finditer(r'\(defn run-read|run-read', src):
    print("run-read at", m.start())
# print context around 15200-15900 (first assoc at 15772)
print(src[15300:15950])
