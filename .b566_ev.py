import sys
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
ev=' falsify 2026-09-09 (第252回, K-Z3 13時台 n 積み増し run566A–C — falsify/bench run565 (13:09, 帯初 falsify 0/60 + bench 3/60) 済の続行枠 (falsify 第251回 NEXT「フォールバックは K-Z3 13時台 n 積み増し」どおり, run566 は未使用を pre-run grep 確認済み), 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:17:40–13:18:03 JST, 全 80/80 200, host load1 36.74 (13:16 pre-run monitor, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) — run566A 散発 3/20 (0.5193s/1.2122s/1.4272s) p50 126.6ms / run566B 単発 1/20 (1.7934s) p50 110.5ms / run566C cold 0/20 p50 155.4ms, control (kotobase.net/signup) cold 1/20 (0.6303s 単発) p50 159.7ms で非静穏 control — query 4/60 (~6.7%) vs control 1/20 (5.0%) は同水準で control 分離不成立 (判別弱い), 悪化時即中止基準 4xx/エラーなし。13時台通算 = falsify run565 0/60 + bench run565 3/60 + 本測 4/60 = 7/180 (~3.9%) — 12時台 8セット 11/480 (~2.3%) から上振れ方向, 10時台 ~7.2% と 12時台の中間。status 判定は rank に委ねる (rank 専門).'
lines=open(p,encoding='utf-8').read().split('\n')
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        lines[i]=l+ev
        break
else:
    sys.exit('no K-Z3 line')
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print('inserted')
