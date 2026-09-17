p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(p).read()
anchor='control 分離成立は有効。status 判定は rank に委ねる (rank 専門)。'
assert s.count(anchor)==1, s.count(anchor)
INS=(' falsify 2026-09-06 (第105回, K-Z3 19時台 5セット目 run238A–C — bench 第93回 run237 (19時台 4セット目 cold 4/60) と run ID 衝突回避のため run238 に読み替え, 独立 2 計測として採用可否は rank 判定に委ねる; 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 19:47:16–19:47:40 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 37.75 (pre-run) は production HTTP 実測のため gate 外): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run238A 単発 1.567s (13番目) p50 47.1ms / run238B 単発 1.051s (5番目) p50 46.6ms / run238C 0/20 p50 61.6ms, control (kotobase.net/signup) cold 0/20 p50 53.4ms max 364.5ms 静穏で control 分離成立、cold 群は search 側に局在。run238A/B 各単発 (warm p50 ~47ms 静穏帯水準) は「帯内 1 窓即消失」パターン継続で bench run237 (同時刻帯独立計測) の 4/60 散発が本 tick で単発型に減弱する弱い続行。19時台通算 = run234 4 + run235 6 + run236 2 + bench-run237 4 + 本 tick 2 = 18/300 (~6.0%) — 18時台 18/240 (~7.5%) と同水準の中間帯で 19時台 n を 300 (5セット) に拡張 (「低位帯から中間帯への弱い遷移方向」継続, evening peak 方向を弱く支持, 深夜帯 ~26-31% 平坦パターンとの対比は不変)。host load 高騰 tick だが warm p50 47ms と静穏で p50 上振れは軽微、cold 濃度判定 2/60 は閾値決定的。status 判定は rank に委ねる (rank 専門)。')
s2=s.replace(anchor, anchor+INS)
assert s2.count(anchor)==1
open(p,'w').write(s2)
print("inserted, runs238 occurrences:", s2.count('run238'))