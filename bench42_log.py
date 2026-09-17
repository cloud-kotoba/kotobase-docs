path = "query-cosientist.md"
entry = (
    "- 2026-09-05: bench 第42回。新規 evidence: K-Z3 8時台 n 積み増し run120A–C "
    "(08:33 JST, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 全 60/60 + control 20/20 200, "
    "host load1 86.6 は production HTTP 実測のため gate 外)。run120A–C cold(≥0.5s) 0/20 × 3 "
    "(p50 0.040–0.041s) — landing control も cold 0/20 p50 0.041s と静穏で control 分離成立。"
    "8時台は run119A–C (falsify, 0/60) に続き 0/120 完全静穏で朝帯低位が再現 — "
    "5時台/6時台/8時台のみ低位という平坦パターン帯別分布の裾を支持。"
    "※ rank 第41回 NEXT は 9時台だったが cron 実行時刻が 08時台のため帯逸脱 (run105/run116 前例に従い記録)。"
    "深夜帯通算 cold>0 は 113 試行中 30 試行 (~26.5%)。status 遷移なし (rank 専門)。"
    "NEXT: 委ねる (rank 判断 — 9時台 n 積み増しの継続、または K-Z2 対比・K-Q1 engine 内訳への焦点移行)。"
)
with open(path, "a") as f:
    f.write(entry + "\n")
print("logged")
