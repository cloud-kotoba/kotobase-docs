import re

path = 'query-cosientist.md'
text = open(path).read()
lines = text.split('\n')

# 1) K-Z3 hypothesis row (line index ~278, starts with "| K-Z3 |"): append evidence sentence at end of row
kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'
ev = (' cosientist 2026-09-09 (第150回, K-Z3 10時台 3セット目 run547A–C, 同測定法 n=20 × 3 + landing control, '
      '別接続 curl, Tokyo, 10:46–10:48 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, '
      'host load1 107→76 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python3 stats のみ): '
      'cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run547A cold 0/20 p50 133.4ms / run547B cold 1/20 (1.1717s 単発) p50 159.6ms / '
      'run547C cold 0/20 p50 122.9ms, landing control (kotobase.net/signup) cold 0/20 p50 110.9ms 完全静穏で control 分離成立。'
      '10時台通算 (falsify run545 6/60 + bench run546 6/60 + 本測 run547 1/60) = 13/180 (~7.2%) — run545/546 の 2 セット ~10% に続き '
      '第 3 セットは 1/60 単発で帯内変動は残るものの日中帯 (7-17時台) の低位〜中位帯分布と整合, traffic 依存説の方向支持継続。'
      'status 判定は rank に委ねる (rank 専門)。')
lines[kz3_idx] = lines[kz3_idx].rstrip() + ev

# 2) Iteration log: append new entry after the last "- 2026-09-0X:" line
ilog_idx = None
for i, l in enumerate(lines):
    if l.startswith('## Iteration log'):
        ilog_idx = i
        break
assert ilog_idx is not None
# find last log line at/after ilog_idx
last = None
for i in range(ilog_idx, len(lines)):
    if lines[i].startswith('- 2026-09-'):
        last = i
assert last is not None
entry = ('- 2026-09-09: cosientist 第150回 (10:46 JST tick)。HEAD a472cde = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため '
         'fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0)。rank 第242回 NEXT 「K-Z3 10時台 run546」は bench 第248回 run546 (10時台 2セット目, '
         'cold 6/60) で消化済みのため、本 tick はフォールバック (production HTTP 実測) で K-Z3 10時台 3セット目 run547A–C を実施 '
         '(同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 10:46–10:48 JST, 全 80/80 200): cold(>=0.5s) 1/60 (~1.7%) — '
         'run547A 0/20 p50 133.4ms / run547B 1/20 (1.1717s 単発) p50 159.6ms / run547C 0/20 p50 122.9ms, control (kotobase.net/signup) '
         '0/20 p50 110.9ms 完全静穏で control 分離成立。10時台通算 13/180 (~7.2%)。host load1 107→76 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外。'
         'evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。K-Q1 (cacao_b64 harness 変更) は host load gate 大幅超過のため '
         '本 tick は実施せず (local harness 測定不可), 次の低負荷 tick 待ち。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。'
         'secret は一切記録せず (curl + python3 stats のみ)。')
lines.insert(last + 1, entry)

open(path, 'w').write('\n'.join(lines))
print('kz3_row_idx=', kz3_idx + 1, 'ilog_insert_after=', last + 1)
