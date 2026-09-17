#!/usr/bin/env python3
# bench 第160回: insert run368 evidence into K-Z3 cell + add Iteration log entry (newest-first, after ## Iteration log).
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    txt = f.read()

evidence = """
 bench 2026-09-07 (第160回, K-Z3 16時台帯初計測 run368A–C — rank 第158回 NEXT「K-Z3 16hr band-first run368」に従い現時刻帯 16時台帯初計測 (15時台 4 セット 9/240 ~3.8% 完了後の帯移行), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 16:00:15–16:00:45 JST, 全 80/80 200, host load1 15.21→24.57 (16:00 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 8/1/0 per 20 = 9/60 (~15%) — run368A cold 8/20 heavy クラスタ (1.2449/0.9887/2.167/1.4193/1.5418/1.1716/0.5438/2.2836s pos2/3/5/7/9/12/13/14 散発配置, warm 群 p50 94ms) p50 104.9ms max 2283.6ms / run368B cold 1/20 (0.7528s pos15 単発) p50 107.9ms / run368C cold 0/20 p50 139ms, control (kotobase.net/signup) cold 1/20 (0.5232s pos19 閾値境界値) p50 204ms — control 完全静穏不成立 (borderline not-separated 注記; search cold 9 件中 8 件は 0.99–2.28s の deep cold で control 境界 0.52s と逆方向の magnitude 分離弱成立)。 run368A cold 8/20 は heavy (>=6/20) 閾値再達の 16時台帯初初候補 (run331A/run359A heavy 型の再出現, run366A 4/20 の帯移行後 1 窓目での heavy 上振れ) — B/C 0/60 + control 境界 1 件で「帯内 1 窓即消失」型は維持 (heavy>=6/20 の持続性は帯内追加 n で確認)。16時台 (9/7) 帯初計測 = 9/60 (~15%) の 1 セット高位帯初期サンプル — 15時台 (~3.8%)・14時台 (~6.3%) より高位で日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。
"""

ilog = """- 2026-09-07: bench 第160回。16:00 JST tick。HEAD 4e6cedb = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 15.21→24.57 (16:00 測定時 uptime 実測, gate 7.5 大幅超過) — production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第158回, 15:46)「K-Z3 16hr band-first run368」の run368 枠を本 tick 実施 (16時台帯初計測, 15時台 run364–367 4 セット 9/240 ~3.8% 完了後の帯移行)。cron tick 15:52 で 16時台開始を待って 16:00:15 から計測した。run368 計測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 16:00:15–16:00:45 JST, 全 80/80 200): cold(>=0.5s) 8/1/0 per 20 = 9/60 (~15%) — run368A cold 8/20 heavy クラスタ (1.2449/0.9887/2.167/1.4193/1.5418/1.1716/0.5438/2.2836s pos2/3/5/7/9/12/13/14) p50 104.9ms max 2283.6ms / run368B cold 1/20 (0.7528s pos15 単発) p50 107.9ms / run368C cold 0/20 p50 139ms, control (kotobase.net/signup) cold 1/20 (0.5232s pos19 境界値) p50 204ms — control 完全静穏不成立 (borderline not-separated 注記, search deep cold 0.99–2.28s と control 境界 0.52s の逆方向 magnitude 分離弱成立)。run368A 8/20 は heavy (>=6/20) 閾値再達の 16時台帯初初候補 (run331A/run359A heavy 型再出現) — B/C 0/60 + control 境界 1 件で「帯内 1 窓即消失」型維持、heavy 持続性は帯内追加 n で確認。16時台 (9/7) 帯初計測 9/60 (~15%) の高位帯初期サンプル。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl + python stats のみ)。詳細は K-Z3 evidence 欄追記。
"""

anchor = "## Iteration log"
assert txt.count(anchor) == 1, "anchor not unique/found: %d" % txt.count(anchor)
idx = txt.index(anchor)
# evidence appended into K-Z3 cell just before the Iteration log section header
newtxt = txt[:idx] + evidence + anchor + txt[idx+len(anchor):]
# iteration entry inserted right after the header (newest-first, before rank 158 entry)
idx2 = newtxt.index(anchor)
newtxt = newtxt[:idx2+len(anchor)] + "\n" + ilog + newtxt[idx2+len(anchor):]

with open(path, "w", encoding="utf-8") as f:
    f.write(newtxt)
print("done, new length", len(newtxt))