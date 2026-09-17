#!/usr/bin/env python3
import re
doc = 'query-cosientist.md'
newptxt = [
'bench 2026-09-08 (bench 第189回, K-Z3 5時台 n 積み増し継続 run424A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 05:55-05:57 JST, 全 80/80 200, host load1 18.04 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 0/0/0 per20 = 0/60 (~0% 完全静穏 - run424A/B/C とも 0/20, warm p50 52/44/41ms (p95 135/131/128ms), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 40ms max 142ms と静穏で control 分離成立。run421 (5時台帯初 0/60) と併せ 5時台通算 0/120 完全静穏 - run112/114 (通算 1/180) の静穏帯継続, status 判定は rank に委ねる.',
''
]
frag = '\n'.join(newptxt)
frag = re.sub(r'[\u0300-\u036f]', '', frag'
frag = frag.replace('Norme', 'None')
with open(doc, 'a', encoding='utf-8') as f:
    f.write(frag)
with open('.b189_run424_evidence.txt', 'w', encoding='utf-8') as f:
    f.write(frag)
print('appended_len', len(frag)