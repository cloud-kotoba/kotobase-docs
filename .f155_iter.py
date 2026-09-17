#!/usr/bin/env python3
# Insert falsify 第155回 iteration-log entry newest-first (right after "## Iteration log").
FP="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(FP,encoding="utf-8").read().split("\n")
# find "## Iteration log" line
marker_idx=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        marker_idx=i
        break
assert marker_idx is not None, "marker not found"
# insert after marker_idx (i.e. at marker_idx+1), newest-first means this entry goes above the current first entry
entry = (
"- 2026-09-07: **falsify 第155回**。10:21 JST tick。HEAD 9a7885c = bench 第141回 (10:16, K-Z3 10時台 run333 cold 5/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 106.11 (10:16 uptime, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。※予定モニタ NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第145回 bump 済み「K-Z3 current-band(10hr) n-add run333」だが同 tick に bench 第141回 (10:15:59–10:16:23) が run333 (cold 5/60, run333A 冒頭クラスタ 4/20 + run333B 単発 1/20) を先行 commit したため 本 tick の実測 (10:20:55–10:21:36, K-Z3 10時台 independent n 積み増しとして run333-indep に読替 — run330/run322-indep 前例で独立 2 計測記録)。K-Z3 10時台 run333-indep A–C を本 tick 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 全 80/80 200): A cold 1/20 (1.2927s 単発散発) p50 144.6ms / B cold 0/20 p50 155.3ms / C cold 0/20 p50 128.5ms / control (kotobase.net/signup) cold 0/20 p50 120.3ms max 248.1ms 完全静穏で control 分離成立、cold 群 search 側に局在 — search cold 1/60 (~1.7%) 散発単発型、bench141-run333A 冒頭クラスタ (4/20) の直後減弱で「帯内 1 窓即消失」継続 (host load 106 で p50 128–155ms 上振れ borderline note 付きだが cold 判定 1/60 は control 完全静穏で確定的)。10時台 (9/7) 通算 = falsify154-run332 (4/60) + bench141-run333 (5/60) + 本 tick run333-indep (1/60) = 10/180 (~5.6%) 中位帯寄り、run331A heavy 9/20 初再出現 (55 セット連続非再現を割る) の弱後続継続 — heavy >=6/20 には至らず帯内 1 窓即消失型へ収束方向。詳細は K-Z3 evidence 欄 (L279 末尾追記)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run334 使用)。"
)
lines.insert(marker_idx+1, entry)
open(FP,"w",encoding="utf-8").write("\n".join(lines))
print("inserted iter-log entry after line", marker_idx+1)