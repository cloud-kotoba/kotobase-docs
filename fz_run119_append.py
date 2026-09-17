f = "query-cosientist.md"
text = open(f, encoding="utf-8").read()
line = "falsify 2026-09-05 (K-Z3 8時台 n 積み増し run119A–C, 同測定法 n=20 × 3 run, 別接続 curl, Tokyo, 08:17–08:17 JST, 全 80/80 200, host load1 41–48 (1/5/15min 41.17/74.45/66.88, 5/15min は前 tick 遺残の可能性) は production HTTP 実測のため gate 外): run119A cold(>=0.5s) 0/20 p50 0.033s (0.029–0.056s) / run119B cold 0/20 p50 0.038s (0.028–0.051s) / run119C cold 0/20 p50 0.037s (0.031–0.044s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.049s (max 0.360s の単発 1 件を除き静穏) で control 分離成立。朝帯 8時台帯初計測で全 3 run 完全静穏 (6時台後半 0/60 と連続)。※本 tick の統計スクリプトは cron runtime の heredoc 拒否により初回実行が空走したため python3 fz_stats.py の別ファイル化で再実行 (失敗分の HTTP リクエストは発生せず、production 負荷影響なし)。status 判定は rank に委ねる\n"
anchor = "falsify 2026-09-05 (K-Z3 深夜帯 5時台 n 積み増し run112A–C"
assert anchor in text and line not in text
text = text.replace(anchor, line + anchor, 1)
open(f, "w", encoding="utf-8").write(text)
print("appended")
