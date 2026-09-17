#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
i = txt.find("\u6df1\u591c\u5e2f\u5e73\u5766")
print("idx", i)
if i>=0:
    print(repr(txt[i-5:i+60]))