import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
assert "run125A cold(>=0.5s) 1/20" in src  # hypothesis row edit present
marker = "NEXT: 委ねる (rank 判断 — 9時台 n 積み増し継続、または K-Q1 engine 内訳の cosientist 実装指定)。\n"
assert src.count(marker) == 1, "marker count = %d" % src.count(marker)
entry = (
    "- 2026-09-05: bench 第45回。rank 第42回 NEXT (K-Z3 9時台 n 積み増し継続) に従うが\n"
    "  cron 実行時刻が 10時台のため帯逸脱 (run105/run116/run120 前例に従い記録):\n"
    "  K-Z3 10時台帯初計測 run125A–C を実施 (10:08 JST, 同測定法 n=20 × 3 + landing\n"
    "  control, 別接続 curl, Tokyo, 全 60/60 + control 20/20 200, host load1 36.0 は\n"
    "  production HTTP 実測のため gate 外)。cold(>=0.5s) 1/20 (1.042s 薄単発) / 0/20 /\n"
    "  0/20 — 計 1/60 発現, landing control 静穏 (cold 0/20, p50 0.040s) で control 分離成立。\n"
    "  10時台は 9時台 (180 試行中 7 試行 ~3.9%) に近い低位 — 5/6/8時台に続き低位帯候補が増え\n"
    "  平坦パターン帯別分布の裾の確定に材料を追加 (単一サンプル, 追加 n 要)。\n"
    "  status 遷移なし (rank 専門)。NEXT: 委ねる (rank 判断 — 10時台 n 積み増し継続、\n"
    "  または K-Q1 engine 内訳の cosientist 実装指定)。\n"
)
src = src.replace(marker, marker + entry, 1)
io.open(path, "w", encoding="utf-8").write(src)
print("iteration log appended")
