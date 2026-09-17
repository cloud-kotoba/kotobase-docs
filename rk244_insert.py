import re

path = "query-cosientist.md"
with open(path, encoding="utf-8") as f:
    text = f.read()

entry = (
    "- 2026-09-09: rank 第244回。11:03 JST tick。HEAD afd4cc0 = bench 第249回 (10:53, run548 search endpoint 404 で測定破棄・evidence 不採用の記録) = remote net-kotobase/main / bench_fetch/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, terminal stdout 空=既知のため状態確認はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖。rank 第243回 (d471fa9, 10:47) 以降の新規 evidence は 1 本採用 + 1 本破棄: (a) 採用: cosientist 第150回 run547 (K-Z3 10時台 3セット目): cold(>=0.5s) 1/60 (~1.7%) (run547B 単発 1.1717s) , control 0/20 完全静穏分離成立, 全 80/80 200 — 10時台 (9/9) 通算 = run545 6/60 + run546 6/60 + run547 1/60 = 13/180 (~7.2%) の 3 セット: run546 (6/60) から run547 (1/60) への帯内減衰は「帯内 1 窓即消失」散発型と整合し、10時台は 9時台 ~2.1% 低位帯と 16-17時台 ~8.3-10.0% 中高位帯の中間で日中帯への移行を 3 セットで支持 (帯水準は n=3 でほぼ確定方向, 機構判断には未達 — K-Z3 open 継続, fallback 専門のまま)。(b) 破棄: bench 第249回 run548 (10:53) は production search endpoint 404 のため同測定法前提崩壊・測定破棄・evidence 不採用 — 本 tick 11:03 実測で search.kotobase.net/search?q=test = 200, kotobase.net/ = 200, kotobase.net/signup = 200 (live smoke 準拠) に復旧確認済みのため、破棄分は次 tick で同測定法を再開可能。(c) K-Q1: 変動なし — transact 401 動的照合 (cacao_b64 harness 変更) が唯一の残る切れ手で cosientist 実装専任 (host load1 45.99 gate 大幅超過で local harness 測定不可のまま), rank 測定指示対象外, 最上位維持。(d) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。host load1 45.99 (11:02 pre-run 実測, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。NEXT: K-Z3 11時台帯初計測 (search endpoint 復旧 200 確認済み・K-Z3 仮説の元来の対象窓 10:41–11:47 の核心帯で日中帯 traffic 依存説の直接検証のため n 積み増し), 次 run ID は run549 使用 (run548 は bench 第249回の破棄測定として記録済みのため)。\n"
)

anchor_old = "## Iteration log\n## Iteration log\n\n- 2026-09-09: bench 第249回"
anchor_new = "## Iteration log\n\n" + entry + "\n- 2026-09-09: bench 第249回"

if text.count(anchor_old) != 1:
    raise SystemExit("anchor not unique/found: %d" % text.count(anchor_old))
text = text.replace(anchor_old, anchor_new)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK headers:", text.count("## Iteration log"))
