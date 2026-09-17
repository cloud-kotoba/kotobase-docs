#!/usr/bin/env python3

path = 'query-cosientist.md'
data = open(path, encoding='utf-8').read()

entry = (
"- 2026-09-09: rank 第238回。05:42 JST tick。HEAD b7c7452 = remote bench_fetch/main・net-kotobase/main (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (bench 第243回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 5時台 n 積み増し続行, 次 run ID は run538 使用)」)。rank 第237回 (05:18) 以降の新規確定 evidence: falsify 第238回 run538 (05:34-05:35, K-Z3 5時台 4セット目 n 積み増し) が worktree に UNCOMMITTED で到着（falsify tick は計測+iter/evidence 追記まで完了し commit 未着, host load1 41-63 で commit が遅延/失敗と判断, ~2分待機+2回 re-fetch で commit 未着のため本 rank tick が evidence を fold して復旧）。falsify run538 実測 (同測定法 n=20 x 3 + landing control, cold>=0.5s, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold 1/0/0 per 20 = 1/60 (~1.7%) - run538A 単発 1/20 (pos12 0.8974s) / B,C 0/40 / control 0/20 完全静穏で control 分離成立。5時台 (9/9) 通算 = run535 (0/60) + run536 (2/60) + run537 (3/60) + 本 tick run538 (1/60) = 6/240 (~2.5%) の 4 セット (完全静穏 0/60 → 2/60 → 3/60 → 1/60 へ散発変動, 深夜帯 traffic 最低帯の 5時台静穏低位帯候補方向を弱く継続)。取り込み判定: K-Z3: run538 を fold、status 遷移なし (5時台 6/240 ~2.5% 4セットは帯水準確定・機構判断未達, heavy>=6/20 は 5時台 未達, 深夜帯 ~26-31% 平坦パターンへの遷移は未達 = K-Z3 traffic 依存説 決定的反証/支持に不十分, open 継続)。K-Q1: 変動なし (transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank 測定指示対象外, KV read 内訳初実測滞留継続, 最上位維持)。K-Z2/K-S1/K-S2: evidence なし (変動なし)。新仮説なし (K-Z 系列登録対象なし)。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 維持)。secret は一切記録せず。NEXT: K-Z3 現在時刻帯 5時台 n 積み増し継続 (次 run ID は run539 使用 - run531..538 消費済みのため次セットは run539, 深夜帯最低帯 5時台 4セット 6/240~2.5% の帯水準確定には rank 追加 n 要として継続)。\n"
)

anchor = '## Iteration log\n'
idx = data.find('## Iteration log\n')
if idx < 0:
    raise SystemExit('header not found')
head = data[:idx]
rest = data[idx+len(anchor):]
newdata = head + anchor + entry + rest

open(path, 'w', encoding='utf-8').write(newdata)
wt = open(path, encoding='utf-8').read()
print('HEADER_COUNT', wt.count('## Iteration log'))
print('RANK238_IN', 'rank 第238回' in wt)
print('FALSIFY238_PRESERVED', 'falsify 第238回' in wt)
print('ORDER_OK', wt.find('rank 第238回。05:42') < wt.find('falsify 第238回。05:34'))
print('TYPO_FALSEIFY', 'FALSEIFY' in wt)
print('NEXT_RUN539', 'run539 使用' in wt)