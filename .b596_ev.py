p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s = open(p).read()
anchor = 'landing control (kotobase.net/signup, 同時刻, n=20, 全 200) cold 0/20 p50 58.1ms max 76.5ms 完全静穏で control 分離成立。11時台通算 14/240 (~5.8%)。'
assert s.count(anchor) == 1, s.count(anchor)
ev = ' falsify 2026-09-13 (第258回, K-Z3 19時台 (9/13) 3日連続ペア 3セット目 run596A-C - rank 第265回 NEXT「K-Z3 19時台 (9/13) run596A-C 同帯 3 日連続ペアで K-Z4 日差成分を直接判定」の run596 枠, 実測前 3 endpoint smoke 200/200/200 確認後実施, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 19:57:19-19:57:39 JST, 全 80/80 200, host load1 14.55 (19:57 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 4/2/1 per 20 = 7/60 (~11.7%) - run596A cold 4/20 (1.207-1.836s 散発配置) p50 56.6ms / run596B cold 2/20 (1.719/2.283s) p50 49.6ms / run596C cold 1/20 (1.037s 単発) p50 47.7ms, control (kotobase.net/signup) cold 0/20 p50 62.2ms max 77.5ms 完全静穏で control 分離成立、cold 群は search 側に局在。19時台 (9/13) 通算 7/60 (~11.7%)。K-Z4 同帯日差 3 日目確定材料: 19時台 9/11 run584 11/60 (~18.3%) vs 9/12 run590 17/180 (~9.4%) vs 9/13 本 tick 7/60 (~11.7%) - 3 日連続 9-18% 帯の中位域内変動で低位帯 (11時台 9/9 ~1.7%) との対比は維持、日差振幅は 11時台より小さい方向。status 判定は rank に委ねる (rank 専門)。'
s = s.replace(anchor, anchor + ev)
open(p, 'w').write(s)
print('ok')
