path = "query-cosientist.md"
text = open(path).read()
old1 = ("bench 2026-09-05 (第42回, K-Z3 9時台 n 積み増し run120A–C, 同測定法 n=20 × 3 run, "
        "別接続 curl, Tokyo, 08:33 JST, 全 60/60 200, host load1 86.6 は production HTTP 実測のため gate 外): "
        "run120A cold(≥0.5s) 0/20 p50 0.040s / run120B 0/20 p50 0.041s / run120C 0/20 p50 0.040s — "
        "landing control (kotobase.net/, 同時刻, n=20, 全 200) も cold 0/20 p50 0.041s と静穏。"
        "9時台は帯初計測で cold 0/60 完全静穏 (8時台 run119 に続き朝帯低位を再確認)。"
        "深夜帯通算 cold>0 は 113 試行中 30 試行 (~26.5%)。status 判定は rank に委ねる")
new1 = ("bench 2026-09-05 (第42回, K-Z3 8時台 n 積み増し run120A–C, 同測定法 n=20 × 3 run, "
        "別接続 curl, Tokyo, 08:33 JST, 全 60/60 200, host load1 86.6 は production HTTP 実測のため gate 外。"
        "※ rank 第41回 NEXT は 9時台だったが cron 実行時刻が 08時台のため帯待機不可能 — "
        "run105/run116 前例に従い同測定法を 8時台として記録): "
        "run120A cold(≥0.5s) 0/20 p50 0.040s / run120B 0/20 p50 0.041s / run120C 0/20 p50 0.040s — "
        "landing control (kotobase.net/, 同時刻, n=20, 全 200) も cold 0/20 p50 0.041s と静穏。"
        "8時台は 2 試行連続 (run119 + 本 tick) で cold 0/120 完全静穏、朝帯低位を再確認。"
        "深夜帯通算 cold>0 は 113 試行中 30 試行 (~26.5%)。status 判定は rank に委ねる")
assert old1 in text
text = text.replace(old1, new1)
open(path, "w").write(text)
print("fixed")
