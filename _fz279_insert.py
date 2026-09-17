#!/usr/bin/env python3
import io, sys

FN = 'query-cosientist.md'
ANCHOR = 'bench 2026-09-07 (第113回, K-Z3 1時台'
INS = ('falsify 2026-09-07 (第127回, K-Z3 1時台 n 積み増し run279A–C — rank 第122回 NEXT '
       '「K-Z3 1時台 n 積み増し継続」の継続枠 + bench 第113回 (01:26, run278) の次 run ID '
       'run279 使用, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, '
       '01:33–01:34 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, '
       'host load1 63.6→62.0 (01:33/01:34 uptime 実測, gate 7.5 大幅超過) は production '
       'HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = '
       '2/60 (~3.3%) — run279A cold 2/20 (1.9094s 1番目 / 1.0088s 2番目 — 冒頭隣接ペア) '
       'p50 137.0ms max 1.909s / run279B cold 0/20 p50 129.5ms max 208.3ms / run279C cold '
       '0/20 p50 58.0ms max 119.0ms, control (kotobase.net/signup) cold 0/20 p50 93.0ms '
       'max 421.5ms 静穏 (max 421ms は閾値内 1 件の 上振れ) で control 分離成立、cold 群は '
       'search 側に局在。run279A 冒頭ペア 2/20 は B/C 0/20 + control 0/20 で即消失し '
       '「帯内 1 窓即消失」散発単発/ペア型継続 (run275A 2/20 → run276A 2/20 → run277A 2/20 '
       '→ run278A 1/20 → 本 tick 2/20 の散発連続, heavy クラスタは run271A 以降 9 セット'
       '非再現)。※A/B の p50 (129–137ms) は C (58ms)・control (93ms) に対しやや上振れだが '
       'host load 63 high tick の混入可能性で cold 濃度判定 (2/60) には影響なし。1時台通算 '
       '= falsify run275 (2/60) + bench run276 (2/60) + falsify run277 (2/60) + bench '
       'run278 (1/60) + 本 tick (2/60) = 9/300 (~3.0%) で 5 セット連続 cold>0 — 24時台 '
       '(18/420 ~4.3%) と同水準の低〜中位帯候補、深夜帯 1時台 (traffic 最低帯) での cold '
       '連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと'
       '整合方向)。帯 n=5 セットで帯水準確定・機構判断には rank 追加 n を要する。status '
       '判定は rank に委ねる (rank 専門)。')

with io.open(FN, encoding='utf-8') as f:
    lines = f.readlines()

idx = None
for i, ln in enumerate(lines):
    if ln.lstrip().startswith(ANCHOR):
        idx = i
        break
if idx is None:
    print('ANCHOR NOT FOUND', file=sys.stderr)
    sys.exit(2)

# insert new line after anchor line
newline = ' ' + INS + '\n'
lines.insert(idx + 1, newline)

with io.open(FN, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('ok idx=%d' % (idx + 1))