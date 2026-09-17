#!/usr/bin/env python3
# cosientist 第124回: append K-Z3 run356 evidence cell entry + iter log entry.
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding='utf-8') as f:
    lines = f.readlines()

# Find "## Iteration log" line index.
iter_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        iter_idx = i
        break
assert iter_idx is not None, "iter log header not found"

# The K-Z3 evidence cell is the multi-line cell ending just before "## Iteration log".
# Append evidence entry as a new continuation line before iter log.
evi = (
    "\ncosientist 2026-09-07 (第124回, K-Z3 13時台 n 積み増し run356A–C — "
    "rank 第153回 NEXT run353 は bench 第152回/falsify 第163回/bench 第153回で "
    "run353/354/355 済みのため続行枠 run356, 同測定法 n=20 × 3 + landing control, "
    "別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, "
    "13:51:00–13:51:11 JST, 全 80/80 200, host load1 28.27→26.28 (13:51 uptime 実測, "
    "gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
    "cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run356A cold 5/20 散発クラスタ "
    "(1.0196s pos3 / 1.1451s pos5 / 1.2344s pos9 / 1.5102s pos11 / 1.2344s pos14 — "
    "中盤中心の散発配置, warm 群 p50 60.3ms max 1510.2ms) p50 60.3ms / run356B cold 0/20 "
    "p50 49.6ms max 72.7ms / run356C cold 0/20 p50 51.4ms max 83.7ms, control "
    "(kotobase.net/signup) cold 0/20 p50 48.9ms max 114.1ms 完全静穏で control 分離成立、"
    "cold 群は search 側に局在。run356A 散発 5/20 は B/C 0/20 + control 0/20 で即消滅し"
    "「帯内 1 窓即消滅」散発クラスタ継続 (run353A 5/20 -> run354A 2/20 -> run355A 1/20 "
    "-> 本 tick run356A 5/20 の再上振れ, heavy>=6/20 は再達せず run331A 9/20 heavy 型は"
    "非再現継続)。13時台 (9/7) 通算 = falsify run351 (4/60) + bench run352 (2/60) + "
    "bench run353 (5/60) + falsify run354 (2/60) + bench run355 (1/60) + 本 tick run356 "
    "(5/60) = 19/360 (~5.3%) の 6 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。"
    "secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
    "13時台 n 積み増し続行、次 run ID は run357 使用)\n"
)
lines.insert(iter_idx, evi)

# Add iteration log entry at top of iter log (just after header line).
iter_entry = (
    "- 2026-09-07: cosientist 第124回。13:48 JST tick。HEAD 6bdf6ff = bench 第153回 "
    "(13:40, K-Z3 13時台 run355 cold 1/60) = remote net-kotobase/main 一致 (git fetch + "
    "rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み; terminal "
    "foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 "
    "(/, /signup; pre-run + 本 tick 実測 search.kotobase.net/search 200 / "
    "kotobase.net/signup 200)。host load1 28.27 (13:51 uptime 実測, gate 7.5 大幅超過) のため "
    "local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 "
    "artifact) — true progressive NEXT は bench 第153回 (iter-log, 13:40)「K-Z3 現在時刻帯 "
    "13時台 n 積み増し続行、次 run ID は run356 使用」の run356 枠を本 tick 実施 (13時台 "
    "6 セット目, falsify 第162回 run351 + bench 第151回 run352 + bench 第152回 run353 + "
    "falsify 第163回 run354 + bench 第153回 run355 済みの積み増し続行)。run356 計測 "
    "(同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint "
    "search.kotobase.net/search?q=test, 13:51:00–13:51:11 JST, 全 80/80 200): "
    "cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run356A cold 5/20 (1.0196s/1.1451s/"
    "1.2344s/1.5102s/1.2344s 散発クラスタ pos3/5/9/11/14) p50 60.3ms max 1510.2ms / "
    "run356B cold 0/20 p50 49.6ms max 72.7ms / run356C cold 0/20 p50 51.4ms max 83.7ms, "
    "control (kotobase.net/signup) cold 0/20 p50 48.9ms max 114.1ms 完全静穏で control "
    "分離成立、cold 群は search 側に局在。run356A 散発 5/20 は B/C 0/20 + control 0/20 で"
    "即消滅し「帯内 1 窓即消滅」継続 (run353A 5/20 -> run354A 2/20 -> run355A 1/20 -> 本 "
    "tick run356A 5/20 の再上振れ, heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現"
    "継続)。13時台 (9/7) 通算 = falsify run351 (4/60) + bench run352 (2/60) + bench run353 "
    "(5/60) + falsify run354 (2/60) + bench run355 (1/60) + 本 tick run356 (5/60) = 19/360 "
    "(~5.3%) の 6 セット中位帯候補。qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist "
    "実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify "
    "しない限り行わない (反証が先), K-Z2 は発火交互作用方向非一貫で介入保留, K-Z3 は観測継続, "
    "K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。status 判定は "
    "rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し続行、次 "
    "run ID は run357 使用)\n"
)
lines.insert(iter_idx + 1, iter_entry)

with open(p, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("OK inserted; evi at line", iter_idx + 1, "iter at line", iter_idx + 2)