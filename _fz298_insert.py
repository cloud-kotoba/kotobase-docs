#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
path = 'query-cosientist.md'
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')
# anchor: the bench run296 evidence line (last K-Z3 evidence entry before Iteration log)
anchor = 'bench 2026-09-07 (第122回'
idx = None
for i, ln in enumerate(lines):
    if ln.startswith(anchor):
        idx = i
        break
if idx is None:
    print('ANCHOR NOT FOUND', file=sys.stderr)
    sys.exit(2)
INS = ('| falsify 2026-09-07 (第136回, K-Z3 3時台(深夜帯) independent n-add run298A–C — '
       'cosientist run297 (在飛, 03:43) とは別の独立 2 回目計測, 同測定法 n=20 × 3 + landing control, '
       '別接続 curl, Tokyo, 03:47:01–03:47:09 JST, 全 80/80 200, 正 endpoint '
       'search.kotobase.net/search?q=test, host load1 41.39 (03:47 uptime 実測, gate 7.5 大幅超過) '
       'は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20 '
       '= 0/60 完全静穏 — run298A 0/20 p50 56.3ms max 123.3ms / run298B 0/20 p50 53.0ms max 165.0ms / '
       'run298C 0/20 p50 43.3ms max 96.0ms, control (kotobase.net/signup) cold 0/20 p50 37.5ms '
       'max 51.2ms 完全静穏で control 分離成立 (search/control とも 0 cold)。run298 全 0/60 完全静穏は '
       '3時台完全静穏 (falsify run293, bench run296 型) を継続する 4 例目で、cosientist run297 '
       '(同帯 independent, 03:43 計測, 別 run 0/60) と合わせ同一 3時台窓で完全静穏 2 セット。'
       '「帯内 1 窓即消失」散発単発型の非再現窓継続 (heavy クラスタは run271A 以降 24 セット非再現)。'
       '3時台通算 (run291 2/60 + run292 1/60 + run293 0/60 + run294 2/60 + run295 2/60 + run296 0/60 '
       '+ 本 tick 0/60) = 7/420 (~1.7%) の 7 セット、deep-night 累計 run275..298 = 29/1440 (~2.0%) '
       'の 24 セットで低位帯水準続位 — 深夜最低帯 (traffic 最低) での完全静穏継続は K-Z3 traffic '
       '依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向)。status 判定は rank に委ねる '
       '(rank 専門)。')
lines.insert(idx + 1, INS)
with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('INSERTED after line', idx + 1)