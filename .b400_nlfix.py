p = "query-cosientist.md"
s = open(p, encoding="utf-8").read()
old = "次 run ID は run401 使用)。- 2026-09-07: bench 第180回"
new = "次 run ID は run401 使用)。\n- 2026-09-07: bench 第180回"
assert s.count(old) == 1, ("count", s.count(old))
s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
print("newline fixed")