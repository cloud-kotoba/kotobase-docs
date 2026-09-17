ev = ("  falsify 2026-09-15 (第253回, K-Z3 3時台 n 積み増し run625A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 03:29 JST, 全 80/80 200, 正 endpoint search.yataverse.com/search?q=test — search.kotobase.net/search は 301 → 同 URL, control は kotoba.cloud/ 直 URL): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) - run625A cold 5/20 (701.5/701.6/758.5/781.3/881.4ms 1 窓集中型) p50 86.2ms / run625B cold 0/20 p50 78.9ms / run625C cold 0/20 p50 47.6ms, landing control (kotoba.cloud/, 同時刻, n=20, 全 200) cold 0/20 p50 74.8ms max 201.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。3時台日次系列 9/11 run578 10/60 (~16.7%) / 9/14 run611 11/60 (~18.3%) / 本測 9/15 5/60 (~8.3%) — 3 日目は低位側で 2 日連続高位は日次変動成分 (K-Z4 材料) と整合。host load1 16.68-35.89 (gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 (curl + python3 stats のみ)。status 判定は rank に委ねる (rank 専門)。")
path = 'query-cosientist.md'
lines = open(path).read().split('\n')
target = 282  # 0-based for line 283 (rank が active evidence 行として追記してきた K-Z3 行)
row = lines[target]
assert row.rstrip().endswith('。'), 'unexpected tail'
newrow = row.rstrip() + ev
lines[target] = newrow
open(path,'w').write('\n'.join(lines))
c = open(path).read().count('第253回')
print('occurrence count 第253回:', c)
assert c == 1, 'dupe or missing'
print('appended to line', target+1)
