#!/usr/bin/env python3
import unicodedata
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
EV = (" falsify 2026-09-13 (第249回, run597A-C K-Z3 23時台 n 積み増し, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 23:41-23:44 JST, 全 80/80 200): cold(>=0.5s) 2/60 (~3.3%) - run597A cold 1/20 (523.0ms 境界付近単発) p50 44.1ms / run597B cold 1/20 (518.0ms 境界付近単発) p50 45.3ms / run597C cold 0/20 p50 45.6ms, landing control (kotobase.net/, 同時刻, n=20, 全 200) cold 1/20 (926.1ms) p50 62.9ms - control にも単発が出たため本窓は帯特有性を分離できず (host load1 8.54 低下傾向)。23時台通算は run596 分と同水準。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)")
LOG = ("- 2026-09-13: falsify 第249回 (23:41 JST tick)。HEAD 0157452 = fetch 後 net-kotobase/main 先端一致 (乖離 0)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」に従い production HTTP 実測で K-Z3 23時台 run597A-C を実施 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 23:41-23:44 JST, 全 80/80 200): cold(>=0.5s) 2/60 (~3.3%) - run597A cold 1/20 p50 44.1ms / run597B cold 1/20 p50 45.3ms / run597C cold 0/20 p50 45.6ms, control cold 1/20 (926.1ms) p50 62.9ms - control 側にも単発が出現し本窓は帯特有性を分離できず。host load1 8.54 (23:40, 低下傾向) は production HTTP 実測のため gate 外。evidence は K-Z3 仮説行に追記済み。status 判定は rank に委ねる。NEXT: 委ねる。secret は一切記録せず (curl + python3 stats のみ)。")

with open(DOC) as f:
    lines = f.read().split("\n")

idxs = [i for i, l in enumerate(lines) if l.startswith("| K-Z3 |")]
print("KZ3 rows:", idxs)
assert len(idxs) == 2
i = max(idxs)  # newer row (inserted later, immediately after '## Iteration log')
lines[i] = lines[i].rstrip() + EV

il = next(j for j, l in enumerate(lines) if l.strip() == "## Iteration log")
lines.insert(il + 1, LOG.rstrip("\n"))

new = "\n".join(lines)
bad = [(k, unicodedata.name(c)) for k, c in enumerate(new) if 0x0300 <= ord(c) <= 0x036F]
print("combining chars:", bad[:5])
assert not bad
with open(DOC, "w") as f:
    f.write(new)
print("done")
