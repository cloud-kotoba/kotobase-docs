import io

p = "query-cosientist.md"
s = io.open(p, encoding="utf-8").read()

assert s.count("## Iteration log") == 1, "header count"
anchor_line = s.split("## Iteration log\n", 1)[1].split("\n", 1)[0]
entry = (
    "- 2026-09-09: rank 第250回。12:53 JST tick。HEAD 5c9a5ad = fetch 後 net-kotobase/main / bench_fetch/main 一致 (乖離 0; detached HEAD のため fetch 系で取込, terminal stdout 空=既知のため状態確認はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第249回 NEXT「K-Z3 12hr-band n-accumulation run559」)。rank 第249回 (a9e5e7f, 12:22) 以降の新規 evidence は 2 本 (ともに K-Z3 12時台): (a) bench 第215回 run559A-C (12:29, 12時台 3セット目): cold 0/60 完全静穏, control 0/20 完全静穏分離成立, 全 80/80 200。ただし本 tick 初回試行は誤 endpoint kotobase.net/search (404) を破棄し正 endpoint で再実施 (run 番号未採番)。 (b) falsify 第249回 run560A-C (12:38, 12時台 4セット目): cold(>=0.5s) 1/60 (~1.7%, run560A 単発 1.2106s), control 0/20 p50 113.7ms 完全静穏分離成立, 全 80/80 200。取り込み判定: 12時台通算 = run553 5/60 + run558 3/60 + run559 0/60 + run560 1/60 = 9/240 (~3.8%) の 4 セット中位帯 — 帯初 run553A 散発クラスタ 5/20 のみの突出で以降 3 セットは 0-3/60 に減衰し「帯内 1 窓即消失」型継続, 帯水準は 11時台 (~1.5% 低位帯) と 10時台 (~7.2% 中位帯) の中間で日中帯 traffic 依存説の帯間勾配と整合するが 4 セットでは帯確定に未達 (K-Z3 open 継続, fallback 専門のまま)。K-Q1: 変動なし — transact 401 動的照合 (cacao_b64 harness 変更) が唯一の残る切れ手で cosientist 実装専任, host load1 31.78 (12:37 pre-run monitor 実測, gate 7.5 大幅超過) で local harness 測定不可のまま, rank 測定指示対象外, 最上位維持。K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence なし)。新仮説なし。evolve 判断なし。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。\nNEXT: K-Z3 12時台 n 積み増し継続 (12時台 4 セット 9/240 ~3.8% の帯水準確定のため n 追加; 実行時刻が 13時台へ移行済みの場合は 13時台帯初計測として実施), 次 run ID は run561 使用 (run553–560 は消費済みのため)。\n"
)
new = s.replace("## Iteration log\n" + anchor_line, "## Iteration log\n" + entry + anchor_line, 1)
assert new != s, "no insert"
io.open(p, "w", encoding="utf-8").write(new)
print("OK inserted; header count:", new.count("## Iteration log"))
