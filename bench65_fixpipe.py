# bench65 — K-Q1/K-Z3 行末に "|" を補完 (bench64 前例どおり evidence 欄末尾に pipe を追加)
import io
path = "query-cosientist.md"
doc = io.open(path, encoding="utf-8").read()
lines = doc.splitlines(keepends=True)
fixed = 0
for idx in (51, 206):  # 0-indexed for lines 52 and 207
    l = lines[idx]
    body = l.rstrip("\n")
    if not body.rstrip().endswith("|"):
        body = body.rstrip() + " |"
        lines[idx] = body + "\n"
        fixed += 1
io.open(path, "w", encoding="utf-8").write("".join(lines))
print("fixed", fixed)
