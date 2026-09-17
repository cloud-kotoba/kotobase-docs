text = open("query-cosientist.md", encoding="utf-8").read()

entry = (
    "\n- 2026-09-05: bench 第35回。新規 evidence: K-Z3 深夜帯 0時台 run104A–C "
    "(00:43 JST, n=20 × 3 + landing control, 別接続 curl, Tokyo, 全 60/60 + control "
    "20/20 200, host load1 7.55 (tick 開始時) は production HTTP 実測のため gate 外)。"
    "run104A cold 2/20 (1.218s 1番目, 0.997s 8番目 — 散発配置) p50 0.056s / run104B cold "
    "0/20 p50 0.056s (0.042–0.089s) / run104C cold 0/20 p50 0.052s (0.041–0.093s) — "
    "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.056s "
    "(0.042–0.118s) と静穏で control 分離成立、cold 群は search 側に局在。run104A は "
    "run100A 型の薄い cold 単独クラスタ (warm p50 上振れを伴わない) で、0時台は "
    "9 試行中 2 試行 (run102A, run104A) で cold>0、深夜帯通算は 81 試行中 24 試行 "
    "(~29.6%)。traffic 依存説に対しては帯内で発現/消失が交互に出るばらつきが継続。"
    "status 遷移なし (rank 専門)。K-Q1 local profiling は load1 7.55 が閾値 7.5 を"
    "わずかに超過のため不実施 (次回 quiet-host 時に再試行)。"
    "NEXT: K-Z3 深夜帯 0時台 n 積み増し継続。\n"
)

text = text.rstrip("\n") + entry
open("query-cosientist.md", "w", encoding="utf-8").write(text)
print("appended")
