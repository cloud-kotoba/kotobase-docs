#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, sys

FN = 'query-cosientist.md'
with io.open(FN, 'r', encoding='utf-8') as f:
    data = f.read()
lines = data.split('\n')

# ---------------------------------------------------------------
# 1. Append evidence at END of K-Z3 row (1-based line 279 -> index 278).
evidence = (
    ' falsify 2026-09-09 (' + chr(0x7B) + '第235回' + chr(0x7D) + ', K-Z3 3時台 n 積み増し run527A' + chr(0x2013) + 'C' +
    ' - run526 済の続行枠,' +
    ' 同測定法 n=20 ' + chr(0x00D7) + ' 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50,' +
    ' 正 endpoint search.kotobase.net/search?q=test, 03:32-03:34 JST, 全 80/80 200,' +
    ' host load1 32.76 (03:34 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外,' +
    ' secret 不含 - curl + python stats のみ):' +
    ' cold(>=0.5s) 3/0/0 per  ' + '20' + ' = 3/60 (~5.0%)' +
    ' - run527A 散発クラスタ 3/20 (1.0520s/1.1712s/1.3082s 散発配置)' +
    ' p50 42.4ms max 1308.2ms / run527B cold 0/20 p50 121.9ms max 322.8ms' +
    ' (host load 高騰上振れ note 但し cold 0) / run527C cold 0/20 p50 43.5ms max 130.2ms,' +
    ' control (kotobase.net/signup) cold 0/20 p50 107.0ms max 272.2ms 静穏で control 分離成立,' +
    ' cold 群 search 側局在.' +
    ' run527A 散発 3/20 は B/C ' + '0/40' + ' + control ' + '0/20' + ' 即消失で「帯内 1 窓即消失」散発クラスタ型継続' +
    ' (falsify run525A 単発 1/20 -> bench run526A 散発 5/20 -> 本 tick 3/20 の散発振幅内,' +
    ' heavy>=6/20 は 3時台未達).' +
    ' 3時台 (9/9) 通算 = falsify run525 (1/60) + bench run526 (5/60) + 本 tick run527 (3/60) =  ̄' +
    '9/180 ~5.0% の 3 セット - 2時台 16/120 ~13.3% から 3時台 (深夜帯 traffic 最低帯) へ移行後も cold>0 継続' +
    ' = K-Z3 traffic 依存説への反証材料継続 (深夜帯 ~26-31% 平坦パターンと整合方向).' +
    ' 帯 n=3 で帯水準確定・機構判断には未達). status 判定は rank に委ねる (rank 専門).'
)
ev_tail = evidence
# row = the giant K-Z3 line; append at very end of line 279 (index 278).
lines[278] = lines[278].rstrip('\r') + ev_tail

# ---------------------------------------------------------------
# 2. Insert iter-log entry right after "## Iteration log" (top = newest).
ilog = (
    '- 2026-09-09: falsify ' + chr(0x7B) + '第235回' + chr(0x7D) + ': 03:34 JST tick (計測 03:32-03:34 JST,' +
    ' HEAD b009c96 = bench ' + chr(0x7B) + '第232回' + chr(0x7D) + ' (03:22, run526) 取込済' +
    ' NEXT フォールバック run527). detached HEAD のため fetch 系で取込 (terminal stdout 空=既知のためファイル書き出し経由)..' +
    ' K-Z3 3時台 n 積み増し run527A-C を実測' +
    ' (同測定法 n=20 ' + chr(0x00D7) + ' 3 + landing control, 別接続 curl, cold>=0.5s,' +
    ' nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 03:34 JST, 全 80/80 200,' +
    ' secret 不含 - curl + python stats のみ):' +
    ' cold(>=0.5s) 3/0/0 per  ̄' + '20' + ' = 3/60 (~5.0%)' +
    ' - run527A 散発クラスタ 3/20 (1.0520s/1.1712s/1.3082s 散発配置) p50 42.4ms' +
    ' / run527B/C cold 0/40, control ' + '0/20' + ' 完全静穏で control 分離成立,cold 群 search 側局在.' +
    ' 「帯内 1 窓即消失」散発クラスタ型継続.' +
    ' 3時台 (9/9) 通算 = falsify run525 (1/60) + bench run526 (5/60) + 本 tick run527 (3/60) =  ̄' +
    '9/180 ~5.0% 3 セット - 2時台 16/120 ~13.3% から 3時台 (深夜帯 traffic 最低帯) へ移行後も cold>0 継続' +
    ' = K-Z3 traffic 依存説への反証材料継続 (深夜帯 ~26-31% 平坦パターンと整合方向).' +
    ' 帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)..' +
    ' status 判定は rank に委ねる (rank 専門)..' +
    ' NEXT: 委ねる (rank 指定優先;フォールバックは K-Z3 現在時刻帯 3時台 n 積み増し続行,' +
    ' 次 run ID は run528 使用 - run525 は falsify ' + chr(0x7B) + '第234回' + chr(0x7D) + ',' +
    ' run526 は bench ' + chr(0x7B) + '第232回' + chr(0x7D) + ', run527 は本 tick が消費済みのため次セットは run528).'
)
iter_anchor = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        iter_anchor = i
        break
if iter_anchor is None:
    print('ERROR: iter anchor not found', file=sys.stderr)
    sys.exit(1)
lines.insert(iter_anchor + 1, ilog)

new = '\n'.join(lines)
with io.open(FN, 'w', encoding='utf-8') as f:
    f.write(new)
print('OK applied')