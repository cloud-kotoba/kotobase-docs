#!/usr/bin/env python3
import io
# read iter log head to confirm the new entry is at top
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
i = txt.find("## Iteration log")
print(txt[i:i+320])