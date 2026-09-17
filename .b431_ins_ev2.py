#!/usr/bin/env python3
# Append run431 evidence to K-Z3 evidence row (before "## Iteration log" header).
fn='query-cosientist.md'
txt=open(fn,encoding='utf-8').read()
anchor="\n## Iteration log"
add=" bench 2026-09-08 (第190回, K-Z3 7時台帯初計測 run431A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl,cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 07:01-07:02 JST, 全 80/80 200, host load1 ~22-28 (pre-run, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + awk stats のみ): cold(>=0.5s) 1/0/0 per  ​20 =  1/60 (~1.7%) - run431A 単発散発 1/20 (1.431s, p50 50.5ms, max 1431.4ms) / run431B cold 0/20 p50 44.8ms max 117.8ms / run431C cold 0/20 p50 40.8ms max 133.7ms, control (kotobase.net/signup) cold  ​0/20 p50 40.8ms max 144.6ms 完全静穏で control 分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続 (run428A/429A/430A 単発 → 本 tick A 単発, heavy>=6/20 は run413A 以降非再現継続)。7時台 (9/8) 帯初計測 cold  ​1/60 ~1.7% - 6時台 (6/360 ~1.7%) に続く朝帯境低位帯継続で深夜帯→朝帯境静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし,帯水準確定は rank 判定を要る)。status 判定は rank に委ねる (rank 専門)。"
add=add.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
assert txt.count(anchor)==1, "anchor not unique"
new=txt.replace(anchor, add+anchor)
open(fn,'w',encoding='utf-8').write(new)
print("inserted run431 evidence ok")