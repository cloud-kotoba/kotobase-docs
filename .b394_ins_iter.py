#!/usr/bin/env python3
# -*- coding: utf-8 -*-
FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(FN, encoding="utf-8").read()

entry = "- 2026-09-07: bench 第176回。20:22 JST tick。HEAD d84bf4a = bench 第175回 (20:09, K-Z3 20時台 run392 cold 7/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 13.30 (20:22 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (falsify 第168回, 20:19)「委ねる (rank 指定優先; falsify/bench フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run394 使用」。run393 は falsify 第168回 (20:19, 在途 uncommitted) が先行実施済みのため本 tick は次枠 run394 を実施 (run216/run256/run263/run278 precedent, 20時台 3 セット目の independent 計測として採用可否は rank 判定に委ねる)。K-Z3 20時台 run394A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:27:21–20:28:xx JST, 全 80/80 200, secret 不含 – curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) – run394A cold 単発 1/20 (2.4655s pos1 冒頭 1 件) p50 60.2ms / run394B 0/20 p50 57.3ms max 494.1ms / run394C 0/20 p50 72.5ms max 168.8ms, control (kotobase.net/signup) cold 0/20 p50 58.1ms max 152.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。run394A 単発は B/C+control 0/40 即消失で「帯内 1 窓即消失」散発単発型継続 (falsify run393A 散発 2/20 の 8 分後さらに減弱) — 20時台通算 = run392 7/60 + run393 2/60 + 本 tick run394 1/60 = 10/180 (~5.6%) 3 セット low-to-mid 帯候補。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run395 使用 – ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。\n"

# Insert as the first entry right after the "## Iteration log" heading
anchor = "## Iteration log\n"
pos = data.find(anchor)
if pos == -1:
    raise SystemExit("iter-log heading not found")
ins = pos + len(anchor)
data2 = data[:ins] + entry + data[ins:]

with open(FN, "w", encoding="utf-8") as f:
    f.write(data2)
print("iter-log entry inserted ok, at pos", pos)