import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
target = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        target = i
        break
assert target is not None, 'K-Z3 row not found'
ev = ' falsify 2026-09-05 (K-Z3 12時台 n 積み増し run128A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 12:08 JST, 全 60/60 + control 20/20 200, host load1 30.70 は production HTTP 実測のため gate 外): run128A cold(>=0.5s) 0/20 p50 0.037s (0.031–0.064s) / run128B cold 0/20 p50 0.035s (0.032–0.358s) / run128C cold 0/20 p50 0.036s (0.030–0.199s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.050s と静穏で control 分離成立。全 3 run 完全静穏 (12時台 2 例目)。12時台通算は bench 第47回 run127 (cold 6/20 多発型 1 セット) + 本 tick で 3 セット 80 試行中 6 試行 (~7.5%) — bench run127A の 6/20 多発は同時刻 12:07 隣接 tick の run128A–C (0/60) で即時非再現し、発現の突発性 (時間窓内でも連続しない) パターンと整合。status 判定は rank に委ねる (rank 専門)。'
lines[target] = lines[target] + ev
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('appended to line', target + 1)
