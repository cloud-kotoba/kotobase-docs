import re

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

old_ev = """falsify 2026-09-04 (K-Z3 深夜帯 23時台 n 積み増し run99A–C, 同測定法 n=20 × 3 run,
別接続 curl, Tokyo, 23:20 JST, 全 80/80 200, host load1 27.83 は production HTTP
実測のため gate 外): run99A cold 2/20 (1.073s 4番目, 2.062s 13番目 — 散発配置) p50
0.064s / run99B cold 0/20 p50 0.056s (0.043–0.339s) / run99C cold 0/20 p50 0.060s
(0.045–0.115s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20
p50 0.071s (0.054–0.133s) と静穏で control 分離成立、cold 群は search 側に局在。
traffic 最低帯の深夜でも日中帯型の突発 (単発/薄クラスタ) が散発 — traffic 依存説に
反する方向の観測で、夜帯通算 cold>0 は 54 試行中 15 試行 (~28%)、深夜帯 (23時台) は
3 試行中 1 試行。status 判定は rank に委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。
"""

new_ev = """falsify 2026-09-04 (K-Z3 深夜帯 23時台 n 積み増し run100A–C, 同測定法 n=20 × 3 run,
別接続 curl, Tokyo, 23:20 JST, 全 80/80 200, host load1 27.83 は production HTTP
実測のため gate 外。※ cosientist run99A–C (23:13–14) との ID 衝突を避け run100 とする):
run100A cold 2/20 (1.073s 4番目, 2.062s 13番目 — 散発配置) p50 0.064s / run100B cold
0/20 p50 0.056s (0.043–0.339s) / run100C cold 0/20 p50 0.060s (0.045–0.115s) —
landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.071s
(0.054–0.133s) と静穏で control 分離成立、cold 群は search 側に局在。traffic 最低帯の
深夜でも日中帯型の突発 (単発/薄クラスタ) が散発 — cosientist run99A (cold 5/20,
landing borderline) と合わせ深夜帯 23時台は 6 試行中 3 試行で cold>0、夜帯通算
cold>0 は 57 試行中 18 試行 (~32%)。深夜対比の低頻度期待に反し K-Z3 traffic 依存説は
弱まるが run99A は landing borderline のため機構確定には至らず。status 判定は rank に
委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。
"""

text = open(path, encoding="utf-8").read()
assert old_ev in text, "old evidence block not found"
text = text.replace(old_ev, new_ev, 1)
open(path, "w", encoding="utf-8").write(text)
print("renamed to run100, ok")
