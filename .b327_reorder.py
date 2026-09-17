#!/usr/bin/env python3
f="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(f,encoding="utf-8").read().split("\n")
# find indices of the two newest entries after header
hdr=lines.index("## Iteration log")
# my entry is the one starting with "- 2026-09-07: bench 第138回"
mine=[i for i,l in enumerate(lines) if l.startswith("- 2026-09-07: bench 第138回")]
old=[i for i,l in enumerate(lines) if l.startswith("- 2026-09-07: falsify 第151回")]
print("hdr",hdr,"mine",mine,"old",old)
if mine and old:
    mi, oi = mine[0], old[0]
    # move mine to hdr+1, old to hdr+2
    # remove mine then insert at hdr+1
    me_line = lines.pop(mi)
    # old index may have shifted if mi<oi
    # re-locate old
    old=[i for i,l in enumerate(lines) if l.startswith("- 2026-09-07: falsify 第151回")]
    oi=old[0]
    lines.insert(hdr+1, me_line)
    # now old should be at hdr+2; verify
    lines2=[i for i,l in enumerate(lines) if l.startswith("- 2026-09-07: falsify 第151回")]
    print("after: old now at", lines2)
open(f,"w",encoding="utf-8").write("\n".join(lines))
print("done")