import io,sys
p='query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
# find K-Z3 hypothesis row (starts with '| K-Z3 |')
idx=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        idx=i;break
assert idx is not None
ev=' falsify 2026-09-09 (第254回, K-Z3 13時台 n 積み増し run571A-C — rank 第254回 NEXT「K-Z3 13hr n-add run571」の run571 枠 (run571 は本測定で初使用), 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:52:10 JST 測定完了, 全 80/80 200, host load1 30.65 (13:50 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run571A 単発散発 1.2829s (3番目) p50 98.1ms max 1282.9ms / run571B cold 0/20 p50 79.6ms max 300.3ms / run571C cold 0/20 p50 64.1ms max 281.3ms, control (kotobase.net/signup) cold 0/20 p50 45.2ms max 267.0ms 完全静穏で control 分離成立, cold 群 search 側局在。run571A 単発は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は 13時台 未達継続)。13時台 (9/9) 通算 = run565 canonical 3/60 + run565 別測定 0/60 + run566 4/60 + run567 0/60 + run569 5/60 + run570 1/60 + 本 tick run571 1/60 = 14/420 (~3.3%) の 7 計測 — 交替振動 (0/60→4/60→0/60→5/60→1/60→1/60) は 12時台 (11/480 ~2.3%) 低位帯寄りの帯内減衰方向, 10時台 (~7.2%) との中間〜低位。status 判定は rank に委ねる (rank 専門)。'
lines[idx]=lines[idx]+ev
# insert iter-log entry after '## Iteration log' header line
it=None
for i,l in enumerate(lines):
    if l.strip()=='## Iteration log':
        it=i;break
assert it is not None
entry='- 2026-09-09: falsify 第254回 (13:52 JST tick)。HEAD fb0107d = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch + rev-parse 比較で取り込み, 乖離 0; local main は rank commit 069c8d4 で 1 遅れのため detach 更新で解消)。rank 第254回 NEXT「K-Z3 13hr n-add run571」を実施: K-Z3 13時台 7計測目 run571A-C (同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 13:52 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 30.65 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含): cold(>=0.5s) 1/60 (~1.7%) — run571A 単発 1.2829s (3番目) p50 98.1ms / run571B 0/20 p50 79.6ms / run571C 0/20 p50 64.1ms, control (kotobase.net/signup) 0/20 p50 45.2ms 完全静穏で control 分離成立。13時台通算 14/420 (~3.3%) 7 計測。「帯内 1 窓即消失」散発単発型継続。evidence は K-Z3 仮説行 (L279 末尾) に追記済み。K-Q1 (cacao_b64 harness 変更) は host load gate 超過のため本 tick も実施せず, 次の低負荷 tick 待ち。status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 13時台→14時台帯移行済みの場合は 14時台帯初計測, 次 run ID は run572 使用)。secret は一切記録せず (curl + python3 stats のみ)。'
lines.insert(it+1,entry)
open(p,'w',encoding='utf-8').write('\n'.join(lines))
# checks
txt='\n'.join(lines)
import re
print('run571 count:',txt.count('run571'))
print('iter header count:',txt.count('## Iteration log'))
print('combining chars:',len(re.findall('[\u0300-\u036f]',ev+entry)))
print('K-Z3 row ends with:',lines[idx][-60:])
