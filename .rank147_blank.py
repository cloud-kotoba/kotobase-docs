#!/usr/bin/env python3
path = "query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
old = "secret は一切記録せず。\n\n- 2026-09-07: bench 第145回。"
new = "secret は一切記録せず。\n- 2026-09-07: bench 第145回。"
assert content.count(old) == 1, "blank-line pattern not unique/found"
content = content.replace(old, new)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("blank removed")