#!/usr/bin/env python3
frag = [
'bench 2026-09-08 (bench 第189回, K-Z3 5時台 n 積み増し run424A-C — run424 ID 衝突: cosientist 第132回 05:50 が同枠 run424 実施済みのため本測 (05:55-05:57 独立) は run425 に読替 (第105/216/263 前例), 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo 05:55-05:57 JST, 全 80/80 200, host load1 18.04 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 0/0/0 per20 = 0/60 完全静穏 - runA warm p50 52ms p95 135ms (max 136), runB p50 44ms p95 131ms, runC p50 41ms p95 128ms, landing control (kotobase.net/signup) cold 0/20 p50 40ms p95 135ms max 142ms 静穏で control 分離成立。5時台当日 4 セット連続完全静穏 (run421 falsify 0/60 / run423 bench 0/60 / run424 cosientist 0/60 / 本測 run425 bench 0/60 = 大時台通算 0/240), run112/114 静穏帯記録と整合し 5時台は深夜帯中最も静穏な帯未確定。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python stats のみ)。',
''
]
out = '\n'.join(frag)
with open('.b189_run425_evidence.txt', 'w', encoding='utf-8') as f:
    f.write(out)
print('len', len(out))