#!/usr/bin/env python3
# falsify run549: append evidence to K-Z3 row (line 279, append at end of physical line) + insert iter-log line after '## Iteration log'
import sys

path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

# locate K-Z3 row
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'

EV = (' falsify 2026-09-09 (第244回, K-Z3 11時台帯初計測 run549A–C, 同測定法 n=20 x 3 + landing control, '
      '別接続 curl, Tokyo, 10:59–11:01 JST, 全 80/80 200 (search endpoint は bench 第249回 run548 の 404 から復旧確認), '
      'host load1 50–80 (gate 7.5 超過) は production HTTP 実測のため gate 外): '
      'run549A cold(>=0.5s) 1/20 (1.045s, 10番目の単発) p50 188ms / run549B cold 0/20 p50 165ms / '
      'run549C cold 0/20 p50 150ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は '
      'cold 0/20 p50 85ms max 250ms と静穏で control 分離成立、cold 群は search 側に局在。'
      '11時台帯初 cold 1/60 (~1.7%) 単発 (帯内 1 窓即消失 パターンと整合)。status 判定は rank に委ねる。')

old = lines[kz3_idx]
assert 'falsify 2026-09-09' not in old, 'already appended'
lines[kz3_idx] = old + EV

# iter log
il_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        il_idx = i
        break
assert il_idx is not None
ITER = ('- 2026-09-09: falsify 第244回 K-Z3 11時台帯初 run549A-C (search endpoint run548 404 から復旧確認後の計測), '
        '同測定法 全 80/80 200, cold 1/60 (~1.7%) - run549A 10番目単発 1.045s のみ, control 0/20 分離成立。'
        '11時台は帯初。evidence は K-Z3 仮説行に追記済み。\n')
lines.insert(il_idx + 1, ITER.rstrip('\n'))

out = '\n'.join(lines)
# combining char scan
import re
bad = re.findall(r'[\u0300-\u036f]', out)
if bad:
    sys.stderr.write('COMBINING FOUND: %r\n' % bad)
    out = re.sub(r'[\u0300-\u036f]', '', out)
with open(path, 'w', encoding='utf-8') as f:
    f.write(out)
print('OK kz3_line=%d il=%d' % (kz3_idx + 1, il_idx + 1))
