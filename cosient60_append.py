import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()

line = ("cosientist 2026-09-05 (K-Z3 22時台 n 積み増し run173A–C, bench 第59回 run172A–C 直後の追加 n, "
        "同測定法 n=20 × 3 run + landing control, 別接続 curl, Tokyo, 22:33–22:40 JST, 全 80/80 200, "
        "host load1 76–114 (15min avg) は production HTTP 実測のため gate 外): "
        "run173A cold(>=0.5s) 1/20 (0.994s 12番目 単発散発型) p50 0.064s (0.042–0.994s) / "
        "run173B cold 0/20 p50 0.077s (0.034–0.215s) / run173C cold 0/20 p50 0.087s (0.042–0.468s) — "
        "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.111s (0.073–0.492s) と静穏で "
        "control 分離成立、cold 群は search 側に局在。22時台通算は run172A–C (5/60) + 本 tick (1/60) で "
        "120 試行中 6 試行 (~5%) — bench 第59回観測の run172A 型薄散発は即時非再現で "
        "22時台は 21時台 (not-separated あり) より低く 18–20時台 (~2-3%) と 12時台 (~8.3%) の中間的な低位帯の "
        "初期パターン。status 判定は rank に委ねる。\n")

# Insert after the K-Z3 12時台 cosientist line (line starting 'cosientist 2026-09-05 (K-Z3 12時台')
marker = "cosientist 2026-09-05 (K-Z3 12時台 n 積み増し run129A–C"
idx = src.find(marker)
assert idx != -1, "marker not found"
# find end of that line
end = src.find("\n", idx)
assert end != -1
new = src[: end + 1] + line + src[end + 1 :]
open(path, "w", encoding="utf-8").write(new)
print("appended, new size", len(new))
