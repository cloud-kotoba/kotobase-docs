import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
evidence = ("falsify 2026-09-04 (K-Z3 深夜帯 23時台 n 積み増し run99A–C, 同測定法 n=20 × 3 run,\n"
"別接続 curl, Tokyo, 23:20 JST, 全 80/80 200, host load1 27.83 は production HTTP\n"
"実測のため gate 外): run99A cold 2/20 (1.073s 4番目, 2.062s 13番目 — 散発配置) p50\n"
"0.064s / run99B cold 0/20 p50 0.056s (0.043–0.339s) / run99C cold 0/20 p50 0.060s\n"
"(0.045–0.115s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20\n"
"p50 0.071s (0.054–0.133s) と静穏で control 分離成立、cold 群は search 側に局在。\n"
"traffic 最低帯の深夜でも日中帯型の突発 (単発/薄クラスタ) が散発 — traffic 依存説に\n"
"反する方向の観測で、夜帯通算 cold>0 は 54 試行中 15 試行 (~28%)、深夜帯 (23時台) は\n"
"3 試行中 1 試行。status 判定は rank に委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。\n")

text = open(path, encoding="utf-8").read()
marker = "| K-Z2 | worker |"
assert marker in text, "K-Z2 marker not found"
new = text.replace(marker, evidence + marker, 1)
open(path, "w", encoding="utf-8").write(new)
print("evidence appended before K-Z2 row, ok")
