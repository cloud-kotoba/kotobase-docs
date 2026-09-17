#!/usr/bin/env python3
path = 'query-cosientist.md'
data = open(path, encoding='utf-8').read()
lines = data.split('\n')
line279 = lines[278]
assert line279.startswith('| K-Z3 | worker |'), line279[:40]
assert 'run310A/C 各単発' in line279, 'run310 anchor missing - sibling changed tail'
assert 'status 判定 は rank に委ねる' in line279 or 'status 判定は rank に委ねる (rank 専門)。' in line279

added = (
 " bench 2026-09-07 (第129回, K-Z3 5時台(deep-night) n-add run311A–C — rank 第136回 NEXT"
 "「K-Z3 current-band(5時台/深夜帯) n-add」の継続枠 (rank 第136回は run310 指定、falsify 第142回 run310A–C が"
 "先行使用のため run311 に読替 (run216/256/263/278 前例)), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, "
 "05:22–05:23 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 27.50 (05:2x uptime, 深夜帯) "
 "は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
 "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run311A 単発散発 1.4705s (5番目) p50 42.4ms / run311B cold 0/20 p50 39.2ms / "
 "run311C cold 0/20 p50 43.0ms, control (kotobase.net/signup) cold 0/20 p50 45.7ms max 66.8ms 完全静穏で control 分離成立、"
 "cold 群は search 側に局在。run311A 単発は B/C + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 "
 "(falsify run310A/C 単発の直後, heavy クラスタ は run271A 以降 36 セット非再現)。status 判定は rank に委ねる (rank 専門)。"
)

lines[278] = line279 + added
open(path, 'w', encoding='utf-8').write('\n'.join(lines))
print('inserted; new line len', len(lines[278]))