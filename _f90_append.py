import re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
raw=open(p,encoding='utf-8').read()
txt=raw.replace('\r\n','\n')
evidence=" falsify 2026-09-06 (第90回, K-Z3 15時台 n 積み増し run216A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 15:16:14-15:16:36 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 18.5 (gate 7.5 超過) は production HTTP 実測のため gate 外): run216A cold(>=0.5s) 1/20 (1.118s 2番目の単発) p50 46.9ms / run216B cold 0/20 p50 41.4ms / run216C cold 0/20 p50 43.3ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 52.5ms max 296ms と静穏で control 分離成立、cold 群は search 側に局在。search cold 1/60 (~1.7%) 単発で run216A 型「帯内 1 窓即消失」パターン。15時台通算 (run215+run216) 3/120 (~2.5%) は 14時台通算 (10/240 ~4.2%) と同水準の低位帯残界で 13-15時帯連続低位帯。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
lines=txt.split('\n')
idx=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        idx=i; break
assert idx is not None, "K-Z3 row not found"
lines[idx]=lines[idx]+evidence
open(p,'w',encoding='utf-8').write('\n'.join(lines))
print("appended at line",idx+1,"new row len",len(lines[idx]))