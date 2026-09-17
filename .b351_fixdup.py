import io
f = "query-cosientist.md"
with io.open(f, encoding="utf-8") as fh:
    data = fh.read()

bad = "追加 n 継続)。\n## Iteration log\n- 2026-09-07: bench 第157回。"
good = "追加 n 継続)。\n- 2026-09-07: bench 第157回。"
n = data.count(bad)
print("bad-pattern count =", n)
assert n == 1, "expected exactly 1 duplicate-header pattern"
data = data.replace(bad, good, 1)
print("Iteration-log headers after fix =", data.count("## Iteration log"))
with io.open(f, "w", encoding="utf-8") as fh:
    fh.write(data)
print("fixed")