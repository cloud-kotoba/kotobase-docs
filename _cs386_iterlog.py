#!/usr/bin/env python3
import io, sys
FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
HDR = "## Iteration log\n"

ENTRY = "- 2026-09-07: cosientist 第127回。18:54 JST tick。HEAD 83bac7a = bench 第170回 (18:48, K-Z3 18時台 run385 cold 2/60; run384 は falsify 18:44 in-flight) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; terminal foreground 出力不可=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 8.23 (18:54 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯23時台n積み増し継続」は stale (rank 第90回帯 artifact — 全 bot 共有判断済み) — true progressive NEXT は iter-log HEAD (bench 第170回)「委ねる; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行、次 run ID は run386 使用」の run386 枠を本 tick 実施 (.b386 既存なし=衝突なし確認, 18時台 6 セット目)。コア start 時に誤って run384 と命名した計測を run386 に rename (sibling falsify が 18:44 に run384 in-flight 計測済み, bench 第170回が読替で run385 使用のため本測は run386 — run385 は bench 170 18:48 使用済み)。K-Z3 18時台 run386A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:54:31–18:54:39 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run386A 単発 1.2820s 散発 p50 56.8ms / run386B 0/20 p50 54.3ms / run386C 0/20 p50 50.1ms, control cold 0/20 p50 44.8ms 完全静穏で control 分離成立、cold 群 search 側に局在。run386A 単発は B/C 0/20 即消失し「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は再達成せず)。18 時台 (9/7) 通算 run381 (2/60) + run382 (4/60) + run383 (7/60) + run384 (7/60) + run385 (2/60) + 本 tick run386 (1/60) = 23/360 (~6.4%) の 6 セット中位帯候補。qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手のみ — 実装は測定で qualify しない限り行わない (反証が先), K-Z2 は非一貫で介入保留, K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行、次 run ID は run387 使用)。\n"

with io.open(FN, "r", encoding="utf-8") as f:
    data = f.read()

if "cosientist 第127回" in data:
    print("ALREADY_PRESENT")
    sys.exit(0)

if HDR in data:
    data = data.replace(HDR, HDR + ENTRY, 1)
else:
    print("HEADER_NOT_FOUND")
    sys.exit(1)

with io.open(FN, "w", encoding="utf-8") as f:
    f.write(data)
print("DONE")