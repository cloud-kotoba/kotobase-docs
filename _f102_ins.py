# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

falsify_line = (
"falsify 2026-09-06 (第102回, K-Z3 18時台 n 積み増し run233A–C, "
"同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, "
"18:46:37–18:47:41 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 80.91–97.20 (18:46 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 "
"— rank 第98回 NEXT「K-Z3 現在時刻帯 18時台 n 積み増し継続」に従い 18時台で実施; "
"run230/231/232 使用済みのため run233): "
"cold(>=0.5s) 2/2/1 per 20 = 5/60 (~8.3%) — run233A cold 2/20 (0.943s 15番目 / 0.792s 17番目) p50 91.6ms warm_p50 85.2ms / "
"run233B cold 2/20 (0.764s 1番目 / 0.775s 3番目) p50 140.9ms warm_p50 137.1ms / "
"run233C cold 1/20 (1.310s 16番目) p50 120.9ms warm_p50 114.8ms, "
"control (kotobase.net/signup) cold 2/20 (0.999s / 0.789s) p50 271.7ms max 998.7ms — "
"※本 tick は host load 高騰 (97) tick で search/control とも warm p50 全体的上振れ (search 85–137ms, control 271.7ms) かつ "
"control にも cold 2 件 (0.999s/0.789s) が出現し control 分離は borderline not-separated 傾向 "
"(search 側 cold 5/60 自体は閾値決定的だが control にも同規模 cold が出たため機構判定としては弱い). "
"run233A/B/C の cold は各 run 内散発配置で B/C 0/20 という「帯内1窓即消失」ではなく 3 run 跨いで弱く連続 (run232A 9/20 heavy burst の weak 続行) — "
"ただし control 向け cold も同格で host load 由素の一般化遅延と整合し実在 cold-start 特有とは判定できない. "
"18時台通算 (run230 1/60 + run231 3/60 + run232 9/60 + 本 tick 5/60) で 18/240 (~7.5%) — "
"run232A 単一窓 heavy (9/60) に加え本 tick が 3 run 跨ぎ弱連続 cold で上振れ、run232〜run233 と 18時台内の独立 2 セットで "
"cold 群がみられ「帯内1窓即消失」パターンは 18時台では成立しない低位帯からの中間帯への弱い遷移方向 (host load 高騰混入で決定的でない余裕). "
"status 判定は rank に委ねる (rank 専門).\n"
)

s = open(PATH, encoding='utf-8').read()
anchor = '## Iteration log\n'
assert s.count(anchor) == 1, f"anchor count={s.count(anchor)}"
s = s.replace(anchor, falsify_line + anchor, 1)
open(PATH, 'w', encoding='utf-8').write(s)
print("OK inserted falsify run233 evidence before Iteration log")