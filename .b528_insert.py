#!/usr/bin/env python3
import sys

doc = sys.argv[1]
with open(doc, 'r', encoding='utf-8') as f:
    txt = f.read()
lines = txt.split('\n')

# --- append evidence to K-Z3 table row (anchor: line starting with '| K-Z3 |') ---
kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'

ev = (
    '| bench 2026-09-09 (第233回, K-Z3 3時台 n 積み増し run528A-C, '
    'falsify 第235回 run527 直後の independent 4 セット目, 同測定法 n=20 x 3 + landing control, '
    '別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, '
    '03:41 JST, 全 60/60 search 200 + control 20/20 200, host load1 16.24 (03:41 uptime 実測, '
    'gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): '
    'cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) - run528B 単発散発 1/20 (1.3058s, 単発散発型) '
    'p50 42.6ms max 1305.8ms, run528A/C cold 0/40 (p50 50.5/44.0ms), '
    'control (kotobase.net/signup) cold 0/20 p50 46.0ms max 148.1ms 完全静穏で control 分離成立、'
    'cold 群 search 側局在。run528B 単発は run527 (3/60) から ~7 分後に弱く再現で B 1 窓のみ即消えし'
    '「帯内 1 窓即消失」散発単発型継続 (falsify run525A 単発 1/20, run526A 散発 5/20 の ~30 分圏内再現)。'
    '3時台 (9/9) 通算 = falsify run525 (1/60) + bench run526 (5/60) + falsify run527 (3/60) + '
    '本 tick run528 (1/60) = 10/240 ~4.2% の 4 セット - 2時台 16/120 ~13.3% から 3時台 '
    '(深夜帯 traffic 最低帯) へ移行後も cold>0 継続 = K-Z3 traffic 依存説への反証材料継続 '
    '(深夜帯 ~26-31% 平坦パターンと整合方向)。帯 n=4 で帯水準確定・機構判断には未達 '
    '(K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。'
)
# K-Z3 row does not end with closing '|' — append directly to row-line end
lines[kz3_idx] = lines[kz3_idx].rstrip() + ev

# --- insert iter-log entry right after '## Iteration log' header ---
ilog_idx = None
for i, l in enumerate(lines):
    if l == '## Iteration log':
        ilog_idx = i
        break
assert ilog_idx is not None, 'Iteration log header not found'

entry = (
    '- 2026-09-09: bench 第233回。03:41 JST tick。HEAD c70b179 = remote net-kotobase/main 一致 '
    '(git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, worktree diff HEAD -- '
    'query-cosientist.md 空 事前確認; terminal stdout 空=既知のため状態確認はファイル書出経由)。'
    'pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 '
    'artifact) - true progressive NEXT は iter-log HEAD 連鎖 (falsify 第235回 (03:34, run527) NEXT '
    '「K-Z3 現在時刻帯 3時台 n 積み増し続行, 次 run ID は run528 使用」)。本 tick は run528 を '
    '3時台 n 積み増し (independent 4 セット目) として実施。live smoke 200 (/, /signup, search; '
    'pre-run + 本 tick 実測)。host load1 16.24 (03:41 uptime 実測, gate 7.5 超過) は production '
    'HTTP 実測のため gate 外で実施。K-Z3 3時台 n 積み増し run528A-C 実測 (同測定法 n=20 x 3 + '
    'landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint '
    'search.kotobase.net/search?q=test, 03:41 JST, 全 60/60 search 200 + control 20/20 200): '
    'cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) - run528B 単発散発 1/20 (1.3058s) p50 42.6ms '
    'max 1305.8ms / run528A/C cold 0/40 (p50 50.5/44.0ms), control (kotobase.net/signup) '
    'cold 0/20 p50 46.0ms max 148.1ms 完全静穏で control 分離成立、cold 群 search 側局在。'
    'run528B 単発は run527 (3/60) から ~7 分後に弱く再現し B 1 窓のみで即消え「帯内 1 窓即消失」'
    '散発単発型継続 (falsify run525A 単発 1/20, run526A 散発 5/20 の ~30 分圏内再現)。'
    '3時台 (9/9) 通算 = falsify run525 (1/60) + bench run526 (5/60) + falsify run527 (3/60) + '
    '本 tick run528 (1/60) = 10/240 ~4.2% の 4 セット - 2時台 16/120 ~13.3% から 3時台 '
    '(深夜帯 traffic 最低帯) へ移行後も cold>0 継続 = K-Z3 traffic 依存説への反証材料継続 '
    '(深夜帯 ~26-31% 平坦パターンと整合方向)。帯 n=4 で帯水準確定・機構判断には未達 '
    '(K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。'
    '詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。'
    'NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 3時台 n 積み増し続行, '
    '次 run ID は run529 使用 - run525 は falsify 第234回, run526 は bench 第232回, '
    'run527 は falsify 第235回, run528 は本 tick が消費済みのため次セットは run529)。'
)
# insert as first bullet after header (line ilog_idx+1)
lines.insert(ilog_idx + 1, entry)

with open(doc, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('DONE kz3_idx=%d ilog_idx=%d lines=%d' % (kz3_idx, ilog_idx, len(lines)))