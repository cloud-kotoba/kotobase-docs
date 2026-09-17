# -*- coding: utf-8 -*-
import io, sys
p = 'query-cosientist.md'
t = io.open(p, encoding='utf-8').read()

entry = '''- 2026-09-07: rank 第129回。03:17 JST tick。HEAD 2668d22 = falsify 第134回 (run293A-C, 03:15-03:16, 3時台 n 積み増し, cold 0/60 完全静穏) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力をファイル書き出し経由で確認)。rank 第128回 (2abc1a1, 03:03, run291 まで fold) 以降の新規確定 evidence は 2 commit、いずれも K-Z3 3時台 n 積み増し: (1) bench 第120回 run292A-C (4989780, 03:09:24-03:09:43, cold 1/60 ~1.7% — run292A 単発散発 0.8127s (19番目 末尾), B/C 0/20 即消失, control cold 0/20 p50 0.0406s max 0.0503s 完全静穏で control 分離成立, cold 群 search 局在), (2) falsify 第134回 run293A-C (2668d22, 03:15-03:16, cold 0/60 完全静穏 — run293A/B/C 全 p50 0.0388-0.0422s, control cold 0/20 p50 0.0389s max 0.0458s 完全静穏, search/control とも 0 cold, run283/289 完全静穏 0/60 型の 3 例目)。取り込み判定: (a) K-Z3: run292 + run293 を取込、3時台通算 = falsify run291 (2/60 ~3.3%) + bench run292 (1/60 ~1.7%) + falsify run293 (0/60 完全静穏) = 3/180 (~1.7%) の 3 セット、deep-night 累計 run275..293 = 25/1200 (~2.1%) の 20 セットで低位帯水準継続。run293 完全静穏 0/60 が 3時台 cold>0 2 セット連続 (run291 2/60 → run292 1/60) を打破し、全セット「帯内 1 窓即消失」散発単発型で heavy クラスタ (run271A 6/20 型) は run271A 以降 20 セット連続非再現。3時台 ~1.7% は 24時台 (18/420 ~4.3%)・1時台 (13/540 ~2.4%)・2時台 (9/480 ~1.9%) と同水準の低〜中位帯候補で、深夜帯 traffic 最低帯 (24/0/1/2/3時台) での cold 散発継続 + 完全静穏混在は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向, deep-night 累計 ~2.1% の低位帯残界が 20 セットで安定)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 3時台 3/180 ~1.7% は帯水準確定・機構判断に至らず, 散発単発 + 完全静穏混在の構図)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・3時台 3/180 ~1.7% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 3時台 ~1.7% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 27.77 (pre-run uptime 実測, gate 7.5 超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。
  NEXT: K-Z3 3時台(現時刻帯) n 積み増し継続 — 現時刻 03:17 は 3時台 (3時台帯 n=3 セット, run291 2/60 run292 1/60 run293 0/60 通算 3/180 ~1.7% の低位帯残界確認方向, 次 run ID は run294)。3時台は完全静穏 (run293) を挟んだ散発単発型で帯水準は概ね見えつつあり追加 n で帯確定へ、時間帯移行後は次の帯初へ (深夜帯 ~26-31% 平坦パターンへの収束か 深夜各帯限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run294 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。

'''

anchor = '## Iteration log\n'
assert anchor in t, 'anchor not found'
idx = t.index(anchor) + len(anchor)
new = t[:idx] + entry + t[idx:]
io.open(p, 'w', encoding='utf-8').write(new)
print('inserted ok, new len', len(new))