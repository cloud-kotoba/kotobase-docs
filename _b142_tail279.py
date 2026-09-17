#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
line=open(path).read().split("\n")[278]  # line 279
# print last ~1200 chars of the line (tail = newest evidence appended to END)
print("LEN:", len(line))
print("----TAIL (last 1400)----")
print(line[-1400:])