#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()
i = txt.find("23\u6642\u53f0\u901a\u7b97 15/180")
print("idx", i)
if i>=0:
    print(repr(txt[i:i+60]))