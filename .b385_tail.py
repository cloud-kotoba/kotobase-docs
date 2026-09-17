#!/usr/bin/env python3
import io
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(path,encoding="utf-8").read()
# find K-Z3 hypothesis row line
lines=s.split("\n")
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i
        break
print("KZ3_ROW_LINE=%d len=%d"%(idx+1,len(lines[idx])))
print("TAIL="+lines[idx][-400:])
# iter anchor
an="## Iteration log\n"
ia=s.find(an)
print("ITER_ANCHOR_AT=",ia)
print("NEXT_SNIPPET="+s[ia:ia+120].replace("\n","<NL>"))