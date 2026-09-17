#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

ev = " bench 2026-09-08 (第195回, K-Z3 8時台帯内 4セット目 n 積み増し run441A–C — rank 第193回 NEXT の run440 枠は falsify 第195回 (8時台帯内 3セット目, cold 2/60) が先行使用のため run441 に読替 (run216/run256/run263/run278 precedent, 同一帯 independent 2計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 08:24–08:29 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 13.5–18.0 (08:23→08:29 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/0/0 per  ̈20 =̈ 1/60 (~1.7%) — run441A 単発 1.4515s (窓内 1 件, p50 51.7ms warm_p50 51.7ms) / run441B cold 0/20 p50 46.6ms max 134.9ms / run441C cold 0/20 p50 42.2ms max 145.6ms, control (kotobase.net/signup) cold 0/20 p50 42.8ms max 128.7ms 完全静穏で control 分離成立,cold 群は search 側に局在。run441A 単発は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (falsify-run440A/B 各単発 に対する独立計測の弱い再現, heavy>=6/20 は run413A 以降非再現継続)。8時台 (9/8) 通算 = bench-run437 (cold 2/60,帯初) + falsify-run438 (cold  ̈1/60) + falsify-run440 (cold  ̈2/60) +本 tick run441 (cold 1/60) =̈ 6/240 (~2.5%) の 4 セット低位帯継続 — 5/6時台 完全静穏 と 7時台 8/360 ~2.2% に続く朝帯境低位帯の遷移継続で 深夜帯→朝帯境静穏方向に整合, 23時台前回帯 (~5.2%) と深夜帯 ~26-31% 平坦パターンとの対比は traffic 依存説の方向支持を維持。status 判定は rank に委ねる (rank 専門)。"

idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 "):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"
lines[idx] = lines[idx].rstrip() + ev

it = "- 2026-09-08: bench 第195回 08:29 JST tick. HEAD 8b7737f = falsify 第195回 (8時台 n-add run440 cold 2/60) = remote net-kotobase/main 一致 ( git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal stdout 不可=既知のため状態確認にはファイル書き出し経由)。live smoke 200 (/, /signup; pre-run + 本 tick 実測 search 200 / landing 200)。host load1 13.5–18.0 (08:29 uptime 実測, gate  ̈7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測 のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale — true progressive NEXT は iter-log HEAD ( bench 第194回, 6ecd75b) の続行枠「K-Z3 8時台 n 積み増し継続 (次 run ID は run440 使用 — run439 枠は試行のみで実測なし)」で, falsify 第195回 (8b7737f) が run440 を実施済みのため 本 tick は独立計測を run441 に読替して実施 (8時台帯内 4セット目)。run441 計測 (同測定法, n=20 × 3 + landing control, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 08:24–08:29 JST, 全 80/80 200): cold(>=0.5s) 1/0/0 per  ̈20 =̈  ̈1/60 (~1.7%) — run441A 単発 1.4515s (p50 51.7ms, B/C 0/20, control 0/20 完全静穏分離成立,cold 群 search 局在,「帯内 1 窓即消失」散発単発型継続)。8時台 (9/8) 通算 = bench-run437 (2/60,帯初) + falsify-run438 (1/60) + falsify-run440 (2/60) + 本 tick run441 (1/60) =̈ 6/240 (~2.5%) の 4 セット低位帯継続。qualify する新 evidence は 0 本 (K-Q1 は残余が cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない, K-Z2 は発火交互作用方向非一貫で介入保留, K-Z3 は観測継続, K-S1/K-S2 は evidence なし) のため cosientist 実装対象なし — 観測 tick。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる ( rank 指定優先;フォールバックは K-Z3 現在時刻帯 8時台 n 積み増し続行,次 run ID は run442 使用 — run441 は本 tick が使用済み, run440 は falsify 使用)。"

h = None
for i, ln in enumerate(lines):
    if ln == "## Iteration log":
        h = i
        break
assert h is not None, "Iteration log header not found"
lines.insert(h+1, it)

out = "\n".join(lines)
open(p, "w", encoding="utf-8").write(out)
print("OK row", idx+1, "ilog_after", h+1)
