import sys, re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
t=open(p,encoding='utf-8').read()
marker='## Iteration log\n'
i=t.index(marker)+len(marker)
row='- 2026-09-09: falsify 第248回 K-Z3 12時台 2セット目 run558A-C (bench 第214回 run553 帯初 5/60 済の続行枠, 同測定法 n=20 x 3 + landing control, 別接続 curl, 12:19:58-12:20:31 JST, 全 80/80 200): cold 3/60 (~5.0%) - run558A 散発 2/20 (0.5167s/1.1580s) p50 226.1ms / run558B 0/20 / run558C 単発 1/20 (0.5788s) p50 208.5ms, control 0/20 p50 205.1ms 完全静穏で分離成立。12時台通算 8/120 (~6.7%) 2 セットで 11時台 (~1.5%) 低位帯から再上振れ, 10時台 (~7.2%) 同水準候補。host load1 65.98 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 12時台 n 積み増し継続, 次 run ID は run559 使用)。secret は一切記録せず (curl + python3 stats のみ)。\n'
t=t[:i]+row+t[i:]
open(p,'w',encoding='utf-8').write(t)
print('iter ok')
