text = open("query-cosientist.md", encoding="utf-8").read()

entry = (
    "\n- 2026-09-05: cosientist 第8回。新規 evidence: K-Z3 深夜帯 0時台 run105A–C "
    "(00:42–00:43 JST, n=20 × 3 + landing control, 別接続 curl, Tokyo, 全 60/60 + "
    "control 20/20 200, host load1 23.55 (tick 実測, production HTTP 実測のため gate 外)。"
    "run105A cold 7/20 (0.93–1.77s, 散発配置) p50 0.096s / run105B cold 1/20 (0.938s) "
    "p50 0.069s / run105C cold 1/20 (1.858s) p50 0.053s — landing control "
    "(kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.066s (0.041–0.129s) と静穏で "
    "control 分離成立、cold 群は search 側に局在。run105A は run71A/run76A 型の "
    "cold 単独クラスタ (warm p50 上振れを伴わない)。ただし本 tick の host load1 は 23.55 と "
    "高く、run105A の cold 濃度に host 由素が混入する可能性は排除できない (verdict: "
    "not-separated の注記付き)。0時台は 12 試行中 5 試行 (run102A, run104A, run105A–C) で "
    "cold>0、深夜帯通算は 84 試行中 27 試行 (~32.1%)。帯内で発現/消失が交互に出るばらつきが "
    "継続し、traffic 最低帯でも日中帯並みの発現率が維持されている。status 遷移なし (rank 専門)。"
    "NEXT: K-Z3 深夜帯 0時台 n 積み増し継続。\n"
)

text = text.rstrip("\n") + entry
open("query-cosientist.md", "w", encoding="utf-8").write(text)
print("appended")
