path = "query-cosientist.md"
lines = open(path).read().splitlines(keepends=True)
i = 170  # 1-indexed line 171 -> index 170? no: line 170 is index 169
idx = 169
l = lines[idx]
assert l.startswith("| K-Z3"), l[:40]
add = (" bench 2026-09-05 (第42回, K-Z3 9時台 n 積み増し run120A–C, 同測定法 n=20 × 3 run, "
       "別接続 curl, Tokyo, 08:33 JST, 全 60/60 200, host load1 86.6 は production HTTP 実測のため gate 外): "
       "run120A cold(≥0.5s) 0/20 p50 0.040s / run120B 0/20 p50 0.041s / run120C 0/20 p50 0.040s — "
       "landing control (kotobase.net/, 同時刻, n=20, 全 200) も cold 0/20 p50 0.041s と静穏。"
       "9時台は帯初計測で cold 0/60 完全静穏 (8時台 run119 に続き朝帯低位を再確認)。"
       "深夜帯通算 cold>0 は 113 試行中 30 試行 (~26.5%)。status 判定は rank に委ねる\n")
lines[idx] = l.rstrip("\n") + add
open(path, "w").write("".join(lines))
print("appended to K-Z3 row")
