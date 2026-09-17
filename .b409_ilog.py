#!/usr/bin/env python3
# Insert falsify 179 iter-log entry newest-first, directly after '## Iteration log'.
import os
path="query-cosientist.md"
txt=open(path,encoding="utf-8").read()
entry=("- 2026-09-08: **falsify 第179回**。00:50 JST tick。HEAD f650bf8 = rank 第174回 = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。"
"live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 ~9.6 (00:47 uptime 実測, gate 7.5 超過) のため local 測定は拒否 "
"- 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
"※pre-run monitor NEXT\u300cK-Z3 深夜帯 23時台 n 積み増し継続\u300dは stale (rank 第90回帯 artifact) - "
"true progressive NEXT は iter-log HEAD (rank 第174回, 00:16, f650bf8)\u300cNEXT: K-Z3 0hr n-add run409 + iter-log\u300dで、"
"cron 実行時刻 00:47 が 0時台 (run407/408 済 8/120 ~6.7%) 中の n 積み増し続行、run409 枠を本 tick 実施 (.b409 既存なし=衝突なし確認)。"
"K-Z3 0時台 run409A-C 実測 (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test, 00:47:03-00:47:22 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
"cold(>=0.5s) 10/0/0 per 20 = 10/60 (~16.7%) - run409A cold 10/20 heavy 散発クラスタ (deep ~0.89-1.95s 冒頭+中盤+末広がり) "
"p50 141.9ms max 1.9454s / run409B cold 0/20 p50 45.2ms / run409C cold 0/20 p50 48.0ms, "
"control (kotobase.net/signup) cold 0/20 p50 44.5ms max 438.9ms 完全静穏で control 分離成立、cold 群 search 側局在。"
"run409A heavy 10/20 は B/C 0/40 + control 0/20 即消失で\u300c帯内 1 窓即消失\u300d最大級単一窓 (0時台 heavy>=6/20 初達成)。"
"0時台 (9/8) 通算 = run407 (4/60) + run408 (4/60) + 本 run409 (10/60) = 18/180 (~10.0%) の 3 セット "
"- 初期 2 セット ~6.7% 中位から run409A heavy により ~10.0% 高位候補へ上昇 (23時台 9/7 ~11.3% と同水準)。"
"深夜帯 traffic 最低での cold 3 セット連続 + heavy 再達は純 traffic 依存説への反証継続。"
"status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run410 使用)。")
entry=entry.replace("\u200b","").replace("\u200c","").replace("\u200d","").replace("\ufeff","")
assert "#####" not in entry, "illegal token"
marker="## Iteration log\n"
assert txt.count(marker)==1
txt=txt.replace(marker, marker+entry+"\n", 1)
open(path,"w",encoding="utf-8").write(txt)
print("iter-log entry inserted; K-Z3 occ=", txt.count("| K-Z3 |"))
print("falsify 第179回 occ=", txt.count("falsify 第179回"))