path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
text = open(path).read()
anchor = 'host load 高騰 tick の 全体的上振れがみられるが cold 濃度判定には影響なし)。status 判定は rank に委ねる (rank 専門)。'
assert text.count(anchor) == 1, text.count(anchor)
entry = ' falsify 2026-09-06 (第72回, K-Z3 7時台帯初計測 run192A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 07:14 JST, 全 80/80 200): run192A cold(>=0.5s) 1/20 (0.935s 単発) p50 189ms / run192B cold 0/20 p50 142ms / run192C cold 0/20 p50 89ms — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 161ms (max 227ms) と上振れ気味で borderline not-separated 傾向 (本 tick 全体の p50 90–190ms は静穏 tick の 40–60ms 帯に対し全体的上振れ, host load 由素混入の可能性あり — cold 濃度判定 1/60 には影響なし)。7時台帯初計測は低位帯寄り (run188A/192A 型薄い単発, warm p50 上振れを伴わない)。status 判定は rank に委ねる (rank 専門)。'
text = text.replace(anchor, anchor + entry, 1)
open(path, 'w').write(text)
print('appended')
