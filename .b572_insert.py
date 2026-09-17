#!/usr/bin/env python3
import re, unicodedata
p = 'query-cosientist.md'
lines = open(p).read().split('\n')
# locate K-Z3 hypothesis row
kz = [i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert len(kz) == 1, kz
i = kz[0]
ev_old = '  falsify 2026-09-09 run554A-C 11時台5セット目'
assert ev_old in lines[i], lines[i][-200:]
add = '  falsify/bench 2026-09-09 run572A-C 15時台帯初計測 cold 10/60 (~16.7%, run572A 7/20 散発クラスタ + run572B 3/20, max 2.2224s) / run572C 0/20, control 0/20 p50 54.4ms 完全静穏で control 分離成立 (Tokyo, 15:24-15:25 JST, 全 80/80 200) — 15時台は 10時台 (7.2%) を超え日中最高帯の兆候'
lines[i] = lines[i] + add
# iter-log insert after '## Iteration log'
it = [j for j,l in enumerate(lines) if l.startswith('## Iteration log')]
assert len(it) == 1, it
iterline = '- 2026-09-09: falsify 第255回 (15:24 JST tick)。HEAD f35abbd = fetch 後 net-kotobase/main 先端一致 (乖離 0)。rank 第255回 NEXT「K-Z3 15hr-band-first run572」に従い K-Z3 15時台帯初計測 run572A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 15:24–15:25 JST, 全 80/80 200): cold(>=0.5s) 10/60 (~16.7%) — run572A cold 7/20 (1.1–2.2s 群, max 2.2224s) p50 60.1ms / run572B cold 3/20 (1.36–2.11s) p50 52.7ms / run572C cold 0/20 p50 51.2ms, control (kotobase.net/signup) cold 0/20 p50 54.4ms 完全静穏で control 分離成立。15時台は 10時台 (13/180 ~7.2%) を超え日中最高帯の兆候。host load1 ~27-30 (gate 7.5 超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。K-Q1 は host load gate 超過のため本 tick も実施せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 15時台 n 積み増し)。secret は一切記録せず (curl + python3 stats のみ)。\n'
lines.insert(it[0]+1, iterline)
out = '\n'.join(lines)
# combining char scan
bad = [(k, hex(ord(c))) for k,c in enumerate(out) if 0x0300 <= ord(c) <= 0x036F]
assert not bad, bad
open(p, 'w').write(out)
print('done, K-Z3 line idx', i, 'len', len(lines[i]))
