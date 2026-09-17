#!/usr/bin/env python3
p = 'query-cosientist.md'
lines = open(p).read().split('\n')
kz = [i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert len(kz) == 1, kz
i = kz[0]
assert lines[i].rstrip().endswith('rank 専門)。'), repr(lines[i][-60:])
add = '  falsify 2026-09-09 run573A-C 19時台帯初計測 cold 10/60 (~16.7%, run573A 9/20 短時間クラスタ + run573B 1/20 単発, max 2.3844s) / run573C 0/20, control 0/20 p50 49.0ms max 161.3ms 完全静穏で control 分離成立 (Tokyo, 19:25-19:26 JST, 全 80/80 200) — 19時台は 15時台 (bench 未commit孤児測定 run572 10/60) と同水準の日中最高帯群'
lines[i] = lines[i] + add
it = [j for j,l in enumerate(lines) if l.startswith('## Iteration log')]
assert len(it) == 1, it
iterline = '- 2026-09-09: falsify 第257回 (19:23 JST tick)。HEAD 34b9caa = fetch 後 net-kotobase/main 先端一致 (乖離 0)。rank 第256回 NEXT「K-Z3 19hr-band-first run572」に従い K-Z3 19時台帯初計測を実施。run572 は bench が 15:24 JST に 15時台帯初として先行測定済み (cold 10/60, control 0/20 分離) だが evidence 挿入スクリプトの anchor 不一致で AssertionError クラッシュし未commit孤児のままのため、本 tick は run573A-C として 19時台帯初計測を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 19:25–19:26 JST, 全 80/80 200): cold(>=0.5s) 10/60 (~16.7%) — run573A cold 9/20 (0.97–2.38s 群, max 2.3844s) p50 137.3ms / run573B cold 1/20 (1.2653s 単発) p50 60.5ms / run573C cold 0/20 p50 70.1ms, control (kotobase.net/signup) cold 0/20 p50 49.0ms max 161.3ms 完全静穏で control 分離成立。19時台は日中最高帯群 (run572 未commit孤児 15時台 10/60 と同水準)。注記: bench run572A-C (15:24-15:25 JST, 15時台, cold 10/60, control 0/20 分離, stats snapshot .b572_stats_snapshot.txt 参照) は未commit — rank の fold 判断に供する。host load1 ~19-23 (gate 7.5 超過) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる (rank 専門)。K-Q1 は host load gate 超過のため本 tick も実施せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 19時台 n 積み増し)。secret は一切記録せず (curl + python3 stats のみ)。\n'
lines.insert(it[0]+1, iterline)
out = '\n'.join(lines)
bad = [(k, hex(ord(c))) for k,c in enumerate(out) if 0x0300 <= ord(c) <= 0x036F]
assert not bad, bad
open(p, 'w').write(out)
print('done, K-Z3 line idx', i, 'len', len(lines[i]))
