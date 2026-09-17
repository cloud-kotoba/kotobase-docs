path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt = open(path).read()

evid = (" falsify 2026-09-05 (K-Z3 23時台 n 積み増し run177A–C, falsify 第67回 run175 (22:59–23:00) と bench 第61回 run176 "
        "(23:43) と ID 衝突した自採分を前例に従い run177 として記録, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, "
        "23:52:55–23:53:05 JST, 全 80/80 200, host load1 12.65 は production HTTP 実測のため gate 外): "
        "run177A cold(>=0.5s) 1/20 (0.965s 単発) p50 42ms / run177B cold 0/20 p50 42ms / run177C cold 0/20 p50 40ms — "
        "合計 1/60, landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 49ms max 59ms と静穏で control 分離成立 "
        "(search 側薄散発単発)。23時台 (9/5) 通算は run175 (0/60) + run176 (7/60) + 本分 (1/60) = 8/180 (~4.4%) — "
        "9/4 の 23時台 (~29-32%) から低位で帯レートは日差込みでは確定途上。status 判定は rank に委ねる (rank 専門)。")

marker = 'run176A cold(>=0.5s) 7/20'
i = txt.find(marker)
assert i >= 0, 'marker not found'
j = txt.find(' |', i)
assert j >= 0
new = txt[:j] + evid + txt[j:]
open(path, 'w').write(new)
print('appended, new len', len(new))
