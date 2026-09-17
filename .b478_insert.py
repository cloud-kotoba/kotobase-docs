#!/usr/bin/env python3
import io, os
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
ev=open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b478_ev.txt",encoding="utf-8").read().rstrip("\n")
il=open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b478_il.txt",encoding="utf-8").read().rstrip("\n")
for z in ["\u200b","\u200c","\u200d"]:
    ev=ev.replace(z,"")
    il=il.replace(z,"")
with io.open(P,encoding="utf-8") as f:
    lines=f.read().split("\n")
idx=None
for i,ln in enumerate(lines):
    if ln.strip()=="## Iteration log":
        idx=i
        break
assert idx is not None, "## Iteration log not found"
# append evidence to band row (line before ## Iteration log)
lines[idx-1]=lines[idx-1]+ev
# insert iter entry right after ## Iteration log (newest-first)
lines.insert(idx+1, il)
with io.open(P,"w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print("inserted idx=%d il_bytes=%d ev_bytes=%d"%(idx,len(il.encode()),len(ev.encode())))
