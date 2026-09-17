#!/usr/bin/env python3
# -*- coding: utf-8 -*-
path = "query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    txt = f.read()

header = "## Iteration log\n"

evidence = ("bench 2026-09-07 (第161回, K-Z3 16時台 n積み増し run370A–C — iter-log HEAD (bench 第160回)「K-Z3 current-band(16時台) n-add 継続, 次 run ID は run369 使用」の続行枠だが run369 は sibling falsify が 16:04–16:05 に in-flight 先行実施済みのため run370 に読替 (run216/run256/run263 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 16:09:12–16:09:29 JST, 全 80/80 200, host load1 282.27→259.71 (16:09 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run370A cold 2/20 冒頭/末尾散発型 (1.0046s pos1 + 1.0898s pos18 単発スパイク) p50 79.5ms / run370B cold 0/20 p50 78.7ms max 256.7ms / run370C cold 0/20 p50 64.8ms max 205.1ms, control (kotobase.net/signup) cold 0/20 p50 83.9ms max 205.1ms 完全静穏で control 分離成立、cold 群は search 側に局在。run368A heavy 8/20 (16:00) の 9 分後の run370A 2/20 散発型は「帯内 1 窓即消失」型を継続 — run368A heavy は sibling run369 + 本 tick run370 で heavy 級持続は再現せず散発に減衰し、heavy (>=6/20) の帯水準持続性は未確認のまま。host load 高騰 (259–282) の warm p50 (65–84ms) 全体的上振れ borderline note だが control 0/20 完全静穏で cold 濃度 2/60 は閾値決定的。16時台 (9/7) 通算は run368 (9/60) + sibling run369 + 本 tick run370 (2/60) の 3 セット — 帯水準確定には rank の run369 取込を待つ。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。\n")

iterlog = ("- 2026-09-07: bench 第161回。16:09 JST tick。HEAD 4661225 = bench 第160回 (16:00, K-Z3 16時台帯初 run368 cold 9/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 127.99 (16:07 pre-run uptime) → 282.27→259.71 (16:09 測定時 uptime 実測, gate 7.5 大幅超過) — production HTTP 実測のため gate 外で実施 (local 測定は拒否)。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第160回, 16:00)「K-Z3 current-band(16時台) n-add 継続, 次 run ID は run369 使用」の run369 枠だが、sibling falsify が同 16時台 run369 を 16:04–16:05 で先行実施 (.b369 データ in-flight 確認) のため run369→run370 に読替 (run216/run256/run263 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる)。K-Z3 16時台 run370A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 16:09:12–16:09:29 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run370A cold 2/20 (1.0046s pos1 + 1.0898s pos18 冒頭/末尾散発型) p50 79.5ms / run370B cold 0/20 p50 78.7ms max 256.7ms / run370C cold 0/20 p50 64.8ms max 205.1ms, control (kotobase.net/signup) cold 0/20 p50 83.9ms max 205.1ms 完全静穏で control 分離成立、cold 群 search 側に局在。run368A heavy 8/20 の 9 分後の散発 2/20 型は「帯内 1 窓即消失」型継続 — heavy (>=6/20) の帯水準持続性は sibling run369 + 本 tick でも再現せず未確認のまま。host load 高騰 (259–282) tick の warm p50 全体的上振れ borderline note だが control 0/20 完全静穏で cold 濃度 2/60 確定。16時台 (9/7) 3 セット目 (run368 9/60 + sibling run369 + 本 tick run370 2/60)、帯水準確定は rank の run369 取込待ち。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行、次 run ID は run371 使用)\n")

# 1) evidence: insert before "## Iteration log"
assert header in txt, "header not found"
txt2 = txt.replace(header, evidence + header, 1)

# 2) iter entry: insert right after "## Iteration log\n" (before the first existing entry line)
assert header in txt2, "header missing after evid insert"
txt3 = txt2.replace(header, header + iterlog, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(txt3)
print("inserted ok; file now starts iterlog at header+1")