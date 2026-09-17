import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

old = """22時台は 7 試行中 2 試行、夜帯通算 cold>0 は 48 試行中 13 試行 (~27%)。
status 判定は rank に委ねる。
"""

new = """22時台は 7 試行中 2 試行、夜帯通算 cold>0 は 48 試行中 13 試行 (~27%)。
status 判定は rank に委ねる。

falsify 2026-09-04 (K-Z3 夜帯 22時台 n 積み増し run98A–C, 同測定法 n=20 × 3 run,
別接続 curl, Tokyo, 22:33–22:35 JST, 全 80/80 200, host load1 11.04 は production
HTTP 実測のため gate 外): run98A cold 2/20 (1.107s/1.230s, 10/11番目連続 2 発,
薄クラスタ型) p50 0.055s / run98B cold 0/20 p50 0.056s (0.037–0.112s) / run98C
cold 0/20 p50 0.052s (0.030–0.084s) — landing page control (kotobase.net/,
同時刻, n=20, 全 200) は cold 0/20 p50 0.053s (max 0.355s, 0.5s 未満の borderline
1 件) で cold 群は search 側に局在 (control 分離成立)。run97A (22:17) に続く
22時台の散発で、直前 2 試行 cold 0 からの再出現 → 即消失パターンと一貫。
22時台は 8 試行中 3 試行、夜帯通算 cold>0 は 51 試行中 14 試行 (~27%)。
status 判定は rank に委ねる。NEXT: K-Z3 深夜帯 (23:00 以降) n=20 × 3。
"""

assert text.count(old) == 1, "anchor not unique"
with io.open(path, "w", encoding="utf-8") as f:
    f.write(text.replace(old, new))
print("appended")
