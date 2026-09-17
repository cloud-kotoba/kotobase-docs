#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
for key in ["\uff08 K-Q2 / K-W1 / K-W2 / K-Z1", "( K-Q2 / K-W1 / K-W2 / K-Z1"]:
    import re
    m = re.search(re.escape(key), txt)
    print(key[:12], "->", bool(m), (m.start() if m else None))