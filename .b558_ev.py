import re, sys
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
ev=' falsify 2026-09-09 (第248回, K-Z3 12時台 2セット目 run558A–C — bench 第214回 run553 (12:14, 帯初 cold 5/60) 済の続行枠 (iter-log HEAD NEXT「次 run ID は run558 使用」どおり), 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 12:19:58–12:20:31 JST, 全 80/80 200, host load1 65.98 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): cold(>=0.5s) 2/0/1 per 20 = 3/60 (~5.0%) — run558A 散発 2/20 (0.5167s/1.1580s) p50 226.1ms / run558B cold 0/20 p50 221.3ms max 439.4ms / run558C 単発 1/20 (0.5788s) p50 208.5ms, control (kotobase.net/signup) cold 0/20 p50 205.1ms max 453.1ms 完全静穏で control 分離成立, cold 群 search 側局在。帯初 run553 (5/60) に続き cold>0 で 12時台通算 = run553 5/60 + run558 3/60 = 8/120 (~6.7%) の 2 セット — 11時台 8セット ~1.7% 低位帯から 12時台は 10時台 ~7.2% と同水準への再上振れ方向, 日中帯 traffic 依存説の帯間勾配継続支持。status 判定は rank に委ねる (rank 専門)。'
lines=open(p,encoding='utf-8').read().split('\n')
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        lines[i]=l+ev
        break
else:
    sys.exit('no K-Z3 line')
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print('inserted')
