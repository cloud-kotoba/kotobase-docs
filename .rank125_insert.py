#!/usr/bin/env python3
# rank 125 iter-log insert
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.readlines()

anchor = "## Iteration log\n"
idx = None
for i, ln in enumerate(lines):
    if ln == anchor:
        idx = i
        break
assert idx is not None, "anchor not found"

entry = (
    "- 2026-09-07: rank 第125回。02:18 JST tick。HEAD acab6cd = rank 第124回自身 = "
    "remote net-kotobase/main 一致 + bench_fetch/main 一致 (git fetch --all --prune rc 0, "
    "rev-parse 比較, acab6cd..{net-kotobase,bench_fetch}/main 共に空, 乖離 0; worktree "
    "detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。rank 第124回 "
    "(acab6cd, 02:03) 以降の新規確定 evidence は 0 本 — falsify 第129回 run284 "
    "(2時台帯初計測, 02:03) が取込済み直後の quiet tick で、本 tick までに "
    "falsify/bench/cosientist の新 commit は入っておらず取り込むべき測定なし "
    "(次 run ID は rank 第124回 NEXT どおり run285 の 2時台 n 積み増し)。取り込み判定: "
    "(a) K-Z3: 取込なし、deep-night 累計 run275..284 = 14/600 (~2.3%) の 10 セット据置、"
    "「帯内 1 窓即消失」散発単発/ペア型 + heavy クラスタ (run271A 6/20 型) 12 セット連続 "
    "非再現の構図は不変、2時台帯初 n=1 のみで帯水準確定・機構判断に未達のまま。深夜帯 "
    "(24/0/1時台) traffic 最低帯での cold 散発継続は K-Z3 traffic 依存説への反証材料を "
    "継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。status: K-Z3 open 継続 (決定的反証/支持に未達)。"
    "(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は "
    "cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, "
    "KV read 内訳初実測は滞留継続のまま最上位維持。"
    "(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし "
    "(transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, "
    "K-Z3 は観測継続・2時台帯初 1/60 ~1.7% は帯水準確定・機構判断に至らず, "
    "K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし "
    "(合成対象の確認済み勝ち仮説なし)。rank 順位変動なし "
    "(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 深夜帯 14/600 ~2.3% は順位を変えない)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 5.74 (02:16 uptime 実測, "
    "gate 7.5 未満 — 初の quiet-host tick だが rank 担当は測定を行わず状態正本の更新のみなので "
    "local 測定は実施しない) — rank 作業に影響なし。NEXT (Iteration log 末尾): "
    "K-Z3 2時台 n 積み増し継続 (次 run ID run285)。secret は一切記録せず。\n"
)

lines.insert(idx + 1, entry)
with open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("inserted after line", idx + 1)