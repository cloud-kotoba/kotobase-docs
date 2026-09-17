import io
doc = io.open("query-cosientist.md", encoding="utf-8").read()
checks = [
    ("K-Q1 bench65 evidence", "3 回目の transact 401 を確認" in doc),
    ("K-Q1 diag evidence", "pre-transact 認証付き query" in doc),
    ("K-Z3 run182 evidence", "run182A" in doc and "4時台帯初計測" in doc),
    ("iteration bench65", "bench 第65回。04:02 JST tick" in doc),
    ("NEXT tail", "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 5時台 n 積み増し継続)。" in doc),
]
ok = True
for name, cond in checks:
    print(name, "OK" if cond else "FAIL")
    ok = ok and cond
# 行構造確認: テーブル行が壊れていないか
for i, l in enumerate(doc.splitlines(), 1):
    if l.startswith("| K-Q1 |") or l.startswith("| K-Z3 |"):
        if not l.rstrip().endswith("|"):
            print("ROW-STRUCT-FAIL line", i)
            ok = False
        else:
            print("row line", i, "ends-with-pipe OK, len", len(l))
print("ALL-OK" if ok else "HAS-FAILURES")
