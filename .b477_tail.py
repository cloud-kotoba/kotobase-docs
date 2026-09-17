# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()
# line 404 is index 403
ln = lines[403]
print("LEN:", len(ln))
print("TAIL120:", repr(ln[-120:]))
# count total lines
print("TOTAL:", len(lines))
