import re
# dispatch: search all engine cljs for the xrpc route mapping (e.g. "datomic.q")
import glob
for f in glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/src/**/*.cljs", recursive=True):
    s = open(f).read()
    for m in re.finditer(r'datomic\.q|datomic/transact|x-kotobase-kv-stats', s):
        print(f.split("engine/")[1], m.start(), m.group(0))
