import io
p='query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
ev='  falsify 2026-09-15 (第256回, K-Z3 23時台 n 積み増し run635A-C — rank 第278回 NEXT run635 枠を消化, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 23:38-23:41 JST, 全 120/120 200, 正 endpoint search.yataverse.com/search?q=test, host load1 87-112 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): cold(>=0.5s) 7/0/0 per 20 = 7/60 (~11.7%) — run635A 早先頭集中 cluster 7/20 (831-1875ms, 1-11番目に偏在, 3番目以降散発) p50 271.4ms warm_p50 228.4ms / run635B cold 0/20 p50 111.6ms / run635C cold 0/20 p50 201.1ms, control (kotoba.cloud/) cold 2/60 単発 2 件 (973ms/656ms 別セット) で分離弱い leaning-separated — 23時台 (9/15) 通算 = run622 6/60 (~10.0%) + run635 7/60 (~11.7%) = 13/120 (~10.8%) 中位帯。「帯内 1 窓即消失」散発型継続だが control 単発 cold 同時で K-Z4 日次分解能評価時は control 分離の弱さを注記。status 判定は rank に委ねる。'
# find K-Z3 hypothesis rows (giant single lines)
idxs=[i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert idxs, 'no K-Z3 row'
i=idxs[-1]
lines[i]=lines[i]+ev
# iter-log insert after '## Iteration log'
j=[k for k,l in enumerate(lines) if l.strip()=='## Iteration log'][0]
it='- 2026-09-15: falsify 第256回 (23:38 JST tick)。HEAD 20160b1 = fetch 後 net-kotobase/main 先端一致 (fetch + rev-parse 比較, 乖離 0; detached HEAD; terminal foreground stdout 空 = 既知のため状態確認はファイル書出経由)。host load1 87.39-111.65 (23:35 pre-tick 実測, gate 7.5 大幅超過, production HTTP 実測のため gate 外)。rank 第278回 NEXT「K-Z3 23時台 (9/15) n 積み増し run635」に従い production HTTP 実測で run635A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 23:38-23:41 JST, 全 120/120 200, 正 endpoint search.yataverse.com/search?q=test): cold(>=0.5s) 7/0/0 per 20 = 7/60 (~11.7%) — run635A 早先頭集中 cluster 7/20 (831-1875ms) / B 0/20 p50 111.6ms / C 0/20 p50 201.1ms, control (kotoba.cloud/) cold 2/60 単発 2 件で分離弱い leaning-separated。23時台 (9/15) 通算 = 13/120 (~10.8%) 中位帯。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し継続)。secret 不含 (curl + python3 stats のみ)。'
lines.insert(j+1,it)
open(p,'w',encoding='utf-8').write('\n'.join(lines))
# verify single occurrence
c=open(p,encoding='utf-8').read().count('run635A-C — rank')
print('ev_count',c,'itlog_ok',any('falsify 第256回 (23:38' in l for l in lines))
