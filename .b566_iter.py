import sys
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
t=open(p,encoding='utf-8').read()
marker='## Iteration log\n'
i=t.index(marker)+len(marker)
row='- 2026-09-09: falsify 第252回 (13:17 JST tick)。HEAD 4de2852 = fetch 後 net-kotobase/main 先端一致 (detached HEAD, fetch+rev-parse 比較, 乖離 0)。rank 第251回 NEXT「K-Z3 13時台帯初計測 run565」は falsify 第251回 (13:09, run565A-C cold 0/60, control 1/20 非静穏) と bench 第215回 (13:09, run565 3/60 別計測扱い) で消化済みのため、フォールバック (production HTTP 実測) で K-Z3 13時台 n 積み増し run566A-C を実施 (同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 13:17:40-13:18:03 JST, 全 80/80 200): cold(>=0.5s) 4/60 (~6.7%) — run566A 散発 3/20 (0.5193s/1.2122s/1.4272s) p50 126.6ms / run566B 単発 1/20 (1.7934s) p50 110.5ms / run566C cold 0/20 p50 155.4ms, control (kotobase.net/signup) cold 1/20 (0.6303s) p50 159.7ms で非静穏 control — query 4/60 vs control 1/20 同水準で control 分離不成立 (判別弱い), 4xx/エラーなし。13時台通算 7/180 (~3.9%) は 12時台 (~2.3%) から上振れ方向, 10時台 (~7.2%) との中間。host load1 36.74 (gate 7.5 超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。K-Q1 (cacao_b64 harness) は host load gate 超過のため本 tick も実施せず。status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 13時台 n 積み増し継続, 次 run ID は run567 使用)。secret は一切記録せず (curl + python3 stats のみ)。\n'
t=t[:i]+row+t[i:]
open(p,'w',encoding='utf-8').write(t)
print('iter ok')
