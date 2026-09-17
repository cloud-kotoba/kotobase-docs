import io, re

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

target = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        target = i
        break
assert target is not None, "K-Z3 row not found"

ev = (" falsify 2026-09-05 (K-Z3 18時台 control 付き追加 n run160A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 18:35:26 JST, 全 80/80 200, host load1 91.78 は production HTTP 実測のため gate 外): "
      "run160A cold(>=0.5s) 1/20 (1.679s) p50 0.182s / run160B cold 1/20 (1.484s) p50 0.073s / run160C cold 0/20 p50 0.069s — "
      "search cold 計数 2/60 (~3.3%) と 18時台通算 (run159 1/60 + run160 2/60) は 3/120 ~2.5% の低位帯で p50 は 50–182ms 帯に復帰。"
      "ただし landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 6/20 p50 0.342s (max 0.754s) と全体的に上振れし "
      "run158 型の全体的遅延窓が 18:01 / 18:35 の 2 窓で再出現 — search 側は p50 への反映が薄く (search/landing 同時ではない部分分離) "
      "control 分離は部分的不成立 (not-fully-separated)。18時台は低位 cold 率だが短時間全体遅延窓の再現性が残り、追加 n と control "
      "分離成立サンプルの確定を rank 判断に委ねる。status 判定は rank に委ねる (rank 専門)。 ")

row = lines[target]
# insert evidence into the evidence column: before " | open | " marker's 2nd cell boundary —
# row format: | K-Z3 | worker | hypothesis | open | <evidence...> |
# append evidence at end of the row line (before trailing newline)
row = row.rstrip("\n")
assert row.endswith("|"), "unexpected row format"
new_row = row[:-1].rstrip() + ev + "|"
lines[target] = new_row + "\n"

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

with io.open("fz160_append.txt", "w", encoding="utf-8") as f:
    f.write("appended to line %d\n" % (target + 1))
