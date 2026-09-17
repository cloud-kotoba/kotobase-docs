path = "query-cosientist.md"
src = open(path).read()

evidence = "falsify 2026-09-05 (K-Z3 20時台 n 積み増し run169A–C, 第63回 run167 直後の追加 n, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 20:53–20:54 JST, 全 80/80 200, host load1 36 は production HTTP 実測のため gate 外): run169A cold(>=0.5s) 0/20 p50 0.050s (max 0.124s) / run169B cold 0/20 p50 0.080s (max 0.163s) / run169C cold 0/20 p50 0.068s (max 0.140s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.047s (max 0.063s) と静穏で control 分離成立。cold 0/60 だが search p50 50–80ms は control (47ms) に対し軽微上振れで run167 型の部分 not-separated 傾向は弱く再現 — run158 型全体遅延窓 (250ms+ 帯) は非再現。20時台通算は run167 (0/60) + 本 tick (0/60) で 120 試行中 0 試行の低位帯。status 判定は rank に委ねる (rank 専門)。"

lines = src.splitlines(keepends=True)
out = []
inserted = False
for ln in lines:
    if not inserted and ln.startswith("| K-Z3 | worker |") and " open |" in ln:
        row = ln.rstrip()
        while not row.endswith("|"):
            row = row[:-1]
        newrow = row[:-1] + " " + evidence + " |\n"
        out.append(newrow)
        inserted = True
    else:
        out.append(ln)
assert inserted, "K-Z3 row not found"
open(path, "w").write("".join(out))
print("inserted ok")
