import io

path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(path,encoding='utf-8') as f:
    d=f.read()

marker='- 2026-09-09: bench 第237回'
mi=d.find(marker)
nl=d.find('\n', mi)
if nl==-1: nl=len(d)

new_entry=("- 2026-09-09: rank 第234回。04:04 JST tick。HEAD 799a736 = bench 第237回 (03:55, "
"K-Z3 3時台 run530 cold 5/60 ~8.3%) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; "
"detached HEAD のため fetch 系で取込, worktree diff HEAD -- query-cosientist.md 空 事前確認)。pre-run monitor NEXT"
"「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 "
"(bench 第237回 NEXT「K-Z3 3時台 n 積み増し続行, 次 run ID は run531 使用」)。rank 第233回 (03:25) 以降の新規確定 evidence は "
"K-Z3 3時台 2 本: falsify 第236回 run529 (03:47-49, cold 1/60 ~1.7%) + bench 第237回 run530 (03:54, cold 5/60 ~8.3%) -> "
"3時台 (9/9) 通算 16/360 ~4.4% 6 セット連続 cold>0 確定 (2時台 16/120 ~13.3% から 3時台深夜最低帯に移行後も連続発現 = "
"K-Z3 traffic 依存説への反証材料継続, 帯 n=6 で帯水準確定・機構判断には未達)。status 遷移なし (transition 要件を満たす判定的 "
"evidence なし: K-Z3 は open 継続・深夜帯継続観測で「帯内 1 窓即消失」散発単発/ペア型が 3時台 6 セット継続, heavy>=6/20 は "
"run271A 以降非再現; K-Q1 は transact 401 解決待ちで cosientist 担当, K-S1/K-S2 は host load gate 超過で evidence なし, "
"K-Z2 は K-Z3 の帯別分布確定待ち)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし "
"(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 - 3時台 6 セット ~4.4% は深夜帯平坦パターンの帯内振幅内で優先度逆転なし)。"
"現時刻 04:04 は 4時台に移行済み (3時台帯水準は n=6 で概ね確定, 9/8 4時台 run421/422 低静穏 2-set に対し日差検証)。"
"live smoke 200 (/, /signup, search)。host load1 33.43 (04:03 pre-run uptime 実測, gate 7.5 大幅超過) は rank 担当は測定せず"
"状態正本更新のみで影響なし。secret は一切記録せず。NEXT: K-Z3 4時台 (現時刻帯) n 積み増し継続, 次 run ID は run531 使用 "
"(- run525..530 消費済みのため)。\n")

new_d = d[:mi] + new_entry + d[mi:]

assert new_d.count('## Iteration log')==1, 'header count != 1'
with io.open(path,'w',encoding='utf-8') as f:
    f.write(new_d)
print('inserted, header count:', new_d.count('## Iteration log'))
print('rank 第234回 present:', 'rank 第234回' in new_d)
print('marker still present:', marker in new_d)