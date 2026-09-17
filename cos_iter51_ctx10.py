src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/xrpc.cljs").read()
# Where is the dispatch table mapping xrpc names to handlers? search for handle-q usage
import re
for m in re.finditer(r'handle-q\b', src):
    print("handle-q at", m.start())
    print(src[max(0,m.start()-200):m.start()+60].replace("\n"," | ")[-220:])
    print("---")
