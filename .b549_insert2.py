#!/usr/bin/env python3
# falsify run549: append evidence to K-Z3 row + insert iter-log line after '## Iteration log'
import sys, re

path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'

EV = (' falsify 2026-09-09 (第244回, K-Z3 11時台帯初計測 run549A–C, 同測定法 n=20 x 3 + landing control, '
      '別接続 curl, Tokyo, 10:59–11:01 JST, 全 80/80 200 (search endpoint は bench 第249回 run548 の 404 から復旧確認), '
      'host load1 50–80 (gate 7.5 超過) は production HTTP 実測のため gate 外): '
      'run549A cold(>=0.5s) 1/20 (1.045s, 10番目の単発) p50 188.4ms / run549B cold 0/20 p50 165.0ms max 280.9ms / '
      'run549C cold 0/20 p50 150.1ms max 226.5ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は '
      'cold 0/20 p50 85.0ms max 249.5ms と静穏で control 分離成立、cold 群は search 側に局在。'
      '11時台帯初 cold 1/60 (~1.7%) 単発 — run547 (10時台 3セット目 1/60) と同型の「帯内 1 窓即消失」単発型と整合、'
      '10時台 13/180 (~7.2%) 3 セットから 11時台帯初は低位発現。status 判定は rank に委ねる (rank 専門)。')

old = lines[kz3_idx]
assert 'run549A' not in old, 'already appended'
lines[kz3_idx] = old + EV

il_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        il_idx = i
        break
assert il_idx is not None
ITER = ('- 2026-09-09: falsify 第244回 K-Z3 11時台帯初計測 run549A–C (rank 第244回 NEXT 指定の run549 枠, '
        'search endpoint run548 404 から復旧 200 確認後の計測), 同測定法 n=20 x 3 + landing control, '
        '別接続 curl, 10:59–11:01 JST, 全 80/80 200: cold(>=0.5s) 1/60 (~1.7%) — run549A 10番目単発 1.045s のみ, '
        'control (kotobase.net/signup) 0/20 p50 85.0ms 完全静穏で分離成立。evidence は K-Z3 仮説行に追記済み。'
        'secret 不含 (curl + python stats のみ)。')
lines.insert(il_idx + 1, ITER)

out = '\n'.join(lines)
bad = re.findall(r'[\u0300-\u036f]', out)
if bad:
    sys.stderr.write('COMBINING FOUND: %r\n' % bad)
    out = re.sub(r'[\u0300-\u036f]', '', out)
with open(path, 'w', encoding='utf-8') as f:
    f.write(out)
print('OK kz3_line=%d il=%d' % (kz3_idx + 1, il_idx + 1))
