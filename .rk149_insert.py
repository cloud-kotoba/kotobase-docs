#!/usr/bin/env python3
path = "query-cosientist.md"
marker = "## Iteration log\n"

entry = (
    "- 2026-09-07: rank 第149回。11:58 JST tick。HEAD f4bc8ea = cosientist 第122回 (11:41, run343) = "
    "remote net-kotobase/main (bench_fetch) 一致 (git fetch + rev-parse 比較, 乖離 0 実測; worktree detached HEAD "
    "のため git pull --ff-only 不可, fetch 系で取り込み)。"
    "※ pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — "
    "true progressive NEXT は cosientist 第122回 (Iteration log 先頭, 11:41) の「K-Z3 現在時刻帯 11時台 "
    "n 積み増し続行, 次 run ID は run344 使用」。rank 第148回 (8c5d4b5, 11:36) 以降の新規確定 evidence は "
    "2 commit, すべて K-Z3 11時台: (1) falsify 第159回 run342A-C (9d74a15, 11:35, cold>=0.5s 3/20 散発 "
    "ペア, control 0/20 完全静穏分離成立, 前 tick run341A heavy 6/20 の 6 分後減弱), "
    "(2) cosientist 第122回 run343A-C (f4bc8ea, 11:41, cold 1/60 単発 1.1281s, B/C 0/20, control 0/20 "
    "完全静穏分離成立)。取り込み判定: (a) K-Z3: run342 + run343 を取込, 11時台 (9/7) 通算 = "
    "run339 (4/60) + run340 (3/60) + run341 (7/60) + run342 (3/60) + run343 (1/60) = 18/300 (~6.0%) の "
    "5 セット中位帯。run341A heavy 6/20 (run331A heavy 型の weak 再出現候補) は run342 3/20 ~ run343 1/60 "
    "へ減衰し「帯内 1 窓即消失」型のまま (heavy≥6/20 の持続性は未再現, 帯水準確定・機構判断には未達)。"
    "status: K-Z3 open 継続 (決定的反証/支持に未達 — 11h 18/300 ~6.0% は帯水準確定に至らず)。"
    "(b) K-Q1: 変動なし — transact 401 静的切れ手 (a)/(i)/(ii)/(iii) は全棄却済みで残余は cosientist 実装専任の "
    "動的切れ手 (delegation-for-request 照合) のみ, KV read 内訳初実測は滞留継続, 最上位維持。"
    "(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (K-Q1 は cosientist 実装待ち, "
    "K-Z3 は観測継続・11h 18/300 ~6.0% は帯水準確定に未達, K-Z2/K-S1/K-S2 は evidence なし)。"
    "新仮説なし。evolve 判断なし。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 41.01 (gate 7.5 大幅超過) — rank 担当は測定を"
    "行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。"
    "NEXT: K-Z3 current-band n-add 継続, 次 run ID は run344 使用 (実行時刻が 12時台へ移行していれば "
    "12時台帯初計測へ — 従来の帯移行前例に従う; 11h 18/300 ~6.0% の帯水準確定には追加 n)。"
    "K-Q1 は cosientist 実装専任のまま rank 測定指示対象外。\n"
)

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

if not content.startswith("# query"):
    raise SystemExit("UNEXPECTED FILE HEADER")

idx = content.find("## Iteration log\n")
if idx == -1:
    raise SystemExit("MARKER NOT FOUND")
pos = idx + len("## Iteration log\n")
new_content = content[:pos] + entry + content[pos:]

with open(path + ".rk_new", "w", encoding="utf-8") as f:
    f.write(new_content)
print("stage-write OK")