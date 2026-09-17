p='query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
# find K-Z3 hypothesis row (| K-Z3 |) and iteration log header
kz3=None; hdr=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |') and kz3 is None:
        kz3=i
    if l.strip()=='## Iteration log' and hdr is None:
        hdr=i
assert kz3 is not None and hdr is not None, (kz3,hdr)
ev=' cosientist 2026-09-10 (第153回, K-Z3 1時台帯初計測 (9/10) run575A-C — iter-log HEAD 連鎖 (rank 第257回 NEXT「K-Z3 19時台 n 積み増し run574」は falsify 第259回が run574 (23時台帯初 9/60) で消化済み, pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は現 1時台のため帯待機不可能 — falsify run275/cosientist run105 precedent に従い現時刻帯 1時台帯初計測として実施, 次 run ID は run575 使用), 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 01:43:51–01:44:12 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 28.89–26.27 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): cold(>=0.5s) 11/0/0 per 20 = 11/60 (~18.3%) — run575A heavy 散発クラスタ 11/20 (0.8654–1.6110s, p50 0.8654s, max 1.6110s, 1番目から連続・中盤以降も散発) / run575B cold 0/20 p50 46.0ms / run575C cold 0/20 p50 43.8ms, control (kotobase.net/signup) cold 0/20 p50 45.5ms max 339.9ms 完全静穏で control 分離成立 (cold 群は search 側に局在)。1時台 (9/10) 帯初 ~18.3% は深夜帯高位 (9/9 23時台帯初 15.0%・19時台 16.7% 群) に次ぐ水準で K-Z3 traffic 依存説の深夜帯高位方向と整合 (n=1 セットのため帯水準確定には追加 n 要, heavy>=6/20 は run575A で再現)。status 判定は rank に委ねる (rank 専門)。'
lines[kz3]=lines[kz3].rstrip('\n')+ev+'\n'
entry='- 2026-09-10: cosientist 第153回 (01:41 JST tick)。HEAD 3014558 = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため fetch + rev-parse 比較手順)。rank 第257回 NEXT「K-Z3 19時台 n 積み増し run574」は falsify 第259回 (23:23) が run574 (23時台帯初 9/60) で消化済み・現 1時台のため 19/23時台待機不可能 — フォールバック (production HTTP 実測) で K-Z3 1時台帯初計測 (9/10) run575A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 01:43:51–01:44:12 JST, 全 80/80 200): cold(>=0.5s) 11/60 (~18.3%) — run575A heavy 散発クラスタ 11/20 (0.8654–1.6110s, p50 0.8654s) / run575B 0/20 p50 46.0ms / run575C 0/20 p50 43.8ms, control (kotobase.net/signup) cold 0/20 p50 45.5ms 完全静穏で control 分離成立。1時台 (9/10) 帯初 ~18.3% は深夜帯高位群 (23時台 15.0%・19時台 16.7%) に次ぐ水準, heavy>=6/20 クラスタは run574A (7/20) に続く連続再現で K-Z3 traffic 依存説の深夜帯高位方向を支持 (帯水準確定には 1時台追加 n 要)。host load1 28.89–26.27 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外。K-Q1 (cacao_b64 harness 変更) は host load gate 超過のため本 tick も実施せず, 次の低負荷 tick 待ち。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 1時台 n 積み増し, 次 run ID run576)。secret は一切記録せず (curl + python3 stats のみ)。'
lines.insert(hdr+1, entry)
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print('OK kz3_line=%d hdr=%d'%(kz3+1,hdr+1))
