#!/usr/bin/env python3
# append falsify 第108回 run242 evidence to K-Z3 hypothesis row (line whose first cell is K-Z3)
INS = " falsify 2026-09-06 (第108回, K-Z3 20時台 n 積み増し run242A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 20:31:05–20:31:29 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 23.11 (pre-run, gate 7.5 超過) は production HTTP 実測のため gate 外 — rank 第105回 NEXT「K-Z3 20時台 n 積み増し継続」に従い 20時台 3セット目で実施; bench 第96回 run241 (20:26) 使用済みのため run242): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run242A 末尾単発 1 件 (1.015s, 20番目) p50 59.4ms / run242B 0/20 p50 56.3ms max 182.9ms / run242C 0/20 p50 56.6ms max 112.5ms, control (kotobase.net/signup) cold 0/20 p50 74.9ms max 141.6ms 静穏で control 分離成立、cold 群は search 側に局在。run242A 末尾単発は B/C 0/20 で即消失し run241A/B (20:26 末尾単発 2 件) に続く「帯内散発単発即消失」型で「帯内 1 窓即消失」パターン継続 (run239A 冒頭集中型は非再現)。20時台通算 (bench run239 3/60 + falsify run239 0/60 + falsify run240 0/60 + bench run241 2/60 + 本 tick 1/60) 6/240 (~2.5%) 低位帯残界確定方向継続 — 日中低位帯分布パターン (13–17時台 ~2-5%) と整合し traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。"

path = 'query-cosientist.md'
lines = open(path).read().split('\n')
# find the hypothesis table row that starts with '| K-Z3 |'
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
        break
assert idx is not None, 'K-Z3 row not found'
# append INS at end of that row line
lines[idx] = lines[idx] + INS
open(path, 'w').write('\n'.join(lines))
print('appended to line', idx + 1)