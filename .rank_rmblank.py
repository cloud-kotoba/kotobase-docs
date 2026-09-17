#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
d=io.open(p,encoding="utf-8").read()
# the rank entry ends with "...実装専任のまま)。\n\n" then "- 2026-09-08: **falsify 第188回**"
old="実装専任のまま)。\n\n- 2026-09-08: **falsify 第188回**"
new="実装専任のまま)。\n- 2026-09-08: **falsify 第188回**"
assert d.count(old)==1, f"anchor count={d.count(old)}"
d=d.replace(old,new)
io.open(p,"w",encoding="utf-8").write(d)
print("done, header count:",d.count("## Iteration log"))
print("rank count:",d.count("rank 第187回"))