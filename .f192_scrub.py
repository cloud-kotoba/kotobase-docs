#!/usr/bin/env python3
import re, ast
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f192_insert.py"
s=open(p,encoding="utf-8").read()
before=len(s)
for ch in ["\u200b","\u200c","\u200d","\u200e","\u200f"]:
    s=s.replace(ch,"")
s=re.sub("[\u0300-\u036f]","",s)
after=len(s)
open(p,"w",encoding="utf-8").write(s)
ast.parse(s)
print("OK before=%d after=%d removed=%d"%(before,after,before-after))