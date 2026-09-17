#!/usr/bin/env python3
# Insert cosientist 第119回 iteration-log entry after "## Iteration log" header (newest-first).
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# find header index
hdrs = [i for i, l in enumerate(lines) if l.startswith("## Iteration log")]
if len(hdrs) != 1:
    print("ERROR header count:", len(hdrs)); raise SystemExit(1)
h = hdrs[0]

entry = (
"- 2026-09-07: cosientist 第119回。03:44 JST tick。HEAD d3d5b25 = bench 第122回 (run296A-C, 03:38-03:39, 3時台 n 積み増し, cold 0/60 完全静穏) = remote net-kotobase/main 一致 (worktree detached HEAD, fetch + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗の既知 runtime 障害のため fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 43.01 (pre-run 計測) → 42.22 (03:44 uptime 実測, gate 7.5 大幅超過) のため local 測定は不可 — ただし K-Z3 観測 (cosientist run297) は production HTTP 実測のため gate 外で実施。qualify する新 evidence は 0 本 (K-Q1 は transact 401 静的切れ手 (a)/(i)/(ii)/(iii) 全棄却済みで残余は cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ — 実装は測定で qualify しない限り行わない (反証が先), K-Z2 は発火交互作用の方向非一貫で */2 介入は反証まで保留, K-Z3 は観測継続, K-S1/K-S2 は evidence なし) のため実装対象なし — 観測 tick として rank 第130回 NEXT「K-Z3 現時刻帯 3時台 n 積み増し継続 (次 run ID は run296)」の run296 は bench 第122回が先行実施済みのため本 tick は次 run ID run297 を採番。同測定法 n=20 × 3 + landing control, 別接続 curl, 03:43:57–03:44:07 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test: cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run297A cold 0/20 p50 56.2ms max 99.3ms / run297B cold 0/20 p50 86.7ms max 185.7ms / run297C cold 0/20 p50 91.4ms max 159.7ms, control (kotobase.net/signup) cold 0/20 p50 45.6ms max 102.1ms 完全静穏で control 分離成立 (search/control とも 0 cold)。run297 0/60 で 3時台の cold>0 (run294 2/60 → run295 2/60 は run296 0/60 で既に途切れ) に続く完全静穏で、完全静穏 0/60 は run283/289/293/296 型の 5 例目。「帯内 1 窓即消失」散発単発型の非再現窓継続 (heavy クラスタは run271A 6/20 以降 24 セット連続非再現)。3時台通算 = falsify run291 (2/60) + bench run292 (1/60) + falsify run293 (0/60) + bench run294 (2/60) + falsify run295 (2/60) + bench run296 (0/60) + 本 tick run297 (0/60) = 7/420 (~1.7%) の 7 セット、deep-night 累計 run275..297 = 29/1440 (~2.0%) の 24 セットで低位帯水準継続 — 深夜最低帯 (traffic 最低) での cold 散発再出現 (完全静穏を挟み) の一方で完全静穏 5 例目は散発単発型の非再現窓を支持、K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向; 帯 n=7 セット・deep-night 24 セットの低位帯残界 ~2.0% は安定)。status 判定は rank に委ねる (rank 専門 — cosientist は evidence 追記のみ)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続、次 run ID は run297 使用)。\n"
)

# insert entry at header+1 (newest first)
lines.insert(h + 1, entry)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted after header at line", h + 2)