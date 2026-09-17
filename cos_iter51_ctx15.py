s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/kotobase/graph_database/physical_index_dispatch.cljs").read()
# where does handle return primary-response? check tail for response return paths
import re
i = s.find("defn handle-with")
seg = s[i:i+6000]
# find mentions of response construction
for m in re.finditer(r'primary-response\b(?!\))|new Response|json-resp|-status\b', seg):
    print(m.start(), m.group(0))
