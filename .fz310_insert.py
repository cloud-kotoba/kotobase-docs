#!/usr/bin/env python3
# -*- coding: utf-8 -*-
path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
INS = (
u" falsify 2026-09-07 (第142回, K-Z3 5時台(深夜帯) n 積み増し run310A\u2013C \u2014 "
u"bench 128 run309 (05:08, 完全静穏 0/60) に続く 5時台 n 積み増し (次 run ID run310), "
u"同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 05:17\u201305:18 JST, "
u"全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 42\u201348 (05:18 uptime 実測, "
u"gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl のみ): "
u"cold(>=0.5s) 1/0/1 per 20 = 2/60 (~3.3%) \u2014 run310A 単発散発 1.4260s (5番目, warm 群 0.04\u20130.07s と交互) "
u"p50 0.053s max 1.426s / run310B cold 0/20 p50 0.051s max 0.117s / run310C 単発散発 0.9563s (9番目) "
u"p50 0.049s max 0.956s, control (kotobase.net/signup) cold 0/20 p50 0.054s max 0.215s 静穏で control 分離成立、"
u"cold 群は search 側に局在。run310A/C 各単発は B 0/20 + control 0/20 で即消失し run309 完全静穏 (0/60) 直後の散発単発再出現 \u2014 "
u"「帯内 1 窓即消失」散発単発型継続 (heavy クラスタ run271A 6/20 型は run271A 以降 35 セット非再現)。"
u"5時台(deep-night) 累計 run275..310 = 39/2160 (~1.8%) の 36 セットで低位帯水準継続、"
u"深夜最低帯での cold 散発再出現 (run309 完全静穏直後) は K-Z3 traffic 依存説への反証材料を続行 "
u"(深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には rank 追加 n を要する。"
u"status 判定は rank に委ねる (rank 専門)。"
)

with open(path) as f:
    lines = f.readlines()
assert '| K-Z3 |' in lines[278], 'anchor check failed'
old = lines[278]
lines[278] = old.rstrip('\n') + INS + '\n'
with open(path, 'w') as f:
    f.writelines(lines)
print('appended ok')