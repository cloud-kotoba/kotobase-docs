import re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt=open(p,encoding='utf-8').read()
lines=txt.split('\n')
kz=-1
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'): kz=i; break
assert kz>=0, 'K-Z3 line not found'
ev=' falsify 2026-09-09 (第253回, K-Z3 13時台 n 積み増し run569A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 13:34:50–13:35:25 JST, 全 80/80 200): cold(>=0.5s) 5/60 (~8.3%) — run569A 2/20 p50 297.4ms p95 1194.8ms / run569B 2/20 p50 297.2ms p95 1272.8ms / run569C 1/20 p50 193.2ms, control (kotobase.net/signup) 0/20 p50 229.9ms max 431.3ms 完全静穏で control 分離成立。13時台通算 12/300 (4.0%) — run565 (canonical 3/60) + run566 (4/60) に続き帯内減衰せず中位~高め帯持続、日中帯 traffic 依存説支持方向。status 判定は rank に委ねる。'
assert 'run569' not in txt, 'run569 already present'
lines[kz]=lines[kz]+ev
txt='\n'.join(lines)
marker='## Iteration log'
mi=txt.index(marker)+len(marker)
iter='- 2026-09-09: falsify 第253回 (13:36 JST tick)。HEAD 289273c = fetch 後 net-kotobase/main 先端一致 (rev-parse 比較, 乖離 0)。rank 第253回 NEXT 指定なしのためフォールバック: K-Z3 13時台 n 積み増し run569A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 13:34:50–13:35:25 JST, 全 80/80 200, host load1 14.89 は production HTTP 実測のため gate 外): cold(>=0.5s) 5/60 (~8.3%) — run569A 2/20 (p95 1194.8ms) / run569B 2/20 (p95 1272.8ms) / run569C 1/20, control (kotobase.net/signup) 0/20 p50 229.9ms max 431.3ms 完全静穏で control 分離成立。13時台通算 12/300 (4.0%)。初回誤 endpoint (kotobase.net/api/search 404, 別測定として不採用) 後 正 endpoint (search.kotobase.net/search?q=test) で実施。evidence は K-Z3 仮説行に追記済み。K-Q1 (cacao_b64 harness 変更) は host load1 14.89 (gate 7.5 超過) のため local 測定不可, 次の低負荷 tick 待ち。status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。secret は一切記録せず (curl + python3 stats のみ)。\n'
txt=txt[:mi]+'\n'+iter+txt[mi:]
open(p,'w',encoding='utf-8').write(txt)
print('ok kz_line',kz+1,'run569_count',txt.count('run569'))
