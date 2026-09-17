#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
l=lines[358]
print("rank146 tail300:",repr(l[-300:]))
print("---contains NEXT?---")
import re
for m in re.finditer(r'NEXT[^\n]{0,200}', l):
    print("NEXT:",m.group(0))