#!/usr/bin/env python3
# falsify: append run365 evidence to K-Z3 row line (line index 279).
import io
p = 'query-cosientist.md'
with io.open(p, encoding='utf-8') as f:
    lines = f.readlines()
n = len(lines)
if n < 279:
    print('ERR file too short', n)
    raise SystemExit(1)
row = lines[278]
if 'K-Z3' not in row or 'worker' not in row:
    print('ERR line279 not K-Z3 row:', row[:80])
    raise SystemExit(1)
adds = (' falsify 2026-09-07 (run365, K-Z3 15hr(9/7) band-first n-add '
         '- relocated from run364 (rank157 NEXT) collision w/ bench158 in-flight shared worktree '
         '(.b364 runner.sh overwritten + double-append -> contaminated 40-line series discarded), '
         'same method: separate-conn curl, TTFB time_starttransfer, cold>=0.5s, nearest-rank p50, '
         'Tokyo, 15:12:28-15:12:33 JST, all 80/80 200, endpoint search.kotobase.net/search?q=test, '
         'host load1 24-25 (pre-run uptime, gate 7.5 大幅超過) is production HTTP 実測のため gate 外, '
         'secret 不含 - curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 - '
         'run365A cold 0/20 p50 46ms max 125ms / run365B cold 0/20 p50 48ms max 119ms / '
         'run365C cold 0/20 p50 47ms max 58ms, control(kotobase.net/signup) cold 0/20 p50 43ms '
         'max 57ms 完全静穏で control 分離成立、cold 群は search 側に局在。'
         'run365 全 0/60 完全静穏で 15時台帯初計測の基底を記録 - 15時台通算は bench158-run364 (独立計測) '
         'と合わせ帯判定は rank に委ねる (rank 専門).)
lines[278] = lines[278].rstrip('\n') + adds + '\n'
with io.open(p, 'w', encoding='utf-8')as f:
    f.writelines(lines)
print('APPENDED_OK total_lines=', n)