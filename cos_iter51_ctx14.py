s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/physical_index_dispatch.cljs").read()
import re
i = s.find("defn handle")
print(s[i:i+1500])
