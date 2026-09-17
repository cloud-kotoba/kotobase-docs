import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

target = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        target = i
        break
assert target is not None, "K-Z3 row not found"

ev = (" falsify 2026-09-05 (K-Z3 19時台帯 n 積み増し run162A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 19:02:26–19:02:44 JST, 全 80/80 200, host load1 29.81 は production HTTP 実測のため gate 外): "
      "run162A cold(>=0.5s) 0/20 p50 0.067s (max 0.133s) / run162B cold 0/20 p50 0.049s / run162C cold 0/20 p50 0.076s (max 0.409s) — "
      "search 3 run 完全静穏 (0/60)。ただし landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 2/20 "
      "(6番目 0.776s, 12番目 0.619s) p50 0.089s と散発 2 件 — search 側は静穏で cold 群は landing 側にのみ出現し "
      "search 局在が逆転した稀なパターン (run162 型, 分離成立だが方向逆転)。19時台通算は 2026-09-04 run88A–C (0/60) + 本 tick "
      "で search cold 0/120 の低位帯 — 18時台 (~2.2%) から 21時台 (~25–58%) へ遷移する中間帯の 19時台は低位を維持。"
      "status 判定は rank に委ねる (rank 専門)。")

row = lines[target].rstrip("\n")
assert row.endswith("|"), "unexpected row format"
new_row = row[:-1].rstrip() + ev + "|"
lines[target] = new_row + "\n"

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

with io.open("fz162_append.txt", "w", encoding="utf-8") as f:
    f.write("appended to line %d\n" % (target + 1))
