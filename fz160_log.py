import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

entry = ("- 2026-09-05: falsify 第58回。rank 第52回 NEXT (委ねる; K-Q1 切分けは cosientist 担当) を受け、"
         "K-Z3 18時台 control 付き追加 n run160A–C を同測定法で実施 (18:35 JST, production HTTP 実測のため gate 外, secret 不含): "
         "search cold 2/60 (~3.3%, 1.48/1.68s 単発 ×2), 18時台通算 3/120 ~2.5% 低位帯, p50 50–182ms 帯に復帰。"
         "ただし landing control cold 6/20 p50 0.342s と上振れし run158 型全体遅延窓が 18:01/18:35 の 2 窓で再出現 (部分 not-separated) — "
         "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先)。\n")

lines = text.split("\n")
# append after last iteration log entry: find last line starting with "- 2026-09-05:"
last = -1
for i, ln in enumerate(lines):
    if ln.startswith("- 2026-09-05:"):
        last = i
lines.insert(last + 1, entry.rstrip("\n"))

with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

with io.open("fz160_log.txt", "w") as f:
    f.write("inserted after line %d\n" % (last + 1))
